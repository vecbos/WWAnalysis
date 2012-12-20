
import FWCore.ParameterSet.Config as cms


#==============================================================================
# corrected gsf electrons
#==============================================================================

calibratedPatElectrons = cms.EDProducer("CalibratedPatElectronProducerCalifornia",

    # input collections
    inputPatElectronsTag = cms.InputTag("boostedElectrons"),

    # data or MC corrections
    # if isMC is false, data corrections are applied
    isMC = cms.bool(False),

    # set to True to read AOD format
    isAOD = cms.bool(False),
    
    # set to True to get debugging printout   
    debug = cms.bool(False),

    # energy measurement type
    energyMeasurementType = cms.uint32(0),

    # input datasets
    # Prompt means May10+Promptv4+Aug05+Promptv6 for 2011
    # ReReco means Jul05+Aug05+Oct03 for 2011
    # Jan16ReReco means Jan16 for 2011
    # Summer11 means summer11 MC..
    #inputDataset = cms.string("ReReco"),
    inputDataset = cms.string("Prompt"),
    
)


