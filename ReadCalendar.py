from rdflib import *

l501 = Namespace("http://courseweb.ischool.illinois.edu/lis/2016fa/lis501/")
event = Namespace("http://purl.org/NET/c4dm/event.owl#")
tl = Namespace("http://purl.org/NET/c4dm/timeline.owl#")
dc = Namespace("http://purl.org/dc/terms/")
skos = Namespace("http://www.w3.org/2004/02/skos/core#")

mygraph = ConjunctiveGraph()
mygraph.parse("fall16calendar.ttl",format="n3")

wlist = []  # List of weeks
weekstart = {} # associate weeks with their starting date

for s in mygraph.subjects(RDF.type, l501.Week):
	for i in mygraph.objects(s,event.time):
	        for a in mygraph.objects(i,tl.at):
			    weekstart[str(a)] = s

wlist = weekstart.keys()
wlist.sort()				
for d in wlist:
        myweek = myconcept = required = background = ''
	for o in mygraph.objects(weekstart[d], RDFS.label):
	      myweek = str(o)
	for s in mygraph.objects(weekstart[d],dc.subject):
	      for p in mygraph.objects(s,skos.prefLabel):
                      myconcept = str(p)
                      for (q,r) in mygraph.predicate_objects(p):
                              background = q
                      for r in mygraph.objects(p,l501.reqReading):
                              required = r
        print myweek
        print myconcept
        print background
        print required
        
	 

