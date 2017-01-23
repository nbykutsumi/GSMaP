import subprocess
import myfunc.util as util

iYM       = [2000,5]
eYM       = [2000,5]
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

if   prdName == "standard":
  baseDir="/standard/%s/hourly"%(ver)
elif prdName == "standard_gauge":
  baseDir="/standard/%s/gauge_hr"%(ver)
elif prdName == "reanalysis":
  baseDir="/reanalysis/%s/hourly"%(ver)

obaseDir = "/data2/GSMaP" 

for year, mon in lYM:
  print year, mon
  target = "ftp://rainmap:Niskur+1404@hokusai.eorc.jaxa.jp/%s/%s/hourly/%04d/%02d"%(prdName, ver, year, mon)

  #s      = "wget -r -nH %s"%(target)
  s      = "wget -nv -r -nH %s -P %s"%(target, obaseDir)
  #print s
  p      =subprocess.call(s,  shell=True)
