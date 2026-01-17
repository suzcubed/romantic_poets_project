from pathlib import Path
from lxml import etree
home = str(Path.home())

xsl_dir = home + "/romantic_poets_project/xsl"
xsl_file = xsl_dir + "/transform.xsl"

xslt_root = etree.parse(xsl_file)
transform = etree.XSLT(xslt_root)

tei_dir = Path(home + "/romantic_poets_project/tei_files")
out_dir = Path(home + "/romantic_poets_project/html")

out_dir.mkdir(exist_ok=True)

import glob

for xml_file in xml_dir.glob("*.xml"):
    tei_doc = etree.parse(str(xml_file))
    transformed = transform(tei_doc)

    out_file = out_dir / (xml_file.stem + ".html") 
    out_file.write_text(str(transformed), encoding="utf-8") 