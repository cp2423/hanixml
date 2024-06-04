import excel_stuff
import schema
import test_data
from hesa_return import HesaReturn

# this example does not do anything with the schema, this is just a demo
schema_file = schema.read_schema()
test_tree = test_data.get_test_tree()

sids = excel_stuff.get_student_ids()

hr = HesaReturn(test_tree)
hr.process_students(sids)
hr.pretty_print()