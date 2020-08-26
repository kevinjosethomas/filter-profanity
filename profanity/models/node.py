
class Node:

    def __init__(self, cargo):
        """Initializes the Node class"""

        self.cargo = cargo
        self.children = []

    def add_child(self, child):
        """Adds a child to the node"""

        self.children.append(child)
