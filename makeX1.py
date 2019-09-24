#For basic execution. No POST, no GET. Good for programs without input.
import sys
inF = open(sys.argv[1],"r")

inTxt = inF.read()
inF.close()

outF = open(sys.argv[2],"w+")
outF.write("""#!/usr/bin/env python
import cgi
import cgitb
cgitb.enable()
print("Content-Type: text/html")
print("")
""")
outF.write(inTxt)
outF.close()

import os; os.system("chmod +x " + sys.argv[2])

