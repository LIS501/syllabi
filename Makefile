# Start by clearing the list of suffixes
.SUFFIXES:
# Then specify our suffixes
.SUFFIXES: .tex .dvi .bib .pdf .sgml .html .m4 .md

M4PATH := ./md
export M4PATH

%.md : %.m4 ABCFall2016.m4
	m4 -DFORMATDEFS="wpformat.m4" -DMYDEFS="$*.m4" ABCFall2016.m4 > $*.md

%.html : %.m4 ABCFall2016.m4
	m4 -DFORMATDEFS="wpformat.m4" -DMYDEFS="$*.m4" ABCFall2016.m4|pandoc -s -c https://www.w3.org/StyleSheets/Core/Swiss -o $*.html

%.docx : %.m4 ABCFall2016.m4
	m4 -DFORMATDEFS="wpformat.m4" -DMYDEFS="$*.m4" ABCFall2016.m4|pandoc -s  -o $*.docx

Topics :
	python NewCalendar.py fall16calendar.ttl > md/fall16topicReadings.md

Readings : SecAFall16.m4 CalendarReadings.m4
	m4 -DFORMATDEFS="wpformat.m4" -DMYDEFS="SecAFall16.m4" CalendarReadings.m4|pandoc -s -c https://www.w3.org/StyleSheets/Core/Swiss -o LIS501Readings.html


AllThree : SecAFall16.docx SecBFall16.docx SecCFall16.docx
	echo "Done"
