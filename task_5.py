import matplotlib.pyplot as plt
import networkx as nx
import uuid


class Node:
    def __init__(self, key, color="#CCCCCC"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def hex_color_gradient(start_color, end_color, steps):
    def hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

    def rgb_to_hex(rgb):
        return "#{:02x}{:02x}{:02x}".format(*rgb)

    start_rgb = hex_to_rgb(start_color)
    end_rgb = hex_to_rgb(end_color)

    gradient = []
    for i in range(steps):
        ratio = i / max(steps - 1, 1)
        rgb = tuple(int(start_rgb[j] + (end_rgb[j] - start_rgb[j]) * ratio) for j in range(3))
        gradient.append(rgb_to_hex(rgb))
    return gradient


def dfs_colored(root):
    stack = [root]
    visited = []
    while stack:
        node = stack.pop()
        if node and node not in visited:
            visited.append(node)
            stack.append(node.right)
            stack.append(node.left)
    return visited


def draw_dfs_colored(root):
    visited_nodes = dfs_colored(root)
    colors = hex_color_gradient("#003366", "#99ccff", len(visited_nodes))
    for node, color in zip(visited_nodes, colors):
        node.color = color

    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    tree = add_edges(tree, root, pos)

    node_colors = [data["color"] for _, data in tree.nodes(data=True)]
    labels = {node: data["label"] for node, data in tree.nodes(data=True)}

    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2000, node_color=node_colors, font_size=12)
    plt.title("DFS Tree Traversal (Color Gradient from Dark to Light)")
    plt.axis("off")
    plt.show()


# Create sample tree
root = Node(10)
root.left = Node(15)
root.right = Node(20)
root.left.left = Node(30)
root.left.right = Node(40)
root.right.left = Node(50)
root.right.right = Node(60)

draw_dfs_colored(root)
