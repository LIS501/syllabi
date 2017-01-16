
# Start by clearing the list of suffixes
.SUFFIXES:
# Then specify our suffixes
.SUFFIXES: .tex .dvi .bib .pdf .sgml .html .md


All: Approaches Documents Classification Collections Convenience Evaluation Interfaces Metadata Methods Overload Preservation Production Represent Searching Serendipity Social Specifying Standards Users LIS501

LIS501:
	curl 'https://api.zotero.org/groups/344216/collections/RQXF535V/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o LIS501.md

Databases:
	curl 'https://api.zotero.org/groups/344216/collections/7N9C63UF/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Databases.md

Documents: 
	curl 'https://api.zotero.org/groups/344216/collections/Q2ZIVKGF/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Documents.md

Collections: 
	curl 'https://api.zotero.org/groups/344216/collections/4HG4XXEC/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Collections.md

Searching: 
	curl 'https://api.zotero.org/groups/344216/collections/Q38UM56R/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Searching.md

Specifying:
	curl 'https://api.zotero.org/groups/344216/collections/I8BM3BUB/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Specifying.md

Serendipity:
	curl 'https://api.zotero.org/groups/344216/collections/NJVZICU3/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Serendipity.md

Interfaces:
	curl 'https://api.zotero.org/groups/344216/collections/EMNCQKV8/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Interfaces.md

Overload:
	curl 'https://api.zotero.org/groups/344216/collections/FPM97CXM/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Overload.md

Convenience:
	curl 'https://api.zotero.org/groups/344216/collections/WAE3FIFM/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Convenience.md

Users:
	curl 'https://api.zotero.org/groups/344216/collections/EF3NZUEH/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Users.md

Metadata:
	curl 'https://api.zotero.org/groups/344216/collections/MHQVQ5JS/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Metadata.md

Methods:
	curl 'https://api.zotero.org/groups/344216/collections/HSJKH49T/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Methods.md

Approaches:
	curl 'https://api.zotero.org/groups/344216/collections/RTXE688E/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Approaches.md

Classification:
	curl 'https://api.zotero.org/groups/344216/collections/NW6T54SW/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Classification.md

Represent:
	curl 'https://api.zotero.org/groups/344216/collections/HR2SVG4Z/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Represent.md

Standards:
	curl 'https://api.zotero.org/groups/344216/collections/DFTSHEQF/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Standards.md

Evaluation:
	curl 'https://api.zotero.org/groups/344216/collections/KAASH5AR/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Evaluation.md


Social: 
	curl 'https://api.zotero.org/groups/344216/collections/MW3WMQ42/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Social.md

Preservation: 
	curl 'https://api.zotero.org/groups/344216/collections/3N9T22FF/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Preservation.md

Production: 
	curl 'https://api.zotero.org/groups/344216/collections/JHUM5Q2Z/items/top?format=bib&v=1'|python filter1.py|pandoc -f html -o Production.md


Test: 
	curl 'https://api.zotero.org/groups/344216/collections/3QGWRGMI/items/top?format=bib&v=1'|python filter1.py > test1.html
	cat test1.html|pandoc -f html -o test1.md

