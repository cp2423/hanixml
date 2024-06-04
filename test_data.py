from lxml import etree

# create some basic test xml
xml = """
<DataFutures>
<Student>
  <SID>12345678901234567</SID>
  <SEXID>invalid</SEXID>
  <Engagement>
  <NUMHUS>abc123</NUMHUS>
  <ENGSTARTDATE>2024-01-01</ENGSTARTDATE>
  </Engagement>
</Student>
<Student>
  <SID>12345678901234568</SID>
  <SEXID></SEXID>
</Student>
</DataFutures>
"""


# get as tree
def get_test_tree():
    return etree.fromstring(xml)
