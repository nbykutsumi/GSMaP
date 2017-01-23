import subprocess

iyear  = 2005
eyear  = 2008
imon   = 1
emon   = 12

for year in range(iyear, eyear+1):
  for mon in range(imon, emon+1):
    print year, mon
    target = "ftp://rainmap:amechi-zu@hokusai.eorc.jaxa.jp/standard/v5/sateinfo/%04d/%02d"%(year, mon)

    s      = "wget -r -nH %s"%(target)
    #print s
    p      =subprocess.call(s,  shell=True)
