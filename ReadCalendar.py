from rdflib import *

l501 = Namespace("http://courseweb.ischool.illinois.edu/lis/2016fa/lis501/")
event = Namespace("http://purl.org/NET/c4dm/event.owl#")
tl = Namespace("http://purl.org/NET/c4dm/timeline.owl#")
dc = Namespace("http://purl.org/dc/terms/")

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
	for o in mygraph.objects(weekstart[d], RDFS.label):
	      print str(o)
	for s in mygraph.objects(weekstart[d],dc.subject):
	      print str(s)
	 

