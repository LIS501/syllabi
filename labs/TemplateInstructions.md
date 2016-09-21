---
title: Notes and instructions for markdown template
author: Dave Dubin
date: September 19, 2016
---

The [accompanying markdown file](https://raw.githubusercontent.com/LIS501/syllabi/master/labs/chalice.md)
expresses a cultural heritage object description. You can add or
modify the structure to suit the needs of the object you have
selected. For example, you are free to add additional descriptive
fields, or omit fields that aren't relevant. We recommend that your
description conform to the following general structure:

1. A YAML metadata block at the top of the file specifying title,
   author, and date of the description. This is documented in the
   Pandoc User Manual in the section
   titled [Metadata Blocks](http://pandoc.org/MANUAL.html#metadata-blocks).

2. A level 1 header presenting the name of the artifact.

3. A **Summary** section, marked with a level 2 header, and containing
   one paragraph of general description in natural language.
   
4. A **Basic Identification** section, marked with a level 2 header,
   and consisting of
   [attribute/value pairings](https://en.wikipedia.org/wiki/Attribute%E2%80%93value_pair)
   expressed as a
   [definition list](http://pandoc.org/MANUAL.html#definition-lists).
   This section should include materials, physical description, and
   methods of creation, if they are known. As described in the
   documentation and demonstrated in the accompanying file, definition
   list entries can more than one definition, so attributes with multiple
   values (such as materials or dimensions) can be grouped together.

5. A **Provenance** section, marked with a level 2 header,
   and consisting of attribute/value pairings expressed as a
   [definition list](http://pandoc.org/MANUAL.html#definition-lists).
   This section should include attributes connected to the origin,
   background and custody of the artifact.

6. A **Notes** section, marked with a level 2 header, and containing
   any additional information that does not seem to fit in with the
   other sections.
   
## Remarks

- Hyperlinks to additonal sources can be tagged using the
  [markdown inline link syntax](http://pandoc.org/MANUAL.html#inline-links),
  but are optional.
  
- You are encouraged to include descriptor IDs from the
  [Getty Arts and Architecture Thesaurus](http://www.getty.edu/research/tools/vocabularies/aat/)
  (AAT) for materials and processes, and from the
  [Getty Thesaurus of Geographic Names](http://vocab.getty.edu/tgn/)
  (TGN) for geographic regions. Be sure to read the scope notes in
  the AAT entries before using them. In the example I've prepared for
  you, the Spurlock Museum refers to the method of manufacture as
  "Electrotyping." But that word has a different meaning in AAT, and
  the correct AAT descriptor for this method is "Electroforming."

