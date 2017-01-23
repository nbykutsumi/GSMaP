from ftplib import FTP
import myfunc.util as util
import calendar
import os

iYM       = [2013, 12]
eYM       = iYM
#eYM       = [2008, 12]
lYM       = util.ret_lYM(iYM, eYM)
iDay      = 1
myid      = "rainmap"
mypass    = "Niskur+1404"


#prdName= "standard"
#prdName= "standard_gauge"
prdName= "reanalysis"
#prdName= "reanalysis_gauge"
#prdName= "standard.sateinfo"
ver    = "v6"
"""
v6
standard: 2014/03-
standard_gauge: 2014/03-
reanalysis: 2011/01-2014/02
reanalysis
"""

hostname  = "hokusai.eorc.jaxa.jp"

if   prdName == "standard":
  ibaseDir="/standard/%s/hourly"%(ver)
elif prdName == "standard_gauge":
  ibaseDir="/standard/%s/gauge_hr"%(ver)
elif prdName == "reanalysis":
  ibaseDir="/reanalysis/%s/hourly"%(ver)
elif prdName == "standard.sateinfo":
  ibaseDir="/standard/%s/sateinfo"%(ver)
else:
  raise Exception
#elif prdName == "reanalysis":


obaseDir = "/data2/GSMaP/%s/%s/hourly"%(prdName,ver)


#----------------------------------
def mk_dir(sodir):
  try:
    os.makedirs(sodir)
  except OSError:
    pass


ftp = FTP(hostname)
ftp.login(myid, mypass)

#----------------------------------
for YM in lYM:
  Year, Mon = YM
  eDay = calendar.monthrange(Year,Mon)[1]
  #lDay = range(1,eDay+1)
  lDay = [3]
  for Day in lDay:
    #--- path and directory: Remote -----------
    iDir = ibaseDir  + "/%04d/%02d/%02d"%(Year,Mon,Day)
    oDir = obaseDir  + "/%04d/%02d/%02d"%(Year,Mon,Day) 
    mk_dir(oDir)
    #--- list --------------
    lPath = ftp.nlst(iDir)
    for sPath in lPath:
      if sPath[-3:] ==".gz":
        oPath = oDir + "/" + sPath.split("/")[-1]
        ftp.retrbinary("RETR %s"%(sPath), open(oPath,"wb").write)
        print oPath
     
ftp.close()

