# Romantic Poets TEI Project

## Objective
- Produce accessible, searchable digital versions of five Romantic era poems.  
- Transform TEI markup into web publication-ready material.  
- Automate TEI transofrmation and data extraction using Python, scaling workflow for future expansion of the corpus.   

## Methods
This toy corpus is meant to show different encoding scenarios.  

### Corpus Selection & Sources
- Authors sampled represent a diversity of perspectives within the Romantic era – class, gender, and differing schools of thought.  
- Five thematically similar poems were chosen to represent a range of views on power and history from these Romantic-era poets.  
- All texts are available in the public domain and hosted on either the Internet Archive or Wikimedia Commons.  
- Research on composition dates and details is captured in `<note type="project">` tags in the TEI files.  

### TEI
- Encoding follows Walt Whitman Archive header schema practices for capturing file, source, and bibliographic details.  
- Minimal interpretive tagging:  
  - Proper names (`<persName>`, `<placeName>`) for searchability  
  - Structural poem types included for comparison  
- Rhyme scheme and meter are **not** encoded.  
- Digital images are credited to the digitizing institutions (often also the holding institutions) as `<orgName>` in the source description.  

### HTML Transformation
- TEI files are transformed to HTML via XSLT.  
- The XSLT stylesheet is available in the `/xsl` project folder.  
- HTML preserves stanzaing, lineation, and embedded metadata.  
- Output files populate in the `/html` project folder.  

### Python Automation
- Two scripts available:
    - tei2html.py - batch transform TEI files into HTML
    - extract_tei_metadata - extract metadata from TEI tags into a CSV
- Scripts are available in the `/scripts` folder.  
- Metadata CSV output populates in the `/metadata_csv_outputs` project folder.  

### Live Demo
Click [here](live_demo/index.html) for a preview of the TEI files transformed into HTML.  
Extracted metadata is also available in the `/live_demo` project folder as a CSV file for download.  
