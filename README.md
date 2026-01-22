# Romantic Poets TEI Project

## Objective
- Produce TEI markup of Romantic era poems with publication metadata. 
- Transform TEI (XML) markup into web-ready HTML.
- Automate transformations and data extraction using Python for scalability. 

## Methods
This toy corpus of five poems is meant to show different encoding scenarios.  

### Corpus Selection & Sources
- Authors sampled represent a diversity of perspectives within the Romantic era – class, gender, and differing schools of thought.  
- Five thematically similar poems were chosen to represent a range of views on power and history from these Romantic-era poets.  
- All texts are available in the public domain and hosted on either the Internet Archive or Wikimedia Commons.  
- Research on composition dates and details is captured in `<note type="project">` tags in the TEI files.  

### TEI
- Encoding follows [Walt Whitman Archive](https://whitmanarchive.org/about/encoding-guidelines) header schema practices for capturing file, source, and bibliographic details.  
- Minimal interpretive tagging used:  
  - Proper names (`<persName>`, `<placeName>`) for searchability  
  - Structural poem types included for comparison  
- Rhyme scheme and meter are **not** encoded.  
- Digital images are credited to the digitizing institutions (often also the holding institutions) as `<orgName>` in the source description.  

### HTML Transformation
- TEI files are transformed to HTML via XSLT.  
- The XSLT stylesheet is available in the `/xsl` project folder.  
- HTML preserves stanzaing, lineation, and embedded metadata.  
- Output files are reproducible for public access and copy-able from the `/html` project folder.  

### Python Automation
- Scripts batch-apply transformations across the corpus.  
- Automates validation, XSLT application, and CSV extraction of metadata.  
- Enables reproducible, scalable workflows for future expansion of the corpus.  
- Scripts are available in the `/scripts` folder.  
- Metadata CSV output is available in the `/metadata_csv_outputs` project folder.  

### Live Demo
Click [here](live_demo/index.html) for a preview of the TEI files transformed into HTML.  
Extracted metadata is also available in the `/live_demo` project folder as a CSV file for download.  
