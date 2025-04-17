import matplotlib.pyplot as plt
import random

class TreeNode:
    def __init__(self, word):
        self.word = word
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, word):
        if self.root is None:
            self.root = TreeNode(word)
        else:
            self._insert(self.root, word)

    def _insert(self, current, word):
        if word < current.word:
            if current.left is None:
                current.left = TreeNode(word)
            else:
                self._insert(current.left, word)
        elif word > current.word:
            if current.right is None:
                current.right = TreeNode(word)
            else:
                self._insert(current.right, word)

def draw_tree(node, x=0, y=0, dx=1.5, level=0, pos=None, lines=None):
    if pos is None: pos = {}
    if lines is None: lines = []

    pos[node] = (x, y)
    if node.left:
        lines.append(((x, y), (x - dx, y - 1)))
        draw_tree(node.left, x - dx, y - 1, dx / 1.5, level + 1, pos, lines)
    if node.right:
        lines.append(((x, y), (x + dx, y - 1)))
        draw_tree(node.right, x + dx, y - 1, dx / 1.5, level + 1, pos, lines)
    return pos, lines

def visualize_tree(root):
    pos, lines = draw_tree(root)

    _, ax = plt.subplots(figsize=(6, 6))
    for line in lines:
        (x1, y1), (x2, y2) = line
        ax.plot([x1, x2], [y1, y2], 'k-', linewidth=1)

    for node, (x, y) in pos.items():
        ax.text(x, y, node.word, ha='center', va='center',
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'),)

    ax.axis('off')
    plt.tight_layout()
    plt.show()

def balanced_insert_order(values):
    """
        Bestimmt eine Einfügereihenfolge der übergebenen Terme, die zu einem
        balancierten binären Suchbaum führt.
    """
    if not values:
        return []
    values.sort()
    mid = len(values) // 2
    # rekursive Berechnung der Einfügereihenfolge (analog zur binären Suche)
    return (
        [values[mid]] +
        balanced_insert_order(values[:mid]) +
        balanced_insert_order(values[mid + 1:]))


# einzufügende Terme
words = ["Affe",
"Bär",
"Maus",
"Nilpferd",
"Reh",
"Wal",
"Zebra"]

# sortierte Reihenfolge der Terme beim Einfügen
#words = sorted(words)

# zufällig Einfügung der Terme
#words = random.sample(words, len(words))

# absteigende Sortierung der Terme
#words = sorted(words, reverse=True)

# Einfügung der Terme, so dass balancierte Baumstruktur entsteht
#words = balanced_insert_order(words)

bst = BinarySearchTree()
for word in words:
    bst.insert(word)

visualize_tree(bst.root)