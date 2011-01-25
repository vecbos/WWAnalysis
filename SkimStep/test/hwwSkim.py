import FWCore.ParameterSet.Config as cms

process = cms.Process("WW")

isMC = True
# isMC = RMMEMC

#  _____               _____                               _                
# |  __ \             |  __ \                             | |               
# | |__) |   _ _ __   | |__) |_ _ _ __ __ _ _ __ ___   ___| |_ ___ _ __ ___ 
# |  _  / | | | '_ \  |  ___/ _` | '__/ _` | '_ ` _ \ / _ \ __/ _ \ '__/ __|
# | | \ \ |_| | | | | | |  | (_| | | | (_| | | | | | |  __/ ||  __/ |  \__ \
# |_|  \_\__,_|_| |_| |_|   \__,_|_|  \__,_|_| |_| |_|\___|\__\___|_|  |___/
# 

from PhysicsTools.PatAlgos.tools.coreTools import *
 
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load("PhysicsTools.PatAlgos.patSequences_cff")

# process.GlobalTag.globaltag = 'START3X_V26::All'
process.GlobalTag.globaltag = 'START38_V12::All'
# process.GlobalTag.globaltag = 'RMMEGlobalTag'


process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.destinations = ['cout', 'cerr']
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(3000) )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
#        'RMMEFileName'
#        '/store/mc/Spring10/SingleTop_sChannel-madgraph/GEN-SIM-RECO/START3X_V26_S09-v1/0076/6045CE55-784B-DF11-8AC4-0025B3E063A8.root'
#         'file:/home/mangano/WW/12.8.2010/CMSSW_3_8_0_patch2/src/H160_2W_2lnu_gluonfusion_7TeV.root'
#         'file:/home/mwlebour/data/EWKTest/TTbar.START36_V9_S09-v1.root'
#         'file:/home/mwlebour/data/WW.38XMC.Samples/RMME'
#         '/store/relval/CMSSW_3_8_4/RelValWjet_Pt_80_120/GEN-SIM-RECO/MC_38Y_V12-v1/0025/4832FEF7-9AC2-DF11-B100-002618943966.root',
#        'file:/home/mwlebour/data/WW.38XMC.Samples/RMME'
#           '/store/relval/CMSSW_3_8_4/RelValWjet_Pt_80_120/GEN-SIM-RECO/MC_38Y_V12-v1/0025/4832FEF7-9AC2-DF11-B100-002618943966.root',
#         '/store/relval/CMSSW_3_8_4/RelValWjet_Pt_80_120/GEN-SIM-RECO/MC_38Y_V12-v1/0023/EE7FAC85-75C2-DF11-9C72-0030486792AC.root',
#         '/store/relval/CMSSW_3_8_4/RelValWjet_Pt_80_120/GEN-SIM-RECO/MC_38Y_V12-v1/0023/6E09EE0A-73C2-DF11-84E5-001A928116FE.root',
#         '/store/relval/CMSSW_3_8_4/RelValWjet_Pt_80_120/GEN-SIM-RECO/MC_38Y_V12-v1/0023/4AD81773-72C2-DF11-A881-001A92971B9A.root',
#         '/store/relval/CMSSW_3_8_4/RelValWjet_Pt_80_120/GEN-SIM-RECO/MC_38Y_V12-v1/0023/48FF5073-73C2-DF11-85A0-0018F3D09604.root',
#         '/store/relval/CMSSW_3_8_4/RelValWjet_Pt_80_120/GEN-SIM-RECO/MC_38Y_V12-v1/0023/06D91B74-74C2-DF11-91F3-00261894387B.root',
    )
)


from glob import glob
process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring())
process.source.fileNames += [ 'file:%s'%x for x in glob('/nfs/bluearc/group/skims/ww/oct29Skim/WWFull/*/*.root')]

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('hwwSkim.root'),
#     fileName = cms.untracked.string('RMMEFileName'),
    outputCommands =  cms.untracked.vstring(
        'drop *',
        # This stuff
        'keep *_patMuonsWithTrigger_*_*',
        'keep *_patElectronsWithTrigger_*_*',
        'keep *_goodMuons_*_*',
        'keep *_goodElectrons_*_*',
        'keep *_zMuMu_*_*',
        'keep *_zElEl_*_*',
        'keep *_diLep_*_*',
        #'keep patJets_patJets_*_*',
        'keep patJets_cleanPatJets_*_*',
        #'keep patJets_patJetsPF_*_*',
        'keep patJets_cleanPatJetsPF_*_*',
        #'keep patJets_patJetsNoPU_*_*',
        'keep patJets_cleanPatJetsNoPU_*_*',
        #'keep patJets_patJetsJPT_*_*',
        'keep patJets_cleanPatJetsJPT_*_*',
        # Tracking
        'keep *_offlinePrimaryVertices_*_*',
        'keep *_offlinePrimaryVerticesWithBS_*_*',
        'keep *_offlineBeamSpot_*_*',
        # MET
        'keep *_tcMet_*_*',
        'keep *_met_*_*',
        'keep *_pfMet_*_*',
        # MC
        'keep *_prunedGen_*_*',
        'keep *_genMetTrue_*_*',
        #'keep recoGenJets_ak5GenJets_*_*',
        # Trigger
        #'keep *_hltTriggerSummaryAOD_*_*',
        'keep *_TriggerResults_*_*',
        'keep *_vertexMapProd_*_*',
    ),
    SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring( 
#         'eePath',
#         'mmPath',
#         'wwPath',
        'wwAllPath',
    )),
    verbose = cms.untracked.bool(True)
)
process.outpath = cms.EndPath(process.out)



#  _______   _                         ______ _ _ _            
# |__   __| (_)                       |  ____(_) | |           
#    | |_ __ _  __ _  __ _  ___ _ __  | |__   _| | |_ ___ _ __ 
#    | | '__| |/ _` |/ _` |/ _ \ '__| |  __| | | | __/ _ \ '__|
#    | | |  | | (_| | (_| |  __/ |    | |    | | | ||  __/ |   
#    |_|_|  |_|\__, |\__, |\___|_|    |_|    |_|_|\__\___|_|   
#               __/ | __/ |                                    
#              |___/ |___/                                  
# 
#import HLTrigger.HLTfilters.hltHighLevel_cfi 
#process.hltFilter = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone() 
#process.hltFilter.HLTPaths = [
#     "HLT_Ele15_LW_L1R",
#     "HLT_Mu9",
# ]
 
#process.primaryVertexFilter = cms.EDFilter("VertexSelector",
#    src = cms.InputTag("offlinePrimaryVertices"),
#    cut = cms.string("!isFake && ndof > 4 && abs(z) <= 15 && position.Rho <= 2"), 
#    filter = cms.bool(True),   
# )
# 
process.noscraping = cms.EDFilter("FilterOutScraping",
    applyfilter = cms.untracked.bool(True),
    debugOn = cms.untracked.bool(False),
    numtrack = cms.untracked.uint32(10),
    thresh = cms.untracked.double(0.25)
)
# 
# process.load("WWAnalysis.Tools.incompleteECALReadout_cfi")
# 
# process.goodEvents = cms.Sequence(
#     process.hltFilter 
#     process.primaryVertexFilter 
#     process.noscraping 
#     process.incompleteECALReadout 
# )

#Trigger Matching (hopefully?!?)
process.load("PhysicsTools.PatAlgos.triggerLayer1.triggerProducer_cff")
process.patTrigger.onlyStandAlone = True
process.patTrigger.processName  = '*' 
process.patTriggerEvent.processName = '*'
process.MessageLogger.suppressWarning += ['patTrigger'] # 1 warning per event on old runs!
    
#     process.hltFilter.TriggerResultsTag = cms.InputTag("TriggerResults","","HLT")

#  _____               _____ _    _           
# / ____|             / ____| |  (_)          
#| |  __  ___ _ __   | (___ | | ___ _ __ ___  
#| | |_ |/ _ \ '_ \   \___ \| |/ / | '_ ` _ \ 
#| |__| |  __/ | | |  ____) |   <| | | | | | |
# \_____|\___|_| |_| |_____/|_|\_\_|_| |_| |_|
#                                             

process.prunedGen = cms.EDProducer( "GenParticlePruner",
    src = cms.InputTag("genParticles"),
    select = cms.vstring(
        "drop  *  ",
        "keep++ pdgId = {Z0}",
        "++keep pdgId = {Z0}",
        "keep++ pdgId = {W+}",
        "++keep pdgId = {W+}",
        "keep++ pdgId = {W-}",
        "++keep pdgId = {W-}",
        "keep++ pdgId = {h0}",
        "++keep pdgId = {h0}",
        "keep++ pdgId = {e+}",
        "++keep pdgId = {e+}",
        "keep++ pdgId = {e-}",
        "++keep pdgId = {e-}",
        "keep++ pdgId = {mu+}",
        "++keep pdgId = {mu+}",
        "keep++ pdgId = {mu-}",
        "++keep pdgId = {mu-}"
    )
)

#  ______ _           _                     _____      _   _      
# |  ____| |         | |                   |  __ \    | | | |     
# | |__  | | ___  ___| |_ _ __ ___  _ __   | |__) |_ _| |_| |__   
# |  __| | |/ _ \/ __| __| '__/ _ \| '_ \  |  ___/ _` | __| '_ \  
# | |____| |  __/ (__| |_| | | (_) | | | | | |  | (_| | |_| | | | 
# |______|_|\___|\___|\__|_|  \___/|_| |_| |_|   \__,_|\__|_| |_| 
#                                                                 


ELE_ISO_CUT=("( isEB && (dr03TkSumPt +" +
             " max(0,dr03EcalRecHitSumEt - 1.0) +" +
             " dr03HcalTowerSumEt)/pt < 0.5) ||"+
             "( isEE && (dr03TkSumPt +" +
             " dr03EcalRecHitSumEt +" +
             " dr03HcalTowerSumEt)/pt < 0.5) ")


process.load("PhysicsTools.PatAlgos.producersLayer1.electronProducer_cfi")
process.load("PhysicsTools.PatAlgos.triggerLayer1.triggerProducer_cfi")

#Code for the liklihood eID
process.load("RecoEgamma.ElectronIdentification.electronIdLikelihoodExt_cfi")
process.liklihoodID = process.eidLikelihoodExt.clone() 

process.eleTriggerMatchHLT = cms.EDProducer( "PATTriggerMatcherDRDPtLessByR",
    src     = cms.InputTag( "patElectrons" ),
    matched = cms.InputTag( "patTrigger" ),
    andOr          = cms.bool( False ),
    filterIdsEnum  = cms.vstring( '*' ),
    filterIds      = cms.vint32( 0 ),
    filterLabels   = cms.vstring( '*' ),
    pathNames      = cms.vstring( '*' ),
    collectionTags = cms.vstring( 'hltL1IsoRecoEcalCandidate', 'hltL1NonIsoRecoEcalCandidate' ),
    maxDPtRel = cms.double( 0.5 ),
    maxDeltaR = cms.double( 0.5 ),
    resolveAmbiguities    = cms.bool( True ),
    resolveByMatchQuality = cms.bool( True )
)
process.eleIdTriggerMatchHLT = process.eleTriggerMatchHLT.clone(collectionTags = cms.vstring('hltPixelMatchElectronsL1Iso', 'hltPixelMatchElectronsL1NonIso') )
process.patElectronsWithTrigger = cms.EDProducer( "PATTriggerMatchElectronEmbedder",
    src     = cms.InputTag(  "patElectrons" ),
    matches = cms.VInputTag(cms.InputTag('eleTriggerMatchHLT'), cms.InputTag('eleIdTriggerMatchHLT'))
) 

process.goodElectrons = cms.EDFilter("PATElectronRefSelector",
    src = cms.InputTag("patElectronsWithTrigger"),
    cut = cms.string(("pt > 10 && "+ELE_ISO_CUT)),
)

import WWAnalysis.SkimStep.expectedHitsComputer_cfi
process.expectedHitsEle = WWAnalysis.SkimStep.expectedHitsComputer_cfi.expectedHitsComputer.clone()
process.expectedHitsEle.inputColl   = cms.InputTag("gsfElectrons")
process.expectedHitsEle.useGsfTrack = cms.bool(True)

process.patElectrons.embedPFCandidate = False
process.patElectrons.embedSuperCluster = False
process.patElectrons.embedTrack = True
process.patElectrons.addElectronID = False
process.electronMatch.matched = "prunedGen"
process.patElectrons.userData.userFloats.src = cms.VInputTag(
    cms.InputTag("convValueMapProd","dist"),
    cms.InputTag("convValueMapProd","dcot"),
    cms.InputTag("liklihoodID")
)
process.patElectrons.userData.userInts.src = cms.VInputTag(
    cms.InputTag("expectedHitsEle","in"),
    cms.InputTag("expectedHitsEle","out"),
)


process.load("WWAnalysis.Tools.convValueMapProd_cfi")

if isMC: 
    process.preElectronSequence = cms.Sequence(
        process.expectedHitsEle + 
        process.convValueMapProd + 
        process.liklihoodID +
        process.patTrigger + 
        process.prunedGen * 
        process.electronMatch 
    )
else:
    removeMCMatching(process, ['Electrons'])
    process.preElectronSequence = cms.Sequence(
        process.expectedHitsEle + 
        process.convValueMapProd + 
        process.liklihoodID +
        process.patTrigger 
    )


process.elSeq = cms.Sequence( 
    process.preElectronSequence * 
    process.patElectrons *
    (process.eleTriggerMatchHLT + process.eleIdTriggerMatchHLT) *
    process.patElectronsWithTrigger *
    process.goodElectrons 
)

#  __  __                     _____      _   _
# |  \/  |                   |  __ \    | | | |
# | \  / |_   _  ___  _ __   | |__) |_ _| |_| |__
# | |\/| | | | |/ _ \| '_ \  |  ___/ _` | __| '_ \
# | |  | | |_| | (_) | | | | | |  | (_| | |_| | | |
# |_|  |_|\__,_|\___/|_| |_| |_|   \__,_|\__|_| |_|
#
MUON_ISO_CUT=("(isolationR03().emEt +" +
              " isolationR03().hadEt +" +
              " isolationR03().sumPt)/pt < 0.5")

process.expectedHitsMu  = WWAnalysis.SkimStep.expectedHitsComputer_cfi.expectedHitsComputer.clone()

process.muonTriggerMatchHLT = cms.EDProducer( 'PATTriggerMatcherDRDPtLessByR',
    src     = cms.InputTag( 'patMuons' ),
    matched = cms.InputTag( 'patTrigger' ),
    andOr          = cms.bool( False ),
    filterIdsEnum  = cms.vstring( '*' ),
    filterIds      = cms.vint32( 0 ),
    filterLabels   = cms.vstring( '*' ),
    pathNames      = cms.vstring( '*' ),
    collectionTags = cms.vstring( 'hltL3MuonCandidates' ),
    maxDPtRel = cms.double( 0.5 ),
    maxDeltaR = cms.double( 0.1 ),
    resolveAmbiguities    = cms.bool( True ),
    resolveByMatchQuality = cms.bool( False )
)
process.patMuonsWithTrigger = cms.EDProducer( 'PATTriggerMatchMuonEmbedder',
    src     = cms.InputTag(  'patMuons' ),
    matches = cms.VInputTag('muonTriggerMatchHLT')
)

process.patMuons.embedPFCandidate = False
process.patMuons.embedTrack = True
process.patMuons.userData.userInts.src = cms.VInputTag(
    cms.InputTag("expectedHitsMu","in"),
    cms.InputTag("expectedHitsMu","out"),
)
process.muonMatch.matched = "prunedGen"


if isMC: 
    if True: ## Turn this on to get extra info on muon MC origin, on GEN-SIM-RECO
        process.load("MuonAnalysis.MuonAssociators.muonClassificationByHits_cfi")
        from MuonAnalysis.MuonAssociators.muonClassificationByHits_cfi import addUserData as addClassByHits
        addClassByHits(process.patMuons, labels=['classByHitsGlb'], extraInfo = True)
        process.muonClassificationByHits = cms.Sequence(process.mix * process.trackingParticlesNoSimHits * process.classByHitsGlb )
        process.preMuonSequence = cms.Sequence(process.prunedGen * process.muonMatch + process.patTrigger + process.expectedHitsMu + process.muonClassificationByHits)
        process.MessageLogger.suppressWarning += ['classByHitsGlb'] # kill stupid RPC hit associator warning
    else:
        process.preMuonSequence = cms.Sequence(process.prunedGen * process.muonMatch + process.patTrigger + process.expectedHitsMu)
else:
    removeMCMatching(process, ['Muons'])
    process.preMuonSequence = cms.Sequence(process.patTrigger + process.expectedHitsMu)


process.goodMuons = cms.EDFilter("PATMuonRefSelector",
    src = cms.InputTag("patMuonsWithTrigger"),
    cut = cms.string("pt > 10 && " + MUON_ISO_CUT)
)

process.muSeq = cms.Sequence( 
    process.preMuonSequence *
    process.patMuons *
    process.muonTriggerMatchHLT *
    process.patMuonsWithTrigger *
    process.goodMuons 
)


#   _____ _    _             _____      _   _     
#  / ____| |  (_)           |  __ \    | | | |    
# | (___ | | ___ _ __ ___   | |__) |_ _| |_| |__  
#  \___ \| |/ / | '_ ` _ \  |  ___/ _` | __| '_ \ 
#  ____) |   <| | | | | | | | |  | (_| | |_| | | |
# |_____/|_|\_\_|_| |_| |_| |_|   \__,_|\__|_| |_|
#                                                 

process.zElEl = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string('goodElectrons patElectronsWithTrigger'),
    cut = cms.string('mass > 12 && daughter(0).pt > 10 && daughter(1).pt > 10 && max(daughter(0).pt,daughter(1).pt) > 20'),
    checkCharge = cms.bool(False)
)

process.zMuMu = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string('goodMuons patMuonsWithTrigger'),
    cut = cms.string('mass > 12 && daughter(0).pt > 10 && daughter(1).pt > 10 && max(daughter(0).pt,daughter(1).pt) > 20'),
    checkCharge = cms.bool(False)
)

process.goodLeps = cms.EDProducer("CandViewMerger",
    src = cms.VInputTag(cms.InputTag("goodMuons"), cms.InputTag("goodElectrons"))
)

process.diLep = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string('goodLeps goodLeps'),
    cut = cms.string('deltaR(daughter(0).eta,daughter(0).phi,daughter(1).eta,daughter(1).phi) > 0.1 && daughter(0).pt > 10 && daughter(1).pt > 10 && max(daughter(0).pt,daughter(1).pt) > 20'),
    checkCharge = cms.bool(False)
)

process.allLeps = cms.EDProducer("CandViewMerger",
    src = cms.VInputTag(cms.InputTag("patElectronsWithTrigger"), cms.InputTag("patMuonsWithTrigger"))
)

process.allDiLep = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string('goodLeps allLeps'),
    cut = cms.string('deltaR(daughter(0).eta,daughter(0).phi,daughter(1).eta,daughter(1).phi) > 0.1 && daughter(0).pt > 10 && daughter(1).pt > 10 && max(daughter(0).pt,daughter(1).pt) > 20'),
    checkCharge = cms.bool(False)
)


# process.countZee = cms.EDFilter("CandViewCountFilter", src = cms.InputTag("zElEl"), minNumber = cms.uint32(1))
# process.countZmm = cms.EDFilter("CandViewCountFilter", src = cms.InputTag("zMuMu"), minNumber = cms.uint32(1))
# process.countWW  = cms.EDFilter("CandViewCountFilter", src = cms.InputTag("diLep"), minNumber = cms.uint32(1))
process.countWWAll  = cms.EDFilter("CandViewCountFilter", src = cms.InputTag("allDiLep"), minNumber = cms.uint32(1))

# process.zElElSeq  = cms.Sequence( process.zElEl * process.countZee)
# process.zMuMuSeq  = cms.Sequence( process.zMuMu * process.countZmm)
# process.wwSeq = cms.Sequence( process.goodLeps * process.diLep * process.countWW )
process.wwAllSeq = cms.Sequence( (process.goodLeps + process.allLeps) * process.allDiLep * process.countWWAll )

#               _               _____      _ _           _   _                 
#    /\        | |             / ____|    | | |         | | (_)                
#   /  \  _   _| |_ _ __ ___  | |     ___ | | | ___  ___| |_ _  ___  _ __  ___ 
#  / /\ \| | | | __| '__/ _ \ | |    / _ \| | |/ _ \/ __| __| |/ _ \| '_ \/ __|
# / ____ \ |_| | |_| | |  __/ | |___| (_) | | |  __/ (__| |_| | (_) | | | \__ \
#/_/    \_\__,_|\__|_|  \___|  \_____\___/|_|_|\___|\___|\__|_|\___/|_| |_|___/
#                                                                              

from PhysicsTools.PatAlgos.tools.jetTools import *

process.load("PhysicsTools.PFCandProducer.pfNoPileUp_cff")  
process.pfPileUp.Enable = True    
process.ak5PFJetsNoPU = process.ak5PFJets.clone(    
    src =   cms.InputTag("pfNoPileUp")  
)
process.jetSequence = cms.Sequence(   
    process.pfNoPileUpSequence  +   
    process.ak5PFJetsNoPU   
)  

if not isMC:
    removeMCMatching(process, ['Jets'])

addJetCollection(
    process,
    cms.InputTag("JetPlusTrackZSPCorJetAntiKt5"),
    algoLabel    = "JPT",
    doJTA        = False,
    doBTagging   = True,
    jetCorrLabel = ('AK5', 'PF'),
    doType1MET   = True,
    genJetCollection=cms.InputTag("ak5GenJets"),
    doJetID      = True,
    typeLabel    = ""
)

addJetCollection(
    process,
    cms.InputTag("ak5PFJetsNoPU"),
    algoLabel    = "NoPU",
    doJTA        = True,
    doBTagging   = True,
    jetCorrLabel = ('AK5', 'PF'),
    doType1MET   = True,
    genJetCollection=cms.InputTag("ak5GenJets"),
    doJetID      = True,
    typeLabel    = ""
)

addJetCollection(
    process,
    cms.InputTag("ak5PFJets"),
    algoLabel    = "PF",
    doJTA        = True,
    doBTagging   = True,
    jetCorrLabel = ('AK5', 'PF'),
    doType1MET   = True,
    genJetCollection=cms.InputTag("ak5GenJets"),
    doJetID      = True,
    typeLabel    = ""
)


# switchJetCollection(
#     process,
#     cms.InputTag('ak5PFJets'),
#     doJTA        = True,
#     doBTagging   = True,
#     jetCorrLabel = ('AK5', 'PF'),
#     doType1MET   = True,
#     genJetCollection=cms.InputTag("ak5GenJets"),
#     doJetID      = True
# )

process.patJets.addGenJetMatch = False
process.patJetsPF.addGenJetMatch = False
process.patJetsNoPU.addGenJetMatch = False
process.patJetsJPT.addGenJetMatch = False

if not isMC:
    process.patJetsPF.addGenJetMatch = False
    process.patJetsPF.addGenPartonMatch = False
    process.patJetsPF.getJetMCFlavour = False
    process.patJetsNoPU.addGenJetMatch = False
    process.patJetsNoPU.addGenPartonMatch = False
    process.patJetsNoPU.getJetMCFlavour = False
    process.patJetsJPT.addGenJetMatch = False
    process.patJetsJPT.addGenPartonMatch = False
    process.patJetsJPT.getJetMCFlavour = False

process.patJets.addTagInfos = False
process.patJetsPF.addTagInfos = False
process.patJetsNoPU.addTagInfos = False
process.patJetsJPT.addTagInfos = False
process.patJets.embedPFCandidates = False
process.patJetsPF.embedPFCandidates = False
process.patJetsNoPU.embedPFCandidates = False
process.patJetsJPT.embedPFCandidates = False
process.patJets.addAssociatedTracks = False
process.patJetsPF.addAssociatedTracks = False
process.patJetsNoPU.addAssociatedTracks = False
process.patJetsJPT.addAssociatedTracks = False

process.patJetCorrFactors.corrLevels.L5Flavor = 'none'
process.patJetCorrFactors.corrLevels.L7Parton = 'none'

process.cleanPatJets = cms.EDProducer("PATJetCleaner",
    src = cms.InputTag("patJets"),
    preselection = cms.string(''),
    checkOverlaps = cms.PSet(
        ele = cms.PSet(
           src       = cms.InputTag("patElectronsWithTrigger"),
           algorithm = cms.string("byDeltaR"),
           preselection        = cms.string(""),
           deltaR              = cms.double(0.5),
           checkRecoComponents = cms.bool(False),
           pairCut             = cms.string(""),
           requireNoOverlaps = cms.bool(False),
        ),
        mu = cms.PSet(
           src       = cms.InputTag("patMuonsWithTrigger"),
           algorithm = cms.string("byDeltaR"),
           preselection        = cms.string(""),
           deltaR              = cms.double(0.5),
           checkRecoComponents = cms.bool(False),
           pairCut             = cms.string(""),
           requireNoOverlaps = cms.bool(False),
        ),
    ),
    finalCut = cms.string(''),
)
process.cleanPatJetsPF = process.cleanPatJets.clone( src = cms.InputTag("patJetsPF") )
process.cleanPatJetsNoPU = process.cleanPatJets.clone( src = cms.InputTag("patJetsNoPU") )
process.cleanPatJetsJPT = process.cleanPatJets.clone( src = cms.InputTag("patJetsJPT") )

process.load("WWAnalysis.Tools.vertexSumPtMapProd_cfi")

process.autreSeq = cms.Sequence( 
    process.jetSequence * 
    process.makePatJets * ( 
        process.cleanPatJets + 
        process.cleanPatJetsPF + 
        process.cleanPatJetsNoPU + 
        process.cleanPatJetsJPT 
    ) + 
    process.vertexMapProd
)


#   _____      _              _       _      
#  / ____|    | |            | |     | |     
# | (___   ___| |__   ___  __| |_   _| | ___ 
#  \___ \ / __| '_ \ / _ \/ _` | | | | |/ _ \
#  ____) | (__| | | |  __/ (_| | |_| | |  __/
# |_____/ \___|_| |_|\___|\__,_|\__,_|_|\___|
#                                            


# process.eePath = cms.Path( ( process.elSeq + process.muSeq ) *  process.zElElSeq + process.autreSeq )
# process.mmPath = cms.Path( ( process.elSeq + process.muSeq ) *  process.zMuMuSeq + process.autreSeq )
# process.wwPath = cms.Path( ( process.elSeq + process.muSeq ) *  process.wwSeq + process.autreSeq )
process.wwAllPath = cms.Path( ( process.elSeq + process.muSeq ) *  process.wwAllSeq + process.autreSeq )
process.scrap = cms.Path( process.noscraping )

# process.sched = cms.Schedule(
#     process.eePath,
#     process.mmPath,
#     process.wwPath,
#     process.wwAllPath,
#     process.outpath
# )



