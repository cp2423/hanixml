import os
import requests

SCHEMA_FILENAME = "schema.xsd"


# only need to run this once!
def download_schema():
    response = requests.get("https://www.hesa.ac.uk/collection/23056/structure/23056_1_4_0.xsd")
    if response.ok:
        # my work laptop does weird stuff, have to explicitly set encoding to UTF8
        with open(SCHEMA_FILENAME, "w", encoding="utf-8") as f:
            f.write(response.text)


# read the schema file
def read_schema():
    if not os.path.isfile(SCHEMA_FILENAME):
        print("Downloading schema...")
        download_schema()
    with open(SCHEMA_FILENAME, encoding="utf-8") as f:
        return f.read()
