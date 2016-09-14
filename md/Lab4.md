# Lab 4: Pandoc encoding and transformation {#Lab4 .task}

This lab will take place LAB4DATE.

## Rationale {.context}

Document structure, the differences between declarative and procedural markup,
and the role of information standards are among the topics we are reading and 
discussing this semester. This exercise provides hands-on experience tagging a 
document structurally, and creating a presentational expression of it using
a formatting utility. There is a community of users who employ Pandoc
for document production, but the rationale for this exercise is not to master
a technical tool, but for an important philosophy of document analysis and 
authorship to become vivid for you.  
 
## Before you begin {.prereq}
1. Install Pandoc on your laptop. You may want to consult the Pandoc Install guide at http://pandoc.org/installing.html
2. Confirm that you can run Pandoc from your shell. You may want to consult the Pandoc Getting Started Guide at
   <http://pandoc.org/getting-started.html>.
3. Confirm that you have an appropriate text editor installed (we have tested Mac TextEdit and Windows Notepad++ https://notepad-plus-plus.org )
4. Bring a (digital, not paper) copy of your Assignment 1 essay to
   class with you.

## Tasks {.steps}

0. Use Pandoc to create an HTML expression of
   [sample1.md](https://raw.githubusercontent.com/LIS501/syllabi/master/labs/sample1.md) (also linked from the Moodle) If
   that input file is in your current working directory, then the
   command will be: `pandoc -o sample1.html sample1.md`
1. Use Pandoc to create a docx expression of
   [SecAFall16.md]:(https://raw.githubusercontent.com/LIS501/syllabi/master/SecAFall16.md) (also linked from the Moodle). If
   that input file is in your current working directory, then the
   command will be: `pandoc -o SecAFall16.docx SecAFall16.md`
2. Save a copy of your essay as a plain text (UTF-8 encoded) file. If
   your essay contains any illustrations, copy them into separate image
   files.
3. Following the examples presented in class (and in the Pandoc user guide)
   tag the text file you just created with markdown for some or all of the
   following content objects in your essay: sections, ordered
   and unordered lists, footnotes, and inline emphasis.
4. Use Pandoc to create an HTML and a docx expression of your
   essay. Note any syntax errors or other difficulties you encounter
   in getting this to work.

## Deliverable {.result}
1. Your essay in Markdown. (i.e. tagged with Pandoc's markdown dialect, in a UTF-8 encoded file)
2. Output from Pandoc: An HTML expression of your essay.
3. Output from Pandoc: A docx (Open Office XML) expression of your essay.
4. Your remarks and observations on this exercise
  (expressed as plain text or markdown) - One to three paragraphs.

## Submitting {.postreq}
Upload the markdown, output, and remarks files to the Moodle drop box
associated with this exercise.

## Going further with Pandoc
If you are interested in doing more advanced work with Pandoc, start with these resources:

- The [markdown essay](https://en.wikipedia.org/wiki/Markdown) on Wikipedia: https://en.wikipedia.org/wiki/Markdown

###Slides
- The Pandoc documentation on creating slide presentations, http://pandoc.org/MANUAL.html#producing-slide-shows-with-pandoc
- A familiar example (Prof Dubin's slides) https://github.com/LIS501/slides/blob/master/standards.md

###Academic Writing
- Kieran Healy's post on markdown for academic writing: https://kieranhealy.org/blog/archives/2014/01/23/plain-text/.

###EBooks
- How I wrote and published my novel using only open source tools: From Markdown to paperback and Kindle without proprietary software. Gabriel Gambetta. Techspiration Aug 9 2016 https://medium.com/techspiration-ideas-making-it-happen/how-i-wrote-and-published-my-novel-using-only-open-source-tools-5cdfbd7c00ca#.wj56jevr9
- Make Your Own E-Books with Pandoc, ProfHacker, The Chronicle of Higher Education, March 20, 2012
http://www.chronicle.com/blogs/profhacker/make-your-own-e-books-with-pandoc/39067
- Creating an ebook with pandoc: http://pandoc.org/epub.html

###Executable code
- R code chunks in Pandoc: http://rmarkdown.rstudio.com/authoring_rcodechunks.html

###Even more
- Various uses of pandoc
https://github.com/jgm/pandoc/wiki/Pandoc-Extras#web-services-to-process-files-by-pandoc
