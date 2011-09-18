// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include <DataFormats/PatCandidates/interface/Muon.h>

#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"

#include "DataFormats/METReco/interface/PFMET.h"
#include "DataFormats/METReco/interface/PFMETCollection.h"

#include<vector>

#include "Math/VectorUtil.h"
#include "DataFormats/Math/interface/deltaPhi.h"


class LooseMuonBooster : public edm::EDProducer {
    public:
        explicit LooseMuonBooster(const edm::ParameterSet&);
        ~LooseMuonBooster();

    private:
        virtual void beginJob() ;
        virtual void produce(edm::Event&, const edm::EventSetup&);
        virtual void endJob() ;

  edm::InputTag muonTag_;
  edm::InputTag muonPairTag_;
  edm::InputTag jetTag_;
  edm::InputTag metTag_;
  double drMin_;

};

LooseMuonBooster::LooseMuonBooster(const edm::ParameterSet& iConfig) :
  muonTag_(iConfig.getParameter<edm::InputTag>("muonTag")),
  muonPairTag_(iConfig.getParameter<edm::InputTag>("muonPairTag")),
  jetTag_(iConfig.getParameter<edm::InputTag>("jetTag")),
  metTag_(iConfig.getParameter<edm::InputTag>("metTag")),
  drMin_(iConfig.getParameter<double>("drMin"))
{
  produces<pat::MuonCollection>();  
}


LooseMuonBooster::~LooseMuonBooster() {

}


// ------------ method called to produce the data  ------------
void LooseMuonBooster::produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {
    using namespace edm;
    using namespace reco;
    using namespace std;


    //ESHandle<TransientTrackBuilder> theTTBuilder;
    //iSetup.get<TransientTrackRecord>().get("TransientTrackBuilder",theTTBuilder);

    Handle<View<Candidate> > muons;
    iEvent.getByLabel(muonTag_,muons);

    Handle<View<Candidate> > muonPairs;
    iEvent.getByLabel(muonPairTag_,muonPairs);

    Handle<View<Candidate> > jets;
    iEvent.getByLabel(jetTag_,jets);

    Handle<PFMETCollection> pfmet;
    iEvent.getByLabel(metTag_,pfmet);
    
    PFMET myMET= pfmet->front();


    std::auto_ptr<pat::MuonCollection> pOut(new pat::MuonCollection);

    double massPair(-999.);
    if(muonPairs->size()) massPair = muonPairs->begin()->mass();


    // ----- here is the real loop over the muons ----
    for(edm::View<reco::Candidate>::const_iterator mu=muons->begin(); mu!=muons->end(); ++mu){    
      pat::Muon clone = *edm::RefToBase<reco::Candidate>(muons,mu-muons->begin()).castTo<pat::MuonRef>();

      clone.addUserFloat("pfmet",myMET.pt());
      float mt = sqrt(2*clone.pt()*myMET.pt()*(1-cos(clone.phi()-myMET.phi())));
      clone.addUserFloat("mt",mt);
      
      double pt = clone.pt();
      double eta = clone.eta();
      double tip = clone.userFloat("tip");
      double lip = clone.userFloat("dzPV");
      double smurf_iso = clone.userFloat("muSmurfPF")/pt;

      bool tight_iso = ( (fabs(eta) < 1.479 && pt >  20 && smurf_iso < 0.13) || ( fabs(eta) >= 1.479 && pt >  20 && smurf_iso < 0.09 ) ||  
			 (fabs(eta) < 1.479 && pt <= 20 && smurf_iso < 0.06) || ( fabs(eta) >= 1.479 && pt <= 20 && smurf_iso < 0.05 ) );
      bool tight_ip = ( ( (pt >= 20 && fabs(tip) < 0.02) || (pt < 20 && fabs(tip) < 0.01) ) && fabs(lip)  < 0.1 );
              
      bool loose_iso = smurf_iso < 0.4;
      bool loose_ip = fabs(tip)<0.1 && fabs(lip)<0.1;

      bool passID = true;
      bool passTightSel = passID && tight_iso && tight_ip;
      bool passLooseSel = passID && loose_iso && loose_ip;

      clone.addUserFloat("passTight",passTightSel);
      clone.addUserFloat("passLoose",passLooseSel);

      clone.addUserFloat("pairMass",massPair);

      if(jets->size()==0)  {
	//cout << "no jet for this event" << endl;
	pOut->push_back(clone);
      }
      else{
	double dr = ROOT::Math::VectorUtil::DeltaR(jets->begin()->momentum(),clone.momentum());
	if(dr>drMin_) pOut->push_back(clone);
      }
    }
    iEvent.put(pOut);
}

// ------------ method called once each job just before starting event loop  ------------
void LooseMuonBooster::beginJob() { }

// ------------ method called once each job just after ending the event loop  ------------
void LooseMuonBooster::endJob() { } 


//define this as a plug-in
DEFINE_FWK_MODULE(LooseMuonBooster);
