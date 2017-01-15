#!/usr/bin/python
from rdflib import *
import bibtexparser
import sys
import re

ttlfilename = str(sys.argv[1])

project = ""
newdefs = {}
regex1 = re.compile(r"([^.]+)\.ttl")
mymatch = re.search(regex1,ttlfilename)
if mymatch:
        project = mymatch.group(1)

if project:
        cldrfilename = project + ".cldr"
        cldrfile = open(cldrfilename,"w")
        defsfilename = project + ".defs"
        defsfile = open(defsfilename,"w")

l501 = Namespace("http://courseweb.ischool.illinois.edu/lis/2017sp/lis501/")
event = Namespace("http://purl.org/NET/c4dm/event.owl#")
tl = Namespace("http://purl.org/NET/c4dm/timeline.owl#")
dc = Namespace("http://purl.org/dc/terms/")
skos = Namespace("http://www.w3.org/2004/02/skos/core#")

mygraph = ConjunctiveGraph()
mygraph.parse(ttlfilename,format="n3")

wlist = []  # List of sessions
sessionstart = {} # associate sessions with their starting date

for s in mygraph.subjects(RDF.type, l501.Session):
	for i in mygraph.objects(s,l501.date):
	    sessionstart[str(i)] = s
deadlines = {}
activities = {}

for d in mygraph.subjects(RDF.type, l501.Deadline):
                            sessiondue = sessiondate = duedate = dlabel = ""
                            for o in mygraph.objects(d,RDFS.label):
                                    dlabel = str(o)
                            for o in mygraph.objects(d,l501.during):
                                    sessiondue = o
                                    for p in mygraph.objects(o,l501.date):
                                        sessiondate = p
                            for o in mygraph.objects(d,l501.date):
                                    duedate = str(o)
                            deadlines[sessiondue] = dlabel + ", Due " + duedate
                            newdefs[duedate] = sessiondate 

for d in mygraph.subjects(RDF.type, l501.Activity):
                            sessiondue = sessiondate = duedate = dlabel = ""
                            for o in mygraph.objects(d,RDFS.label):
                                    dlabel = str(o)
                            for o in mygraph.objects(d,l501.during):
                                    sessiondue = o
                                    for p in mygraph.objects(o,l501.date):
                                        sessiondate = p
                            for o in mygraph.objects(d,l501.date):
                                    duedate = str(o)
                            activities[sessiondue] = dlabel + ", Due " + duedate
                            newdefs[duedate] = sessiondate 


                            
cldrfile.write("# Topic Schedule\n")

wlist = sessionstart.keys()
wlist.sort()
weeknum = 0
for d in wlist:
        myweek = myconcept = required = background  = ''
	for o in mygraph.objects(sessionstart[d], RDFS.label):
	      myweek = str(o)
	for s in mygraph.objects(sessionstart[d],dc.subject):
	      for p in mygraph.objects(s,skos.prefLabel):
                      myconcept = str(p)
                      for q in mygraph.objects(s,l501.backgroundReading):
                              background = str(q)
                      for r in mygraph.objects(s,l501.reqReading):
                              required = str(r)
        weeknum += 1
        weekdate = 'PRES' + str(weeknum) + 'DATE'
        cldrfile.write("\n")
        cldrfile.write("### " +  myweek + ": " + weekdate + ": " + myconcept + "\n")
        cldrfile.write("\n")
        rstring = "**Required Readings:** "
        if required:
          cldrfile.write(rstring + " " + required + "\n")
          cldrfile.write("\n")
        dstring = "**Due this week:** "
        if sessionstart[d] in deadlines.keys():
                cldrfile.write(dstring + " " + deadlines[sessionstart[d]] + "\n")
                cldrfile.write("\n")
        bstring = "**Further Background:** "
        if background:
          cldrfile.write(bstring + " " + background + "\n")
          cldrfile.write("\n")

if newdefs:
        for k in newdefs.keys():
                defsfile.write("define(" + k + ", " + newdefs[k] + ")dnl\n")

          
cldrfile.close()
defsfile.close()