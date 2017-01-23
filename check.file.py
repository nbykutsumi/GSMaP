import os, sys
import calendar
from datetime import datetime, timedelta
import myfunc.IO.GSMaP as GSMaP
import myfunc.util as util

iYM       = [2009, 11]
eYM       = [2014, 2]
lYM       = util.ret_lYM(iYM, eYM)

#prdName= "standard"
#prdName= "standard_gauge"
prdName= "reanalysis"
#prdName= "reanalysis_gauge"
ver    = "v6"
"""
v6
standard: 2014/03-
standard_gauge: 2014/03-
reanalysis: 2011/01-2014/02
reanalysis
"""
gsmap   = GSMaP.GSMaP(prj=prdName, ver=ver)

baseDir = "/data2/GSMaP/%s/%s/hourly"%(prdName,ver)

for (Year,Mon) in lYM:
  print Year,Mon  
  eDay = calendar.monthrange(Year,Mon)[1]
  iDTime = datetime(Year,Mon,1,0)
  eDTime = datetime(Year,Mon,eDay,23)
  dDTime = timedelta(hours=1)
  lDTime = util.ret_lDTime(iDTime,eDTime,dDTime)
  for DTime in lDTime:
    try:
      srcPath = gsmap.ret_path(DTime)
    except IndexError:
      print "No file", DTime
      print srcPath
      continue
    #if not os.path.exists(srcPath):
    #  print srcPath
