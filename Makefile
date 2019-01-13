# Start by clearing the list of suffixes
.SUFFIXES:
# Then specify our suffixes
.SUFFIXES: .tex .dvi .bib .pdf .sgml .html .m4 .md

M4PATH := ./md
export M4PATH

%.md : %.m4 %.cldr %.defs IS501Spring2019.m4
	m4 -DFORMATDEFS="wpformat.m4" -DMYDEFS="$*.m4" LIS501Spring2017.m4 > $*.md

%.docx : %.md
	pandoc -o $*.docx $*.md


%.cldr : %.ttl 
	./NewCalendar3.py $*.ttl

%.defs : %.ttl 
	./NewCalendar3.py $*.ttl

