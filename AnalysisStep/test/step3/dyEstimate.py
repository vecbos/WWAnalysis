from WWAnalysis.AnalysisStep.tree2yield import *
from optparse import OptionParser
parser = OptionParser(usage="%prog [options] tree.root cuts.txt")
parser.add_option("-t", "--tree",  dest="tree", default='%sTree', help="Pattern for tree name");
parser.add_option("-l", "--lumi",   dest="lumi", type="float", default="1.0", help="Luminosity (in 1/fb)");
parser.add_option("-f", "--final",  dest="final", action="store_true", help="Just compute final yield after all cuts");
parser.add_option("--kmm", dest="kmm", type="float", nargs=2, default=(0.592288, 0.592288), help="kappa factor and uncertainty, for mu mu");
parser.add_option("--kee", dest="kee", type="float", nargs=2, default=(0.592288, 0.592288), help="kappa factor and uncertainty, for el el");
parser.add_option("-U", "--up-to-cut",   dest="upToCut",   type="string", help="Run selection only up to the cut matched by this regexp, included.") 
parser.add_option("-X", "--exclude-cut", dest="cutsToExclude", action="append", default=[], help="Cuts to exclude (regexp matching cut name), can specify multiple times.") 
parser.add_option("-I", "--invert-cut",  dest="cutsToInvert",  action="append", default=[], help="Cuts to invert (regexp matching cut name), can specify multiple times.") 
parser.add_option("-R", "--replace-cut", dest="cutsToReplace", action="append", default=[], nargs=3, help="Cuts to invert (regexp of old cut name, new name, new cut); can specify multiple times.") 
parser.add_option("-A", "--add-cut",     dest="cutsToAdd",     action="append", default=[], nargs=3, help="Cuts to insert (regexp of cut name after which this cut should go, new name, new cut); can specify multiple times.") 
(options, args) = parser.parse_args()
options.inclusive = False
options.nMinusOne = False
options.weight    = True
datasets = [ "SingleMuon2011A", "SingleMuon2011Av2", "DoubleMuon2011A", "DoubleMuon2011Av2",
             "DoubleElectron2011A", "DoubleElectron2011Av2", "MuEG2011A", "MuEG2011Av2" ]
mcsets = [ "DYtoMuMu", "DYtoElEl" ]
ttysData = [ TreeToYield("tree_%s.root" % D, options) for D in datasets ]
ttysMC   = [ TreeToYield("tree_%s.root" % D, options) for D in mcsets   ] 
cf0j = CutsFile(args[0],options)
cf1j = CutsFile(cf0j).replace('Jet veto', 'One jet', 'njet == 1 && dphilljet*sameflav < 165./180.*3.1415926').replace('B veto', 'B veto', 'bveto && nbjet == 0')
cf0jNoMET = CutsFile(cf0j).remove('pMET').remove('met')
cf1jNoMET = CutsFile(cf1j).remove('pMET').remove('met')
cfZ0j = CutsFile(cf0j).remove('m\(?ll\)?').remove('gMR').remove('dphi').replace('Z veto','Z window','abs(mll-91.1876)<15').remove('B veto').remove('m\(?ll\)? >|pT (min|max)|dphi|gMR').replace('pMET','pMET > 35', 'pmmet > 35')
cfZ1j = CutsFile(cf1j).remove('m\(?ll\)?').remove('gMR').remove('dphi').replace('Z veto','Z window','abs(mll-91.1876)<15').remove('B veto').remove('m\(?ll\)? >|pT (min|max)|dphi|gMR').replace('pMET','pMET > 35', 'pmmet > 35')
cfZ0jNoMET = CutsFile(cfZ0j).remove('pMET').remove('met')
cfZ1jNoMET = CutsFile(cfZ1j).remove('pMET').remove('met')
## get yields in peak, with MET cut
reportDataZ0j = mergeReports([tty.getYields(cfZ0j) for tty in ttysData])
reportMCZ0j   = mergeReports([tty.getYields(cfZ0j) for tty in ttysMC])
reportDataZ1j = mergeReports([tty.getYields(cfZ1j) for tty in ttysData])
reportMCZ1j   = mergeReports([tty.getYields(cfZ1j) for tty in ttysMC])
print "\nZ peak in Data, WW level no btag, with MET cut, 0 jets"; ttysData[0].prettyPrint(reportDataZ0j)
print "\nZ peak in Sim., WW level no btag, with MET cut, 0 jets";   ttysMC[0].prettyPrint(reportMCZ0j)
print "\nZ peak in Data, WW level no btag, with MET cut, 1 jets"; ttysData[0].prettyPrint(reportDataZ1j)
print "\nZ peak in Sim., WW level no btag, with MET cut, 1 jets";   ttysMC[0].prettyPrint(reportMCZ1j)
Z0jmmData = reportDataZ0j[-1][1][MM][1];  Z0jeeData = reportDataZ0j[-1][1][EE][1]; Z0jxxData = (reportDataZ0j[-1][1][EM][1]+reportDataZ0j[-1][1][ME][1])
Z1jmmData = reportDataZ1j[-1][1][MM][1];  Z1jeeData = reportDataZ1j[-1][1][EE][1]; Z1jxxData = (reportDataZ1j[-1][1][EM][1]+reportDataZ1j[-1][1][ME][1])
Z0jmmMC = reportMCZ0j[-1][1][MM][1];  Z0jeeMC = reportMCZ0j[-1][1][EE][1]; Z0jxxMC = (reportMCZ0j[-1][1][EM][1]+reportMCZ0j[-1][1][ME][1])
Z1jmmMC = reportMCZ1j[-1][1][MM][1];  Z1jeeMC = reportMCZ1j[-1][1][EE][1]; Z1jxxMC = (reportMCZ1j[-1][1][EM][1]+reportMCZ1j[-1][1][ME][1])

## Now we compute events in the peak without MET cut, to get efficiencies
reportDataZNoMET = mergeReports([tty.getYields(cfZ0jNoMET) for tty in ttysData])
reportMCZNoMET   = mergeReports([tty.getYields(cfZ0jNoMET) for tty in ttysMC])
print "\nZ peak in Data, WW level no btag, no MET, 0 jets"; ttysData[0].prettyPrint(reportDataZNoMET)
print "\nZ peak in Sim., WW level no btag, no MET, 0 jets";   ttysMC[0].prettyPrint(reportMCZNoMET)
keeData = sqrt(reportDataZNoMET[-1][1][EE][1]/float(reportDataZNoMET[-1][1][MM][1]));
kmmData = 1.0/keeData;
keeMC = sqrt(reportMCZNoMET[-1][1][EE][1]/float(reportMCZNoMET[-1][1][MM][1]));
kmmMC = 1.0/keeMC;

# Do flavour subtraction to get DY-only yield
Z0jmmSubData = Z0jmmData - 0.5*kmmData*Z0jxxData; Z0jmmSubDataErr = sqrt(Z0jxxData+pow(0.5*kmmData,2)*Z0jxxData)
Z1jmmSubData = Z1jmmData - 0.5*kmmData*Z1jxxData; Z1jmmSubDataErr = sqrt(Z1jxxData+pow(0.5*kmmData,2)*Z1jxxData)
Z0jeeSubData = Z0jeeData - 0.5*keeData*Z0jxxData; Z0jeeSubDataErr = sqrt(Z0jxxData+pow(0.5*keeData,2)*Z0jxxData)
Z1jeeSubData = Z1jeeData - 0.5*keeData*Z1jxxData; Z1jeeSubDataErr = sqrt(Z1jxxData+pow(0.5*keeData,2)*Z1jxxData)
Z0jmmSubMC   = Z0jmmMC   - 0.5*kmmMC  *Z0jxxMC;   Z0jmmSubMCErr   = sqrt(Z0jxxMC  +pow(0.5*kmmMC  ,2)*Z0jxxMC)
Z1jmmSubMC   = Z1jmmMC   - 0.5*kmmMC  *Z1jxxMC;   Z1jmmSubMCErr   = sqrt(Z1jxxMC  +pow(0.5*kmmMC  ,2)*Z1jxxMC)
Z0jeeSubMC   = Z0jeeMC   - 0.5*keeMC  *Z0jxxMC;   Z0jeeSubMCErr   = sqrt(Z0jxxMC  +pow(0.5*keeMC  ,2)*Z0jxxMC)
Z1jeeSubMC   = Z1jeeMC   - 0.5*keeMC  *Z1jxxMC;   Z1jeeSubMCErr   = sqrt(Z1jxxMC  +pow(0.5*keeMC  ,2)*Z1jxxMC)

## Now we compute events in the signal region. we need the weight regularize the yields
avgweightMM  = ttysMC[0].getAverageWeight(cfZ0jNoMET.allCuts());
avgweightEE  = ttysMC[1].getAverageWeight(cfZ0jNoMET.allCuts());
print "\nAverage event weight: ",avgweightMM,"(mm),\t",avgweightEE,"(ee)"
report0jMC = mergeReports([tty.getYields(cf0j) for tty in ttysMC])
report1jMC = mergeReports([tty.getYields(cf1j) for tty in ttysMC])
print "\nFull selection in Sim., 0 jets";   ttysMC[0].prettyPrint(report0jMC)
print "\nFull selection in Sim., 1 jets";   ttysMC[0].prettyPrint(report1jMC)

## Then we try to do the same but as a function of the MET cut
plot0j  = mergePlots([tty.getPlots("pmmet","pmmet_0j", "50,0.,50.", cf0jNoMET.allCuts()) for tty in ttysMC])
plot1j  = mergePlots([tty.getPlots("pmmet","pmmet_1j", "50,0.,50.", cf1jNoMET.allCuts()) for tty in ttysMC])
plotZ0j = mergePlots([tty.getPlots("pmmet","pmmetZ_0j","50,0.,50.",cfZ0jNoMET.allCuts()) for tty in ttysMC])
plotZ1j = mergePlots([tty.getPlots("pmmet","pmmetZ_1j","50,0.,50.",cfZ1jNoMET.allCuts()) for tty in ttysMC])
print "\nEstimate of alpha vs pMET, regularized"
totZmm0j = plotZ0j[MM][1].Integral(1,51); totSmm0j = plot0j[MM][1].Integral(1,51);
totZee0j = plotZ0j[EE][1].Integral(1,51); totSee0j = plot0j[EE][1].Integral(1,51);
totZmm1j = plotZ1j[MM][1].Integral(1,51); totSmm1j = plot1j[MM][1].Integral(1,51);
totZee1j = plotZ1j[EE][1].Integral(1,51); totSee1j = plot1j[EE][1].Integral(1,51);
print "\tpMET  Zmm0j   Smm0j   alpha  err  |  Zee0j   See0j   alpha  err  |  Zmm1j   Smm1j   alpha  err  |  Zee1j   See1j   alpha  err"

alpha0jmm = (report0jMC[-1][1][MM][1]+avgweightMM)/(reportMCZ0j[-1][1][MM][1]+avgweightMM);
alpha1jmm = (report1jMC[-1][1][MM][1]+avgweightMM)/(reportMCZ1j[-1][1][MM][1]+avgweightMM);
alpha0jmmErr = min(1.0, sqrt(1.0/(report0jMC[-1][1][MM][1]/avgweightMM+1) + 1.0/(reportMCZ0j[-1][1][MM][1]/avgweightMM+1)));
alpha1jmmErr = min(1.0, sqrt(1.0/(report1jMC[-1][1][MM][1]/avgweightMM+1) + 1.0/(reportMCZ1j[-1][1][MM][1]/avgweightMM+1)));
alpha0jee = (report0jMC[-1][1][EE][1]+avgweightEE)/(reportMCZ0j[-1][1][EE][1]+avgweightEE);
alpha1jee = (report1jMC[-1][1][EE][1]+avgweightEE)/(reportMCZ1j[-1][1][EE][1]+avgweightEE);
alpha0jeeErr = min(1.0, sqrt(1.0/(report0jMC[-1][1][EE][1]/avgweightEE+1) + 1.0/(reportMCZ0j[-1][1][EE][1]/avgweightEE+1)));
alpha1jeeErr = min(1.0, sqrt(1.0/(report1jMC[-1][1][EE][1]/avgweightEE+1) + 1.0/(reportMCZ1j[-1][1][EE][1]/avgweightEE+1)));

## Let's do a scan of alpha vs pMET cut
for b in range(50):
    print "\t %2d   %9.1f %5.2f  %5.3f %4.2f |  %9.1f %5.2f  %5.3f %4.2f |  %9.1f %5.2f  %5.3f %4.2f |  %9.1f %5.2f  %5.3f %4.2f" % (
            b,
            totZmm0j, totSmm0j, (totSmm0j+avgweightMM)/(totZmm0j+avgweightMM), 
                min(1.0, sqrt(1.0/(totZmm0j/avgweightMM+1) + 1.0/(totSmm0j/avgweightMM+1))),
            totZee0j, totSee0j, (totSee0j+avgweightEE)/(totZee0j+avgweightEE), 
                min(1.0, sqrt(1.0/(totZee0j/avgweightEE+1) + 1.0/(totSee0j/avgweightEE+1))),
            totZmm1j, totSmm1j, (totSmm1j+avgweightMM)/(totZmm1j+avgweightMM), 
                min(1.0, sqrt(1.0/(totZmm1j/avgweightMM+1) + 1.0/(totSmm1j/avgweightMM+1))),
            totZee1j, totSee1j, (totSee1j+avgweightEE)/(totZee1j+avgweightEE), 
                min(1.0, sqrt(1.0/(totZee1j/avgweightEE+1) + 1.0/(totSee1j/avgweightEE+1))),
          )
    totZmm0j -= plotZ0j[MM][1].GetBinContent(b+1); totSmm0j -= plot0j[MM][1].GetBinContent(b+1)
    totZmm1j -= plotZ1j[MM][1].GetBinContent(b+1); totSmm1j -= plot1j[MM][1].GetBinContent(b+1)
    totZee0j -= plotZ0j[EE][1].GetBinContent(b+1); totSee0j -= plot0j[EE][1].GetBinContent(b+1)
    totZee1j -= plotZ1j[EE][1].GetBinContent(b+1); totSee1j -= plot1j[EE][1].GetBinContent(b+1)


bg0jmm = alpha0jmm*Z0jmmSubData; bg0jee = alpha0jee*Z0jeeSubData;
bg1jee = alpha1jee*Z1jeeSubData; bg1jmm = alpha1jmm*Z1jmmSubData;
print "\n"
print "\n --- Efficiency factors, from Z peak with no MET cut.  --- "
print "kee(Data) = sqrt(N(ee)/N(mm)) = %6.4f\tkee(MC) = %6.4f" % (keeData ,keeMC)
print "kmm(Data) = sqrt(N(mm)/N(ee)) = %6.4f\tkmm(MC) = %6.4f" % (kmmData ,kmmMC)

print "\n --- Yields in the peak, with MET cut                  --- "
print "N(Zmm 0j, Data) = (%5.1f - %5.3f/2 * %5.1f) = %5.2f +/- %4.2f" % (Z0jmmData, kmmData, Z0jxxData, Z0jmmSubData, Z0jmmSubDataErr)
print "N(Zmm 0j, Sim.) = (%5.1f - %5.3f/2 * %5.1f) = %5.2f +/- %4.2f" % (Z0jmmMC  , kmmMC  , Z0jxxMC  , Z0jmmSubMC  , Z0jmmSubMCErr  )
print "N(Zmm 1j, Data) = (%5.1f - %5.3f/2 * %5.1f) = %5.2f +/- %4.2f" % (Z1jmmData, kmmData, Z1jxxData, Z1jmmSubData, Z1jmmSubDataErr)
print "N(Zmm 1j, Sim.) = (%5.1f - %5.3f/2 * %5.1f) = %5.2f +/- %4.2f" % (Z1jmmMC  , kmmMC  , Z1jxxMC  , Z1jmmSubMC  , Z1jmmSubMCErr  )
print "N(Zee 0j, Data) = (%5.1f - %5.3f/2 * %5.1f) = %5.2f +/- %4.2f" % (Z0jeeData, keeData, Z0jxxData, Z0jeeSubData, Z0jeeSubDataErr)
print "N(Zee 0j, Sim.) = (%5.1f - %5.3f/2 * %5.1f) = %5.2f +/- %4.2f" % (Z0jeeMC  , keeMC  , Z0jxxMC  , Z0jeeSubMC  , Z0jeeSubMCErr  )
print "N(Zee 1j, Data) = (%5.1f - %5.3f/2 * %5.1f) = %5.2f +/- %4.2f" % (Z1jeeData, keeData, Z1jxxData, Z1jeeSubData, Z1jeeSubDataErr)
print "N(Zee 1j, Sim.) = (%5.1f - %5.3f/2 * %5.1f) = %5.2f +/- %4.2f" % (Z1jeeMC  , keeMC  , Z1jxxMC  , Z1jeeSubMC  , Z1jeeSubMCErr  )


print "\n --- Extrapolation factors to final selection, from MC --- "
print "alpha mm, 0j, bare: %6.2f / %6.2f = %6.2f / %6.2f (effective events) " % (
         report0jMC[-1][1][MM][1], Z0jmmMC, report0jMC[-1][1][MM][1]/avgweightMM, Z0jmmMC/avgweightMM)
print "alpha ee, 0j, bare: %6.2f / %6.2f = %6.2f / %6.2f (effective events) " % (
         report0jMC[-1][1][EE][1], Z0jeeMC, report0jMC[-1][1][EE][1]/avgweightEE, Z0jeeMC/avgweightEE)
print "alpha mm, 1j, bare: %6.2f / %6.2f = %6.2f / %6.2f (effective events) " % (
         report1jMC[-1][1][MM][1], Z1jmmMC, report1jMC[-1][1][MM][1]/avgweightMM, Z1jmmMC/avgweightMM)
print "alpha ee, 1j, bare: %6.2f / %6.2f = %6.2f / %6.2f (effective events) " % (
         report1jMC[-1][1][EE][1], Z1jeeMC, report1jMC[-1][1][EE][1]/avgweightEE, Z1jeeMC/avgweightEE)
print "alpha mm, 0j, regularized: %7.4f   (rel. uncertainty %6.2f%%)" % ( alpha0jmm, alpha0jmmErr*100 )
print "alpha ee, 0j, regularized: %7.4f   (rel. uncertainty %6.2f%%)" % ( alpha0jee, alpha0jeeErr*100 )
print "alpha ee, 1j, regularized: %7.4f   (rel. uncertainty %6.2f%%)" % ( alpha1jee, alpha1jeeErr*100 )
print "alpha mm, 1j, regularized: %7.4f   (rel. uncertainty %6.2f%%)" % ( alpha1jmm, alpha1jmmErr*100 )

print "\n --- Estimated background in the final selection       --- "
print "N(Z->mm, all cuts, 0j) = %7.3f +/- %7.3f (stat. data) +/- %7.3f (stat. mc)" % (bg0jmm, alpha0jmm*Z0jmmSubDataErr, bg0jmm*alpha0jmmErr)
print "N(Z->ee, all cuts, 0j) = %7.3f +/- %7.3f (stat. data) +/- %7.3f (stat. mc)" % (bg0jee, alpha0jee*Z0jeeSubDataErr, bg0jee*alpha0jeeErr)
print "N(Z->mm, all cuts, 1j) = %7.3f +/- %7.3f (stat. data) +/- %7.3f (stat. mc)" % (bg1jmm, alpha1jmm*Z1jmmSubDataErr, bg1jmm*alpha1jmmErr)
print "N(Z->ee, all cuts, 1j) = %7.3f +/- %7.3f (stat. data) +/- %7.3f (stat. mc)" % (bg1jee, alpha1jee*Z1jeeSubDataErr, bg1jee*alpha1jeeErr)

