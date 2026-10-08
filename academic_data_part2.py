# academic_data_part2.py - Topics 6 to 10
# Mission 02: Data Structures (Topics 6-8) & Mission 03: Divide and Conquer (Topics 9-10)

PART2_TOPICS = [
    # 6. TREES (Groot)
    {
        "filename": "topic-trees.html",
        "topic_id": "trees",
        "mission_num": "02",
        "mission_title": "DATA STRUCTURES",
        "mission_url": "mission-02.html",
        "topic_num": "TOPIC 03",
        "topic_title": "TREES & BINARY SEARCH TREES",
        "hero_name": "GROOT",
        "hero_color": "#15803d",
        "hero_tag": "HIERARCHICAL CANOPY RECURSION",
        "hero_quote": "I am Groot. (Every branch, node, and leaf in our galactic forest maintains recursive balance.)",
        "badge_color": "#dcfce7",
        "viz_type": "tree",
        "problem_invariants": """
<p>A <strong>Tree</strong> is a non-linear hierarchical data structure consisting of a collection of nodes connected by directed edges, with zero cycles. A distinguished node called the <strong>Root</strong> sits at top level, with each descendant node having exactly one parent.</p>
<p><strong>Binary Search Tree (BST) Ordering Invariant:</strong> For any node \(u\) with value \(K\):</p>
<ul>
  <li>All keys in the left subtree of \(u\) must be strictly less than \(K\): \(\forall x \in \text{Left}(u), x < K\).</li>
  <li>All keys in the right subtree of \(u\) must be strictly greater than \(K\): \(\forall y \in \text{Right}(u), y > K\).</li>
</ul>
<p><strong>Tree Traversal Strategies:</strong></p>
<ul>
  <li><strong>In-Order (Left, Root, Right):</strong> Produces elements in strictly ascending sorted order for any BST.</li>
  <li><strong>Pre-Order (Root, Left, Right):</strong> Ideal for cloning trees and serializing hierarchical structures.</li>
  <li><strong>Post-Order (Left, Right, Root):</strong> Essential for bottom-up computation (e.g., directory size calculation, expression tree evaluation, and garbage collection deletion).</li>
</ul>
""",
        "naive_vs_optimal": """
<p>In an unbalanced BST, inserting elements in sorted order (\(1, 2, 3, \dots, n\)) degrades the tree into a degenerate linear linked list of height \(h = n\). This causes lookup time to collapse to \(O(n)\). Self-balancing trees (AVL Trees, Red-Black Trees) perform rotations upon insertion/deletion to enforce \(h = \Theta(\log n)\), guaranteeing \(O(\log n)\) search time in all cases.</p>
<div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px; margin-top:12px;">
  <div style="background:#fee2e2; border:2px solid #ef4444; padding:12px; font-size:0.85rem;">
    <strong style="color:#b91c1c;">DEGENERATE SKEWED BST</strong><br>
    Height \(h = n\).<br>
    Search: \(O(n)\)<br>
    Tree behaves identically to a singly-linked list; no binary search advantage.
  </div>
  <div style="background:#dcfce7; border:2px solid #16a34a; padding:12px; font-size:0.85rem;">
    <strong style="color:#15803d;">BALANCED TREE (AVL / RED-BLACK)</strong><br>
    Height \(h \le 1.44 \log_2(n)\).<br>
    Search: \(\Theta(\log n)\)<br>
    Logarithmic height bounds guarantee sub-millisecond lookups across billions of records.
  </div>
</div>
""",
        "math_formulation": r"""
<p><strong>Binary Tree Structural Properties:</strong></p>
<ul>
  <li>Maximum nodes at depth \(d\) (root at \(d=0\)): \(2^d\).</li>
  <li>Maximum total nodes in binary tree of height \(h\): \(\sum_{i=0}^{h} 2^i = 2^{h+1} - 1\).</li>
  <li>Minimum height for a tree with \(n\) nodes: \(\lceil \log_2(n + 1) \rceil - 1 \implies \Omega(\log n)\).</li>
  <li>Number of leaf nodes \(L\) in a full binary tree with \(I\) internal nodes: \(L = I + 1\).</li>
</ul>
<p><strong>Recurrence for Balanced Tree Search:</strong></p>
\[ T(n) = T(n/2) + O(1) \implies T(n) = \Theta(\log n) \]
""",
        "worked_example": """
<p><strong>Worked Example:</strong> Insert sequence <code>[50, 30, 70, 20, 40, 60, 80]</code> into an initially empty BST, then execute In-Order Traversal.</p>
<ol style="margin-left:20px; line-height:1.8;">
  <li><strong>Insert 50:</strong> Root = <code>50</code>.</li>
  <li><strong>Insert 30:</strong> \(30 < 50 \implies\) Left child of 50.</li>
  <li><strong>Insert 70:</strong> \(70 > 50 \implies\) Right child of 50.</li>
  <li><strong>Insert 20:</strong> \(20 < 50 \to 20 < 30 \implies\) Left child of 30.</li>
  <li><strong>Insert 40:</strong> \(40 < 50 \to 40 > 30 \implies\) Right child of 30.</li>
  <li><strong>Insert 60:</strong> \(60 > 50 \to 60 < 70 \implies\) Left child of 70.</li>
  <li><strong>Insert 80:</strong> \(80 > 50 \to 80 > 70 \implies\) Right child of 70.</li>
  <li><strong>In-Order Traversal (L, Root, R):</strong>
      <br>Left subtree of 50: <code>(20, 30, 40)</code>
      <br>Root: <code>50</code>
      <br>Right subtree of 50: <code>(60, 70, 80)</code>
      <br><strong>Result:</strong> <code>[20, 30, 40, 50, 60, 70, 80]</code> (Strictly sorted!).
  </li>
</ol>
""",
        "complexity_table": [
            ("BST Search (Average / Balanced)", "O(log n)", "Omega(1)", "Height bounded by log2(n)"),
            ("BST Search (Worst Case Skewed)", "O(n)", "Omega(n)", "Tree degenerates to linear stick"),
            ("BST Insertion", "O(log n) avg", "O(n) worst", "Traverses path from root to leaf insertion site"),
            ("BST Deletion", "O(log n) avg", "O(n) worst", "Requires finding in-order successor for 2-child nodes"),
            ("In-Order Traversal", "O(n)", "O(h) space", "Visits every node exactly once")
        ],
        "code": '''class TreeNode:
    def __init__(self, key: int):
        self.key = key
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None

class GrootBST:
    """
    Binary Search Tree with In-Order Traversal property.
    """
    def __init__(self):
        self.root: TreeNode | None = None
        
    def insert(self, key: int) -> None:
        self.root = self._insert_node(self.root, key)
        
    def _insert_node(self, current: TreeNode | None, key: int) -> TreeNode:
        if current is None:
            return TreeNode(key)
        if key < current.key:
            current.left = self._insert_node(current.left, key)
        elif key > current.key:
            current.right = self._insert_node(current.right, key)
        return current
        
    def inorder_traversal(self, node: TreeNode | None, result: list) -> list:
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.key)
            self.inorder_traversal(node.right, result)
        return result''',
        "practical_considerations": """
<p><strong>1. Database B-Trees & B+ Trees:</strong> In real-world databases (PostgreSQL, MySQL, SQLite), in-memory binary trees suffer from excessive disk I/O. Instead, multi-way B-Trees and B+ Trees with block-sized node branching factors (e.g., 100-1000 keys per node) are used to keep disk seeks below 3-4 accesses.</p>
<p><strong>2. In-Order Successor Deletion:</strong> Deleting a node with two children requires replacing it with its in-order successor (the smallest key in its right subtree) or in-order predecessor, preserving the BST invariant.</p>
<p><strong>3. Memory Footprint:</strong> A binary tree node requires three pointers (left, right, parent) totaling 24 bytes of pointer overhead per node on 64-bit systems. For small data values, cache-conscious array representations (like binary heaps) are more memory-efficient.</p>
""",
        "speech_bubbles": [
            ("Groot", "I am Groot! (Translation: Remember the ancient forestry rule: smaller keys branch to the left, larger keys branch to the right!)"),
            ("Groot", "I am Groot. (Translation: An in-order traversal of a BST always yields numbers in perfectly sorted ascending order. Keep the branches balanced!)")
        ],
        "quiz": [
            {
                "q": "Which tree traversal strategy produces keys in strictly ascending sorted order for a Binary Search Tree?",
                "options": [
                    "Pre-Order Traversal",
                    "In-Order Traversal",
                    "Post-Order Traversal",
                    "Level-Order Traversal"
                ],
                "answer": 1,
                "explanation": "In-Order traversal recursively visits Left subtree, Root, and Right subtree. By BST invariant, this outputs elements in ascending order."
            },
            {
                "q": "What is the worst-case search time in a naive, unbalanced BST with n elements?",
                "options": [
                    "O(1)",
                    "O(log n)",
                    "O(n)",
                    "O(n log n)"
                ],
                "answer": 2,
                "explanation": "If elements are inserted in already-sorted order, an unbalanced BST degenerates into a linear chain of height n, yielding O(n) search time."
            },
            {
                "q": "What is the maximum number of nodes in a binary tree of height h (where root is at height 0)?",
                "options": [
                    "2^h",
                    "2^(h+1) - 1",
                    "2^(h-1)",
                    "h^2"
                ],
                "answer": 1,
                "explanation": "The maximum number of nodes in a binary tree of height h is 2^0 + 2^1 + ... + 2^h = 2^(h+1) - 1."
            },
            {
                "q": "How does an AVL Tree prevent the BST from degrading into a linear list?",
                "options": [
                    "By discarding duplicate keys immediately",
                    "By enforcing that the height difference between left and right subtrees is at most 1 via rotations",
                    "By storing all keys in an auxiliary hash map",
                    "By restricting the tree to a depth of 3"
                ],
                "answer": 1,
                "explanation": "AVL trees maintain a balance factor of -1, 0, or +1 at every node, executing tree rotations to guarantee O(log n) height."
            }
        ],
        "summary": "Trees provide hierarchical modeling. In a Binary Search Tree, In-Order traversal yields sorted order. Keeping tree height balanced at O(log n) is the key to logarithmic search, insert, and delete performance."
    },

    # 7. DICTIONARIES / HASHING (Iron Man)
    {
        "filename": "topic-dictionaries.html",
        "topic_id": "dictionaries",
        "mission_num": "02",
        "mission_title": "DATA STRUCTURES",
        "mission_url": "mission-02.html",
        "topic_num": "TOPIC 04",
        "topic_title": "DICTIONARIES & HASH TABLES",
        "hero_name": "IRON MAN",
        "hero_color": "#b91c1c",
        "hero_tag": "ARC REACTOR CONSTANT-TIME ACCESS",
        "hero_quote": "JARVIS, run a direct hash key probe. When the suit needs targeting coordinates, waiting O(n) is out of the question.",
        "badge_color": "#fee2e2",
        "viz_type": "hash",
        "problem_invariants": """
<p>A <strong>Dictionary</strong> (or Associative Array / Map) is an abstract data type storing key-value pairs \((k, v)\), supporting three core operations: <code>Insert(k, v)</code>, <code>Delete(k)</code>, and <code>Search(k)</code>. A <strong>Hash Table</strong> is the definitive data structure implementing dictionaries with average \(\Theta(1)\) constant-time access.</p>
<p><strong>Hash Function Architecture:</strong> A hash function \(h(k)\) maps arbitrary universe keys \(U\) into discrete integer bucket indices \(\{0, 1, \dots, m-1\}\). A desirable hash function satisfies:</p>
<ul>
  <li><strong>Deterministic:</strong> The same key must always produce the identical hash code.</li>
  <li><strong>Uniform Distribution:</strong> Spreads keys uniformly across all \(m\) slots to minimize collisions (Simple Uniform Hashing Assumption).</li>
  <li><strong>Fast Computation:</strong> Computable in \(O(1)\) arithmetic operations.</li>
</ul>
<p><strong>Collision Resolution Strategies:</strong> By the Pigeonhole Principle, since \(|U| > m\), collisions (\(h(k_1) = h(k_2)\)) are inevitable. Resolved via:</p>
<ol>
  <li><strong>Separate Chaining (Open Hashing):</strong> Each bucket stores a linked list of collided key-value pairs.</li>
  <li><strong>Open Addressing (Closed Hashing):</strong> All items stored directly in the table array; collisions resolved via probe sequences: Linear Probing (\(h(k, i) = (h'(k) + i) \bmod m\)), Quadratic Probing (\((h'(k) + c_1 i + c_2 i^2) \bmod m\)), or Double Hashing (\((h_1(k) + i \cdot h_2(k)) \bmod m\)).</li>
</ol>
""",
        "naive_vs_optimal": """
<p>Storing \(1,000,000\) Stark Industries personnel records in an unsorted array requires scanning all \(10^6\) entries on every search (\(O(n)\)). Even a sorted array requires \(O(\log n)\) search and an agonizing \(O(n)\) insertion due to shifting. Iron Man's Hash Table achieves instantaneous \(O(1)\) average-time lookups and insertions by computing the exact memory bucket via modular arithmetic.</p>
<div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px; margin-top:12px;">
  <div style="background:#fee2e2; border:2px solid #ef4444; padding:12px; font-size:0.85rem;">
    <strong style="color:#b91c1c;">UNSORTED ARRAY / LIST</strong><br>
    Search: \(O(n)\)<br>
    Insertion: \(O(1)\)<br>
    Unusable for high-throughput database lookups.
  </div>
  <div style="background:#dcfce7; border:2px solid #16a34a; padding:12px; font-size:0.85rem;">
    <strong style="color:#15803d;">HASH TABLE (JARVIS CACHE)</strong><br>
    Search: \(\Theta(1)\) average<br>
    Insertion: \(\Theta(1)\) average<br>
    Direct memory addressing via hash keys; zero searching loops.
  </div>
</div>
""",
        "math_formulation": r"""
<p><strong>Load Factor (\(\alpha\)):</strong></p>
\[ \alpha = \frac{n}{m} = \frac{\text{Number of elements stored}}{\text{Total bucket slots in table}} \]
<p><strong>Average Search Time under Simple Uniform Hashing:</strong></p>
<ul>
  <li><strong>Separate Chaining:</strong> Unsuccessful Search = \(\Theta(1 + \alpha)\), Successful Search = \(\Theta(1 + \alpha/2)\).</li>
  <li><strong>Open Addressing (Uniform Hashing):</strong> Unsuccessful Search \(\le \frac{1}{1 - \alpha}\), Successful Search \(\le \frac{1}{\alpha} \ln \frac{1}{1 - \alpha}\).</li>
</ul>
<p><em>Example:</em> If \(\alpha = 0.5\) (table half full), expected probes for an unsuccessful search in open addressing \(\le \frac{1}{1 - 0.5} = 2\) probes!</p>
""",
        "worked_example": """
<p><strong>Worked Example:</strong> Insert keys <code>[23, 43, 13, 27, 33]</code> into a hash table of size \(m = 10\) using hash function \(h(k) = k \bmod 10\) and Linear Probing for collision resolution.</p>
<ol style="margin-left:20px; line-height:1.8;">
  <li><strong>Key 23:</strong> \(h(23) = 23 \bmod 10 = 3\). Slot 3 empty \(\to\) Store 23 at <strong>index 3</strong>.</li>
  <li><strong>Key 43:</strong> \(h(43) = 43 \bmod 10 = 3\). Slot 3 occupied! Probe \(i=1\): \((3 + 1) \bmod 10 = 4\). Slot 4 empty \(\to\) Store 43 at <strong>index 4</strong>.</li>
  <li><strong>Key 13:</strong> \(h(13) = 13 \bmod 10 = 3\). Slots 3 and 4 occupied! Probe \(i=2\): \((3 + 2) \bmod 10 = 5\). Slot 5 empty \(\to\) Store 13 at <strong>index 5</strong>.</li>
  <li><strong>Key 27:</strong> \(h(27) = 27 \bmod 10 = 7\). Slot 7 empty \(\to\) Store 27 at <strong>index 7</strong>.</li>
  <li><strong>Key 33:</strong> \(h(33) = 33 \bmod 10 = 3\). Slots 3, 4, 5 occupied. Probe \(i=3\): \((3 + 3) \bmod 10 = 6\). Slot 6 empty \(\to\) Store 33 at <strong>index 6</strong>.</li>
</ol>
<p><strong>Final Table:</strong> <code>[_, _, _, 23, 43, 13, 33, 27, _, _]</code>. Clusters form around index 3-6 (demonstrating Primary Clustering in linear probing!).</p>
""",
        "complexity_table": [
            ("Average Search / Lookup", "O(1)", "Omega(1)", "Direct hash indexing under uniform distribution"),
            ("Worst-Case Search (All Collide)", "O(n)", "Omega(n)", "Occurs when all keys hash to the identical slot"),
            ("Average Insertion", "O(1)", "Omega(1)", "Amortized O(1) including dynamic table doubling"),
            ("Average Deletion", "O(1)", "Omega(1)", "Requires tombstone markers in open addressing"),
            ("Space Complexity", "O(n + m)", "O(n)", "Total memory proportional to element count and bucket capacity")
        ],
        "code": '''class JarvisHashTable:
    """
    Open Addressing Hash Table with Linear Probing and O(1) average lookup.
    """
    def __init__(self, size: int = 10):
        self.size = size
        self.table = [None] * size
        self.count = 0
        
    def _hash(self, key: int) -> int:
        return key % self.size
        
    def insert(self, key: int, value: str) -> bool:
        if self.count >= self.size:
            raise OverflowError("HASH TABLE FULL: Dynamic rehash required!")
            
        idx = self._hash(key)
        for i in range(self.size):
            probe_idx = (idx + i) % self.size
            if self.table[probe_idx] is None or self.table[probe_idx][0] == key:
                self.table[probe_idx] = (key, value)
                self.count += 1
                return True
        return False
        
    def get(self, key: int) -> str | None:
        idx = self._hash(key)
        for i in range(self.size):
            probe_idx = (idx + i) % self.size
            entry = self.table[probe_idx]
            if entry is None:
                return None  # Key not found
            if entry[0] == key:
                return entry[1]
        return None''',
        "practical_considerations": """
<p><strong>1. Dynamic Resizing & Rehashing:</strong> When the load factor exceeds a defined threshold (typically \(\alpha \ge 0.7\) or \(0.75\)), open addressing performance deteriorates exponentially. The table doubles its capacity (\(m \to 2m\)) and re-hashes all existing keys. This resizing takes \(O(n)\) but occurs infrequently, yielding \(O(1)\) amortized cost.</p>
<p><strong>2. Primary Clustering in Linear Probing:</strong> Linear probing suffers from clusters: long contiguous runs of occupied slots that grow longer as more collisions occur. Double Hashing eliminates primary and secondary clustering by computing a secondary step size \(h_2(k)\).</p>
<p><strong>3. Cryptographic Hash Functions:</strong> Standard hash functions (like modulo or polynomial rolling) are vulnerable to Denial-of-Service (HashDoS) collision attacks where an adversary injects millions of colliding keys. Security-sensitive engines use randomized hashing (SipHash) to preserve \(O(1)\) defense.</p>
""",
        "speech_bubbles": [
            ("Iron Man", "Rule number one of Stark Engineering: Never scan an array when a hash function can jump directly to the memory address in O(1) constant time!"),
            ("Iron Man", "Watch your load factor alpha! Once your table passes 70% capacity, primary clustering will drag your supersonic suit down to linear crawl. Double that table and rehash!")
        ],
        "quiz": [
            {
                "q": "What is the average time complexity of searching for a key in a Hash Table under simple uniform hashing?",
                "options": [
                    "O(1)",
                    "O(log n)",
                    "O(n)",
                    "O(n log n)"
                ],
                "answer": 0,
                "explanation": "Under simple uniform hashing and a bounded load factor, searching a Hash Table takes O(1) constant time on average."
            },
            {
                "q": "What is the Load Factor (alpha) of a hash table containing 60 elements across 100 buckets?",
                "options": [
                    "1.67",
                    "0.60",
                    "6.0",
                    "0.06"
                ],
                "answer": 1,
                "explanation": "Load factor alpha = n / m = 60 / 100 = 0.60."
            },
            {
                "q": "In Open Addressing with Linear Probing, what phenomenon causes long contiguous runs of occupied slots?",
                "options": [
                    "Secondary Clustering",
                    "Primary Clustering",
                    "Hash Inversion",
                    "Modular Drift"
                ],
                "answer": 1,
                "explanation": "Primary clustering is the tendency for linear probing to create long blocks of occupied cells, increasing average probe counts."
            },
            {
                "q": "What is the worst-case search time in a Hash Table if all n keys collide into the identical bucket?",
                "options": [
                    "O(1)",
                    "O(log n)",
                    "O(n)",
                    "O(2^n)"
                ],
                "answer": 2,
                "explanation": "If every single key collides into the exact same bucket, the table degenerates into a linear linked list of length n, requiring O(n) search."
            }
        ],
        "summary": "Hash Tables are the workhorses of software engineering, providing O(1) average lookup, insert, and delete. Maintaining a low load factor via dynamic rehashing prevents performance degradation."
    },

    # 8. SETS & DISJOINT SETS (Scarlet Witch)
    {
        "filename": "topic-sets-and-disjoint-sets.html",
        "topic_id": "sets-and-disjoint-sets",
        "mission_num": "02",
        "mission_title": "DATA STRUCTURES",
        "mission_url": "mission-02.html",
        "topic_num": "TOPIC 05",
        "topic_title": "SETS & DISJOINT-SET UNION (DSU)",
        "hero_name": "SCARLET WITCH",
        "hero_color": "#e11d48",
        "hero_tag": "HEX DISJOINT PARTITION MAGIC",
        "hero_quote": "Reality divides into disjoint realms. With chaos magic, we fuse universes and find root realities in near-constant time.",
        "badge_color": "#ffe4e6",
        "viz_type": "disjoint_set",
        "problem_invariants": """
<p>A <strong>Disjoint-Set Data Structure</strong> (also termed <strong>Union-Find</strong> or <strong>DSU</strong>) maintains a collection of disjoint (non-overlapping) dynamic sets of elements \(\mathcal{S} = \{S_1, S_2, \dots, S_k\}\), where each set is identified by a unique <strong>Representative</strong> element (the root of the set tree).</p>
<p>Core DSU Primitive Operations:</p>
<ul>
  <li><code>make_set(x)</code>: Initializes a singleton set containing element \(x\) where \(x\) is its own parent and representative.</li>
  <li><code>find(x)</code>: Traverses parent pointers to return the unique representative (root) of the set containing element \(x\). Allows testing if elements belong to the same set: <code>find(u) == find(v)</code>.</li>
  <li><code>union(x, y)</code>: Merges the set containing \(x\) with the set containing \(y\). If both elements already share the same representative, union does nothing (or flags a cycle).</li>
</ul>
<p><strong>Two Vital Heuristic Optimizations:</strong></p>
<ol>
  <li><strong>Union by Rank / Size:</strong> Always attaches the root of the shallower (or smaller) tree to the root of the deeper tree, preventing deep unbalanced tree chains and bounding tree height to \(O(\log n)\).</li>
  <li><strong>Path Compression:</strong> During any <code>find(x)</code> query, flattens the tree structure by making every node on the traversal path point directly to the root, achieving the nearly-constant Inverse Ackermann bound \(\alpha(n)\).</li>
</ol>
""",
        "naive_vs_optimal": """
<p>A naive DSU implementation simply links parents arbitrarily (<code>parent[root_x] = root_y</code>). On adversarial inputs (e.g., repeatedly calling union on consecutive elements), the trees degenerate into a tall linear vine of height \(n\), causing <code>find</code> operations to take \(O(n)\) time. Combining Union by Rank with Path Compression crushes the amortized cost per operation to \(\Theta(\alpha(n)) \le 4\) for any universe size conceivable.</p>
<div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px; margin-top:12px;">
  <div style="background:#fee2e2; border:2px solid #ef4444; padding:12px; font-size:0.85rem;">
    <strong style="color:#b91c1c;">NAIVE UNION-FIND</strong><br>
    Arbitrary parent pointer updates.<br>
    Tree Height: Up to \(O(n)\)<br>
    Find Time: \(O(n)\)<br>
    Catastrophic slowdown when running Kruskal's MST algorithm.
  </div>
  <div style="background:#dcfce7; border:2px solid #16a34a; padding:12px; font-size:0.85rem;">
    <strong style="color:#15803d;">DSU WITH RANK + PATH COMPRESSION</strong><br>
    Dynamic path flattening during traversal.<br>
    Amortized Time: \(\Theta(\alpha(n))\)<br>
    Inverse Ackermann \(\alpha(n) \le 4\) for \(n = 10^{80}\) (particles in observable universe!).
  </div>
</div>
""",
        "math_formulation": r"""
<p><strong>The Tarjan Bound:</strong> For a sequence of \(m\) operations on \(n\) elements:</p>
\[ T(m, n) = \Theta(m \cdot \alpha(n)) \]
<p>Where \(\alpha(n)\) is the <strong>Inverse Ackermann Function</strong>. The standard Ackermann function \(A(i, j)\) grows with astronomical speed:</p>
\[ A(1, n) = 2n, \quad A(2, n) = 2^n, \quad A(3, n) = 2^{2^{\cdot^{\cdot^2}}} (n \text{ towers of 2}), \quad A(4, 2) = 2^{65536} \]
<p>Since \(A(4, 2)\) exceeds the estimated total number of atoms in the entire observable universe (\(\sim 10^{80}\)), \(\alpha(n) \le 4\) for all practical inputs \(n\). In algorithmic practice, DSU operations run in effective \(O(1)\) constant time!</p>
""",
        "worked_example": """
<p><strong>Worked Example:</strong> Execute DSU operations on elements \(\{1, 2, 3, 4, 5\}\) using Union by Rank and Path Compression.</p>
<ol style="margin-left:20px; line-height:1.8;">
  <li><strong>Initial:</strong> <code>parent = [0, 1, 2, 3, 4, 5], rank = [0, 0, 0, 0, 0, 0]</code>. Five isolated components.</li>
  <li><strong>Union(1, 2):</strong> <code>find(1) = 1, find(2) = 2</code>. Ranks equal (0). Make 1 parent of 2: <code>parent[2] = 1, rank[1] = 1</code>.</li>
  <li><strong>Union(3, 4):</strong> <code>find(3) = 3, find(4) = 4</code>. Make 3 parent of 4: <code>parent[4] = 3, rank[3] = 1</code>.</li>
  <li><strong>Union(2, 4):</strong>
      <br>Find(2): Follows <code>parent[2] = 1</code> \(\implies\) root = 1.
      <br>Find(4): Follows <code>parent[4] = 3</code> \(\implies\) root = 3.
      <br>Roots differ! <code>rank[1] = 1, rank[3] = 1</code>. Make 1 parent of 3: <code>parent[3] = 1, rank[1] = 2</code>.
      <br>Set {1, 2, 3, 4} now merged under root 1.
  </li>
  <li><strong>Find(4) with Path Compression:</strong> Traverses \(4 \to 3 \to 1\). Compresses pointer: <code>parent[4] = 1</code> directly! Subsequent <code>find(4)</code> takes exactly 1 step!</li>
</ol>
""",
        "complexity_table": [
            ("MakeSet(x)", "O(1)", "O(1)", "Allocates single parent and rank cell"),
            ("Find(x) (Naive)", "O(n)", "Omega(1)", "Can degrade to chain without optimizations"),
            ("Find(x) (Rank + Path Compression)", "O(alpha(n))", "Omega(1)", "Nearly constant inverse Ackermann amortized bound"),
            ("Union(x, y)", "O(alpha(n))", "Omega(1)", "Dominated by two find root queries"),
            ("Connected Components Check", "O(alpha(n))", "Omega(1)", "Direct comparison find(u) == find(v)")
        ],
        "code": '''class ChaosDisjointSet:
    """
    Disjoint-Set Union with Union by Rank and Path Compression.
    Amortized complexity per operation: O(alpha(n)).
    """
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.num_components = n
        
    def find(self, i: int) -> int:
        # Path Compression: make nodes point directly to root
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
        
    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)
        
        if root_i == root_j:
            return False  # Already in same set; indicates cycle!
            
        # Union by Rank: attach shallower tree to deeper tree
        if self.rank[root_i] < self.rank[root_j]:
            self.parent[root_i] = root_j
        elif self.rank[root_i] > self.rank[root_j]:
            self.parent[root_j] = root_i
        else:
            self.parent[root_j] = root_i
            self.rank[root_i] += 1
            
        self.num_components -= 1
        return True''',
        "practical_considerations": """
<p><strong>1. Cycle Detection in Undirected Graphs:</strong> For every edge \((u, v)\), if <code>find(u) == find(v)</code>, the edge connects two vertices already in the same component, proving that adding this edge would create a cycle! This is the engine powering Kruskal's algorithm.</p>
<p><strong>2. Dynamic Connectivity:</strong> DSU efficiently supports incremental edge additions (online connectivity queries). However, standard DSU does not support edge <em>deletions</em> efficiently (requires offline rollback stacks).</p>
<p><strong>3. Image Segmentation & Percolation:</strong> In computer vision, Connected-Component Labeling (CCL) groups neighboring pixels of matching colors using DSU union passes over the image matrix.</p>
""",
        "speech_bubbles": [
            ("Scarlet Witch", "Reality is shaped by boundaries. When two alternate timelines must unite, chaos magic bonds them by rank to keep the multiverse tree shallow!"),
            ("Scarlet Witch", "Path compression is the ultimate spell: the instant you trace a path to the root reality, all intermediate universes collapse directly to the nexus. Alpha(n) is practically constant!")
        ],
        "quiz": [
            {
                "q": "What is the amortized time complexity of Union-Find when combining Union by Rank with Path Compression?",
                "options": [
                    "O(1) strict",
                    "O(alpha(n)) where alpha is the inverse Ackermann function",
                    "O(log n)",
                    "O(n)"
                ],
                "answer": 1,
                "explanation": "Robert Tarjan proved that Union by Rank combined with Path Compression achieves O(alpha(n)) amortized time, which is <= 4 for all practical universe inputs."
            },
            {
                "q": "How does Path Compression optimize the find(x) operation?",
                "options": [
                    "By deleting visited nodes from memory",
                    "By making every visited node point directly to the root of the set",
                    "By sorting the parent pointers numerically",
                    "By converting the tree into a doubly linked list"
                ],
                "answer": 1,
                "explanation": "Path compression flattens the tree during find(x) by reparenting every node on the traversal path directly to the root."
            },
            {
                "q": "Which major Minimum Spanning Tree algorithm relies heavily on Disjoint Sets to prevent cycles?",
                "options": [
                    "Prim's Algorithm",
                    "Kruskal's Algorithm",
                    "Dijkstra's Algorithm",
                    "Bellman-Ford Algorithm"
                ],
                "answer": 1,
                "explanation": "Kruskal's algorithm iterates over sorted edges, using DSU find queries to test whether endpoints already belong to the same connected component."
            },
            {
                "q": "What does a return value of find(u) == find(v) indicate when testing endpoints of edge (u, v)?",
                "options": [
                    "The edge is the shortest path",
                    "Adding edge (u, v) creates a cycle in the graph",
                    "Vertices u and v have degree 0",
                    "The graph is disconnected"
                ],
                "answer": 1,
                "explanation": "If u and v already share the same set representative, an alternative path already connects them, meaning adding edge (u, v) forms a cycle."
            }
        ],
        "summary": "Disjoint-Set Union (Union-Find) with Union by Rank and Path Compression operates in near-constant O(alpha(n)) time. It is the premier data structure for cycle detection, dynamic connectivity, and Kruskal's MST."
    },

    # 9. MAXIMUM AND MINIMUM / TOURNAMENT METHOD (Hawkeye)
    {
        "filename": "topic-maximum-and-minimum.html",
        "topic_id": "maximum-and-minimum",
        "mission_num": "03",
        "mission_title": "DIVIDE AND CONQUER",
        "mission_url": "mission-03.html",
        "topic_num": "TOPIC 01",
        "topic_title": "MAXIMUM & MINIMUM (TOURNAMENT METHOD)",
        "hero_name": "HAWKEYE",
        "hero_color": "#7c3aed",
        "hero_tag": "PRECISION TOURNAMENT TARGETING",
        "hero_quote": "Never waste an arrow. Divide the battlefield, pair up targets in tournament brackets, and lock onto both extremes in 1.5n comparisons.",
        "badge_color": "#ede9fe",
        "viz_type": "min_max",
        "problem_invariants": """
<p>The <strong>Simultaneous Maximum and Minimum Problem</strong> requires finding both the largest element (\(\max\)) and the smallest element (\(\min\)) in an unordered array of \(n\) elements.</p>
<p><strong>Theoretical Comparison Lower Bound:</strong></p>
<ul>
  <li>Finding maximum alone requires at least \(n - 1\) comparisons.</li>
  <li>Finding minimum alone requires at least \(n - 1\) comparisons.</li>
  <li>A naive sequential approach requires \((n - 1) + (n - 1) = 2n - 2\) comparisons.</li>
  <li>Can we do better? <strong>Yes!</strong> By leveraging the <strong>Divide-and-Conquer Tournament Method</strong> (or pairwise grouping), the information-theoretic lower bound is strictly \(\lceil \frac{3n}{2} \rceil - 2\) comparisons.</li>
</ul>
<p><strong>Tournament Divide-and-Conquer Strategy:</strong></p>
<ol>
  <li><strong>Base Case 1 (\(n = 1\)):</strong> Return \((arr[0], arr[0])\) (0 comparisons).</li>
  <li><strong>Base Case 2 (\(n = 2\)):</strong> Compare \(arr[0]\) and \(arr[1]\); assign larger to \(\max\), smaller to \(\min\) (1 comparison).</li>
  <li><strong>Recursive Step (\(n > 2\)):</strong> Divide array into two equal halves at \(\text{mid} = \lfloor \frac{\text{low} + \text{high}}{2} \rfloor\). Recursively find \((\min_1, \max_1)\) and \((\min_2, \max_2)\). Combine by computing \(\min = \min(\min_1, \min_2)\) and \(\max = \max(\max_1, \max_2)\) (2 comparisons).</li>
</ol>
""",
        "naive_vs_optimal": """
<p>A naive linear scan compares each element against the running maximum, and if false, compares against the running minimum. In the worst case (monotonically decreasing array), it executes \(2(n - 1)\) comparisons. Hawkeye's Tournament Method cuts comparisons by 25% to \(\frac{3n}{2} - 2\), reaching the theoretical absolute minimum comparison limit proved by adversary arguments.</p>
<div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px; margin-top:12px;">
  <div style="background:#fee2e2; border:2px solid #ef4444; padding:12px; font-size:0.85rem;">
    <strong style="color:#b91c1c;">NAIVE LINEAR SCAN</strong><br>
    \(2n - 2\) comparisons.<br>
    For \(n = 1000 \implies 1998\) comparisons.<br>
    Redundant tests comparing confirmed smaller elements against maximum.
  </div>
  <div style="background:#dcfce7; border:2px solid #16a34a; padding:12px; font-size:0.85rem;">
    <strong style="color:#15803d;">TOURNAMENT METHOD</strong><br>
    \(\frac{3n}{2} - 2\) comparisons.<br>
    For \(n = 1000 \implies 1498\) comparisons.<br>
    Saves 500 comparison operations! Reaches optimal adversary bound.
  </div>
</div>
""",
        "math_formulation": r"""
<p><strong>Recurrence Relation for Tournament Divide-and-Conquer:</strong></p>
\[ T(n) = \begin{cases} 0 & \text{if } n = 1 \\ 1 & \text{if } n = 2 \\ 2T(n/2) + 2 & \text{if } n > 2 \end{cases} \]
<p><strong>Solving the Recurrence (Assuming \(n = 2^k\)):</strong></p>
\[ T(n) = 2T(n/2) + 2 = 2(2T(n/4) + 2) + 2 = 4T(n/4) + 4 + 2 \]
\[ T(n) = 2^{k-1} T(2) + \sum_{i=1}^{k-1} 2^i = \frac{n}{2}(1) + (2^k - 2) = \frac{n}{2} + n - 2 = \frac{3n}{2} - 2 \]
<p>Thus, exact comparison step count: \(T(n) = \frac{3n}{2} - 2\). Asymptotically: \(\Theta(n)\).</p>
""",
        "worked_example": """
<p><strong>Worked Example:</strong> Trace Tournament Min-Max on array <code>arr = [22, 13, -5, 88, 7, 31, 99, 4]</code> (\(n = 8\)).</p>
<ol style="margin-left:20px; line-height:1.8;">
  <li><strong>Subdivide:</strong> Left <code>[22, 13, -5, 88]</code>, Right <code>[7, 31, 99, 4]</code>.</li>
  <li><strong>Left Subtree:</strong>
      <br>Pair <code>[22, 13]</code>: 1 comparison \(\implies (\min=13, \max=22)\).
      <br>Pair <code>[-5, 88]</code>: 1 comparison \(\implies (\min=-5, \max=88)\).
      <br>Combine: \(\min = \min(13, -5) = -5\) (1 comp), \(\max = \max(22, 88) = 88\) (1 comp). Left result: <code>(-5, 88)</code>. (Total = 4 comps).
  </li>
  <li><strong>Right Subtree:</strong>
      <br>Pair <code>[7, 31]</code>: 1 comparison \(\implies (\min=7, \max=31)\).
      <br>Pair <code>[99, 4]</code>: 1 comparison \(\implies (\min=4, \max=99)\).
      <br>Combine: \(\min = \min(7, 4) = 4\) (1 comp), \(\max = \max(31, 99) = 99\) (1 comp). Right result: <code>(4, 99)</code>. (Total = 4 comps).
  </li>
  <li><strong>Final Root Combine:</strong>
      <br>\(\min = \min(-5, 4) = -5\) (1 comparison).
      <br>\(\max = \max(88, 99) = 99\) (1 comparison).
  </li>
</ol>
<p><strong>Final Solution:</strong> \(\min = -5, \max = 99\).
<br><strong>Total Comparisons Executed:</strong> \(4 + 4 + 2 = 10\) comparisons.
<br><strong>Formula Verification:</strong> \(\frac{3(8)}{2} - 2 = 12 - 2 = 10\). Matches formula perfectly!</p>
""",
        "complexity_table": [
            ("Tournament Divide & Conquer", "3n/2 - 2 comps", "O(log n) space", "Proven information-theoretic comparison lower bound"),
            ("Pairwise Iterative Scan", "3n/2 comps", "O(1) space", "Iterates in pairs of 2; achieves same comparison count in-place"),
            ("Naive Linear Scan (Worst)", "2n - 2 comps", "O(1) space", "Monotonically decreasing input tests every element twice"),
            ("Naive Linear Scan (Best)", "n - 1 comps", "O(1) space", "Monotonically increasing input skips second if condition"),
            ("Sorting Array First", "O(n log n) comps", "O(1) / O(n) space", "Extremely wasteful if only extremes are needed")
        ],
        "code": '''def tournament_min_max(arr: list[int], low: int, high: int) -> tuple[int, int]:
    """
    Divide and Conquer Tournament Method to find Min and Max.
    Executes exactly 3n/2 - 2 comparisons when n is a power of 2.
    """
    # Base Case 1: Only 1 element
    if low == high:
        return arr[low], arr[low]
        
    # Base Case 2: Exactly 2 elements (1 comparison)
    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
            
    # Divide step
    mid = (low + high) // 2
    min1, max1 = tournament_min_max(arr, low, mid)
    min2, max2 = tournament_min_max(arr, mid + 1, high)
    
    # Conquer / Combine step (2 comparisons)
    overall_min = min1 if min1 < min2 else min2
    overall_max = max1 if max1 > max2 else max2
    
    return overall_min, overall_max''',
        "practical_considerations": """
<p><strong>1. Second-Best Element (Tournament Tree):</strong> The classic question in computer science: how many comparisons to find the 2nd largest element? A tournament bracket determines the max in \(n - 1\) comparisons. The 2nd largest must have lost directly to the champion during the bracket, which is one of only \(\lceil \log_2 n \rceil\) elements! Thus, finding both max and 2nd max takes only \(n + \lceil \log_2 n \rceil - 2\) comparisons.</p>
<p><strong>2. Iterative Pairwise Processing:</strong> The recursive tournament method requires \(O(\log n)\) stack frames. An iterative pairwise algorithm pairs elements up sequentially (\(arr[i], arr[i+1]\)), compares them (1 comparison), and tests the larger against global max and smaller against global min. It achieves the exact same \(\frac{3n}{2}\) comparison bound with strictly \(O(1)\) auxiliary memory!</p>
<p><strong>3. SIMD Vectorization:</strong> Modern Intel/ARM CPUs feature vector instructions (<code>_mm256_min_epi32</code>, <code>_mm256_max_epi32</code>) capable of computing min/max across 8 integers simultaneously in hardware clock cycles.</p>
""",
        "speech_bubbles": [
            ("Hawkeye", "Bullseye! If you're comparing every element against both min and max, you're shooting double the arrows. Pair them up in tournament brackets and hit both extremes in 1.5n shots!"),
            ("Hawkeye", "Check your recurrence relation: T(n) = 2T(n/2) + 2. In university exams, solving this using induction down to 3n/2 - 2 is guaranteed marks. Never miss a target.")
        ],
        "quiz": [
            {
                "q": "What is the exact number of comparisons executed by the Tournament Method to find Min and Max for n = 16 elements?",
                "options": [
                    "30",
                    "22",
                    "16",
                    "32"
                ],
                "answer": 1,
                "explanation": "Using T(n) = (3n/2) - 2: for n = 16, T(16) = (3 * 16 / 2) - 2 = 24 - 2 = 22 comparisons."
            },
            {
                "q": "How many comparisons does the naive linear scan execute in the worst-case for an array of size n?",
                "options": [
                    "n - 1",
                    "2n - 2",
                    "3n/2 - 2",
                    "n log n"
                ],
                "answer": 1,
                "explanation": "In the worst case (e.g. descending order), each element from index 1 to n-1 fails the max check and must be evaluated in the min check, totaling 2(n - 1) comparisons."
            },
            {
                "q": "What is the minimum number of comparisons needed to identify both the largest and second-largest element in an array of size n?",
                "options": [
                    "2n - 3",
                    "n + log2(n) - 2",
                    "3n/2 - 2",
                    "n log n"
                ],
                "answer": 1,
                "explanation": "In a tournament tree, finding the winner takes n - 1 comparisons. The runner-up must have lost directly to the winner along the tree path of height log2(n), requiring log2(n) - 1 further comparisons."
            },
            {
                "q": "What is the auxiliary space complexity of the recursive Divide-and-Conquer Tournament Min-Max algorithm?",
                "options": [
                    "O(1)",
                    "O(log n)",
                    "O(n)",
                    "O(n^2)"
                ],
                "answer": 1,
                "explanation": "The recursion tree halves the array at each level, requiring O(log n) activation frames on the call stack."
            }
        ],
        "summary": "The Tournament Method is a textbook example of Divide-and-Conquer efficiency, reducing comparisons from 2n - 2 down to the proven theoretical lower bound of 3n/2 - 2."
    },

    # 10. BINARY SEARCH (Spider-Man)
    {
        "filename": "topic-binary-search.html",
        "topic_id": "binary-search",
        "mission_num": "03",
        "mission_title": "DIVIDE AND CONQUER",
        "mission_url": "mission-03.html",
        "topic_num": "TOPIC 02",
        "topic_title": "BINARY SEARCH",
        "hero_name": "SPIDER-MAN",
        "hero_color": "#dc2626",
        "hero_tag": "LOGARITHMIC WEB-SLINGING HALVING",
        "hero_quote": "My spider-sense detects sorted data! With every web zip, we slice the search space in half until the target is trapped.",
        "badge_color": "#fee2e2",
        "viz_type": "binary_search",
        "problem_invariants": """
<p><strong>Binary Search</strong> is the quintessential Divide-and-Conquer algorithm for locating the position of a target key \(K\) within a <strong>strictly sorted array</strong> \(A[0 \dots n-1]\).</p>
<p><strong>Loop Invariant:</strong> At the start of every iteration, if key \(K\) exists within array \(A\), it is guaranteed to reside within the index sub-range \([\text{low}, \text{high}]\).</p>
<p>Algorithm Steps:</p>
<ol>
  <li>Initialize search boundaries: \(\text{low} = 0, \text{high} = n - 1\).</li>
  <li>While \(\text{low} \le \text{high}\):
      <ul>
        <li>Compute probe index: \(\text{mid} = \text{low} + \lfloor \frac{\text{high} - \text{low}}{2} \rfloor\).</li>
        <li><strong>Match:</strong> If \(A[\text{mid}] == K\), return \(\text{mid}\) (Target found!).</li>
        <li><strong>Left Sub-Array:</strong> If \(K < A[\text{mid}]\), target cannot reside in right half; set \(\text{high} = \text{mid} - 1\).</li>
        <li><strong>Right Sub-Array:</strong> If \(K > A[\text{mid}]\), target cannot reside in left half; set \(\text{low} = \text{mid} + 1\).</li>
      </ul>
  </li>
  <li>If \(\text{low} > \text{high}\), return \(-1\) (Target does not exist in array).</li>
</ol>
""",
        "naive_vs_optimal": """
<p>Searching for a criminal in a New York City phonebook of \(n = 1,000,000\) names using Linear Search takes up to \(1,000,000\) comparisons. Spider-Man's Binary Search eliminates 500,000 possibilities on the very first web zip, trapping any target in at most \(\lfloor \log_2(1,000,000) \rfloor + 1 = 20\) comparisons!</p>
<div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px; margin-top:12px;">
  <div style="background:#fee2e2; border:2px solid #ef4444; padding:12px; font-size:0.85rem;">
    <strong style="color:#b91c1c;">LINEAR SEARCH [O(n)]</strong><br>
    Scans every index sequentially.<br>
    Worst Case: \(n\) steps.<br>
    For \(n = 10^9 \implies 1,000,000,000\) operations (takes ~1 second on 1GHz CPU).
  </div>
  <div style="background:#dcfce7; border:2px solid #16a34a; padding:12px; font-size:0.85rem;">
    <strong style="color:#15803d;">BINARY SEARCH [O(log n)]</strong><br>
    Halves search interval on every comparison.<br>
    Worst Case: \(\lfloor \log_2 n \rfloor + 1\) steps.<br>
    For \(n = 10^9 \implies \le 30\) operations (takes ~30 nanoseconds!).
  </div>
</div>
""",
        "math_formulation": r"""
<p><strong>Recurrence Relation for Binary Search:</strong></p>
\[ T(n) = T(n/2) + c \]
<p><strong>Solving via Master Theorem:</strong> Here \(a = 1, b = 2, f(n) = c = \Theta(n^0)\).</p>
\[ n^{\log_b a} = n^{\log_2 1} = n^0 = 1 \]
<p>Since \(f(n) = \Theta(n^{\log_b a})\) (Case 2 of Master Theorem with \(k = 0\)):</p>
\[ T(n) = \Theta(n^{\log_b a} \log^{k+1} n) = \Theta(1 \cdot \log^1 n) = \Theta(\log_2 n) \]
<p><strong>Maximum Number of Comparisons:</strong> In the worst case, the search continues until the interval size is 1:</p>
\[ \frac{n}{2^k} = 1 \implies 2^k = n \implies k = \log_2 n \implies \text{Total comparisons} = \lfloor \log_2 n \rfloor + 1 \]
""",
        "worked_example": """
<p><strong>Worked Example:</strong> Locate key \(K = 47\) inside sorted array <code>arr = [3, 9, 14, 21, 33, 47, 59, 68, 72, 85, 91]</code> (\(n = 11\)).</p>
<ol style="margin-left:20px; line-height:1.8;">
  <li><strong>Iteration 1:</strong> <code>low = 0, high = 10</code>.
      <br>\(\text{mid} = 0 + (10 - 0) // 2 = 5\).
      <br>Inspect <code>arr[5] = 47</code>.
      <br>Comparison: \(arr[5] == 47\)? <strong>MATCH FOUND on first probe!</strong> Return index 5.
  </li>
  <li><strong>Now search for \(K = 72\) (Multi-step Trace):</strong>
      <br><strong>Pass 1:</strong> <code>low = 0, high = 10 \implies mid = 5 (arr[5] = 47)</code>. Since \(72 > 47\), set <code>low = 6</code>.
      <br><strong>Pass 2:</strong> <code>low = 6, high = 10 \implies mid = 6 + (10-6)//2 = 8 (arr[8] = 72)</code>.
      <br>Comparison: \(arr[8] == 72\)? <strong>MATCH!</strong> Return index 8. (Completed in only 2 comparisons out of 11 elements!).
  </li>
</ol>
""",
        "complexity_table": [
            ("Best Case", "O(1)", "Omega(1)", "Target located immediately at initial midpoint index"),
            ("Average Case", "Theta(log n)", "Omega(1)", "Expected comparisons over uniform key distribution"),
            ("Worst Case", "O(log n)", "Omega(log n)", "Target at array extremity or not present in array"),
            ("Iterative Auxiliary Space", "O(1)", "O(1)", "Strictly three index variables (low, mid, high)"),
            ("Recursive Auxiliary Space", "O(log n)", "O(log n)", "Call stack depth bounded by log2(n) levels")
        ],
        "code": '''def binary_search(arr: list[int], target: int) -> int:
    """
    Classic iterative Binary Search with integer overflow protection.
    Returns index of target if found, else -1.
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        # Crucial: prevents integer overflow in fixed-width languages (C++/Java)
        # Instead of mid = (low + high) // 2:
        mid = low + (high - low) // 2
        
        if arr[mid] == target:
            return mid  # Target acquired!
        elif arr[mid] < target:
            low = mid + 1   # Target in right partition
        else:
            high = mid - 1  # Target in left partition
            
    return -1  # Target not in array''',
        "practical_considerations": """
<p><strong>1. The Infamous Midpoint Overflow Bug:</strong> In 2006, Joshua Bloch revealed that the standard binary search in Java's standard library contained a bug that existed for 9 years: writing <code>mid = (low + high) / 2</code> overflows a 32-bit signed integer if <code>low + high > 2^{31} - 1</code>, resulting in a negative index and <code>ArrayIndexOutOfBoundsException</code>. The fix is <code>low + (high - low) / 2</code> or unsigned shift <code>(low + high) >>> 1</code>.</p>
<p><strong>2. Binary Search on Answer / Monotonic Predicates:</strong> Binary Search isn't just for arrays! It solves optimization problems where a predicate function \(P(x)\) is monotonic (e.g. 'Can we ship all packages within \(D\) days with capacity \(W\)?'). We binary search over the answer range \([1, \sum W]\) in \(O(\log(\text{range}))\).</p>
<p><strong>3. Lower Bound & Upper Bound:</strong> Standard binary search finds any match. C++'s <code>std::lower_bound</code> finds the first index \(\ge K\), and <code>std::upper_bound</code> finds the first index \(> K\), enabling \(O(\log n)\) range counting.</p>
""",
        "speech_bubbles": [
            ("Spider-Man", "Friendly neighborhood reminder! Always write 'mid = low + (high - low) // 2'! That famous integer overflow bug slipped past engineers for nearly a decade!"),
            ("Spider-Man", "Remember rule #1: Binary search only works on SORTED arrays! If your web fluid is scrambled, sort it first or stick to linear scan.")
        ],
        "quiz": [
            {
                "q": "What is the maximum number of comparisons needed to locate an element in a sorted array of 1,000,000 elements using Binary Search?",
                "options": [
                    "20",
                    "1,000",
                    "500,000",
                    "1,000,000"
                ],
                "answer": 0,
                "explanation": "2^19 = 524,288 and 2^20 = 1,048,576. Thus floor(log2(1,000,000)) + 1 = 20 comparisons."
            },
            {
                "q": "Why is 'low + (high - low) // 2' preferred over '(low + high) // 2' in fixed-width integer languages?",
                "options": [
                    "It executes faster in machine code",
                    "It prevents arithmetic integer overflow when (low + high) exceeds maximum integer range",
                    "It automatically sorts the array",
                    "It eliminates the need for a while loop"
                ],
                "answer": 1,
                "explanation": "If low and high are large positive integers near 2^31 - 1, their sum overflows into a negative value, causing an index out of bounds crash."
            },
            {
                "q": "What is the Master Theorem case and resulting complexity for the recurrence T(n) = T(n/2) + O(1)?",
                "options": [
                    "Case 1: Theta(n)",
                    "Case 2: Theta(log n)",
                    "Case 3: Theta(n log n)",
                    "Case 2: Theta(n^2)"
                ],
                "answer": 1,
                "explanation": "Here a = 1, b = 2, f(n) = O(1). Since n^(log_2 1) = n^0 = 1 = f(n), Master Theorem Case 2 gives T(n) = Theta(log n)."
            },
            {
                "q": "What essential precondition must be satisfied before Binary Search can be executed on an array?",
                "options": [
                    "Array size must be a power of two",
                    "Elements must be unique with zero duplicates",
                    "Elements must be in sorted order",
                    "Array must contain positive numbers only"
                ],
                "answer": 2,
                "explanation": "Binary Search relies on the sorting invariant to eliminate half the remaining array on every midpoint comparison."
            }
        ],
        "summary": "Binary Search divides the problem size by 2 at each step, achieving O(log n) worst-case time with O(1) space. It is one of the most powerful algorithms in computer science."
    }
]

print(f"Loaded Part 2: {len(PART2_TOPICS)} topics")
