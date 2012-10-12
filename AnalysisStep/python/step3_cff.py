import FWCore.ParameterSet.Config as cms
import os
from WWAnalysis.AnalysisStep.wwMuons_cfi import Scenario6_ICHEP2012,Scenario2_KINK_MUONS,Scenario1_LP_MUONS
from WWAnalysis.AnalysisStep.wwElectrons_cfi import Scenario6_ICHEP,Scenario4_BDT_ELECTRONS,Scenario3_LH_ELECTRONS,Scenario2_LP_ELECTRONS,Scenario1_LP_ELECTRONS

nverticesModule = cms.EDProducer("VertexMultiplicityCounter",
    probes = cms.InputTag("REPLACE_ME"),
    objects = cms.InputTag("goodPrimaryVertices"),
    objectSelection = cms.string("!isFake && ndof > 4 && abs(z) <= 25 && position.Rho <= 2"),
)

# option for PhilJetid
# 4 possible workingpoints
# jetId_WP  
#         0   NONE  no requirement
#         1   OLD Simple Jet ID
#         2   DZ ID        (Not implemented ! )  
#         3   HGG CutBased (Not implemented ! )
#         4   MVA LOOSE   
#         5   MVA MEDIUM
#         6   MVA TIGHT
jetId_WP="4" 

# JetCuts

CJVminPt="30."
CJVmaxEta="4.7"
DphiJetVetominPt="15."
DphiJetVetominEta="4.7"

DzBVeto="999999.9"
minPtBVeto="10.0"


step3Tree = cms.EDFilter("ProbeTreeProducer",
#    cut = cms.string("q(0)*q(1) > 0 && !isSTA(0) && !isSTA(1) && "+
    cut = cms.string("q(0)*q(1) < 0 && !isSTA(0) && !isSTA(1) && "+
                     "leptEtaCut(2.4,2.5) && ptMax > 20 && ptMin > 10"
#                      " && triggerMatchingCut('DATASET')"
#                      "nExtraLep(10) == 0 "
#                     +" && passesIP"
#                    +(" && triggerMatchingCut('DATASET')")
    ),
    variables = cms.PSet(
        hypo = cms.string("hypo()"),
        channel = cms.string("channel()"),
        mll  = cms.string("mll()"),
        ptll = cms.string("pTll()"),
        yll  = cms.string("yll()"),  #fixed! returns (p4a+p4b).Rapidity()
        pt1  = cms.string("ptMax"),
        pt2  = cms.string("ptMin"),
        peaking  = cms.string("peaking"),
        trigger  = cms.string("guillelmoTrigger('DATASET')"),
        nextra  = cms.string("nExtraLep(10)"),
        pfSumEt = cms.string("pfSumEt"),
        pfmet  = cms.string("pfMet"),
        pfmetphi  = cms.string("pfMetPhi"),
        ppfmet = cms.string("projPfMet"),
#        mvamet = cms.string("mvaMet"),
#        mvamethi = cms.string("mvaMetPhi"),
#        pmvamet = cms.string("projMvaMet"),
        chSumEt = cms.string("chargedMetSmurfSumEt"),
        pfmetMEtSig = cms.string("pfMetMEtSig"),
        pfmetSignificance = cms.string("pfMetSignificance"),
        chmet = cms.string("chargedMetSmurf"), 
        chmetphi = cms.string("chargedMetSmurfPhi"), 
        pchmet = cms.string("projChargedMetSmurf"),
        dymva0 = cms.string("userFloat('dymva0')"),
        dymva1 = cms.string("userFloat('dymva1')"),
        redmet = cms.string("-9999"), 
        predmet = cms.string("-9999"), 
        mpmet = cms.string("min(projPfMet,projChargedMetSmurf)"), ##note: min of proj and proj of min are not the same
        imet = cms.string("min(projPfMet,projChargedMetSmurf)*cos(pfMetPhi-chargedMetSmurfPhi)"), 
        dphill = cms.string("dPhill()"),
        drll   = cms.string("dRll()"),
        dphilljet  = cms.string("dPhillLeadingJet("+CJVmaxEta+",1,"+jetId_WP+")"),
        dphilljetjet = cms.string("dPhilljetjet("+CJVmaxEta+",1,"+jetId_WP+")"),   #WHAT
        dphillmet  = cms.string("dPhillMet('PFMET')"),
        dphilmet  = cms.string("dPhilMet('PFMET')"),
        dphilmet1 = cms.string("dPhilMetByPt(0,'PFMET')"),
        dphilmet2 = cms.string("dPhilMetByPt(1,'PFMET')"),
        mtw1 = cms.string("mTByPt(0,'PFMET')"),
        mtw2 = cms.string("mTByPt(1,'PFMET')"),
        mth  = cms.string("mTHiggs('PFMET')"),
        gammaMRStar = cms.string("gammaMRStar"),
        njet  = cms.string("nCentralJets("+CJVminPt+","+CJVmaxEta+",1,"+jetId_WP+")"),
        njetid  = cms.string("nCentralJets("+CJVminPt+","+CJVmaxEta+",1,0)"), 
        # here we do apply a dz cut cause we are actually counting bjets
        nbjettche = cms.string("bTaggedJetsOver("+CJVminPt+",2.1,'trackCountingHighEffBJetTags',"+jetId_WP+","+DzBVeto+")"),
        nbjet = cms.string("bTaggedJetsOver("+CJVminPt+",1.05,'jetBProbabilityBJetTags',"+jetId_WP+","+DzBVeto+")"),
        # here we don't apply the dz cut, cause we just use the b-tag value of highest pt jets
        jetpt1   = cms.string("leadingJetPt(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jeteta1  = cms.string("leadingJetEta(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetphi1  = cms.string("leadingJetPhi(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetid1   = cms.string("leadingJetId(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetmva1   = cms.string("leadingJetMva(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetbjpb1 = cms.string("leadingJetBtag(0,'jetBProbabilityBJetTags',0,"+CJVmaxEta+",1,"+jetId_WP+","+DzBVeto+")"),
        jettche1 = cms.string("leadingJetBtag(0,'trackCountingHighEffBJetTags',0,"+CJVmaxEta+",1,"+jetId_WP+","+DzBVeto+")"),
        jettchp1 = cms.string("leadingJetBtag(0,'trackCountingHighPurBJetTags',0,"+CJVmaxEta+",1,"+jetId_WP+","+DzBVeto+")"),
        jetptd1 = cms.string("leadingJetPtD(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetCHM1 = cms.string("leadingJetChargedHadronMultiplicity(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetNHM1 = cms.string("leadingJetNeutralHadronMultiplicity(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetPhM1 = cms.string("leadingJetPhotonMultiplicity(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetpt2   = cms.string("leadingJetPt(1,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jeteta2  = cms.string("leadingJetEta(1,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetphi2  = cms.string("leadingJetPhi(1,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetid2   = cms.string("leadingJetId(1,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetmva2  = cms.string("leadingJetMva(1,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jettche2 = cms.string("leadingJetBtag(1,'trackCountingHighEffBJetTags',0,"+CJVmaxEta+",1,"+jetId_WP+","+DzBVeto+")"),
        jetbjpb2 = cms.string("leadingJetBtag(1,'jetBProbabilityBJetTags',0,"+CJVmaxEta+",1,"+jetId_WP+","+DzBVeto+")"),
        jettchp2 = cms.string("leadingJetBtag(1,'trackCountingHighEffBJetTags',0,"+CJVmaxEta+",1,"+jetId_WP+","+DzBVeto+")"),
        jetptd2 = cms.string("leadingJetPtD(1,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetCHM2 = cms.string("leadingJetChargedHadronMultiplicity(1,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetNHM2 = cms.string("leadingJetNeutralHadronMultiplicity(1,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetPhM2 = cms.string("leadingJetPhotonMultiplicity(1,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetpt3   = cms.string("leadingJetPt(2,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jeteta3  = cms.string("leadingJetEta(2,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetphi3  = cms.string("leadingJetPhi(2,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetid3   = cms.string("leadingJetId(2,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetmva3  = cms.string("leadingJetMva(2,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jettche3 = cms.string("leadingJetBtag(2,'trackCountingHighEffBJetTags',0,"+CJVmaxEta+",1,"+jetId_WP+","+DzBVeto+")"),
        jetbjpb3 = cms.string("leadingJetBtag(2,'jetBProbabilityBJetTags',0,"+CJVmaxEta+",1,"+jetId_WP+","+DzBVeto+")"),
        jettchp3 = cms.string("leadingJetBtag(2,'trackCountingHighPurBJetTags',0,"+CJVmaxEta+",1,"+jetId_WP+","+DzBVeto+")"),
        jetptd3 = cms.string("leadingJetPtD(2,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetCHM3 = cms.string("leadingJetChargedHadronMultiplicity(2,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetNHM3 = cms.string("leadingJetNeutralHadronMultiplicity(2,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetPhM3 = cms.string("leadingJetPhotonMultiplicity(2,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetpt4   = cms.string("leadingJetPt(3,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jeteta4  = cms.string("leadingJetEta(3,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetphi4  = cms.string("leadingJetPhi(3,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetid4   = cms.string("leadingJetId(3,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetmva4  = cms.string("leadingJetMva(3,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jettche4 = cms.string("leadingJetBtag(3,'trackCountingHighEffBJetTags',0,"+CJVmaxEta+",1,"+jetId_WP+","+DzBVeto+")"),
        jetbjpb4 = cms.string("leadingJetBtag(3,'jetBProbabilityBJetTags',0,"+CJVmaxEta+",1,"+jetId_WP+","+DzBVeto+")"),
        jettchp4 = cms.string("leadingJetBtag(3,'trackCountingHighPurBJetTags',0,"+CJVmaxEta+",1,"+jetId_WP+","+DzBVeto+")"),
        jetptd4 = cms.string("leadingJetPtD(3,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetCHM4 = cms.string("leadingJetChargedHadronMultiplicity(3,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetNHM4 = cms.string("leadingJetNeutralHadronMultiplicity(3,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetPhM4 = cms.string("leadingJetPhotonMultiplicity(3,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetRho = cms.string("getJetRhoIso()"),
        iso1 = cms.string("allIsoByPt(0)/ptByPt(0)"),
        iso2 = cms.string("allIsoByPt(1)/ptByPt(1)"),
        eta1 = cms.string("etaByPt(0)"),
        eta2 = cms.string("etaByPt(1)"),
        sceta1 = cms.string("etaSCByPt(0)"),
        sceta2 = cms.string("etaSCByPt(1)"),
        phi1 = cms.string("phiByPt(0)"),
        phi2 = cms.string("phiByPt(1)"),
        ch1 = cms.string("qByPt(0)"),
        ch2 = cms.string("qByPt(1)"),
        bdt1 = cms.string("leptBdtByPt(0)"),
        bdt2 = cms.string("leptBdtByPt(1)"),
        lh1 = cms.string("leptLHByPt(0)"),
        lh2 = cms.string("leptLHByPt(1)"),
        nbrem1 = cms.string("nBremByPt(0)"),
        nbrem2 = cms.string("nBremByPt(1)"),
        # in the 2012 selection, 2 BJet algorithms are used: softtche and hardbjpb !
        # softbdisc = cms.string("highestBDiscRange(10.0,30.0,'trackCountingHighEffBJetTags',"+jetId_WP+","+DzBVeto+")"),
        # hardbdisc = cms.string("highestBDiscRange(30.0,999999.,'jetBProbabilityBJetTags',"+jetId_WP+","+DzBVeto+",1)"),       
        softtche = cms.string("highestBDiscRange("+minPtBVeto+","+CJVminPt+"   ,'trackCountingHighEffBJetTags',"+jetId_WP+","+DzBVeto+")"),
        hardtche = cms.string("highestBDiscRange("+CJVminPt+",999999.,'trackCountingHighEffBJetTags',"+jetId_WP+","+DzBVeto+",1)"),
        softbjpb = cms.string("highestBDiscRange("+minPtBVeto+","+CJVminPt+"   ,'jetBProbabilityBJetTags',"+jetId_WP+","+DzBVeto+")"),
        hardbjpb = cms.string("highestBDiscRange("+CJVminPt+",999999.,'jetBProbabilityBJetTags',"+jetId_WP+","+DzBVeto+",1)"),
        tightmu = cms.string("passesSmurfMuonID"),
        worstJetLepPt = cms.string("max(matchedJetPt(0, 0.5)/pt(0), matchedJetPt(1, 0.5)/pt(1))"),
        dataset = cms.string("REPLACE_ME"),
        puAW   = cms.InputTag("puWeightA"),
        puBW   = cms.InputTag("puWeightB"),
        puW    = cms.InputTag("puWeight"),
        kfW   = cms.InputTag("ptWeight"),
        baseW = cms.string("REPLACE_ME"),
        fourW = cms.string("REPLACE_ME"),
        fermiW = cms.string("REPLACE_ME"),
        trpu  = cms.InputTag("nPU:tr"),
        itpu  = cms.InputTag("nPU:it"),
        ootpup1  = cms.InputTag("nPU:p1"),
        ootpum1  = cms.InputTag("nPU:m1"),
        effAW = cms.string("1"),
        effBW = cms.string("1"),
        effW = cms.string("1"),
        triggAW = cms.string("1"),
        triggBW = cms.string("1"),
        triggW = cms.string("1"),
        fakeAW   = cms.string("1"),
        fakeBW   = cms.string("1"),
        fakeW   = cms.string("1"),
        #vbf stuff:
        njetvbf = cms.string("nJetVBF(30,"+CJVmaxEta+",1,"+jetId_WP+")"),
        mjj = cms.string("mjj(0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        detajj = cms.string("dEtajj(30,"+CJVmaxEta+",1,"+jetId_WP+")"),
        cjetpt1   = cms.string("leadingVBFJetPt(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        cjeteta1  = cms.string("leadingVBFJetEta(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        cjetphi1  = cms.string("leadingVBFJetPhi(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        cjetid1   = cms.string("leadingVBFJetId(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        cjetmva1   = cms.string("leadingVBFJetMva(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        cjetpt2   = cms.string("leadingVBFJetPt(1,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        cjeteta2  = cms.string("leadingVBFJetEta(1,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        cjetphi2  = cms.string("leadingVBFJetPhi(1,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        cjetid2  = cms.string("leadingVBFJetId(1,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        cjetmva2  = cms.string("leadingVBFJetMva(1,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        # mc info
        mctruth = cms.string("-1"),
    ),
    flags = cms.PSet(
        sameflav   = cms.string("hypo == 3 || hypo == 6"),
        zveto      = cms.string("abs(mll-91.1876)>15. || hypo == 4 || hypo == 5"),
        # here we do apply a dz cut cause we are actually counting bjets
        bveto      = cms.string("bTaggedJetsBetween(10,30,2.1,'trackCountingHighEffBJetTags',"+jetId_WP+","+DzBVeto+") == 0 && nSoftMu(3) == 0"),
        bveto_ip   = cms.string("bTaggedJetsBetween(10,30,2.1,'trackCountingHighEffBJetTags',"+jetId_WP+","+DzBVeto+") == 0"),
        bveto_mu   = cms.string("nSoftMu(3) == 0"),
        bveto_nj   = cms.string("bTaggedJetsBetween(10,30,2.1,'trackCountingHighEffBJetTags',"+jetId_WP+","+DzBVeto+") == 0 && nSoftMu(3,1) == 0"),
        bveto_munj = cms.string("nSoftMu(3,1) == 0"),
        bveto_nj30   = cms.string("bTaggedJetsBetween(10,30,2.1,'trackCountingHighEffBJetTags',"+jetId_WP+","+DzBVeto+") == 0 && nSoftMu(3,30) == 0"),
        bveto_munj30 = cms.string("nSoftMu(3,30) == 0"),
        bveto_nj05   = cms.string("bTaggedJetsBetween(10,30,2.1,'trackCountingHighEffBJetTags',"+jetId_WP+","+DzBVeto+") == 0 && nSoftMu(3,1,0.5) == 0"),
        bveto_munj05 = cms.string("nSoftMu(3,1,0.5) == 0"),
        bveto_nj3005   = cms.string("bTaggedJetsBetween(10,30,2.1,'trackCountingHighEffBJetTags',"+jetId_WP+","+DzBVeto+") == 0 && nSoftMu(3,30,0.5) == 0"),
        bveto_munj3005 = cms.string("nSoftMu(3,30,0.5) == 0"),
        dphiveto   = cms.string("passesDPhillJet("+DphiJetVetominPt+","+DphiJetVetominEta+",1,"+jetId_WP+")"),
        pass2012ICHEP1   = cms.string('passCustomByPt(0,"'+Scenario6_ICHEP2012+'","'+Scenario6_ICHEP+'")'),
        pass2012ICHEP2   = cms.string('passCustomByPt(1,"'+Scenario6_ICHEP2012+'","'+Scenario6_ICHEP+'")'),
#        passBDT1   = cms.string('passCustomByPt(0,"'+Scenario2_KINK_MUONS+'","'+Scenario4_BDT_ELECTRONS+'")'),
#        passBDT2   = cms.string('passCustomByPt(1,"'+Scenario2_KINK_MUONS+'","'+Scenario4_BDT_ELECTRONS+'")'),
#        passLH1    = cms.string('passCustomByPt(0,"'+Scenario2_KINK_MUONS+'","'+Scenario3_LH_ELECTRONS+ '")'),
#        passLH2    = cms.string('passCustomByPt(1,"'+Scenario2_KINK_MUONS+'","'+Scenario3_LH_ELECTRONS+ '")'),
#        passCB1    = cms.string('passCustomByPt(0,"'+Scenario2_KINK_MUONS+'","'+Scenario2_LP_ELECTRONS+ '")'),
#        passCB2    = cms.string('passCustomByPt(1,"'+Scenario2_KINK_MUONS+'","'+Scenario2_LP_ELECTRONS+ '")'),
#        passCBOld1 = cms.string('passCustomByPt(0,"'+Scenario1_LP_MUONS  +'","'+Scenario1_LP_ELECTRONS+ '")'),
#        passCBOld2 = cms.string('passCustomByPt(1,"'+Scenario1_LP_MUONS  +'","'+Scenario1_LP_ELECTRONS+ '")'),
# WRONG FOR 2012 SELECTION
#         passWW     = cms.string("guillelmoTrigger('DATASET') && pfMet > 20 && mll()>20 && (abs(mll-91.1876)>15 || hypo == 4 || hypo == 5) && min(projPfMet,projChargedMetSmurf) && nCentralJets(30,4.7) && (passesDPhillJet||!sameflav) && bTaggedJetsBetween(10,30,2.1,'trackCountingHighEffBJetTags',2.0) == 0 && nSoftMu(3) == 0 && nExtraLep(10)"),

    ),
    addRunLumiInfo = cms.bool(True)
)

# from WWAnalysis.AnalysisStep.pileupReweighting_cfi import reWeightVector
from WWAnalysis.AnalysisStep.pileupReweighting_cfi import *
nPU     = cms.EDProducer("PileUpMultiplicityCounter",
    puLabel    = cms.InputTag("addPileupInfo"),
    src        = cms.InputTag("REPLACE_ME"),
)
puWeightS4AB     = cms.EDProducer("CombinedWeightProducer",
    baseWeight = cms.double(1.0),
    puWeight   = cms.vdouble(s42011AB[:]),
    puLabel    = cms.InputTag("addPileupInfo"),
#     s4Dist = cms.vdouble(puS4fromMC[:]),
#     dataDist = cms.vdouble(pu2011AB[:]),
#     useOOT = cms.bool(False),
    src        = cms.InputTag("REPLACE_ME"),
    nTrueInt   = cms.bool(False),
)
puWeightS4A = puWeightS4AB.clone(puWeight = s42011A[:])
puWeightS4B = puWeightS4AB.clone(puWeight = s42011B[:])
puWeightS6AB = puWeightS4AB.clone(puWeight = s62011AB[:])
puWeightS6A  = puWeightS4AB.clone(puWeight = s62011A[:])
puWeightS6B  = puWeightS4AB.clone(puWeight = s62011B[:])
puWeightS7AB = puWeightS4AB.clone(puWeight = s72012AB[:])
puWeightS7A  = puWeightS4AB.clone(puWeight = s72012A[:])
puWeightS7B  = puWeightS4AB.clone(puWeight = s72012B[:])
# puWeightA = puWeight.clone(dataDist = pu2011A[:])
# puWeightB = puWeight.clone(dataDist = pu2011B[:])
higgsPt = cms.EDProducer("HWWKFactorProducer",
    genParticlesTag = cms.InputTag("prunedGen"),
    inputFilename = cms.untracked.string("REPLACE_ME"),
    ProcessID = cms.untracked.int32(10010),
    Debug =cms.untracked.bool(False)
)
ptWeight     = cms.EDProducer("CombinedWeightProducer",
    baseWeight = cms.double(1.0),
    ptWeight   = cms.InputTag("higgsPt"),
    src        = cms.InputTag("REPLACE_ME"),
)
dyWeight = cms.EDProducer("DYFactorProducer",
    weightFile = cms.string('WWAnalysis/Misc/data/fewz_powheg_weights_stepwise_2011_fine7.root'),
    src = cms.InputTag("REPLACE_ME"),
)


def addBTaggingVariables(pt,dzCut=99999):
    if hasattr(pt,"variables"):
        pt.variables.softtche = cms.string("highestBDiscRange("+minPtBVeto+","+CJVminPt+"   ,'trackCountingHighEffBJetTags',"+jetId_WP+",%f)"%dzCut)
        pt.variables.hardtche = cms.string("highestBDiscRange("+CJVminPt+",999999.,'trackCountingHighEffBJetTags',"+jetId_WP+",%f,1)"%dzCut)
        pt.variables.softtchp = cms.string("highestBDiscRange("+minPtBVeto+","+CJVminPt+"   ,'trackCountingHighPurBJetTags',"+jetId_WP+",%f)"%dzCut)
        pt.variables.hardtchp = cms.string("highestBDiscRange("+CJVminPt+",999999.,'trackCountingHighPurBJetTags',"+jetId_WP+",%f,1)"%dzCut)
        pt.variables.softcsv  = cms.string("highestBDiscRange("+minPtBVeto+","+CJVminPt+"   ,'combinedSecondaryVertexBJetTags',"+jetId_WP+",%f)"%dzCut)
        pt.variables.hardcsv  = cms.string("highestBDiscRange("+CJVminPt+",999999.,'combinedSecondaryVertexBJetTags',"+jetId_WP+",%f,1)"%dzCut)
        pt.variables.softcsvm = cms.string("highestBDiscRange("+minPtBVeto+","+CJVminPt+"   ,'combinedSecondaryVertexMVABJetTags',"+jetId_WP+",%f)"%dzCut)
        pt.variables.hardcsvm = cms.string("highestBDiscRange("+CJVminPt+",999999.,'combinedSecondaryVertexMVABJetTags',"+jetId_WP+",%f,1)"%dzCut)
        pt.variables.softjbpb = cms.string("highestBDiscRange("+minPtBVeto+","+CJVminPt+"   ,'jetBProbabilityBJetTags',"+jetId_WP+",%f)"%dzCut)
        pt.variables.hardjbpb = cms.string("highestBDiscRange("+CJVminPt+",999999.,'jetBProbabilityBJetTags',"+jetId_WP+",%f,1)"%dzCut)
        pt.variables.softjpb  = cms.string("highestBDiscRange("+minPtBVeto+","+CJVminPt+"   ,'jetProbabilityBJetTags',"+jetId_WP+",%f)"%dzCut)
        pt.variables.hardjpb  = cms.string("highestBDiscRange("+CJVminPt+",999999.,'jetProbabilityBJetTags',"+jetId_WP+",%f,1)"%dzCut)

        pt.variables.jetcsv1 = cms.string("leadingJetBtag(0,'combinedSecondaryVertexBJetTags',0,"+CJVmaxEta+","+jetId_WP+",1,1,%f)"%dzCut)
        pt.variables.jetcsv2 = cms.string("leadingJetBtag(1,'combinedSecondaryVertexBJetTags',0,"+CJVmaxEta+","+jetId_WP+",1,1,%f)"%dzCut)
        pt.variables.jetcsvm1 = cms.string("leadingJetBtag(0,'combinedSecondaryVertexMVABJetTags',0,"+CJVmaxEta+","+jetId_WP+",1,1,%f)"%dzCut)
        pt.variables.jetcsvm2 = cms.string("leadingJetBtag(1,'combinedSecondaryVertexMVABJetTags',0,"+CJVmaxEta+","+jetId_WP+",1,1,%f)"%dzCut)
#       pt.variables.jetjbpb1 = cms.string("leadingJetBtag(0,'jetBProbabilityBJetTags',0,"+CJVmaxEta+","+jetId_WP+",1,1,%f)"%dzCut)
#       pt.variables.jetjbpb2 = cms.string("leadingJetBtag(1,'jetBProbabilityBJetTags',0,"+CJVmaxEta+","+jetId_WP+",1,1,%f)"%dzCut)
        pt.variables.jetjpb1 = cms.string("leadingJetBtag(0,'jetProbabilityBJetTags',0,"+CJVmaxEta+","+jetId_WP+",1,1,%f)"%dzCut)
        pt.variables.jetjpb2 = cms.string("leadingJetBtag(1,'jetProbabilityBJetTags',0,"+CJVmaxEta+","+jetId_WP+",1,1,%f)"%dzCut)
    else:
        raise RuntimeError, "In addBTaggingVariables, %s doesn't look like a ProbeTreeProducer object, it has no 'variables' attribute." % pt

def addIsoStudyVariables(process,pt):
    if hasattr(pt,"variables"):
      for i,l in enumerate(["lep1", "lep2"]):
        setattr(pt.variables, l+"isoMergePf"     , cms.string("? abs(candByPt({0}).pdgId) == 13 ? candByPt({0}).userFloat('muSmurfPF') : candByPt({0}).userFloat('eleSmurfPF04')".format(i)))
        setattr(pt.variables, l+"isoRecoTracks"  , cms.string("? abs(candByPt({0}).pdgId) == 13 ? candByPt({0}).isolationR03().sumPt : candByPt({0}).dr03TkSumPt".format(i)))
        setattr(pt.variables, l+"isoRecoEcal"    , cms.string("? abs(candByPt({0}).pdgId) == 13 ? candByPt({0}).isolationR03().emEt  : ".format(i) +
                                                              "  ( max(0,candByPt({0}).dr03EcalRecHitSumEt - 1)*candByPt({0}).isEB + (1-candByPt({0}).isEB)*candByPt({0}).dr03EcalRecHitSumEt )".format(i)))
        setattr(pt.variables, l+"isoRecoHCal"    , cms.string("? abs(candByPt({0}).pdgId) == 13 ? candByPt({0}).isolationR03().hadEt  : candByPt({0}).dr03HcalTowerSumEt ".format(i)))
        setattr(pt.variables, l+"isoRecoHCalFull", cms.string("? abs(candByPt({0}).pdgId) == 13 ? candByPt({0}).isolationR03().hadEt  : candByPt({0}).userFloat('hcalFull')".format(i)))
        setattr(pt.variables, l+"isoPfCharged"   , cms.string("candByPt({0}).userFloat('pfCharged')".format(i)))
        setattr(pt.variables, l+"isoPfNeutral"   , cms.string("candByPt({0}).userFloat('pfNeutral')".format(i)))
        setattr(pt.variables, l+"isoPfPhoton"    , cms.string("candByPt({0}).userFloat('pfPhoton')".format(i)))
        setattr(pt.variables, l+"isoSmurfCharged", cms.string("candByPt({0}).userFloat('smurfCharged')".format(i)))
        setattr(pt.variables, l+"isoSmurfNeutral", cms.string("candByPt({0}).userFloat('smurfNeutral')".format(i)))
        setattr(pt.variables, l+"isoSmurfPhoton" , cms.string("candByPt({0}).userFloat('smurfPhoton')".format(i)))
        setattr(pt.variables, l+"isoSmurfNoOverCharged", cms.string("candByPt({0}).userFloat('smurfNoOverCharged')".format(i)))
        setattr(pt.variables, l+"isoSmurfNoOverNeutral", cms.string("candByPt({0}).userFloat('smurfNoOverNeural')".format(i)))
        setattr(pt.variables, l+"isoSmurfNoOverPhoton" , cms.string("candByPt({0}).userFloat('smurfNoOverPhoton')".format(i)))
        for algo in ("JetCone", "FixCone03", "FixCone04", "MaxCone03", "MaxCone04", "SumCone02", "SumCone04"):
            for name in ("Charged", "ChargedNoOvRem"): #, "NeutralHadAll", "NeutralHadPt05", "NeutralHadPt1", "Photons", "PhotonsMuStrip"):
                setattr(pt.variables, "%sjetiso%s%s"%(l,algo,name), cms.string("candByPt(%d).userFloat('jetIso%s%s')"%(i,algo,name)))
    else:
        raise RuntimeError, "In addIsoStudyVariables, %s doesn't look like a ProbeTreeProducer object, it has no 'variables' attribute." % pt
    if not hasattr(process,"isoStudySequence"):
        process.load("WWAnalysis.AnalysisStep.isoStudySequence_cff")

def addExtraPUWeights(process,tree,X,seq):
    print "WARNING, all the distro's haven't been designed yet, don't turn addExtraPUWeights on yet"
    from WWAnalysis.AnalysisStep.pileupReweighting_cfi import lpOld, lpNew, currentOld, currentNew, mcNominal, mcTemplate
    dataDistros = {
        "LPOld": lpOld,
        "LPNew": lpNew,
        "CurrentOld": currentOld,
        "CurrentNew": currentNew,
    }
    mcDistros = {
        "MCNominal": mcNominal,
        "MCTemplate": mcTemplate,
    }
    for data in dataDistros:
        for mc in mcDistros:
            newName = X+mc+data
            setattr(tree.variables, 'pu'+mc+data, cms.InputTag(newName))
            setattr(tree.variables, 'puOOT'+mc+data, cms.InputTag(newName+"OOT"))
            setattr(process, newName, process.puWeight.clone(src = cms.InputTag("ww%s"% (X)), dataDist = dataDistros[data][:], s4Dist = mcDistros[mc][:]))
            setattr(process, newName+"OOT", process.puWeight.clone(src = cms.InputTag("ww%s"% (X)), dataDist = dataDistros[data][:], s4Dist = mcDistros[mc][:], useOOT=True))
            seq += getattr(process, newName)
            seq += getattr(process, newName+"OOT")
            


