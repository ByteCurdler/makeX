#Provides the _POST and _GET dictionaries. Does not render "%xx" except "%0D%0A" (\r\n) as \n. Use makeX3 instead.
import sys
inF = open(sys.argv[1],"r")

inTxt = inF.read()
inF.close()

outF = open(sys.argv[2],"w+")
outF.write("""#!/usr/bin/env python
import cgi,sys,os
import cgitb
cgitb.enable()
print("Content-Type: text/html")
print("")
RAW_POST = sys.stdin.read()
_POST = {}
for i in RAW_POST.replace("%0D%0A","\\n").split("&"):
    if("=" in i):
        _POST.update({i.split("=")[0]:i.split("=")[1]})
    else:
        _POST.update({i:True})
if(_POST == {'':True}):
    _POST = {}
RAW_GET = os.getenv('QUERY_STRING')
_GET = {}
for i in RAW_GET.replace("%0D%0A","\\n").split("&"):
    if("=" in i):
        _GET.update({i.split("=")[0]:i.split("=")[1]})
    else:
        _GET.update({i:True})
if(_GET == {'':True}):
    _GET = {}
""")
outF.write(inTxt)
outF.close()

import os; os.system("chmod +x " + sys.argv[2])

