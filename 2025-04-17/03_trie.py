import matplotlib.pyplot as plt
import networkx as nx

class TrieNode:
    def __init__(self, char=""):
        self.char = char
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode(char)
            current = current.children[char]
        current.is_end = True

def build_trie(words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    return trie

def visualize_trie(trie):
    G = nx.DiGraph()
    pos = {}
    labels = {}

    def add_edges(node, parent_id=None, node_id=[0], x=0, y=0):
        current_id = node_id[0]
        node_id[0] += 1

        label = node.char if node.char else ""
        if node.is_end:
            label += "*"

        G.add_node(current_id)
        pos[current_id] = (x, -y)
        labels[current_id] = label

        if parent_id is not None:
            G.add_edge(parent_id, current_id)

        dx = -len(node.children) / 1.5
        for i, child in enumerate(sorted(node.children)):
            add_edges(node.children[child], current_id, node_id, x + dx + i, y + 1)

    add_edges(trie.root)

    plt.figure(figsize=(20, 10))
    nx.draw(G, pos, with_labels=False, arrows=True, node_size=500, node_color="lightblue", font_size=10)
    nx.draw_networkx_labels(G, pos, labels, font_size=10, font_family="monospace", verticalalignment='center')
    plt.axis("off")
    plt.tight_layout()
    plt.show()

# einzufügende Terme
words = [
"entstehen",
"entwickeln",
"entwickelt",
"entwicklung",
"fahrt",
"vorlesung",
"vorfahrt"]

trie = build_trie(words)
visualize_trie(trie)