
# Start by clearing the list of suffixes
.SUFFIXES:
# Then specify our suffixes
.SUFFIXES: .tex .dvi .bib .pdf .sgml .html .md


All: Approaches Collections Evaluation General Introduction Identity Preservation Research Search Structures SubjLanguages UseUsers LIS501

Approaches: 
	curl 'https://api.zotero.org/groups/344216/collections/TKFSRD56/items/top?start=0&limit=95&format=bibtex&v=1' > ApproachesBackground.bib
	curl 'https://api.zotero.org/groups/344216/collections/SCAZAMMH/items/top?start=0&limit=95&format=bibtex&v=1' > ApproachesRequired.bib

Collections: 
	curl 'https://api.zotero.org/groups/344216/collections/Z8V7XKUD/items/top?start=0&limit=95&format=bibtex&v=1' > CollectionsBackground.bib
	curl 'https://api.zotero.org/groups/344216/collections/IND4XSQX/items/top?start=0&limit=95&format=bibtex&v=1' > CollectionsRequired.bib

Evaluation: 
	curl 'https://api.zotero.org/groups/344216/collections/GK7SVKMJ/items/top?start=0&limit=95&format=bibtex&v=1' > EvaluationBackground.bib
	curl 'https://api.zotero.org/groups/344216/collections/665399P8/items/top?start=0&limit=95&format=bibtex&v=1' > EvaluationRequired.bib

General: 
	curl 'https://api.zotero.org/groups/344216/collections/P9XVEEDG/items/top?start=0&limit=95&format=bibtex&v=1' > GeneralBackground.bib

Introduction: 
	curl 'https://api.zotero.org/groups/344216/collections/2B5TZR74/items/top?start=0&limit=95&format=bibtex&v=1' > IntroductionBackground.bib
	curl 'https://api.zotero.org/groups/344216/collections/M4VAFZ3G/items/top?start=0&limit=95&format=bibtex&v=1' > IntroductionRequired.bib
	curl 'https://api.zotero.org/groups/344216/collections/2B5TZR74/items/top?format=bib&v=1'|pandoc -f html -o IntroductionBackground.md
	curl 'https://api.zotero.org/groups/344216/collections/M4VAFZ3G/items/top?format=bib&v=1'|pandoc -f html -o IntroductionRequired.md

Identity: 
	curl 'https://api.zotero.org/groups/344216/collections/T3T95I4B/items/top?start=0&limit=95&format=bibtex&v=1' > IdentityBackground.bib
	curl 'https://api.zotero.org/groups/344216/collections/F6WM8HP8/items/top?start=0&limit=95&format=bibtex&v=1' > IdentityRequired.bib

Preservation: 
	curl 'https://api.zotero.org/groups/344216/collections/QB399RJC/items/top?start=0&limit=95&format=bibtex&v=1' > PreservationBackground.bib
	curl 'https://api.zotero.org/groups/344216/collections/8DH6TR78/items/top?start=0&limit=95&format=bibtex&v=1' > PreservationRequired.bib

Research: 
	curl 'https://api.zotero.org/groups/344216/collections/7TJ9WWEE/items/top?start=0&limit=95&format=bibtex&v=1' > ResearchBackground.bib
	curl 'https://api.zotero.org/groups/344216/collections/HK7PM5MN/items/top?start=0&limit=95&format=bibtex&v=1' > ResearchRequired.bib

Search: 
	curl 'https://api.zotero.org/groups/344216/collections/VQR3IP7Q/items/top?start=0&limit=95&format=bibtex&v=1' > SearchBackground.bib
	curl 'https://api.zotero.org/groups/344216/collections/IPSBZMD8/items/top?start=0&limit=95&format=bibtex&v=1' > SearchRequired.bib

Structures: 
	curl 'https://api.zotero.org/groups/344216/collections/EXRP2V7P/items/top?start=0&limit=95&format=bibtex&v=1' > StructuresBackground.bib
	curl 'https://api.zotero.org/groups/344216/collections/39669DZH/items/top?start=0&limit=95&format=bibtex&v=1' > StructuresRequired.bib

SubjAnalysis: 
	curl 'https://api.zotero.org/groups/344216/collections/VKJ9KXK2/items/top?start=0&limit=95&format=bibtex&v=1' > SubjAnalysisBackground.bib
	curl 'https://api.zotero.org/groups/344216/collections/3U7AKIUM/items/top?start=0&limit=95&format=bibtex&v=1' > SubjAnalysisRequired.bib

SubjLanguages: 
	curl 'https://api.zotero.org/groups/344216/collections/2GH7KA69/items/top?start=0&limit=95&format=bibtex&v=1' > SubjLanguagesBackground.bib
	curl 'https://api.zotero.org/groups/344216/collections/EZC36Z9N/items/top?start=0&limit=95&format=bibtex&v=1' > SubjLanguagesRequired.bib

UseUsers: 
	curl 'https://api.zotero.org/groups/344216/collections/ACJIKKDC/items/top?start=0&limit=95&format=bibtex&v=1' > UseUsersBackground.bib
	curl 'https://api.zotero.org/groups/344216/collections/3QGWRGMI/items/top?start=0&limit=95&format=bibtex&v=1' > UseUsersRequired.bib

LIS501: 
	curl 'https://api.zotero.org/groups/344216/items/top?start=0&limit=95&format=bibtex&v=1' > LIS501.bib
