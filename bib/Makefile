
# Start by clearing the list of suffixes
.SUFFIXES:
# Then specify our suffixes
.SUFFIXES: .tex .dvi .bib .pdf .sgml .html .md


All: Approaches Documents Classification Collections Convenience Evaluation General Interfaces Methods Overload Preservation Production Represent Research Searching Serendipity Social Specifying Standards Users LIS501

LIS501: 
	curl 'https://api.zotero.org/groups/344216/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o LIS501.md

Documents: 
	curl 'https://api.zotero.org/groups/344216/collections/TKFSRD56/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Documents.md

Collections: 
	curl 'https://api.zotero.org/groups/344216/collections/TKFSRD56/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Collections.md

Searching: 
	curl 'https://api.zotero.org/groups/344216/collections/TKFSRD56/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Searching.md

Specifying:
	curl 'https://api.zotero.org/groups/344216/collections/TKFSRD56/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Specifying.md

Serendipity:
	curl 'https://api.zotero.org/groups/344216/collections/Z8V7XKUD/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Serendipity.md

Interfaces:
	curl 'https://api.zotero.org/groups/344216/collections/Z8V7XKUD/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Interfaces.md

Overload:
	curl 'https://api.zotero.org/groups/344216/collections/Z8V7XKUD/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Overload.md

Convenience:
	curl 'https://api.zotero.org/groups/344216/collections/Z8V7XKUD/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Convenience.md

Users:
	curl 'https://api.zotero.org/groups/344216/collections/Z8V7XKUD/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Users.md

Methods:
	curl 'https://api.zotero.org/groups/344216/collections/IND4XSQX/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Methods.md

Approaches:
	curl 'https://api.zotero.org/groups/344216/collections/IND4XSQX/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Approaches.md

Classification:
	curl 'https://api.zotero.org/groups/344216/collections/IND4XSQX/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Classification.md

Represent:
	curl 'https://api.zotero.org/groups/344216/collections/IND4XSQX/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Represent.md

Standards:
	curl 'https://api.zotero.org/groups/344216/collections/IND4XSQX/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Standards.md

Evaluation:
	curl 'https://api.zotero.org/groups/344216/collections/IND4XSQX/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Evaluation.md


Social: 
	curl 'https://api.zotero.org/groups/344216/collections/TKFSRD56/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Social.md

Preservation: 
	curl 'https://api.zotero.org/groups/344216/collections/QB399RJC/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Preservation.md

Production: 
	curl 'https://api.zotero.org/groups/344216/collections/GK7SVKMJ/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Production.md


Test: 
	curl 'https://api.zotero.org/groups/344216/collections/3QGWRGMI/items/top?format=bib&v=1'|python filter1.py > test1.html
	cat test1.html|pandoc -f html -o test1.md

