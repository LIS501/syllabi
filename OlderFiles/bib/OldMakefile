
# Start by clearing the list of suffixes
.SUFFIXES:
# Then specify our suffixes
.SUFFIXES: .tex .dvi .bib .pdf .sgml .html .md


All: Approaches Collections Evaluation General Introduction Identity Preservation Research Search Structures SubjLanguages UseUsers LIS501

Approaches: 
	curl 'https://api.zotero.org/groups/344216/collections/TKFSRD56/items/top?start=0&limit=95&format=bibtex&v=1' > ApproachesBackground.bib
	curl 'https://api.zotero.org/groups/344216/collections/SCAZAMMH/items/top?start=0&limit=95&format=bibtex&v=1' > ApproachesRequired.bib
	curl 'https://api.zotero.org/groups/344216/collections/TKFSRD56/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o ApproachesBackground.md
	curl 'https://api.zotero.org/groups/344216/collections/SCAZAMMH/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o  ApproachesRequired.md

Collections: 
	curl 'https://api.zotero.org/groups/344216/collections/Z8V7XKUD/items/top?start=0&limit=95&format=bibtex&v=1' > CollectionsBackground.bib
	curl 'https://api.zotero.org/groups/344216/collections/IND4XSQX/items/top?start=0&limit=95&format=bibtex&v=1' > CollectionsRequired.bib
	curl 'https://api.zotero.org/groups/344216/collections/Z8V7XKUD/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o CollectionsBackground.md
	curl 'https://api.zotero.org/groups/344216/collections/IND4XSQX/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o CollectionsRequired.md

Evaluation: 
	curl 'https://api.zotero.org/groups/344216/collections/GK7SVKMJ/items/top?start=0&limit=95&format=bibtex&v=1' > EvaluationBackground.bib
	curl 'https://api.zotero.org/groups/344216/collections/665399P8/items/top?start=0&limit=95&format=bibtex&v=1' > EvaluationRequired.bib
	curl 'https://api.zotero.org/groups/344216/collections/GK7SVKMJ/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o EvaluationBackground.md
	curl 'https://api.zotero.org/groups/344216/collections/665399P8/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o EvaluationRequired.md

General: 
	curl 'https://api.zotero.org/groups/344216/collections/P9XVEEDG/items/top?start=0&limit=95&format=bibtex&v=1' > GeneralBackground.bib
	curl 'https://api.zotero.org/groups/344216/collections/P9XVEEDG/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o GeneralBackground.md

Introduction: 
	curl 'https://api.zotero.org/groups/344216/collections/2B5TZR74/items/top?start=0&limit=95&format=bibtex&v=1' > IntroductionBackground.bib
	curl 'https://api.zotero.org/groups/344216/collections/M4VAFZ3G/items/top?start=0&limit=95&format=bibtex&v=1' > IntroductionRequired.bib
	curl 'https://api.zotero.org/groups/344216/collections/2B5TZR74/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o IntroductionBackground.md
	curl 'https://api.zotero.org/groups/344216/collections/M4VAFZ3G/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o IntroductionRequired.md

Identity: 
	curl 'https://api.zotero.org/groups/344216/collections/T3T95I4B/items/top?start=0&limit=95&format=bibtex&v=1' > IdentityBackground.bib
	curl 'https://api.zotero.org/groups/344216/collections/F6WM8HP8/items/top?start=0&limit=95&format=bibtex&v=1' > IdentityRequired.bib
	curl 'https://api.zotero.org/groups/344216/collections/T3T95I4B/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o IdentityBackground.md
	curl 'https://api.zotero.org/groups/344216/collections/F6WM8HP8/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o IdentityRequired.md

Preservation: 
	curl 'https://api.zotero.org/groups/344216/collections/QB399RJC/items/top?start=0&limit=95&format=bibtex&v=1' > PreservationBackground.bib
	curl 'https://api.zotero.org/groups/344216/collections/8DH6TR78/items/top?start=0&limit=95&format=bibtex&v=1' > PreservationRequired.bib
	curl 'https://api.zotero.org/groups/344216/collections/QB399RJC/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o PreservationBackground.md
	curl 'https://api.zotero.org/groups/344216/collections/8DH6TR78/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o PreservationRequired.md

Research: 
	curl 'https://api.zotero.org/groups/344216/collections/7TJ9WWEE/items/top?start=0&limit=95&format=bibtex&v=1' > ResearchBackground.bib
	curl 'https://api.zotero.org/groups/344216/collections/HK7PM5MN/items/top?start=0&limit=95&format=bibtex&v=1' > ResearchRequired.bib
	curl 'https://api.zotero.org/groups/344216/collections/7TJ9WWEE/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o ResearchBackground.md
	curl 'https://api.zotero.org/groups/344216/collections/HK7PM5MN/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o ResearchRequired.md

Search: 
	curl 'https://api.zotero.org/groups/344216/collections/VQR3IP7Q/items/top?start=0&limit=95&format=bibtex&v=1' > SearchBackground.bib
	curl 'https://api.zotero.org/groups/344216/collections/IPSBZMD8/items/top?start=0&limit=95&format=bibtex&v=1' > SearchRequired.bib
	curl 'https://api.zotero.org/groups/344216/collections/VQR3IP7Q/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o SearchBackground.md
	curl 'https://api.zotero.org/groups/344216/collections/IPSBZMD8/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o SearchRequired.md

Structures: 
	curl 'https://api.zotero.org/groups/344216/collections/EXRP2V7P/items/top?start=0&limit=95&format=bibtex&v=1' > StructuresBackground.bib
	curl 'https://api.zotero.org/groups/344216/collections/39669DZH/items/top?start=0&limit=95&format=bibtex&v=1' > StructuresRequired.bib
	curl 'https://api.zotero.org/groups/344216/collections/EXRP2V7P/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o StructuresBackground.md
	curl 'https://api.zotero.org/groups/344216/collections/39669DZH/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o StructuresRequired.md

SubjAnalysis: 
	curl 'https://api.zotero.org/groups/344216/collections/VKJ9KXK2/items/top?start=0&limit=95&format=bibtex&v=1' > SubjAnalysisBackground.bib
	curl 'https://api.zotero.org/groups/344216/collections/3U7AKIUM/items/top?start=0&limit=95&format=bibtex&v=1' > SubjAnalysisRequired.bib
	curl 'https://api.zotero.org/groups/344216/collections/VKJ9KXK2/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o SubjAnalysisBackground.md
	curl 'https://api.zotero.org/groups/344216/collections/3U7AKIUM/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o SubjAnalysisRequired.md

SubjLanguages: 
	curl 'https://api.zotero.org/groups/344216/collections/2GH7KA69/items/top?start=0&limit=95&format=bibtex&v=1' > SubjLanguagesBackground.bib
	curl 'https://api.zotero.org/groups/344216/collections/EZC36Z9N/items/top?start=0&limit=95&format=bibtex&v=1' > SubjLanguagesRequired.bib
	curl 'https://api.zotero.org/groups/344216/collections/2GH7KA69/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o SubjLanguagesBackground.md
	curl 'https://api.zotero.org/groups/344216/collections/EZC36Z9N/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o SubjLanguagesRequired.md

UseUsers: 
	curl 'https://api.zotero.org/groups/344216/collections/ACJIKKDC/items/top?start=0&limit=95&format=bibtex&v=1' > UseUsersBackground.bib
	curl 'https://api.zotero.org/groups/344216/collections/3QGWRGMI/items/top?start=0&limit=95&format=bibtex&v=1' > UseUsersRequired.bib
	curl 'https://api.zotero.org/groups/344216/collections/ACJIKKDC/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o UseUsersBackground.md
	curl 'https://api.zotero.org/groups/344216/collections/3QGWRGMI/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o UseUsersRequired.md

LIS501: 
	cat *.bib > LIS501.bibtex
	curl 'https://api.zotero.org/groups/344216/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o LIS501.md

Test: 
	curl 'https://api.zotero.org/groups/344216/collections/3QGWRGMI/items/top?format=bib&v=1'|python filter1.py > test1.html
	cat test1.html|pandoc -f html -o test1.md

