from student import Student
import tree_stuff


class HesaReturn:
    def __init__(self, tree):
        self.tree = tree

    def process_students(self, sids):
        for sid in sids:
            student = Student(self.tree, sid)
            student.process()

    # you would add other processes here for other sections of the return file, for example:
    # process_courses
    # process_modules
    # etc etc

    def pretty_print(self):
        tree_stuff.pretty_print(self.tree)
