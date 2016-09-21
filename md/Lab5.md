# Lab 5: Cultural heritage object description {#Lab5 .task}

This lab will take place on LAB5DATE.

## Rationale {.context}

## Before you begin {.prereq}
1. Read the Spurlock Museum patron conduct policy <http://www.spurlock.illinois.edu/policy/patronconduct.html>.

2. Locate [Spurlock on the campus map](http://tinyurl.com/nsj8brt)

3. Browse the Getty A&A Thesaurus <http://www.getty.edu/research/tools/vocabularies/aat/>

## Tasks {.steps}

1. Convene at the Spurlock Museum at the start of class.
2. Choose a [cultural heritage](https://en.wikipedia.org/wiki/Cultural_heritage) object on display, 
   and make a note of its accession number, and the name of the gallery in which it is displayed.
3. On the basis of what you can see, and the written description accompanying the artifact, answer as many of
   the following questions as you can:
   - What physical materials is the object made from?
   - What techniques or processes were used in its creation?
   - Is the object a reproduction of some other artifact? If so, which one?
   - Does the description include precise physical measurements? If so, what are they?
   - What culture produced this object (or the original from which it was copied)?
   - During what time period was this object (or the original) created?
   - Was this object used for some particular or general purpose?
   - Is there information about the specific person who created this object or the specific time and place of creation?
   - Was the creation of the object (as opposed to the object itself) for some particular purpose?
   - If the artifact is a copy or reproduction, is the person who made the copy identified?
   - Does the object depict or represent some specific historical, mythical, or fictional person or event? If so, which?
   - Was the object contributed to the museum by an agent identified in the description? What information (if any) 
     is available about the provenance or chain of custody?
4. Reconvene in the usual classroom at GSLIS 90 minutes into the class period.
5. Lookup the record for the object you selected (by accession number) in the 
   [Spurlock online catalog](http://www.spurlock.illinois.edu/search/index.php). Compare the information in the
   record to your notes.
6. Determine whether the physical materials from which the object was made are listed in the A&A materials hierarchy.
   What are their hierarchical positions?
7. Determine whether the methods for creating the object are listed in the A&A processes and techniques hierarchy.
   What are their hierarchical positions?

## Deliverable {.result}
The deliverable for this exercise is a markdown expression of your structured notes, stored in a plain text file.
See the guidelines below for expressing your description using markdown.

## Submitting {.postreq}
Upload the  file to the Moodle drop box associated with this exercise.

## Appendix: Markdown Guidelines
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
   
### Remarks

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

