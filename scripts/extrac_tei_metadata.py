from pathlib import Path
from lxml import etree
import pandas as pd

home = Path.home()
tei_dir = home / "romantic_poets_project/tei_files"

def extract_metadata(file): 
    tree = etree.parse(file)
    ns = {"tei": "http://www.tei-c.org/ns/1.0"}
    data = {}

    #file details 
    data["file name"] = Path(file).name
    
    #author details
    ref = ""
    author = ""
    file_author = tree.xpath("//tei:teiHeader/tei:fileDesc/tei:titleStmt/tei:author", namespaces=ns) 
    for a in file_author:
        ref = a.get("ref", "")
        author = a.text.strip() if a.text else ""         
    data["author"] = author
    data["author_reference"] = ref
 

    # source details 
    coll_titles = tree.xpath("//tei:teiHeader/tei:fileDesc/tei:sourceDesc/tei:biblStruct/tei:monogr/tei:title", namespaces=ns)
    coll_title = ""
    coll_subtitle = ""
    poem_title = ""
    for t in coll_titles:
        text = t.text.strip() if t.text else ""
        level = t.get("level")
        ttype = t.get("type") 
        if level == "m" and ttype == "main": 
            coll_title = text
        elif level == "m" and ttype == "sub":
            coll_subtitle = text
        elif level == "a" and ttype == "main":
            poem_title = text
    data["poem_title"] = poem_title
    data["print_collection_title"] = coll_title
    data["print_collection_subtitle"] = coll_subtitle
    
    #physical book details    
    pub_editor = tree.xpath("//tei:teiHeader/tei:fileDesc/tei:sourceDesc/tei:biblStruct/tei:monogr/tei:editor/text()", namespaces=ns)
    pub_editor = pub_editor[0] if pub_editor else ""
    data["print_editor"] = pub_editor
    
    pub_date = tree.xpath("//tei:teiHeader/tei:fileDesc/tei:sourceDesc/tei:biblStruct/tei:monogr/tei:imprint/tei:date/text()", namespaces=ns)
    pub_date = pub_date[0] if pub_date else ""
    data["print_publication_date"] = pub_date
    
    publisher = tree.xpath("//tei:teiHeader/tei:fileDesc/tei:sourceDesc/tei:biblStruct/tei:monogr/tei:imprint/tei:publisher/text()", namespaces=ns)
    publisher = publisher[0] if publisher else ""
    data["print_publisher"] = publisher
    
    pub_place = tree.xpath("//tei:teiHeader/tei:fileDesc/tei:sourceDesc/tei:biblStruct/tei:monogr/tei:imprint/tei:pubPlace/text()", namespaces=ns)
    pub_place = pub_place[0] if pub_place else ""
    data["print_publication_location"] = pub_place

    # archival details 
    digital_lib = tree.xpath("//tei:teiHeader/tei:fileDesc/tei:sourceDesc/tei:biblStruct/tei:monogr/tei:orgName/text()", namespaces=ns)
    digital_lib = digital_lib[0] if digital_lib else ""
    data["digitizing_institution"] = digital_lib
    
    archive_elem = tree.xpath("//tei:teiHeader/tei:fileDesc/tei:sourceDesc/tei:biblStruct/tei:note/tei:ptr", namespaces=ns)
    archive_link = archive_elem[0].get("target") if archive_elem and archive_elem[0].get("target") else ""
    data["digital_archive_link"] = archive_link

    #composition details & manuscript details, if avail 
    orig_date = tree.xpath("//tei:teiHeader/tei:fileDesc/tei:sourceDesc/tei:bibl/tei:date/text()", namespaces=ns)
    orig_date = orig_date[0] if orig_date else ""
    data["composition_date"] = orig_date

    composition_notes = tree.xpath("string(//tei:teiHeader/tei:fileDesc/tei:sourceDesc/tei:bibl/tei:note)",namespaces=ns).strip()
    data["notes_on_composition"] = composition_notes

    manuscript_loc = tree.xpath("//tei:teiHeader/tei:fileDesc/tei:sourceDesc/tei:bibl/tei:orgName/text()", namespaces=ns)
    manuscript_loc = manuscript_loc[0] if manuscript_loc else ""
    data["manuscript_location"] = manuscript_loc
    
    return data


metadata_records = []
for file in tei_dir.glob("*.xml"):
    metadata = extract_metadata(file)
    metadata_records.append(metadata)

df = pd.DataFrame(metadata_records)
output_path = home / "romantic_poets_project/metadata_csv_outputs/metadata.csv"
df.to_csv(output_path, index=False)