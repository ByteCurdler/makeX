#    Provides the _POST and _GET dictionaries. Renders "%xx" and makes "%0D%0A" (\r\n) into \n. Use instead of makeX2.
#    _status(dct,value) returns True if value is a "flag", returns a str if value is an input, and returns False if
#value is nonexistent.
import sys
inF = open(sys.argv[1],"r")

inTxt = inF.read()
inF.close()

outF = open(sys.argv[2],"w+")
outF.write(u"""#!/usr/bin/env python
import cgi,sys,os
import cgitb
cgitb.enable()
print("Content-Type: text/html")
print("")

def _status(dct,value):
    if(value in dct):
        return dct[value]
    else:
        return False

def _cleanup(raw):
    ret = {}
    raw = raw.replace("+"," ")
    while "%" in raw:
        i = raw.index("%")
        char = chr(int(raw[i+1:i+3],16))
        if(raw[i:i+6] == "%0D%0A"):
            char = ""
        elif(char == "&"):
            char = "\x05"
        elif(char == "="):
            char = "\x04"
        elif(char == "%"):
            char = "\x03"
        raw = raw[:i] + char + raw[i+3:]
    for j in raw.split("&"):
        i = j.replace("\x05","&").replace("\x03","%")
        if("=" in i):
            ret.update({i.split("=")[0].replace("\x04","="):"=".join(i.split("=")[1:]).replace("\x04","=")})
        else:
            ret.update({i:True})
    if(ret == {'':True}):
        ret = {}
    return ret

RAW_POST = sys.stdin.read()
_POST = _cleanup(RAW_POST)

RAW_GET = os.getenv('QUERY_STRING')
_GET = _cleanup(RAW_GET)
""")
outF.write(inTxt)
outF.close()

import os; os.system("chmod +x " + sys.argv[2])

