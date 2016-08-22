import sys
import re

regex1 = re.compile(r'<div class="csl-entry">(.+)</div>')

for line in sys.stdin:
    mymatch = re.search(regex1,line)
    if mymatch:
        print('<p>' + str(mymatch.group(1)) + '</p>')
    else:
        print line
        
