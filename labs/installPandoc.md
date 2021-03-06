---
title: Pandoc - Structures and Standards Lab
author: Jodi Schneider
date: October 4, 2017
---

# Pandoc in Lab
Please work in pairs to complete today's exercises. Try to work with someone using the same operating system (Mac, Windows, Linux).

Overall you will:

1. Install pandoc.
2. Get ready to use pandoc. 
3. Test that pandoc is working.
4. [Try using pandoc at the command line as a filter](http://pandoc.org/getting-started.html#step-4-using-pandoc-as-a-filter).
5. Transform your cultural heritage object description into two versions (e.g. HTML and DOCX), with pandoc. 
6. Markup a recipe in markdown and post it to this week's forum.
7. Download several recipes from the forum. Use pandoc to make an EPUB cookbook.
8. Upload your HTML and DOCX of the cultural heritage object description, and your EPUB cookbook to this week's forum. Try to do this by the end of the week. Need help? Please come to office hours.

Here are the details for each of these steps:

## 1. First install Pandoc

1.  Download the right installer for your operating system. (Pick
    the [installer for Mac OS
    X](https://github.com/jgm/pandoc/releases/download/1.19.2.1/pandoc-1.19.2.1-osx.pkg), [installer
    for
    Windows](https://github.com/jgm/pandoc/releases/download/1.19.2.1/pandoc-1.19.2.1-windows.msi),
    or [installer for Debian/
    Ubuntu](https://github.com/jgm/pandoc/releases/download/1.19.2.1/pandoc-1.19.2.1-1-amd64.deb).)
2.  Double-click the downloaded file.
3.  Follow menu prompts.

## 2. Get ready to use Pandoc

1.  Do you know how to get to your shell? ("[command line
    interface](https://www.ictlounge.com/html/operating_systems.htm)")
2. Later you will need to know how to do certain things with your shell. Some useful sites:
[Windows](https://www.lifewire.com/list-of-windows-7-command-prompt-commands-4107370)
[Mac](https://ss64.com/osx/)
    
## 3. Test that pandoc is working

1.  Open your shell (Terminal, Windows Command Prompt, etc.)
2.  At the command line, type the following:
    1.  `pandoc --version`
    2.  Then hit the 'Enter' key

If the message you get shows an error, ask one of the instructors. If you're doing this outside of class, post to this week's forum. For best results, copy and paste what you entered and what happened, and/or share a screenshot.

## 4. Try using Pandoc at the command line as a filter 

1. Follow the instructions at <http://pandoc.org/getting-started.html#step-4-using-pandoc-as-a-filter>

## 5. Transform your cultural heritage object description into two versions (e.g. HTML and DOCX), with pandoc. 

1.  Linked is an input file, [sample1.md](https://raw.githubusercontent.com/LIS501/syllabi/master/labs/sample1.md)
2.  Can you figure out how to get HTML or a DOCX file from this input
    file with Pandoc?
3.  Hint: You will need to use an output file.
4.  Hint: Check steps 3 and 6 of the "getting started" guide:
    <http://pandoc.org/getting-started.html> What about the rest of the
    guide?
5.  What needs to be different to use your own file?
6.  Hint: What do spaces mean in commands at the command line?

## 6. Markup a recipe in markdown and post it to this week's forum.

1. Find (or remember) a recipe. You can use any recipe. If you don't know one off-hand, you might like to find a public domain recipe from searching <http://archive.org>.
2. Type the recipe. Add markdown formatting. For formatting tips, see Table 2 of Dominici's "An Overview of Pandoc" or [sample1.md](https://raw.githubusercontent.com/LIS501/syllabi/master/labs/sample1.md) 
3. Post your recipe to this week's forum.

## 7. Download several recipes from this week's forum. Use pandoc to make an EPUB cookbook.

1. From this week's forum, download several recipes (or markup a second recipe).
2. Can you figure out how to get EPUB from multiple files at once with Pandoc?
3. Add a YAML block with title, author, and date to one of your recipes. What happens when you run Pandoc on all the files?
4. Can you open your EPUB file? If you don't already have an ebook readiner, [Calibre](https://calibre-ebook.com) is a good option.

## 8. Upload files
1. By the end of today (or by the week if you need more time), upload your HTML and DOCX of the cultural heritage object description, and your EPUB cookbook to this week's forum. 
2. Need help? Please come to office hours.
