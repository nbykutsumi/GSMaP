import myfunc.util as util
import subprocess, os, sys
import calendar
import glob
iYM   = [2013,12]
eYM   = [2013,12]
ver   = "v6"

#prdName = "standard"
prdName = "reanalysis"
#prdName = "standard.sateinfo"
lYM = util.ret_lYM(iYM,eYM)

for year,mon in lYM:
  print year, mon
  for day in range(1, calendar.monthrange(year, mon)[1] +1):
    sidir  = "/data2/GSMaP/%s/%s/hourly/%04d/%02d/%02d"%(prdName,ver,year,mon,day)
    lfiles = glob.glob(sidir + "/*.gz")
    #lfiles = glob.glob(sidir + "/*.dat")
    for sfile in lfiles:
      if not os.path.exists(sfile):
        print "no file"
        print sfile
        sys.exit()
      s    = "gunzip %s"%(sfile)
      print s
      p      =subprocess.Popen(s,  shell=True, stdin=subprocess.PIPE)
      p.stdin.write('y')
