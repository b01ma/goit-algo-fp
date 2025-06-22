import uuid

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def add_edges_for_heap(graph, heap, nodes, pos, index=0, x=0, y=0, layer=1):
    if index >= len(heap):
        return

    node = nodes[index]
    graph.add_node(node.id, color=node.color, label=node.val)

    # Left child
    left_index = 2 * index + 1
    if left_index < len(heap):
        left_node = nodes[left_index]
        graph.add_edge(node.id, left_node.id)
        lx = x - 1 / 2 ** layer
        pos[left_node.id] = (lx, y - 1)
        add_edges_for_heap(graph, heap, nodes, pos, index=left_index, x=lx, y=y - 1, layer=layer + 1)

    # Right child
    right_index = 2 * index + 2
    if right_index < len(heap):
        right_node = nodes[right_index]
        graph.add_edge(node.id, right_node.id)
        rx = x + 1 / 2 ** layer
        pos[right_node.id] = (rx, y - 1)
        add_edges_for_heap(graph, heap, nodes, pos, index=right_index, x=rx, y=y - 1, layer=layer + 1)

    return graph

def draw_heap_tree(heap):
    # Convert heap values to Node objects
    nodes = [Node(val) for val in heap]

    # Build graph
    graph = nx.DiGraph()
    pos = {nodes[0].id: (0, 0)} if nodes else {}
    add_edges_for_heap(graph, heap, nodes, pos)

    # Extract colors and labels
    colors = [data['color'] for _, data in graph.nodes(data=True)]
    labels = {node: data['label'] for node, data in graph.nodes(data=True)}

    # Draw the graph
    plt.figure(figsize=(10, 6))
    nx.draw(graph, pos=pos, labels=labels, arrows=False, node_size=2000, node_color=colors, font_size=12)
    plt.title("Binary Heap Tree")
    plt.axis("off")
    plt.show()

# Приклад: мін-купа
heap = [10, 15, 20, 30, 40, 50, 60]
draw_heap_tree(heap)