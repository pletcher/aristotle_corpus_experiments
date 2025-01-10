import os
import polars as pl

from lxml import etree
from MyCapytain.common.constants import Mimetypes
from MyCapytain.resources.texts.local.capitains.cts import CapitainsCtsText

NAMESPACES = {
    "tei": "http://www.tei-c.org/ns/1.0",
    "xml": "http://www.w3.org/XML/1998/namespace",
}

DIR = "./OpenGreekAndLatin/First1KGreek/data"

def main():
    TEXTS = [f"{DIR}/{f}" for f in os.listdir(DIR) if f.endswith(".xml")]
    
    urns = []
    raw_xmls = []
    unannotated_strings = []

    for t in TEXTS:
        tree = etree.parse(t)
        edition = tree.find(".//tei:div[@type='edition']", namespaces=NAMESPACES)
        text_urn = edition.attrib['n']
        
        with open(t) as f:
            text = CapitainsCtsText(urn=text_urn, resource=f)

        for ref in text.getReffs(level=len(text.citation)):
            urn = f"{text.urn}:{ref}"
            node = text.getTextualNode(ref)
            raw_xml = node.export(Mimetypes.XML.TEI)
            tree = node.export(Mimetypes.PYTHON.ETREE)
            s = etree.tostring(tree, encoding="unicode", method="text")

            urns.append(urn)
            raw_xmls.append(raw_xml)
            unannotated_strings.append(s)

    d = {
        "urn": pl.Series(urns),
        "raw_xml": raw_xmls,
        "unannotated_strings": pl.Series(unannotated_strings)
    }

    df = pl.DataFrame(d)

    df.write_parquet("./1st1KGreek_aristotle.parquet")

if __name__ == "__main__":
    main()