#!/usr/bin/python
from rdflib import *
import bibtexparser
import sys

calfilename = str(sys.argv[1])

l501 = Namespace("http://courseweb.ischool.illinois.edu/lis/2016fa/lis501/")
event = Namespace("http://purl.org/NET/c4dm/event.owl#")
tl = Namespace("http://purl.org/NET/c4dm/timeline.owl#")
dc = Namespace("http://purl.org/dc/terms/")
skos = Namespace("http://www.w3.org/2004/02/skos/core#")

mygraph = ConjunctiveGraph()
mygraph.parse(calfilename,format="n3")

wlist = []  # List of weeks
weekstart = {} # associate weeks with their starting date

for s in mygraph.subjects(RDF.type, l501.Week):
	for i in mygraph.objects(s,event.time):
	        for a in mygraph.objects(i,tl.at):
			    weekstart[str(a)] = s

print "# Topic Schedule"
                            
wlist = weekstart.keys()
wlist.sort()
weeknum = 0
for d in wlist:
        myweek = myconcept = required = background = ''
	for o in mygraph.objects(weekstart[d], RDFS.label):
	      myweek = str(o)
	for s in mygraph.objects(weekstart[d],dc.subject):
	      for p in mygraph.objects(s,skos.prefLabel):
                      myconcept = str(p)
                      for q in mygraph.objects(s,l501.backgroundReading):
                              background = str(q)[5:] + '.md'
                      for r in mygraph.objects(s,l501.reqReading):
                              required = str(r)[5:] + '.md'
        weeknum += 1
        weekdate = 'PRES' + str(weeknum) + 'DATE'
        print                      
        print "## " +  myweek + ", " + weekdate + ": " + myconcept
        print
        rstring = "### Required Readings "
        if required:
          print rstring
          with open(required, 'r') as md_file:
                  md_str = md_file.read()
                  print md_str
        bstring = "### Further Background "
        if background:
          print bstring
          with open(background, 'r') as md_file:
                  md_str = md_file.read()
                  print md_str



        
	 

