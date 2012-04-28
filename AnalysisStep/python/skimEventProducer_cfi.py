import FWCore.ParameterSet.Config as cms

from WWAnalysis.AnalysisStep.wwElectrons_cfi import *
from WWAnalysis.AnalysisStep.wwMuons_cfi import *



skimEventProducer = cms.EDProducer('SkimEventProducer',
    genParticlesTag = cms.InputTag(""),
    muTag         = cms.InputTag("wwMuons"),
    elTag         = cms.InputTag("wwElectrons"),
    softMuTag     =   cms.InputTag("wwMuons4Veto"),
    # extraElTag    = cms.InputTag("wwElectrons"),
    jetTag        = cms.InputTag("slimPatJetsTriggerMatch"), 
    tagJetTag     = cms.InputTag("slimPatJetsTriggerMatch"), 
    pfMetTag      = cms.InputTag("pfMet"),
    tcMetTag      = cms.InputTag("tcMet"),
    chargedMetTag = cms.InputTag("trackMetProducer"),
    vtxTag        = cms.InputTag("goodPrimaryVertices"),
    chCandsTag    = cms.InputTag("reducedPFCands"),
    sptTag        = cms.InputTag("vertexMapProd","sumPt"),
    spt2Tag       = cms.InputTag("vertexMapProd","sumPt2"),
    # branchAlias   = cms.string("wwelmu"),
    hypoType      = cms.string("WWELMU"),
    
    triggerTag        = cms.InputTag("TriggerResults","","HLT"),
    singleMuDataPaths = cms.vstring(
        "1-163261:HLT_Mu15_v*",
        "163262-165099:HLT_Mu24_v*",
        "165102-173235:HLT_Mu30_v*",
        "173236-175972:HLT_Mu40_v*",
        "175973-999999:HLT_Mu40_eta2p1_v*",
        "163262-170901:HLT_IsoMu17_v*",
        "171050-175910:HLT_IsoMu20_v*",
        "175911-175921:HLT_IsoMu24_v*",
        "175922-999999:HLT_IsoMu24_eta2p1_v*",
    ),
    doubleMuDataPaths = cms.vstring(
        "1-165208:HLT_DoubleMu7_v*",
        "165364-178419:HLT_Mu13_Mu8_v*",
        "178420-999999:HLT_Mu17_Mu8_v*",
        "178420-999999:HLT_Mu17_TkMu8_v*",
    ),
    doubleElDataPaths = cms.vstring(
        "1-170901:HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v*",
        "171050-999999:HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",
    ),
    muEGDataPaths     = cms.vstring(
        "1-175972:HLT_Mu17_Ele8_CaloIdL_v*",
        "175973-999999:HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_v*",
        "1-167913:HLT_Mu8_Ele17_CaloIdL_v*",
        "167914-999999:HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_v*",
    ),
    singleElDataPaths = cms.vstring(
        "1-164237:HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v*",
        "165085-166967:HLT_Ele32_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v*",
        "166968-170901:HLT_Ele52_CaloIdVT_TrkIdT_v*",
        "170902-178419:HLT_Ele65_CaloIdVT_TrkIdT_v*",
        "178420-999999:HLT_Ele80_CaloIdVT_TrkIdT_v*",
    ),
    singleMuMCPaths   = cms.vstring("*"),
    singleElMCPaths   = cms.vstring("*"),
    doubleMuMCPaths   = cms.vstring("*"),
    doubleElMCPaths   = cms.vstring("*"),
    muEGMCPaths       = cms.vstring("*"),
    # singleMuMCPaths   = cms.vstring("HLT_Mu21_v*"),
    # singleElMCPaths   = cms.vstring("FILLME"),
    # doubleMuMCPaths   = cms.vstring("HLT_DoubleMu5_v*"),
    # doubleElMCPaths   = cms.vstring("HLT_Ele17_SW_TightCaloEleId_Ele8HE_L1R_v*"),
    # muEGMCPaths       = cms.vstring("HLT_Mu5_Ele17_v*","HLT_Mu11_Ele8_v*"),

    looseMuSelection = cms.string(PRESEL_MU +"&&"+ MUON_ID_LOOSE),                                   
    tightMuSelection = cms.string(PRESEL_MU +"&&"+  MUON_ID_CUT +"&&"+ MUON_MERGE_ISO+"&&"+MUON_MERGE_IP),
    looseEleSelection = cms.string(ELE_BASE + " && " + ELE_ID_LOOSE_2011),
    tightEleSelection = cms.string(ELE_BASE + " && " + ELE_MERGE_ID + " && " + ELE_MERGE_ISO + " && " + ELE_MERGE_CONV + " && " + ELE_MERGE_IP),
)

def addEventHypothesis(process,label,thisMuTag,thisEleTag,thisSoftMuTag='wwMuons4Veto',preSequence=cms.Sequence()):
# def addEventHypothesis(process,label,thisMuTag,thisEleTag,thisSoftMuTag='wwMuons4Veto',peakingType=None, preSequence=cms.Sequence()):
    hypos = ['mumu','muel','elmu','elel']
    process.peakingFilter = cms.EDFilter("GenFilterDiBosons")

    tempSkimEventFilter = cms.EDFilter("SkimEventSelector",
       src = cms.InputTag(""),
       filter = cms.bool(True),
       cut = cms.string("nLep >=2 "),                                   
    )

    for hypo in hypos:
        #create the four hypothesis:
        setattr(process,'ww'+hypo+label,process.skimEventProducer.clone(hypoType='WW'+hypo.upper(),muTag=thisMuTag,elTag=thisEleTag,softMuTag=thisSoftMuTag))
        #create SkimEventSelectors (asking for nLep >=2) 
        setattr(process,'skim'+hypo+label,tempSkimEventFilter.clone(src='ww'+hypo+label))
        # create sequence
        p = cms.Path(preSequence)
#         if peakingType == 'peaking':     p = cms.Path( process.peakingFilter)
#         if peakingType == 'non-peaking': p = cms.Path(~process.peakingFilter)
        p += ( 
            getattr(process,thisMuTag)  +
            getattr(process,thisEleTag)  +
            getattr(process,thisSoftMuTag)  +
            getattr(process,'ww'+hypo+label)  +
            getattr(process,'skim'+hypo+label)
        )
        setattr(process,'sel'+hypo+label,p)
        # add to scheduler
        if getattr(process,'schedule') != None: process.schedule.append( getattr(process,'sel'+hypo+label) )
        # add to pooloutput module
        if hasattr(process,'out'): process.out.outputCommands.append( 'keep *_{0}_*_*'.format( 'ww'+hypo+label ) )
        if hasattr(process,'out'): process.out.SelectEvents.SelectEvents.append( 'sel'+hypo+label )


# process.ttLeps = cms.EDProducer("CandViewMerger",
#     src = cms.VInputTag(
#         cms.InputTag("wwMuonsMergeIP"),
#         cms.InputTag("wwEleIPMerge"),
#     )
# )
# 
# process.ttDiLeps = cms.EDProducer("CandViewShallowCloneCombiner",
#     decay = cms.string('ttLeps@+ ttLeps@-'),
#     cut = cms.string(
#         'deltaR(daughter(0).eta,daughter(0).phi,daughter(1).eta,daughter(1).phi) > 0.05 && ' +
#         'min(daughter(0).pt,daughter(1).pt) > 10 && ' +
#         'max(daughter(0).pt,daughter(1).pt) > 20'
#     ),
#     checkCharge = cms.bool(True)
# )
# 
# process.ttCount  = cms.EDFilter("CandViewCountFilter", src = cms.InputTag("ttDiLeps"), minNumber = cms.uint32(1))
# 
# 
# process.ttFilter = cms.Sequence( process.wwEleIPMerge + process.wwMuonsMergeIP + process.ttLeps + process.ttDiLeps + process.ttCount)
# process.ttPath = cms.Path( process.ttFilter )
# process.schedule.append( process.ttPath )
# process.out.SelectEvents.SelectEvents.append( 'ttPath' )
