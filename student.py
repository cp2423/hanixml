import tree_stuff


class Student:
    def __init__(self, tree, sid):
        self.node = tree_stuff.get_student_node(tree, sid)
        if self.node is None:
            print(f"WARNING student not found with sid {sid}")

    def process(self):
        if self.node is None:
            # sid was not found so do nothing
            return
        self.process_engagement()

    def process_engagement(self):
        if not tree_stuff.student_has_element(self.node, "Engagement"):
            tree_stuff.add_engagement(self.node)