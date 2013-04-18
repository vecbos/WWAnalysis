#include <vector>
#include <iostream>
#include <iomanip>
#include <utility>
#include <string>
#include <fstream>
#include <sstream>
#include <iostream>
#include <cmath>
#include <algorithm>

std::string getSignalCBMeanString(float m, int ch, bool do7TeV, bool doFFT) {
    stringstream fss;
    if (m<400.) fss << "( ";  

    if (!doFFT) fss << "@0 + ";

    if (m<400.) {
      if (do7TeV) {
        if (ch == 0) fss << "(-4.08807) + (0.110583*@0) + (-0.00111048*@0*@0) + (5.04336e-06*@0*@0*@0) + (-1.03646e-08*@0*@0*@0*@0) + (7.79214e-12*@0*@0*@0*@0*@0)";
        if (ch == 1) fss << "(26.5702) + (-0.692027*@0) + (0.00680888*@0*@0) + (-3.24132e-05*@0*@0*@0) + (7.37704e-08*@0*@0*@0*@0) + (-6.37514e-11*@0*@0*@0*@0*@0)";
        if (ch == 2) fss << "(7.74041) + (-0.1993*@0) + (0.00199694*@0*@0) + (-1.00463e-05*@0*@0*@0) + (2.46727e-08*@0*@0*@0*@0) + (-2.33501e-11*@0*@0*@0*@0*@0)";
        if (ch == 3) fss << "(7.74041) + (-0.1993*@0) + (0.00199694*@0*@0) + (-1.00463e-05*@0*@0*@0) + (2.46727e-08*@0*@0*@0*@0) + (-2.33501e-11*@0*@0*@0*@0*@0)";
      }
      else {
        if (ch == 0) fss << "(-5.71849) + (0.145626*@0) + (-0.00138862*@0*@0) + (6.03825e-06*@0*@0*@0) + (-1.19684e-08*@0*@0*@0*@0) + (8.75281e-12*@0*@0*@0*@0*@0)";
        if (ch == 1) fss << "(14.8494) + (-0.405085*@0) + (0.00422887*@0*@0) + (-2.16441e-05*@0*@0*@0) + (5.32721e-08*@0*@0*@0*@0) + (-5.00455e-11*@0*@0*@0*@0*@0)";
        if (ch == 2) fss << "(-5.56876) + (0.155983*@0) + (-0.00167517*@0*@0) + (8.37884e-06*@0*@0*@0) + (-2.01225e-08*@0*@0*@0*@0) + (1.89793e-11*@0*@0*@0*@0*@0)";
        if (ch == 3) fss << "(-5.56876) + (0.155983*@0) + (-0.00167517*@0*@0) + (8.37884e-06*@0*@0*@0) + (-2.01225e-08*@0*@0*@0*@0) + (1.89793e-11*@0*@0*@0*@0*@0)";
      }
    }
    else {
      if (do7TeV) {
        if (ch == 0) fss << "(-8.5) + (0.0594112*@0) + (-0.000104333*@0*@0) + (4.29597e-08*@0*@0*@0)";
        if (ch == 1) fss << "(-57.0151) + (0.279453*@0) + (-0.000428555*@0*@0) + (1.93863e-07*@0*@0*@0)";
        if (ch == 2) fss << "(82.1279) + (-0.457539*@0) + (0.000816838*@0*@0) + (-4.6665e-07*@0*@0*@0)";
        if (ch == 3) fss << "(82.1279) + (-0.457539*@0) + (0.000816838*@0*@0) + (-4.6665e-07*@0*@0*@0)";
      }
      else {
        if (ch == 0) fss << "(-86.5422) + (0.447758*@0) + (-0.000708361*@0*@0) + (3.2711e-07*@0*@0*@0)";
        if (ch == 1) fss << "(-96.4993) + (0.472794*@0) + (-0.000704832*@0*@0) + (3.08549e-07*@0*@0*@0)";
        if (ch == 2) fss << "(-96.4993) + (0.472794*@0) + (-0.000704832*@0*@0) + (3.08549e-07*@0*@0*@0)";
        if (ch == 3) fss << "(-96.4993) + (0.472794*@0) + (-0.000704832*@0*@0) + (3.08549e-07*@0*@0*@0)";
      }
    }

    if (m<400.) {
        if (ch == 0 || ch == 1) fss << " ) +  @0*@1";
        else                    fss << " ) +  @0*@1";
    }
    return fss.str();
}

std::string getSignalCBSigmaString(float m, int ch, bool do7TeV) {
    stringstream fss;
    if (m<400.) fss << "( ";  

    if (m<400.) {
      if (do7TeV) {
        if (ch == 0) fss << "(-8.89255) + (0.22671*@0) + (-0.00198135*@0*@0) + (8.14781e-06*@0*@0*@0) + (-1.42808e-08*@0*@0*@0*@0) + (7.69453e-12*@0*@0*@0*@0*@0)";
        if (ch == 1) fss << "(-42.9661) + (1.16387*@0) + (-0.0116153*@0*@0) + (5.54285e-05*@0*@0*@0) + (-1.25301e-07*@0*@0*@0*@0) + (1.07428e-10*@0*@0*@0*@0*@0)";
        if (ch == 2) fss << "(-32.5568) + (0.867983*@0) + (-0.00861782*@0*@0) + (4.13108e-05*@0*@0*@0) + (-9.4314e-08*@0*@0*@0*@0) + (8.23655e-11*@0*@0*@0*@0*@0)";
        if (ch == 3) fss << "(-32.5568) + (0.867983*@0) + (-0.00861782*@0*@0) + (4.13108e-05*@0*@0*@0) + (-9.4314e-08*@0*@0*@0*@0) + (8.23655e-11*@0*@0*@0*@0*@0)";
      }
      else {
        if (ch == 0) fss << "(-4.56178) + (0.123209*@0) + (-0.00107193*@0*@0) + (4.5413e-06*@0*@0*@0) + (-8.19429e-09*@0*@0*@0*@0) + (4.75955e-12*@0*@0*@0*@0*@0)";
        if (ch == 1) fss << "(-15.2189) + (0.442707*@0) + (-0.00452573*@0*@0) + (2.27111e-05*@0*@0*@0) + (-5.39753e-08*@0*@0*@0*@0) + (4.8518e-11*@0*@0*@0*@0*@0)";
        if (ch == 2) fss << "(-23.0489) + (0.624282*@0) + (-0.00621035*@0*@0) + (2.9971e-05*@0*@0*@0) + (-6.8571e-08*@0*@0*@0*@0) + (5.95102e-11*@0*@0*@0*@0*@0)";
        if (ch == 3) fss << "(-23.0489) + (0.624282*@0) + (-0.00621035*@0*@0) + (2.9971e-05*@0*@0*@0) + (-6.8571e-08*@0*@0*@0*@0) + (5.95102e-11*@0*@0*@0*@0*@0)";
      }
    }
    else {
      if (do7TeV) {
        if (ch == 0) fss << "(-92.01) + (0.36984*@0) + (-0.000483809*@0*@0) + (3.35801e-07*@0*@0*@0)";
        if (ch == 1) fss << "(132.52) + (-0.797134*@0) + (0.00144076*@0*@0) + (-6.8979e-07*@0*@0*@0)";
        if (ch == 2) fss << "(41.2978) + (-0.237919*@0) + (0.000343944*@0*@0) + (-1.18454e-08*@0*@0*@0)";
        if (ch == 3) fss << "(41.2978) + (-0.237919*@0) + (0.000343944*@0*@0) + (-1.18454e-08*@0*@0*@0)";
      }
      else {
        if (ch == 0) fss << "(151.967) + (-0.939938*@0) + (0.00173551*@0*@0) + (-8.26677e-07*@0*@0*@0)";
        if (ch == 1) fss << "(107.493) + (-0.624171*@0) + (0.0010989*@0*@0) + (-4.61003e-07*@0*@0*@0)";
        if (ch == 2) fss << "(225.609) + (-1.28759*@0) + (0.00224219*@0*@0) + (-1.0702e-06*@0*@0*@0)";
        if (ch == 3) fss << "(225.609) + (-1.28759*@0) + (0.00224219*@0*@0) + (-1.0702e-06*@0*@0*@0)";
      }
    }
    
    if (m<400.) {
        if (ch == 0 || ch == 1) fss << " ) * (1+@1)";
        else                    fss << " ) * (1+@1)";
    }
    return fss.str();
}

std::string getSignalCBAlphaLString(float m, int ch, bool do7TeV) {
    stringstream fss;
   
    if (m<400.) {
      if (do7TeV) {
        if (ch == 0) fss << "(-16.9313) + (0.451691*@0) + (-0.00425974*@0*@0) + (1.91392e-05*@0*@0*@0) + (-4.09456e-08*@0*@0*@0*@0) + (3.3503e-11*@0*@0*@0*@0*@0)";
        if (ch == 1) fss << "(-21.6016) + (0.602213*@0) + (-0.00620193*@0*@0) + (3.03257e-05*@0*@0*@0) + (-7.05553e-08*@0*@0*@0*@0) + (6.28615e-11*@0*@0*@0*@0*@0)";
        if (ch == 2) fss << "(-19.1247) + (0.511858*@0) + (-0.00507084*@0*@0) + (2.40314e-05*@0*@0*@0) + (-5.4294e-08*@0*@0*@0*@0) + (4.70018e-11*@0*@0*@0*@0*@0)";
        if (ch == 3) fss << "(-19.1247) + (0.511858*@0) + (-0.00507084*@0*@0) + (2.40314e-05*@0*@0*@0) + (-5.4294e-08*@0*@0*@0*@0) + (4.70018e-11*@0*@0*@0*@0*@0)";
      }
      else {
        if (ch == 0) fss << "(-6.83599) + (0.196814*@0) + (-0.00179054*@0*@0) + (7.59602e-06*@0*@0*@0) + (-1.48893e-08*@0*@0*@0*@0) + (1.07477e-11*@0*@0*@0*@0*@0)";
        if (ch == 1) fss << "(-22.3693) + (0.627422*@0) + (-0.0064991*@0*@0) + (3.20674e-05*@0*@0*@0) + (-7.51115e-08*@0*@0*@0*@0) + (6.71038e-11*@0*@0*@0*@0*@0)";
        if (ch == 2) fss << "(-14.5509) + (0.395116*@0) + (-0.00385822*@0*@0) + (1.78522e-05*@0*@0*@0) + (-3.88799e-08*@0*@0*@0*@0) + (3.20036e-11*@0*@0*@0*@0*@0)";
        if (ch == 3) fss << "(-14.5509) + (0.395116*@0) + (-0.00385822*@0*@0) + (1.78522e-05*@0*@0*@0) + (-3.88799e-08*@0*@0*@0*@0) + (3.20036e-11*@0*@0*@0*@0*@0)";
      }
    }
    else {
      if (do7TeV) {
        if (ch == 0) fss << "(2.17096) + (-0.00111638*@0)";
        if (ch == 1) fss << "(2.01281) + (-0.00136512*@0)";
        if (ch == 2) fss << "(1.94522) + (-0.0012104*@0)";
        if (ch == 3) fss << "(1.94522) + (-0.0012104*@0)";
      }
      else {
        if (ch == 0) fss << "(1.6377) + (-0.000344394*@0)";
        if (ch == 1) fss << "(0.807196) + (0.000324715*@0)";
        if (ch == 2) fss << "(1.26942) + (-0.000113644*@0)";
        if (ch == 3) fss << "(1.26942) + (-0.000113644*@0)";
      }
    }

    return fss.str();
}

std::string getSignalCBNLString(float m, int ch, bool do7TeV) {
    stringstream fss;

    if (m<400.) {
      if (do7TeV) {
        if (ch == 0) fss << "TMath::Max((46.8517) + (-1.07861*@0) + (0.0100183*@0*@0) + (-4.47408e-05*@0*@0*@0) + (9.58959e-08*@0*@0*@0*@0) + (-7.92287e-11*@0*@0*@0*@0*@0),1)";
        if (ch == 1) fss << "TMath::Max((-261.056) + (5.8594*@0) + (-0.047926*@0*@0) + (0.000186032*@0*@0*@0) + (-3.48259e-07*@0*@0*@0*@0) + (2.53758e-10*@0*@0*@0*@0*@0),1)";
        if (ch == 2) fss << "TMath::Max((-80.2755) + (1.92682*@0) + (-0.0163889*@0*@0) + (6.61152e-05*@0*@0*@0) + (-1.29134e-07*@0*@0*@0*@0) + (9.86492e-11*@0*@0*@0*@0*@0),1)";
        if (ch == 3) fss << "TMath::Max((-80.2755) + (1.92682*@0) + (-0.0163889*@0*@0) + (6.61152e-05*@0*@0*@0) + (-1.29134e-07*@0*@0*@0*@0) + (9.86492e-11*@0*@0*@0*@0*@0),1)";
      }
      else {
        if (ch == 0) fss << "TMath::Max((24.2026) + (-0.5443*@0) + (0.00517101*@0*@0) + (-2.3485e-05*@0*@0*@0) + (5.07143e-08*@0*@0*@0*@0) + (-4.18694e-11*@0*@0*@0*@0*@0),1)";
        if (ch == 1) fss << "TMath::Max((-197.954) + (4.6367*@0) + (-0.0391504*@0*@0) + (0.000155755*@0*@0*@0) + (-2.97342e-07*@0*@0*@0*@0) + (2.20176e-10*@0*@0*@0*@0*@0),1)";
        if (ch == 2) fss << "TMath::Max((4.71546) + (-0.174103*@0) + (0.00338962*@0*@0) + (-2.3452e-05*@0*@0*@0) + (6.66662e-08*@0*@0*@0*@0) + (-6.68915e-11*@0*@0*@0*@0*@0),1)";
        if (ch == 3) fss << "TMath::Max((4.71546) + (-0.174103*@0) + (0.00338962*@0*@0) + (-2.3452e-05*@0*@0*@0) + (6.66662e-08*@0*@0*@0*@0) + (-6.68915e-11*@0*@0*@0*@0*@0),1)";
      }
    }
    else {
      if (do7TeV) {
        if (ch == 0) fss << "TMath::Max((22.7304) + (-0.0769053*@0) + (0.000125898*@0*@0) + (-6.21946e-08*@0*@0*@0),1)";
        if (ch == 1) fss << "TMath::Max((-64.4151) + (0.302132*@0) + (-0.000401769*@0*@0) + (1.75386e-07*@0*@0*@0),1)";
        if (ch == 2) fss << "TMath::Max((-27.4789) + (0.146712*@0) + (-0.000188824*@0*@0) + (7.99675e-08*@0*@0*@0),1)";
        if (ch == 3) fss << "TMath::Max((-27.4789) + (0.146712*@0) + (-0.000188824*@0*@0) + (7.99675e-08*@0*@0*@0),1)";
      }
      else {
        if (ch == 0) fss << "TMath::Max((-9.1524) + (0.0730485*@0) + (-9.1524e-05*@0*@0) + (3.76554e-08*@0*@0*@0),1)";
        if (ch == 1) fss << "TMath::Max((-15.5676) + (0.0957725*@0) + (-0.000117759*@0*@0) + (4.75733e-08*@0*@0*@0),1)";
        if (ch == 2) fss << "TMath::Max((-5.08746) + (0.0588206*@0) + (-7.53751e-05*@0*@0) + (3.17173e-08*@0*@0*@0),1)";
        if (ch == 3) fss << "TMath::Max((-5.08746) + (0.0588206*@0) + (-7.53751e-05*@0*@0) + (3.17173e-08*@0*@0*@0),1)";
      }
    }

    return fss.str();
}

std::string getSignalCBAlphaRString(float m, int ch, bool do7TeV) {
    stringstream fss;

    if (m<400.) {
      if (do7TeV) {
        if (ch == 0) fss << "(-4.46307) + (0.166093*@0) + (-0.00176293*@0*@0) + (8.94642e-06*@0*@0*@0) + (-2.13451e-08*@0*@0*@0*@0) + (1.91314e-11*@0*@0*@0*@0*@0)";
        if (ch == 1) fss << "(110.088) + (-2.74006*@0) + (0.0263436*@0*@0) + (-0.000120005*@0*@0*@0) + (2.59845e-07*@0*@0*@0*@0) + (-2.1514e-10*@0*@0*@0*@0*@0)";
        if (ch == 2) fss << "(2.83488) + (-0.0208357*@0) + (8.703e-05*@0*@0)";
        if (ch == 3) fss << "(2.83488) + (-0.0208357*@0) + (8.703e-05*@0*@0)";
      }
      else {
        if (ch == 0) fss << "(-26.1111) + (0.767139*@0) + (-0.00830412*@0*@0) + (4.35986e-05*@0*@0*@0) + (-1.10717e-07*@0*@0*@0*@0) + (1.09256e-10*@0*@0*@0*@0*@0)";
        if (ch == 1) fss << "(-33.5339) + (0.956795*@0) + (-0.0100707*@0*@0) + (4.99974e-05*@0*@0*@0) + (-1.15201e-07*@0*@0*@0*@0) + (9.94549e-11*@0*@0*@0*@0*@0)";
        if (ch == 2) fss << "(-6.15641) + (0.244828*@0) + (-0.00311039*@0*@0) + (1.8662e-05*@0*@0*@0) + (-5.19696e-08*@0*@0*@0*@0) + (5.39877e-11*@0*@0*@0*@0*@0)";
        if (ch == 3) fss << "(-6.15641) + (0.244828*@0) + (-0.00311039*@0*@0) + (1.8662e-05*@0*@0*@0) + (-5.19696e-08*@0*@0*@0*@0) + (5.39877e-11*@0*@0*@0*@0*@0)";
      }
    }
    else {
      if (do7TeV) {
        if (ch == 0) fss << "(0.965224) + (9.63026e-05*@0)";
        if (ch == 1) fss << "(4.49443) + (-0.00436133*@0)";
        if (ch == 2) fss << "(0.878941) + (0.000326235*@0)";
        if (ch == 3) fss << "(0.878941) + (0.000326235*@0)";
      }
      else {
        if (ch == 0) fss << "(15.6515) + (-0.0460885*@0) + (3.61238e-05*@0*@0)";
        if (ch == 1) fss << "(16.0914) + (-0.0433479*@0) + (3.09642e-05*@0*@0)";
        if (ch == 2) fss << "(5.48901) + (-0.0144101*@0) + (1.15529e-05*@0*@0)";
        if (ch == 3) fss << "(5.48901) + (-0.0144101*@0) + (1.15529e-05*@0*@0)";
      }
    }

    return fss.str();
}

std::string getSignalCBNRString(float m, int ch, bool do7TeV) {
    stringstream fss;
    
    if (m<400.) {
      if (do7TeV) {
        if (ch == 0) fss << "20";
        if (ch == 1) fss << "20";
        if (ch == 2) fss << "20";
        if (ch == 3) fss << "20";
      }
      else {
        if (ch == 0) fss << "20";
        if (ch == 1) fss << "20";
        if (ch == 2) fss << "20";
        if (ch == 3) fss << "20";
      }
    }
    else {
      if (do7TeV) {
        if (ch == 0) fss << "20";
        if (ch == 1) fss << "20";
        if (ch == 2) fss << "20";
        if (ch == 3) fss << "20";
      }
      else {
        if (ch == 0) fss << "20";
        if (ch == 1) fss << "20";
        if (ch == 2) fss << "20";
        if (ch == 3) fss << "20";
      }
    }

    return fss.str();
}


std::string getSignalBWGammaString(float m, int ch, bool do7TeV) {
    stringstream fss;
    fss << "( ";  

    if (do7TeV) {
      if (ch == 0) fss << "TMath::Max((185.192) + (-1.15885*@0) + (0.0025093*@0*@0) + (-1.44677e-06*@0*@0*@0),30)";
      if (ch == 1) fss << "TMath::Max((-374.291) + (1.52069*@0) + (-0.00153017*@0*@0) + (4.37304e-07*@0*@0*@0),30)";
      if (ch == 2) fss << "TMath::Max((59.6861) + (-0.59096*@0) + (0.00169122*@0*@0) + (-1.05572e-06*@0*@0*@0),30)";
      if (ch == 3) fss << "TMath::Max((59.6861) + (-0.59096*@0) + (0.00169122*@0*@0) + (-1.05572e-06*@0*@0*@0),30)";
    }
    else {
      if (ch == 0) fss << "TMath::Max((-204.695) + (1.06734*@0) + (-0.00151823*@0*@0) + (7.88569e-07*@0*@0*@0),30)";
      if (ch == 1) fss << "TMath::Max((-446.657) + (2.13856*@0) + (-0.00298553*@0*@0) + (1.4181e-06*@0*@0*@0),30)";
      if (ch == 2) fss << "TMath::Max((-559.553) + (2.68625*@0) + (-0.00383806*@0*@0) + (1.84304e-06*@0*@0*@0),30)";
      if (ch == 3) fss << "TMath::Max((-559.553) + (2.68625*@0) + (-0.00383806*@0*@0) + (1.84304e-06*@0*@0*@0),30)";
    }

    fss << " ) * (1+@1)";    
    return fss.str();
}

std::string getSignalEBELandauMeanString(int ch, bool do7TeV) {
  stringstream fss;
  if (do7TeV) {
    if (ch == 0) fss << "(0.0134009) + (-8.01228e-05*@0) + (2.77214e-07*@0*@0)";
    if (ch == 1) fss << "(-0.00687259) + (0.000211674*@0) + (-7.26176e-07*@0*@0)";
    if (ch == 2) fss << "(0.0210129) + (-0.000220759*@0) + (8.7588e-07*@0*@0)";
    if (ch == 3) fss << "(0.0210129) + (-0.000220759*@0) + (8.7588e-07*@0*@0)";
  } 
  else {
    if (ch == 0) fss << "(0.146537) + (-0.00221371*@0) + (8.81577e-06*@0*@0)";
    if (ch == 1) fss << "(0.00798885) + (2.07364e-05*@0) + (-7.68043e-08*@0*@0)";
    if (ch == 2) fss << "(-0.0303858) + (0.000587672*@0) + (-2.21995e-06*@0*@0)";
    if (ch == 3) fss << "(-0.0303858) + (0.000587672*@0) + (-2.21995e-06*@0*@0)";
  } 
  return fss.str();
}

std::string getSignalEBELandauSigmaString(int ch, bool do7TeV) {
  stringstream fss;
  if (do7TeV) {
    if (ch == 0) fss << "(-0.00408833) + (8.28301e-05*@0) + (-3.23195e-07*@0*@0)";
    if (ch == 1) fss << "(0.000955492) + (7.11031e-06*@0) + (-3.35679e-08*@0*@0)";
    if (ch == 2) fss << "(0.00379671) + (-4.41107e-05*@0) + (1.7516e-07*@0*@0)";
    if (ch == 3) fss << "(0.00379671) + (-4.41107e-05*@0) + (1.7516e-07*@0*@0)";
  } 
  else {
    if (ch == 0) fss << "(-0.00136417) + (3.93313e-05*@0) + (-1.5185e-07*@0*@0)";
    if (ch == 1) fss << "(0.0040108) + (-3.60197e-05*@0) + (1.16329e-07*@0*@0)";
    if (ch == 2) fss << "(-0.0164325) + (0.000268018*@0) + (-1.00625e-06*@0*@0)";
    if (ch == 3) fss << "(-0.0164325) + (0.000268018*@0) + (-1.00625e-06*@0*@0)";
  } 
  return fss.str();
}

std::string getSignalEBELogNMeanString(int ch, bool do7TeV) {
  stringstream fss;
  if (do7TeV) {
    if (ch == 0) fss << "(0.0134009) + (-8.01228e-05*@0) + (2.77214e-07*@0*@0)";
    if (ch == 1) fss << "ERROR! not a log normal for 4e!";
    if (ch == 2) fss << "ERROR! not a log normal for 2e2mu!";
    if (ch == 3) fss << "ERROR! not a log normal for 2mu2e!";
  } 
  else {
    if (ch == 0) fss << "(0.146537) + (-0.00221371*@0) + (8.81577e-06*@0*@0)";
    if (ch == 1) fss << "ERROR! not a log normal for 4e!";
    if (ch == 2) fss << "ERROR! not a log normal for 2e2mu!";
    if (ch == 3) fss << "ERROR! not a log normal for 2mu2e!";
  } 
  return fss.str();
}

std::string getSignalEBELogNKString(int ch, bool do7TeV) {
  stringstream fss;
  if (do7TeV) {
    if (ch == 0) fss << "(1.09548) + (-0.00429616*@0) + (1.42497e-05*@0*@0)";
    if (ch == 1) fss << "ERROR! not a log normal for 4e!";
    if (ch == 2) fss << "ERROR! not a log normal for 2e2mu!";
    if (ch == 3) fss << "ERROR! not a log normal for 2e2mu!";
  } 
  else {
    if (ch == 0) fss << "(1.35325) + (-0.00927874*@0) + (3.68071e-05*@0*@0)";
    if (ch == 1) fss << "ERROR! not a log normal for 4e!";
    if (ch == 2) fss << "ERROR! not a log normal for 2e2mu!";
    if (ch == 3) fss << "ERROR! not a log normal for 2mu2e!";
  } 
  return fss.str();
}

std::string getSignalEBEGaussianMeanString(int ch, bool do7TeV) {
  stringstream fss;
  if (do7TeV) {
    if (ch == 0) fss << "ERROR! not a Gaussian for 4mu!";
    if (ch == 1) fss << "(0.0792865) + (-0.00094503*@0) + (3.55867e-06*@0*@0)";
    if (ch == 2) fss << "(0.0150001) + (-1.00122e-09*@0) + (3.89981e-12*@0*@0)";
    if (ch == 3) fss << "(0.0150001) + (-1.00122e-09*@0) + (3.89981e-12*@0*@0)";
  } 
  else {
    if (ch == 0) fss << "ERROR! not a Gaussian for 4mu!";
    if (ch == 1) fss << "(0.0481624) + (-0.00040788*@0) + (1.33567e-06*@0*@0)";
    if (ch == 2) fss << "(0.016304) + (1.22315e-05*@0) + (-1.4359e-07*@0*@0)";
    if (ch == 3) fss << "(0.016304) + (1.22315e-05*@0) + (-1.4359e-07*@0*@0)";
  } 
  return fss.str();
}

std::string getSignalEBEGaussianSigmaString(int ch, bool do7TeV) {
  stringstream fss;
  if (do7TeV) {
    if (ch == 0) fss << "ERROR! not a Gaussian for 4mu!";
    if (ch == 1) fss << "(0.00812389) + (-4.66255e-05*@0) + (1.55668e-07*@0*@0)";
    if (ch == 2) fss << "(0.00853809) + (-6.01857e-05*@0) + (1.93121e-07*@0*@0)";
    if (ch == 3) fss << "(0.00853809) + (-6.01857e-05*@0) + (1.93121e-07*@0*@0)";
  } 
  else {
    if (ch == 0) fss << "ERROR! not a Gaussian for 4mu!";
    if (ch == 1) fss << "(-0.00433283) + (0.000134763*@0) + (-5.13103e-07*@0*@0)";
    if (ch == 2) fss << "(0.00421353) + (4.27287e-06*@0) + (-5.9121e-08*@0*@0)";
    if (ch == 3) fss << "(0.00421353) + (4.27287e-06*@0) + (-5.9121e-08*@0*@0)";
  } 
  return fss.str();
}

std::string getSignalEBELandauFracString(int ch, bool do7TeV) {
  stringstream fss;
  if (do7TeV) {
    if (ch == 0) fss << "(-6.35246) + (0.106138*@0) + (-0.000406468*@0*@0)";
    if (ch == 1) fss << "(-2.63862) + (0.0528919*@0) + (-0.000210164*@0*@0)";
    if (ch == 2) fss << "(-0.142724) + (0.0132325*@0) + (-4.92025e-05*@0*@0)";
    if (ch == 3) fss << "(-0.142724) + (0.0132325*@0) + (-4.92025e-05*@0*@0)";
  } 
  else {
    if (ch == 0) fss << "(0.407962) + (0.00116124*@0) + (-7.66417e-07*@0*@0)";
    if (ch == 1) fss << "(0.414303) + (0.00661032*@0) + (-4.01388e-05*@0*@0)";
    if (ch == 2) fss << "(-0.565547) + (0.0204287*@0) + (-8.13434e-05*@0*@0)";
    if (ch == 3) fss << "(-0.565547) + (0.0204287*@0) + (-8.13434e-05*@0*@0)";
  } 
  return fss.str();
}

std::string getYieldEfficiencyString(float m, int ch, bool do7TeV) {
    stringstream fss;

        if (do7TeV) {
                if      (ch == 0) return "(-2.88111) + (0.0622853)*@0 + (-0.000462734)*@0*@0 + (1.86882e-06)*@0*@0*@0 + (-4.47457e-09)*@0*@0*@0*@0 + (6.54111e-12)*@0*@0*@0*@0*@0 + (-5.73716e-15)*@0*@0*@0*@0*@0*@0 + (2.77594e-18)*@0*@0*@0*@0*@0*@0*@0 + (-5.70027e-22)*@0*@0*@0*@0*@0*@0*@0*@0";
                else if (ch == 1) return "(-2.4738) + (0.0492514)*@0 + (-0.000352104)*@0*@0 + (1.38777e-06)*@0*@0*@0 + (-3.28968e-09)*@0*@0*@0*@0 + (4.82906e-12)*@0*@0*@0*@0*@0 + (-4.30705e-15)*@0*@0*@0*@0*@0*@0 + (2.1403e-18)*@0*@0*@0*@0*@0*@0*@0 + (-4.54497e-22)*@0*@0*@0*@0*@0*@0*@0*@0";
                else if (ch == 2) return "(-4.03012) + (0.0952339)*@0 + (-0.000820963)*@0*@0 + (3.75696e-06)*@0*@0*@0 + (-1.00155e-08)*@0*@0*@0*@0 + (1.60776e-11)*@0*@0*@0*@0*@0 + (-1.53023e-14)*@0*@0*@0*@0*@0*@0 + (7.94868e-18)*@0*@0*@0*@0*@0*@0*@0 + (-1.73493e-21)*@0*@0*@0*@0*@0*@0*@0*@0";
                else              return "(-1.60868) + (0.0276975)*@0 + (-0.000130818)*@0*@0 + (2.65285e-07)*@0*@0*@0 + (-6.41512e-11)*@0*@0*@0*@0 + (-6.90472e-13)*@0*@0*@0*@0*@0 + (1.26267e-15)*@0*@0*@0*@0*@0*@0 + (-9.16054e-19)*@0*@0*@0*@0*@0*@0*@0 + (2.48033e-22)*@0*@0*@0*@0*@0*@0*@0*@0";
        }
        else {
                if      (ch == 0) return "(-3.4992) + (0.0736735)*@0 + (-0.000550042)*@0*@0 + (2.21855e-06)*@0*@0*@0 + (-5.28463e-09)*@0*@0*@0*@0 + (7.66064e-12)*@0*@0*@0*@0*@0 + (-6.64183e-15)*@0*@0*@0*@0*@0*@0 + (3.16635e-18)*@0*@0*@0*@0*@0*@0*@0 + (-6.38457e-22)*@0*@0*@0*@0*@0*@0*@0*@0";
                else if (ch == 1) return "(-2.28779) + (0.0422891)*@0 + (-0.000271859)*@0*@0 + (9.3784e-07)*@0*@0*@0 + (-1.88777e-09)*@0*@0*@0*@0 + (2.27959e-12)*@0*@0*@0*@0*@0 + (-1.61928e-15)*@0*@0*@0*@0*@0*@0 + (6.19803e-19)*@0*@0*@0*@0*@0*@0*@0 + (-9.77706e-23)*@0*@0*@0*@0*@0*@0*@0*@0";
                else if (ch == 2) return "(-4.50592) + (0.103976)*@0 + (-0.000891562)*@0*@0 + (4.06841e-06)*@0*@0*@0 + (-1.08297e-08)*@0*@0*@0*@0 + (1.7376e-11)*@0*@0*@0*@0*@0 + (-1.65433e-14)*@0*@0*@0*@0*@0*@0 + (8.60202e-18)*@0*@0*@0*@0*@0*@0*@0 + (-1.8805e-21)*@0*@0*@0*@0*@0*@0*@0*@0";
                else              return "(-1.65737) + (0.0245722)*@0 + (-7.82617e-05)*@0*@0 + (-6.15927e-08)*@0*@0*@0 + (9.58005e-10)*@0*@0*@0*@0 + (-2.47158e-12)*@0*@0*@0*@0*@0 + (3.01807e-15)*@0*@0*@0*@0*@0*@0 + (-1.83102e-18)*@0*@0*@0*@0*@0*@0*@0 + (4.43981e-22)*@0*@0*@0*@0*@0*@0*@0*@0";
        }

}

std::string getYieldEfficiencyStringOfficial(float m, int ch, bool do7TeV) {
    stringstream fss;

    float a1 = 0.0;
    float a2 = 0.0;
    float a3 = 0.0;
    float a4 = 0.0;
    float b1 = 0.0;
    float b2 = 0.0;
    float b3 = 0.0;
    float g1 = 0.0;
    float g2 = 0.0;
    float g3 = 0.0;

    if (do7TeV) {

        if (ch == 0) {
            a1 = -4.39808;
            a2 = 4.64087;
            a3 = -79.9918;
            a4 = 117.213;
            b1 = 2.3748;
            b2 = 0.00116211;
            b3 = 2.8371e-07;
            g1 = 0.0230365;
            g2 = 187.957;
            g3 = 30;
        }

        else if (ch == 1) {
            a1 = -4.427;
            a2 = 4.61261;
            a3 = -63.4763;
            a4 = 111.314;
            b1 = 2.0858;
            b2 = 0.0018265;
            b3 = -1.6838e-07;
            g1 = 0.0139683;
            g2 = 194.418;
            g3 = 20.373;
        }

        else if (ch == 2) {
            a1 = -4.41001;
            a2 = 4.62925;
            a3 = -74.1568;
            a4 = 118.193;
            b1 = 2.28629;
            b2 = 0.00127503;
            b3 = 6.8788e-08;
            g1 = 0.000122206;
            g2 = 165.295;
            g3 = 20.5555;
        }

        else {
            a1 = -4.41001;
            a2 = 4.62925;
            a3 = -74.1568;
            a4 = 118.193;
            b1 = 2.28629;
            b2 = 0.00127503;
            b3 = 6.8788e-08;
            g1 = 0.000122206;
            g2 = 165.295;
            g3 = 20.5555;
        }


    }

    else {

        if (ch == 0) {
            a1 = -4.41793;
            a2 = 4.62153;
            a3 = -60.0558;
            a4 = 106.942;
            b1 = 2.55505;
            b2 = 0.00197459;
            b3 = -5.39188e-07;
            g1 = 0.026982;
            g2 = 189.743;
            g3 = 27.1286;
        }

        else if (ch == 1) {
            a1 = -4.28831;
            a2 = 4.74537;
            a3 = -130.478;
            a4 = 195.735;
            b1 = 0.802598;
            b2 = 0.000803703;
            b3 = -2.71801e-07;
            g1 = 0.0996699;
            g2 = 166.07;
            g3 = 43.7637;
        }

        else if (ch == 2) {
            a1 = -4.40203;
            a2 = 4.6367;
            a3 = -73.3644;
            a4 = 123.19;
            b1 = 1.95391;
            b2 = 0.00149841;
            b3 = -4.45075e-07;
            g1 = 0.0192592;
            g2 = 184.301;
            g3 = 20;
        }

        else {
            a1 = -4.40203;
            a2 = 4.6367;
            a3 = -73.3644;
            a4 = 123.19;
            b1 = 1.95391;
            b2 = 0.00149841;
            b3 = -4.45075e-07;
            g1 = 0.0192592;
            g2 = 184.301;
            g3 = 20;
        }

    }

    //(a1+a2*TMath::Erf((@0-a3)/a4))*(b1+b2*@0+b3*@0*@0)+g1*TMath::Gaus(@0,g2,@g3)

    fss << "("<< a1 << "+" << "("<<a2<<")" << "*TMath::Erf((@0-" << "("<<a3<<")" << ")/" << "("<<a4<<")" << "))*(" << "("<<b1<<")" << "+" << "("<<b2<<")" << "*@0+" << "("<<b3<<")" << "*@0*@0)+" << "("<<g1<<")" << "*TMath::Gaus(@0," << g2 << "," << g3 << ")";

    return fss.str();
}


//**************************************************************
// Signal Efficiency After requiring MELA > 0.5
// Only use for MH below 160 GeV.
//**************************************************************
std::string getYieldAfterMelaCutEfficiencyString(float m, int ch, bool do7TeV) {
    stringstream fss;

    if (do7TeV) {
      if      (ch == 0) return "(2.18631) + (-0.0516415)*@0 + (0.000425474)*@0*@0 + (-1.09444e-06)*@0*@0*@0";
      else if (ch == 1) return "(2.64613) + (-0.0620898)*@0 + (0.000487386)*@0*@0 + (-1.2107e-06)*@0*@0*@0";
      else if (ch == 2) return "(4.67907) + (-0.107809)*@0 + (0.000837657)*@0*@0 + (-2.09664e-06)*@0*@0*@0";
      else              return "(4.67907) + (-0.107809)*@0 + (0.000837657)*@0*@0 + (-2.09664e-06)*@0*@0*@0";
      
    }
    else {
        if      (ch == 0) return "(0.721964) + (-0.0225676)*@0 + (0.00022874)*@0*@0 + (-6.49567e-07)*@0*@0*@0";
        else if (ch == 1) return "(2.82425) + (-0.0675405)*@0 + (0.000534755)*@0*@0 + (-1.34247e-06)*@0*@0*@0";
        else if (ch == 2) return "(1.96282) + (-0.0495243)*@0 + (0.000417514)*@0*@0 + (-1.08888e-06)*@0*@0*@0";
        else              return "(1.96282) + (-0.0495243)*@0 + (0.000417514)*@0*@0 + (-1.08888e-06)*@0*@0*@0";
    }

    return fss.str();
}

