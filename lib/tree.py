class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        # uses depth first
        queue = [self.root]

        while len(queue):
            node = queue.pop(0)
            if node["id"] == id:
                return node
            queue = node["children"] + queue

        return None

    def breadth_first_traversal(node):
        result = []
        nodes_to_visit = [node]

        while len(nodes_to_visit):
            current = nodes_to_visit.pop(0)

            result.append(current["value"])
            nodes_to_visit += current["children"]

        return result

    def depth_first_traversal(node):
        result = []
        nodes_to_visit = [node]

        while len(nodes_to_visit):
            current = nodes_to_visit.pop(0)
            result.append(current["value"])
            nodes_to_visit = node["children"] + nodes_to_visit

        return result

    def depth_first_recursive(node, result=[]):
        result.append(node["value"])
        for child in node["children"]:
            Tree.depth_first_recursive(child)
        return result
