import io

from .collection import EntrySet


def create_uniprot_collection_from_xml_file(xml_file):
    new_coll = EntrySet(collectionXML=xml_file)
    return new_coll


def create_uniprot_collection_from_xml_string(xml_string):
    new_coll = EntrySet(streamXML=io.StringIO(xml_string))
    return new_coll
