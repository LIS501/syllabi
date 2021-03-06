# Start by clearing the list of suffixes
.SUFFIXES:
# Then specify our suffixes
.SUFFIXES: .tex .dvi .bib .pdf .sgml .html .m4 .md

M4PATH := ./md
export M4PATH

%.md : %.m4 %.cldr %.defs IS501Spring2019.m4
	m4 -DFORMATDEFS="wpformat.m4" -DMYDEFS="$*.m4" IS501Spring2019.m4 > $*.md

%.docx : %.md
	pandoc -o $*.docx $*.md


%.cldr : %.ttl 
	python3 NewCalendar3.py $*.ttl

%.defs : %.ttl 
	python3 NewCalendar3.py $*.ttl

