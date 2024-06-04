from lxml import etree


def pretty_print(element):
    xml = etree.tostring(element, pretty_print=True)
    print(xml.decode(), end='')


def get_student_node(tree, sid):
    return tree.find(f".//Student[SID='{sid}']")

def student_has_element(student_node, tag_name):
    elem = student_node.find(f".//{tag_name}")
    return etree.iselement(elem)


def add_engagement(student_node):
    engagement = etree.SubElement(student_node, "Engagement")
    etree.SubElement(engagement, "NUMHUS").text = "Some valid numhus"
    etree.SubElement(engagement, "ENGSTARTDATE").text = "2024-01-01"
