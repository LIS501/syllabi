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
1. Read the Pandoc Getting Started Guide at
   <http://pandoc.org/getting-started.html>.
2. [Install](http://pandoc.org/installing.html)
   Pandoc on your laptop and confirm you can run it.
3. Bring a (digital, not paper) copy of your Assignment 1 essay to
   class with you.

## Tasks {.steps}

0. Use Pandoc to create an HTML expression of
   [sample1.md](https://raw.githubusercontent.com/LIS501/syllabi/master/labs/sample1.md). If
   that input file is in your current working directory, then the
   command will be: `pandoc -o sample1.html sample1.md`
1. Use Pandoc to create a docx expression of
   [SecAFall16.md](https://raw.githubusercontent.com/LIS501/syllabi/master/SecAFall16.md). If
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
- Your UTF-8 encoded essay tagged with Pandoc's markdown dialect.
- An HTML expression of your essay output from Pandoc.
- A docx (Open Office XML) expression of your essay output from
  Pandoc.
- One to three paragraphs of remarks and observations on this exercise
  (expressed as plain text or markdown).

## Submitting {.postreq}
Upload the markdown, output, and remarks files to the Moodle drop box
associated with this exercise.

## Going further with Pandoc
If you are interested in doing more advanced work with pandoc, start with these resources:

- The [markdown essay](https://en.wikipedia.org/wiki/Markdown) on Wikipedia
- The Pandoc documentation on creating [slide presentations](http://pandoc.org/MANUAL.html#producing-slide-shows-with-pandoc).
- Kieran Healy's post on [markdown for academic writing](https://kieranhealy.org/blog/archives/2014/01/23/plain-text/).
