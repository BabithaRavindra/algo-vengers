# academic_data_part4.py - Topics 16 to 19
# Mission 04: Advanced Algorithms (Topics 16-17) & Mission 05: Master Mission (Topics 18-19)

PART4_TOPICS = [
    # 16. KRUSKAL'S & PRIM'S ALGORITHMS (Wolverine)
    {
        "filename": "topic-kruskals-and-prims.html",
        "topic_id": "kruskals-and-prims",
        "mission_num": "04",
        "mission_title": "ADVANCED ALGORITHMS",
        "mission_url": "mission-04.html",
        "topic_num": "TOPIC 04",
        "topic_title": "KRUSKAL'S & PRIM'S ALGORITHMS",
        "hero_name": "WOLVERINE",
        "hero_color": "#ca8a04",
        "hero_tag": "ADAMANTIUM CUTTING STRATEGIES",
        "hero_quote": "Two ways to slice an MST: sort global edges with adamantium claws (Kruskal) or expand from one root (Prim). Either way, villains don't escape.",
        "badge_color": "#fef9c3",
        "viz_type": "kruskal_prim",
        "problem_invariants": """
<p>Kruskal's and Prim's algorithms represent two contrasting greedy methodologies for computing a <strong>Minimum Cost Spanning Tree (MST)</strong> on a connected, weighted, undirected graph \(G = (V, E)\).</p>
<p><strong>1. Kruskal's Algorithm (Edge-Centric / Forest-Growing):</strong></p>
<ul>
  <li>Sorts all \(|E|\) edges globally in non-decreasing order of weight: \(w(e_1) \le w(e_2) \le \dots \le w(e_m)\).</li>
  <li>Iterates through sorted edges, greedily adding edge \((u, v)\) to the MST if and only if it does not form a cycle with previously chosen edges.</li>
  <li>Cycle detection is maintained in \(O(\alpha(V))\) time using a <strong>Disjoint-Set Union (DSU)</strong> data structure.</li>
  <li>Works best on <strong>Sparse Graphs</strong> where \(|E| \ll |V|^2\).</li>
</ul>
<p><strong>2. Prim's Algorithm (Vertex-Centric / Tree-Growing):</strong></p>
<ul>
  <li>Begins at an arbitrary starting root vertex \(s\), initializing a growing tree \(T = \{s\}\).</li>
  <li>At each iteration, identifies the minimum-weight edge connecting a vertex in \(T\) to a vertex outside \(T\) (the cut \((T, V - T)\)).</li>
  <li>Greedily adds this lightest frontier edge and the adjacent vertex to \(T\), repeating until all \(|V|\) vertices are spanned.</li>
  <li>Maintained using a <strong>Min-Priority Queue (Binary Heap)</strong>.</li>
  <li>Works best on <strong>Dense Graphs</strong> where \(|E| \approx |V|^2\).</li>
</ul>
""",
        "naive_vs_optimal": """
<p>Comparing Kruskal's vs Prim's performance depends fundamentally on graph density. On a sparse road network with \(V = 10,000\) and \(E = 20,000\), Kruskal's edge sorting takes \(20,000 \log(20,000)\) steps, beating Prim. On a dense telecommunications mesh where \(E = 50,000,000\), Prim with a Fibonacci Heap executes in \(O(E + V \log V)\), vastly outperforming Kruskal's massive edge sort!</p>
<div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px; margin-top:12px;">
  <div style="background:#fef9c3; border:2px solid #ca8a04; padding:12px; font-size:0.85rem;">
    <strong style="color:#854d0e;">KRUSKAL'S ALGORITHM</strong><br>
    Time: \(O(E \log E) = O(E \log V)\)<br>
    Data Structure: Disjoint Sets (Union-Find)<br>
    Excels on: Sparse Graphs (\(E = O(V)\))
  </div>
  <div style="background:#dcfce7; border:2px solid #16a34a; padding:12px; font-size:0.85rem;">
    <strong style="color:#15803d;">PRIM'S ALGORITHM</strong><br>
    Time: \(O((V + E) \log V)\) with Min-Heap<br>
    Data Structure: Priority Queue<br>
    Excels on: Dense Graphs (\(E = \Omega(V^2)\))
  </div>
</div>
""",
        "math_formulation": r"""
<p><strong>Asymptotic Complexity Breakdown:</strong></p>
<ul>
  <li><strong>Kruskal's Algorithm:</strong>
      \[ T_{\text{Kruskal}} = \underbrace{O(E \log E)}_{\text{Sort edges}} + \underbrace{O(E \cdot \alpha(V))}_{\text{DSU find/unions}} = O(E \log E) = O(E \log V) \]
  </li>
  <li><strong>Prim's Algorithm with Binary Heap:</strong>
      \[ T_{\text{Prim}} = \underbrace{O(V \log V)}_{\text{Extract-Min on V vertices}} + \underbrace{O(E \log V)}_{\text{Decrease-Key on E edges}} = O((V + E) \log V) \]
  </li>
  <li><strong>Prim's Algorithm with Fibonacci Heap:</strong>
      \[ T_{\text{Fib}} = O(V \log V + E \cdot 1) = O(E + V \log V) \]
  </li>
</ul>
""",
        "worked_example": """
<p><strong>Worked Example:</strong> Trace Kruskal's and Prim's on a graph with vertices \(\{A, B, C, D, E\}\) and edges:</p>
<p><code>(A, B): 4, (A, C): 2, (B, C): 1, (B, D): 5, (C, D): 8, (C, E): 10, (D, E): 2, (D, A): 7</code></p>
<ol style="margin-left:20px; line-height:1.8;">
  <li><strong>Kruskal's Trace:</strong>
      <br>Sorted edges: <code>(B, C): 1, (D, E): 2, (A, C): 2, (A, B): 4, (B, D): 5, (D, A): 7, (C, D): 8, (C, E): 10</code>.
      <br>1. Pick <code>(B, C): 1</code>. Components: \(\{B, C\}\). (Edges in MST = 1).
      <br>2. Pick <code>(D, E): 2</code>. Components: \(\{B, C\}, \{D, E\}\). (Edges = 2).
      <br>3. Pick <code>(A, C): 2</code>. Components: \(\{A, B, C\}, \{D, E\}\). (Edges = 3).
      <br>4. Inspect <code>(A, B): 4</code>. <code>find(A) == find(B)</code>! Cycle detected! <strong>REJECT!</strong>
      <br>5. Pick <code>(B, D): 5</code>. Connects \(\{A, B, C\}\) to \(\{D, E\}\). (Edges = 4 = \(V - 1\)).
      <br><strong>MST Edges:</strong> \(\{(B, C): 1, (D, E): 2, (A, C): 2, (B, D): 5\}\). Total cost = <strong>10</strong>.
  </li>
  <li><strong>Prim's Trace (Start at Root A):</strong>
      <br>Initial tree: \(\{A\}\). Frontier edges from A: \((A, C): 2, (A, B): 4, (A, D): 7\).
      <br>1. Lightest edge: \((A, C): 2\). Add \(C\) to tree. Tree: \(\{A, C\}\).
      <br>2. Frontier from \(\{A, C\}\): \((C, B): 1, (A, B): 4, (C, D): 8, (C, E): 10\).
      <br>Lightest: \((C, B): 1\). Add \(B\) to tree. Tree: \(\{A, B, C\}\).
      <br>3. Frontier from \(\{A, B, C\}\): \((B, D): 5, (A, D): 7, (C, D): 8, (C, E): 10\).
      <br>Lightest: \((B, D): 5\). Add \(D\) to tree. Tree: \(\{A, B, C, D\}\).
      <br>4. Frontier from \(\{A, B, C, D\}\): \((D, E): 2, (C, E): 10\).
      <br>Lightest: \((D, E): 2\). Add \(E\) to tree. Tree: \(\{A, B, C, D, E\}\). (All vertices spanned!).
      <br><strong>Total Weight:</strong> \(2 + 1 + 5 + 2 = \mathbf{10}\). Exactly identical to Kruskal!
  </li>
</ol>
""",
        "complexity_table": [
            ("Kruskal's Time", "O(E log V)", "O(V) space", "Disjoint-Set Union; edge sorting dominates"),
            ("Prim's Time (Binary Heap)", "O((V + E) log V)", "O(V) space", "Priority queue with decrease-key"),
            ("Prim's Time (Adjacency Matrix)", "O(V^2)", "O(V^2) space", "Optimal for dense graphs where E approx V^2"),
            ("Cycle Detection Method", "Union-Find (Kruskal)", "N/A (Prim)", "Kruskal checks DSU; Prim maintains visited set"),
            ("Forest vs Tree", "Forest of subtrees (Kruskal)", "Single growing tree (Prim)", "Structural growth dynamic difference")
        ],
        "code": '''def kruskal_mst(vertices: int, edges: list[tuple[int, int, float]]) -> tuple[float, list]:
    """
    Kruskal's Algorithm: Sort edges + Union-Find cycle check.
    edges: list of (u, v, weight).
    Time Complexity: O(E log E), Space: O(V).
    """
    edges.sort(key=lambda x: x[2])  # Sort by weight ascending
    parent = list(range(vertices))
    
    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]
        
    mst = []
    total_cost = 0.0
    
    for u, v, w in edges:
        root_u, root_v = find(u), find(v)
        if root_u != root_v:
            parent[root_u] = root_v  # Union
            mst.append((u, v, w))
            total_cost += w
            if len(mst) == vertices - 1:
                break
                
    return total_cost, mst''',
        "practical_considerations": """
<p><strong>1. Choosing Between Kruskal and Prim:</strong> In real-world software engineering, if the graph is given as an edge list or is sparse (\(E \ll V^2\)), Kruskal's algorithm is vastly simpler to implement and faster. If the graph is dense (\(E \approx V^2\)), Prim's with an adjacency matrix (\(O(V^2)\)) avoids the expensive \(O(E \log E)\) edge sort.</p>
<p><strong>2. Disjoint Disconnected Graphs:</strong> If graph \(G\) is disconnected, Kruskal's naturally outputs a <em>Minimum Spanning Forest</em> (an MST for each connected component). Prim's terminates after spanning the starting component and requires restarting on unvisited vertices.</p>
<p><strong>3. Cluster Analysis (Single-Linkage Clustering):</strong> Stopping Kruskal's algorithm when \(k\) connected components remain produces a single-linkage hierarchical clustering that maximizes the minimum inter-cluster distance!</p>
""",
        "speech_bubbles": [
            ("Wolverine", "Listen bub: Kruskal sorts every edge up front with adamantium precision and uses Union-Find to dodge cycles. Prim grows outward from one root like a badger defending its den."),
            ("Wolverine", "Exam tip: If the graph is sparse, Kruskal wins. If it's dense with edges connecting everything in sight, Prim takes the crown. Choose your weapon wisely!")
        ],
        "quiz": [
            {
                "q": "What data structure is essential for Kruskal's algorithm to achieve O(E log V) runtime by preventing cycles?",
                "options": [
                    "Stack",
                    "Disjoint-Set Union (Union-Find)",
                    "Binary Search Tree",
                    "Hash Map"
                ],
                "answer": 1,
                "explanation": "Kruskal's algorithm relies on Disjoint-Set Union (DSU) to check whether two vertices belong to the same component and prevent cycles in near-constant time."
            },
            {
                "q": "When is Prim's algorithm with an adjacency matrix (O(V^2)) preferred over Kruskal's algorithm (O(E log V))?",
                "options": [
                    "When the graph is completely disconnected",
                    "When the graph is Dense (E is close to V^2)",
                    "When all edge weights are negative",
                    "When the graph is a tree"
                ],
                "answer": 1,
                "explanation": "In dense graphs where E is close to V^2, sorting edges in Kruskal takes O(V^2 log V), while Prim's matrix implementation takes only O(V^2)."
            },
            {
                "q": "What is the primary difference in structural growth between Kruskal's and Prim's algorithms?",
                "options": [
                    "Kruskal builds directed graphs; Prim builds undirected graphs",
                    "Kruskal builds an intermediate forest of disconnected trees that merge; Prim grows a single connected tree continuously",
                    "Kruskal requires positive weights; Prim allows negative weights",
                    "Kruskal uses BFS; Prim uses DFS"
                ],
                "answer": 1,
                "explanation": "Kruskal adds edges anywhere globally, forming a forest of subtrees that eventually merge. Prim always grows an unbroken tree outward from a starting root."
            },
            {
                "q": "If all edge weights in a graph are distinct, what is true about the MST produced by Kruskal vs Prim?",
                "options": [
                    "Kruskal finds a lighter tree than Prim",
                    "Both algorithms produce the exact same unique Minimum Spanning Tree",
                    "Prim's tree will contain fewer edges",
                    "Kruskal fails to terminate"
                ],
                "answer": 1,
                "explanation": "When all edge weights are distinct, the Minimum Spanning Tree is mathematically unique, meaning Kruskal and Prim will find the exact same MST."
            }
        ],
        "summary": "Kruskal sorts edges globally and merges components via DSU (best for sparse graphs). Prim expands a single tree greedily via a priority queue (best for dense graphs). Both find the optimal MST."
    },

    # 17. DIJKSTRA'S ALGORITHM (Captain Marvel)
    {
        "filename": "topic-dijkstras-algorithm.html",
        "topic_id": "dijkstras-algorithm",
        "mission_num": "04",
        "mission_title": "ADVANCED ALGORITHMS",
        "mission_url": "mission-04.html",
        "topic_num": "TOPIC 05",
        "topic_title": "DIJKSTRA'S SHORTEST PATH ALGORITHM",
        "hero_name": "CAPTAIN MARVEL",
        "hero_color": "#dc2626",
        "hero_tag": "COSMIC PHOTON BEAM RELAXATION",
        "hero_quote": "Higher, further, faster! Channel photon energy along the path of minimum cosmic resistance across planetary relay coordinates.",
        "badge_color": "#fee2e2",
        "viz_type": "dijkstra",
        "problem_invariants": """
<p><strong>Dijkstra's Algorithm</strong>, designed by Edsger W. Dijkstra in 1956, solves the <strong>Single-Source Shortest Path (SSSP)</strong> problem on a weighted, directed or undirected graph \(G = (V, E)\) with a fundamental constraint: <strong>all edge weights must be non-negative</strong> (\(\forall e \in E, w(e) \ge 0\)).</p>
<p>Given a source vertex \(s \in V\), the algorithm computes the minimum path distance \(d[v]\) from \(s\) to every vertex \(v \in V\).</p>
<p><strong>Core Algorithmic Invariant (Edge Relaxation):</strong></p>
\[ \text{If } d[u] + w(u, v) < d[v] \implies d[v] = d[u] + w(u, v) \]
<p><strong>Greedy Execution Loop:</strong></p>
<ol>
  <li>Initialize tentative distances: \(d[s] = 0\) and \(d[v] = \infty\) for all \(v \ne s\). Maintain a set \(S\) of finalized vertices (initially empty).</li>
  <li>Extract the vertex \(u \notin S\) with the minimum tentative distance \(d[u]\) using a <strong>Min-Priority Queue</strong>.</li>
  <li>Add \(u\) to finalized set \(S\). The distance \(d[u]\) is now mathematically guaranteed to be the true shortest path distance!</li>
  <li>Relax all outgoing edges \((u, v)\): if \(d[u] + w(u, v) < d[v]\), update \(d[v]\) and decrease key in priority queue.</li>
  <li>Repeat until all reachable vertices are finalized.</li>
</ol>
""",
        "naive_vs_optimal": """
<p>Why does Dijkstra require non-negative weights? The greedy choice assumes that once a vertex \(u\) is extracted with minimum distance, its distance can never be decreased by traveling through another unvisited vertex. If negative edges exist, this invariant collapses completely: a longer preliminary path could later encounter a massive negative edge (e.g. \(-50\)) and become shorter, causing Dijkstra to return incorrect answers. Graphs with negative weights require the <strong>Bellman-Ford Algorithm</strong> (\(O(V \cdot E)\)).</p>
<div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px; margin-top:12px;">
  <div style="background:#fee2e2; border:2px solid #ef4444; padding:12px; font-size:0.85rem;">
    <strong style="color:#b91c1c;">NEGATIVE EDGE WEIGHTS (FAILS)</strong><br>
    Greedy invariant violated.<br>
    Premature finalization locks incorrect distance.<br>
    Requires Bellman-Ford \(O(VE)\) to handle negative cycles.
  </div>
  <div style="background:#dcfce7; border:2px solid #16a34a; padding:12px; font-size:0.85rem;">
    <strong style="color:#15803d;">NON-NEGATIVE WEIGHTS [OPTIMAL]</strong><br>
    Monotonically increasing path lengths.<br>
    Min-Heap extracts guaranteed optimal vertex.<br>
    Blazing fast: \(O((V + E) \log V)\).
  </div>
</div>
""",
        "math_formulation": r"""
<p><strong>Triangle Inequality Invariant:</strong> For all edges \((u, v) \in E\), the true shortest path distances \(\delta(s, v)\) satisfy:</p>
\[ \delta(s, v) \le \delta(s, u) + w(u, v) \]
<p><strong>Complexity Derivation:</strong></p>
<ul>
  <li>Total <code>Insert</code> operations into Priority Queue: \(|V|\).</li>
  <li>Total <code>Extract-Min</code> operations: \(|V|\), each taking \(O(\log V)\). Total = \(O(V \log V)\).</li>
  <li>Total <code>Decrease-Key</code> / edge relaxations: \(|E|\), each taking \(O(\log V)\). Total = \(O(E \log V)\).</li>
  <li><strong>Total Time with Binary Heap:</strong> \(O((V + E) \log V)\).</li>
  <li><strong>Total Time with Fibonacci Heap:</strong> \(O(V \log V + E \cdot 1) = O(E + V \log V)\).</li>
</ul>
""",
        "worked_example": """
<p><strong>Worked Example:</strong> Find shortest paths from source \(S\) on graph with vertices \(\{S, A, B, C, D\}\):</p>
<ul>
  <li>Edges: \((S, A): 10, (S, C): 5, (A, B): 1, (C, A): 3, (C, B): 9, (C, D): 2, (D, B): 4, (B, D): 6\).</li>
</ul>
<ol style="margin-left:20px; line-height:1.8;">
  <li><strong>Initial State:</strong> \(d[S]=0\), all others \(\infty\). Priority Queue: \([(0, S)]\).</li>
  <li><strong>Extract \(S\) (\(d=0\)):</strong>
      <br>Relax \((S, A): 0 + 10 = 10 < \infty \implies d[A] = 10\).
      <br>Relax \((S, C): 0 + 5 = 5 < \infty \implies d[C] = 5\).
      <br>Queue: \([(5, C), (10, A)]\). Finalized: \(\{S\}\).
  </li>
  <li><strong>Extract \(C\) (\(d=5\)):</strong>
      <br>Relax \((C, A): 5 + 3 = 8 < 10 \implies d[A] = 8\) (Shorter path to A via C!).
      <br>Relax \((C, B): 5 + 9 = 14 < \infty \implies d[B] = 14\).
      <br>Relax \((C, D): 5 + 2 = 7 < \infty \implies d[D] = 7\).
      <br>Queue: \([(7, D), (8, A), (14, B)]\). Finalized: \(\{S, C\}\).
  </li>
  <li><strong>Extract \(D\) (\(d=7\)):</strong>
      <br>Relax \((D, B): 7 + 4 = 11 < 14 \implies d[B] = 11\).
      <br>Queue: \([(8, A), (11, B)]\). Finalized: \(\{S, C, D\}\).
  </li>
  <li><strong>Extract \(A\) (\(d=8\)):</strong>
      <br>Relax \((A, B): 8 + 1 = 9 < 11 \implies d[B] = 9\).
      <br>Queue: \([(9, B)]\). Finalized: \(\{S, C, D, A\}\).
  </li>
  <li><strong>Extract \(B\) (\(d=9\)):</strong>
      <br>Finalized: \(\{S, C, D, A, B\}\).
  </li>
</ol>
<p><strong>Final Shortest Distances from S:</strong> \(S: 0, A: 8, B: 9, C: 5, D: 7\). Paths reconstructed via predecessors!</p>
""",
        "complexity_table": [
            ("Binary Heap Implementation", "O((V + E) log V)", "O(V) space", "Standard competitive programming implementation"),
            ("Fibonacci Heap Implementation", "O(E + V log V)", "O(V) space", "Theoretical optimal bound with O(1) amortized decrease-key"),
            ("Array / Matrix Implementation", "O(V^2)", "O(V) space", "Optimal on dense graphs where E approx V^2"),
            ("Bellman-Ford (Negative Weights)", "O(V * E)", "O(V) space", "Handles negative weights and detects negative cycles"),
            ("Floyd-Warshall (All-Pairs)", "O(V^3)", "O(V^2) space", "Dynamic programming for all-pairs shortest paths")
        ],
        "code": '''import heapq

def dijkstra_shortest_path(graph: dict, source: str) -> tuple[dict, dict]:
    """
    Dijkstra's SSSP Algorithm with Min-Heap priority queue.
    graph: dict mapping vertex -> list of (neighbor, weight).
    Time Complexity: O((V + E) log V), Space: O(V).
    """
    distances = {v: float('inf') for v in graph}
    predecessors = {v: None for v in graph}
    distances[source] = 0.0
    
    # Priority Queue stores tuples of (distance, vertex)
    pq = [(0.0, source)]
    visited = set()
    
    while pq:
        curr_dist, u = heapq.heappop(pq)
        
        if u in visited:
            continue
        visited.add(u)
        
        # Edge relaxation
        for v, weight in graph[u]:
            if curr_dist + weight < distances[v]:
                distances[v] = curr_dist + weight
                predecessors[v] = u
                heapq.heappush(pq, (distances[v], v))
                
    return distances, predecessors''',
        "practical_considerations": """
<p><strong>1. GPS & Google Maps Routing:</strong> Real-world map navigation systems use advanced variants of Dijkstra: the <strong>A* Search Algorithm</strong> (which augments Dijkstra with a Euclidean distance heuristic function \(h(v)\) to direct the search cone toward the destination) and <em>Contraction Hierarchies</em> for sub-millisecond continental queries.</p>
<p><strong>2. Network Routing Protocols (OSPF & IS-IS):</strong> The Open Shortest Path First (OSPF) protocol running in global internet routers executes Dijkstra's algorithm inside every router to build the shortest-path forwarding table for IP packet routing.</p>
<p><strong>3. Early Exit Optimization:</strong> When looking for the shortest path between a specific start and destination pair (point-to-point SSSP), the loop can terminate immediately the moment the destination vertex is extracted from the priority queue!</p>
""",
        "speech_bubbles": [
            ("Captain Marvel", "Photon beam trajectory locked! Dijkstra's edge relaxation is like redirecting cosmic energy: if a newly discovered path through vertex u is shorter, update tentative distance and accelerate!"),
            ("Captain Marvel", "NEVER use Dijkstra on graphs with negative weights! The greedy assumption breaks down. If negative anomalies appear in the timeline, call in Bellman-Ford!")
        ],
        "quiz": [
            {
                "q": "What strict precondition must be satisfied to use Dijkstra's Algorithm?",
                "options": [
                    "Graph must be acyclic (DAG)",
                    "All edge weights must be non-negative (w(e) >= 0)",
                    "Graph must be complete",
                    "Number of vertices must be even"
                ],
                "answer": 1,
                "explanation": "Dijkstra relies on non-negative edge weights to guarantee that finalized shortest distances can never be reduced by subsequent paths."
            },
            {
                "q": "What is the time complexity of Dijkstra's algorithm implemented with a Min-Heap on a graph with V vertices and E edges?",
                "options": [
                    "O(V^2)",
                    "O((V + E) log V)",
                    "O(V * E)",
                    "O(V^3)"
                ],
                "answer": 1,
                "explanation": "Extracting min takes O(V log V) and relaxing edges with priority queue updates takes O(E log V), totaling O((V + E) log V)."
            },
            {
                "q": "What is the fundamental relaxation condition in Dijkstra's algorithm?",
                "options": [
                    "d[u] = d[v] + w(u, v)",
                    "if d[u] + w(u, v) < d[v], then d[v] = d[u] + w(u, v)",
                    "d[v] = min(d[v], w(u, v))",
                    "if d[u] > d[v], then swap u and v"
                ],
                "answer": 1,
                "explanation": "Edge relaxation checks if reaching vertex v through vertex u yields a shorter total distance than previously recorded, updating d[v] if true."
            },
            {
                "q": "Which algorithm is used when a graph contains negative edge weights?",
                "options": [
                    "Kruskal's Algorithm",
                    "Bellman-Ford Algorithm",
                    "Prim's Algorithm",
                    "Binary Search"
                ],
                "answer": 1,
                "explanation": "The Bellman-Ford algorithm correctly computes single-source shortest paths on graphs with negative edge weights and detects negative weight cycles in O(V * E) time."
            }
        ],
        "summary": "Dijkstra's algorithm finds single-source shortest paths on graphs with non-negative weights in O((V + E) log V) time. It is the cornerstone of GPS routing and Internet packet navigation."
    },

    # 18. TRAVELING SALESMAN PROBLEM (Loki)
    {
        "filename": "topic-traveling-salesman-problem.html",
        "topic_id": "traveling-salesman-problem",
        "mission_num": "05",
        "mission_title": "THE MASTER MISSION",
        "mission_url": "mission-05.html",
        "topic_num": "TOPIC 01",
        "topic_title": "TRAVELING SALESPERSON PROBLEM (TSP)",
        "hero_name": "LOKI",
        "hero_color": "#16a34a",
        "hero_tag": "ASGARDIAN ILLUSIONS & NP-HARD EXPLOSION",
        "hero_quote": "I am burdened with glorious purpose! To rule all realms, one must traverse every planetary capital exactly once and return home with minimal cosmic fuel.",
        "badge_color": "#dcfce7",
        "viz_type": "tsp",
        "problem_invariants": """
<p>The <strong>Traveling Salesperson Problem (TSP)</strong> is one of the most famous, heavily studied problems in computer science and combinatorial optimization. It belongs to the notorious class of <strong>NP-Hard</strong> problems.</p>
<p><strong>Formal Problem Statement:</strong></p>
<ul>
  <li>Given a complete weighted graph \(G = (V, E)\) with \(n = |V|\) cities and distance matrix \(C_{ij}\).</li>
  <li>A salesperson must visit <strong>every city exactly once</strong> and return to the starting departure city.</li>
  <li>Such a closed tour visiting every vertex once is termed a <strong>Hamiltonian Cycle</strong>.</li>
  <li><strong>Objective:</strong> Find a Hamiltonian cycle with the <strong>minimum total tour distance</strong>:
      \[ \min \sum_{k=1}^{n-1} C_{\pi(k), \pi(k+1)} + C_{\pi(n), \pi(1)} \]
  </li>
</ul>
<p><strong>The Combinatorial Explosion:</strong></p>
<p>For a directed graph of \(n\) cities, there are \((n - 1)!\) possible tours. For an undirected symmetric graph (\(C_{ij} = C_{ji}\)), there are \(\frac{(n - 1)!}{2}\) distinct tours. For just \(n = 20\) cities, the search space contains \(\approx 6.08 \times 10^{16}\) tours!</p>
""",
        "naive_vs_optimal": """
<p>A naive brute force permutation search tests all \((n-1)!\) tours. For \(n = 25\), brute force would take billions of years even on the world's fastest supercomputers. Loki's <strong>Held-Karp Dynamic Programming Algorithm</strong> uses state-space memoization over subsets of visited vertices, reducing runtime from \(\Theta(n!)\) down to \(\Theta(n^2 2^n)\), making problems up to \(n = 30\) solvable.</p>
<div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px; margin-top:12px;">
  <div style="background:#fee2e2; border:2px solid #ef4444; padding:12px; font-size:0.85rem;">
    <strong style="color:#b91c1c;">BRUTE FORCE PERMUTATIONS</strong><br>
    Complexity: \(\Theta(n!)\)<br>
    \(n = 20 \implies 1.2 \times 10^{17}\) tours.<br>
    Factorial explosion; utterly intractable.
  </div>
  <div style="background:#dcfce7; border:2px solid #16a34a; padding:12px; font-size:0.85rem;">
    <strong style="color:#15803d;">HELD-KARP DYNAMIC PROGRAMMING</strong><br>
    Complexity: \(\Theta(n^2 2^n)\)<br>
    \(n = 20 \implies 20^2 \times 2^{20} \approx 4.19 \times 10^8\) ops.<br>
    Executes in under 1 second on a standard CPU!
  </div>
</div>
""",
        "math_formulation": r"""
<p><strong>Held-Karp Dynamic Programming Recurrence:</strong></p>
<p>Let \(g(i, S)\) be the minimum cost of a path starting at vertex \(1\), visiting every vertex in subset \(S \subseteq \{2, 3, \dots, n\}\) exactly once, and ending at vertex \(i \in S\):</p>
\[ g(i, S) = \min_{j \in S \setminus \{i\}} \left\{ g(j, S \setminus \{i\}) + C_{ji} \right\} \]
<p><strong>Base Case:</strong> For subsets of size 1 containing only vertex \(i\):</p>
\[ g(i, \{i\}) = C_{1, i} \]
<p><strong>Optimal Tour Final Answer:</strong></p>
\[ \text{Opt Cost} = \min_{j \in \{2, \dots, n\}} \left\{ g(j, \{2, \dots, n\}) + C_{j, 1} \right\} \]
<p><strong>Complexity Derivation:</strong></p>
<ul>
  <li>Number of subsets \(S \subseteq V\): \(2^n\).</li>
  <li>Number of ending vertices \(i\): \(n\). Total states = \(n \cdot 2^n\).</li>
  <li>Transitions per state: \(n\) choices for predecessor \(j\).</li>
  <li><strong>Total Time:</strong> \(\Theta(n^2 2^n)\). <strong>Space:</strong> \(\Theta(n 2^n)\).</li>
</ul>
""",
        "worked_example": """
<p><strong>Worked Example (4 Cities):</strong> Cost matrix \(C\) between cities \(\{1, 2, 3, 4\}\):</p>
\[ C = \begin{pmatrix} 0 & 10 & 15 & 20 \\ 10 & 0 & 35 & 25 \\ 15 & 35 & 0 & 30 \\ 20 & 25 & 30 & 0 \end{pmatrix} \]
<ol style="margin-left:20px; line-height:1.8;">
  <li><strong>Stage 1 (Subsets of size 1):</strong>
      <br>\(g(2, \{2\}) = C_{12} = \mathbf{10}\)
      <br>\(g(3, \{3\}) = C_{13} = \mathbf{15}\)
      <br>\(g(4, \{4\}) = C_{14} = \mathbf{20}\)
  </li>
  <li><strong>Stage 2 (Subsets of size 2):</strong>
      <br>\(g(2, \{2, 3\}) = g(3, \{3\}) + C_{32} = 15 + 35 = 50\)
      <br>\(g(3, \{2, 3\}) = g(2, \{2\}) + C_{23} = 10 + 35 = 45\)
      <br>\(g(2, \{2, 4\}) = g(4, \{4\}) + C_{42} = 20 + 25 = 45\)
      <br>\(g(4, \{2, 4\}) = g(2, \{2\}) + C_{24} = 10 + 25 = 35\)
      <br>\(g(3, \{3, 4\}) = g(4, \{4\}) + C_{43} = 20 + 30 = 50\)
      <br>\(g(4, \{3, 4\}) = g(3, \{3\}) + C_{34} = 15 + 30 = 45\)
  </li>
  <li><strong>Stage 3 (Subsets of size 3 = {2, 3, 4}):</strong>
      <br>\(g(2, \{2,3,4\}) = \min(g(3,\{3,4\}) + C_{32}, g(4,\{3,4\}) + C_{42}) = \min(50+35, 45+25) = \mathbf{70}\)
      <br>\(g(3, \{2,3,4\}) = \min(g(2,\{2,4\}) + C_{23}, g(4,\{2,4\}) + C_{43}) = \min(45+35, 35+30) = \mathbf{65}\)
      <br>\(g(4, \{2,3,4\}) = \min(g(2,\{2,3\}) + C_{24}, g(3,\{2,3\}) + C_{34}) = \min(50+25, 45+30) = \mathbf{75}\)
  </li>
  <li><strong>Final Return to City 1:</strong>
      <br>\(\text{Cost} = \min(g(2) + C_{21}, g(3) + C_{31}, g(4) + C_{41})\)
      <br>\(= \min(70 + 10, 65 + 15, 75 + 20) = \min(80, 80, 95) = \mathbf{80}\).
  </li>
</ol>
<p><strong>Optimal Tour:</strong> \(1 \to 2 \to 4 \to 3 \to 1\) (Distance = \(10 + 25 + 30 + 15 = \mathbf{80}\)).</p>
""",
        "complexity_table": [
            ("Brute-Force Permutations", "Theta(n!)", "O(n) space", "Factorially explosive; impractical for n > 12"),
            ("Held-Karp Dynamic Programming", "Theta(n^2 2^n)", "Theta(n 2^n) space", "Bitmask memoization; practical up to n = 25-30"),
            ("Branch & Bound", "O(n!) worst, faster avg", "O(n) space", "Prunes search space using matrix reduction lower bounds"),
            ("2-Approximation (Metric TSP)", "O(E log V)", "O(V) space", "Uses MST doubling + triangle inequality shortcutting"),
            ("Christofides 1.5-Approximation", "O(V^3)", "O(V) space", "MST + Minimum Weight Perfect Matching on odd vertices")
        ],
        "code": '''def held_karp_tsp(dist_matrix: list[list[int]]) -> int:
    """
    Held-Karp Dynamic Programming algorithm for TSP using bitmasking.
    Time Complexity: O(n^2 * 2^n), Space Complexity: O(n * 2^n).
    """
    n = len(dist_matrix)
    # memo[mask][u] = min cost to visit vertices in mask ending at u
    memo = {}
    
    def get_min_cost(mask: int, u: int) -> int:
        # Base case: all cities visited, return cost to return to start (0)
        if mask == (1 << n) - 1:
            return dist_matrix[u][0]
            
        state = (mask, u)
        if state in memo:
            return memo[state]
            
        min_cost = float('inf')
        for v in range(n):
            # If city v has not been visited yet
            if not (mask & (1 << v)):
                cost = dist_matrix[u][v] + get_min_cost(mask | (1 << v), v)
                min_cost = min(min_cost, cost)
                
        memo[state] = min_cost
        return min_cost
        
    return get_min_cost(1, 0)  # Start at city 0 with mask 1 (city 0 visited)''',
        "practical_considerations": """
<p><strong>1. NP-Hardness & P vs NP:</strong> TSP is NP-Hard. Unless \(\text{P} = \text{NP}\), no polynomial-time algorithm exists to solve general TSP to exact optimality. In industry logistics (Amazon, FedEx routing), heuristic and approximation algorithms are mandatory.</p>
<p><strong>2. Metric TSP & Triangle Inequality:</strong> If the distance matrix satisfies the Triangle Inequality (\(C_{ac} \le C_{ab} + C_{bc}\)), we can construct polynomial-time approximation algorithms: the MST-based 2-approximation and Christofides' 1.5-approximation algorithm.</p>
<p><strong>3. Concorde TSP Solver:</strong> The state-of-the-art exact solver (Concorde) uses linear programming relaxations, cutting planes, and Branch-and-Cut to solve exact instances with up to 85,900 cities!</p>
""",
        "speech_bubbles": [
            ("Loki", "I am burdened with glorious purpose! You mortals thought n! was an inescapable curse. With Held-Karp bitmask memoization, we tame the combinatorial explosion down to n^2 * 2^n!"),
            ("Loki", "Remember the metric shortcut: when triangle inequality holds, doubling the Minimum Spanning Tree guarantees a tour no worse than 2x optimal! Chaos magic made practical.")
        ],
        "quiz": [
            {
                "q": "What is the time complexity of the Held-Karp Dynamic Programming algorithm for solving TSP?",
                "options": [
                    "O(n!)",
                    "O(n^2 2^n)",
                    "O(2^n)",
                    "O(n^3)"
                ],
                "answer": 1,
                "explanation": "Held-Karp considers 2^n subsets and n ending vertices, evaluating transitions in O(n) per state, yielding Theta(n^2 2^n) time."
            },
            {
                "q": "What is the computational complexity classification of the Traveling Salesperson Problem?",
                "options": [
                    "P (Polynomial time)",
                    "NP-Hard",
                    "Logarithmic",
                    "Undecidable"
                ],
                "answer": 1,
                "explanation": "TSP is an NP-Hard problem; its decision variant ('Does a tour of cost <= K exist?') is NP-Complete."
            },
            {
                "q": "How many distinct tours exist for a symmetric undirected TSP with n = 5 cities?",
                "options": [
                    "120",
                    "24",
                    "12",
                    "6"
                ],
                "answer": 2,
                "explanation": "For an undirected symmetric TSP, total tours = (n - 1)! / 2. For n = 5: (5 - 1)! / 2 = 24 / 2 = 12 distinct tours."
            },
            {
                "q": "What approximation ratio is guaranteed by the MST-based metric TSP algorithm using the Triangle Inequality?",
                "options": [
                    "1.5-approximation",
                    "2-approximation",
                    "3-approximation",
                    "log(n)-approximation"
                ],
                "answer": 1,
                "explanation": "Doubling MST edges creates an Eulerian tour of cost 2 * w(MST) <= 2 * OPT. Taking shortcut skips via triangle inequality preserves cost <= 2 * OPT."
            }
        ],
        "summary": "TSP seeks the minimum-cost Hamiltonian cycle across n cities. It is NP-Hard; Held-Karp Dynamic Programming reduces runtime from O(n!) to O(n^2 2^n) via subset bitmasking."
    },

    # 19. 0/1 KNAPSACK PROBLEM (Black Widow)
    {
        "filename": "topic-0-1-knapsack-problem.html",
        "topic_id": "0-1-knapsack-problem",
        "mission_num": "05",
        "mission_title": "THE MASTER MISSION",
        "mission_url": "mission-05.html",
        "topic_num": "TOPIC 02",
        "topic_title": "0/1 KNAPSACK PROBLEM (DYNAMIC PROGRAMMING)",
        "hero_name": "BLACK WIDOW",
        "hero_color": "#0f172a",
        "hero_tag": "RED ROOM TACTICAL DP MEMOIZATION",
        "hero_quote": "In covert espionage, decisions are binary: take the objective or leave it behind. Dynamic programming charts the optimal path through enemy vaults.",
        "badge_color": "#fee2e2",
        "viz_type": "knapsack_01",
        "problem_invariants": """
<p>The <strong>0/1 Knapsack Problem</strong> is the foundational problem establishing the power of <strong>Dynamic Programming (DP)</strong> in computer science. Unlike Fractional Knapsack, items <strong>cannot be broken</strong> into fractional pieces. Each item must either be taken in its entirety (\(x_i = 1\)) or left behind entirely (\(x_i = 0\)).</p>
<p><strong>Formal Problem Statement:</strong></p>
<ul>
  <li>Given \(n\) items, each with integer value \(v_i > 0\) and integer weight \(w_i > 0\).</li>
  <li>A knapsack with maximum integer weight capacity \(W\).</li>
  <li>Binary decision variable: \(x_i \in \{0, 1\}\) for each \(i \in \{1, \dots, n\}\).</li>
  <li><strong>Objective:</strong> Maximize total profit \(\sum_{i=1}^{n} x_i \cdot v_i\) subject to total weight \(\sum_{i=1}^{n} x_i \cdot w_i \le W\).</li>
</ul>
<p><strong>Two Core Principles of Dynamic Programming:</strong></p>
<ol>
  <li><strong>Optimal Substructure:</strong> An optimal solution to the knapsack of capacity \(W\) using items \(1 \dots i\) incorporates optimal solutions to subproblems of capacity \(W\) or \(W - w_i\) using items \(1 \dots i-1\).</li>
  <li><strong>Overlapping Subproblems:</strong> A naive recursive search recomputes the identical \((i, w)\) subproblem thousands of times. DP stores solutions in a 2D table \(DP[i][w]\), computing each state exactly once.</li>
</ol>
""",
        "naive_vs_optimal": """
<p>A naive brute-force recursion explores all \(2^n\) binary subsets. For \(n = 40\) items, \(2^{40} \approx 1.1 \times 10^{12}\) states must be evaluated, taking hours. Black Widow's 2D Dynamic Programming table memoizes subproblem states in a table of size \(n \times W\), computing the exact optimal loot selection in \(\Theta(n \cdot W)\) pseudo-polynomial time!</p>
<div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px; margin-top:12px;">
  <div style="background:#fee2e2; border:2px solid #ef4444; padding:12px; font-size:0.85rem;">
    <strong style="color:#b91c1c;">BRUTE FORCE RECURSION</strong><br>
    Examines power set: \(2^n\).<br>
    \(n = 40 \implies 1,099,511,627,776\) calls.<br>
    Exponential explosion; freezes runtime.
  </div>
  <div style="background:#dcfce7; border:2px solid #16a34a; padding:12px; font-size:0.85rem;">
    <strong style="color:#15803d;">DYNAMIC PROGRAMMING [O(n W)]</strong><br>
    2D Memoization Table of size \(n \times W\).<br>
    \(n = 40, W = 100 \implies 4,000\) table cells.<br>
    Computes in less than 1 millisecond!
  </div>
</div>
""",
        "math_formulation": r"""
<p><strong>The Definitive Bellman Recurrence:</strong></p>
<p>Let \(DP[i][w]\) represent the maximum value attainable using a subset of the first \(i\) items with knapsack capacity limit \(w\) (\(0 \le i \le n, 0 \le w \le W\)):</p>
\[ DP[i][w] = \begin{cases} 
0 & \text{if } i = 0 \text{ or } w = 0 \\
DP[i-1][w] & \text{if } w_i > w \quad (\text{Item too heavy to fit}) \\
\max \Big( DP[i-1][w], \; DP[i-1][w - w_i] + v_i \Big) & \text{if } w_i \le w \quad (\text{Exclude vs Include})
\end{cases} \]
<p><strong>Complexity:</strong></p>
<ul>
  <li>Time Complexity: \(\Theta(n \cdot W)\).</li>
  <li>Space Complexity: \(\Theta(n \cdot W)\) with 2D table, reducible to \(\Theta(W)\) using a 1D array traversed backwards.</li>
  <li><em>Note:</em> \(\Theta(n \cdot W)\) is <strong>Pseudo-polynomial</strong> because it depends on the magnitude of the numeric integer \(W\), not the number of input bits \(\log_2 W\).</li>
</ul>
""",
        "worked_example": """
<p><strong>Worked Example:</strong> Capacity \(W = 7\). Three items available:</p>
<ul>
  <li>Item 1: \(w_1 = 1, v_1 = 1\)</li>
  <li>Item 2: \(w_2 = 3, v_2 = 4\)</li>
  <li>Item 3: \(w_3 = 4, v_3 = 5\)</li>
  <li>Item 4: \(w_4 = 5, v_4 = 7\)</li>
</ul>
<p><strong>Constructing the DP Table \(DP[i][w]\):</strong></p>
<table style="width:100%; border-collapse:collapse; margin-top:8px; font-size:0.85rem; text-align:center;">
  <tr style="background:#f1f5f9;"><th style="padding:6px; border:1px solid #cbd5e1;">i \ w</th><th>0</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th></tr>
  <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:bold;">i=0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
  <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:bold;">i=1 (w=1,v=1)</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr>
  <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:bold;">i=2 (w=3,v=4)</td><td>0</td><td>1</td><td>1</td><td>4</td><td>5</td><td>5</td><td>5</td><td>5</td></tr>
  <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:bold;">i=3 (w=4,v=5)</td><td>0</td><td>1</td><td>1</td><td>4</td><td>5</td><td>6</td><td>6</td><td>9</td></tr>
  <tr style="background:#dcfce7;"><td style="padding:6px; border:1px solid #cbd5e1; font-weight:bold;">i=4 (w=5,v=7)</td><td>0</td><td>1</td><td>1</td><td>4</td><td>5</td><td>7</td><td>8</td><td><strong>9</strong></td></tr>
</table>
<ol style="margin-left:20px; line-height:1.8; margin-top:8px;">
  <li><strong>Optimal Max Profit:</strong> Value in \(DP[4][7] = \mathbf{9}\).</li>
  <li><strong>Backtracking Solution to find Items Selected:</strong>
      <br>Is \(DP[4][7] \ne DP[3][7]\)? \(9 == 9 \implies\) Item 4 was <strong>NOT taken</strong>.
      <br>Is \(DP[3][7] \ne DP[2][7]\)? \(9 \ne 5 \implies\) <strong>Item 3 WAS TAKEN!</strong>
      <br>Subtract weight of Item 3: remaining \(w = 7 - 4 = 3\). Move to \(DP[2][3]\).
      <br>Is \(DP[2][3] \ne DP[1][3]\)? \(4 \ne 1 \implies\) <strong>Item 2 WAS TAKEN!</strong>
      <br>Subtract weight of Item 2: remaining \(w = 3 - 3 = 0\). (Capacity depleted).
  </li>
  <li><strong>Items In Vault Stash:</strong> Item 2 ($4, 3kg) + Item 3 ($5, 4kg). Total weight = \(3 + 4 = 7\text{ kg}\), Total Profit = \(\$4 + \$5 = \mathbf{\$9}\)!</li>
</ol>
""",
        "complexity_table": [
            ("Brute-Force Recursion", "Theta(2^n)", "O(n) stack", "Tests all 2^n binary subsets; intractable for n > 30"),
            ("Standard 2D Dynamic Programming", "Theta(n * W)", "Theta(n * W) space", "Standard tabular bottom-up formulation"),
            ("Space-Optimized 1D DP Array", "Theta(n * W)", "Theta(W) space", "Single 1D array traversed backwards from W down to w_i"),
            ("Branch & Bound", "O(2^n) worst, faster avg", "O(n) space", "Prunes states using Fractional Knapsack upper bounds"),
            ("FPTAS Approximation Scheme", "O(n^3 / epsilon)", "O(n^2 / epsilon)", "Polynomial time guarantee within (1 - epsilon) factor")
        ],
        "code": '''def knapsack_01(capacity: int, weights: list[int], values: list[int]) -> tuple[int, list[int]]:
    """
    0/1 Knapsack Dynamic Programming with solution backtracking.
    Time Complexity: O(n * W), Space Complexity: O(n * W).
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Build DP table iteratively
    for i in range(1, n + 1):
        w_i = weights[i - 1]
        v_i = values[i - 1]
        for w in range(1, capacity + 1):
            if w_i <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - w_i] + v_i)
            else:
                dp[i][w] = dp[i - 1][w]
                
    # Backtrack to find exact items chosen
    selected_items = []
    w_curr = capacity
    for i in range(n, 0, -1):
        if dp[i][w_curr] != dp[i - 1][w_curr]:
            selected_items.append(i - 1)  # Item index chosen
            w_curr -= weights[i - 1]
            
    return dp[n][capacity], selected_items[::-1]''',
        "practical_considerations": """
<p><strong>1. Space Optimization to \(O(W)\):</strong> Notice that computing row \(i\) only requires values from row \(i-1\). We can compress the 2D table into a single 1D array <code>dp[w]</code>. <strong>Crucial rule:</strong> we must iterate \(w\) <em>backwards</em> from \(W\) down to \(w_i\). Iterating forwards would allow an item to be selected multiple times (which solves Unbounded Knapsack, not 0/1 Knapsack!).</p>
<p><strong>2. Pseudo-Polynomial Time & Strong NP-Completeness:</strong> 0/1 Knapsack is NP-Complete, yet solvable in \(O(n \cdot W)\). Why? Because \(W\) is an integer whose input size is \(\log_2 W\) bits. If \(W = 2^{64}\), \(O(n \cdot W)\) is exponential! This makes 0/1 Knapsack <em>weakly NP-Complete</em>.</p>
<p><strong>3. Cryptographic Merkle-Hellman Knapsack Cryptosystem:</strong> In early public-key cryptography, the difficulty of solving the subset sum / knapsack problem was used to create one-way trapdoor encryption functions.</p>
""",
        "speech_bubbles": [
            ("Black Widow", "Red Room espionage rule: Every mission decision is strictly binary: take the intel or leave it. When subproblems overlap, memoize every result in the DP table!"),
            ("Black Widow", "Pay attention to memory optimization! You can compress the entire 2D table into a single 1D array of size W by running the loop backwards from capacity down to weight_i. Efficiency is survival.")
        ],
        "quiz": [
            {
                "q": "What recurrence relation defines the 0/1 Knapsack DP state DP[i][w] when weight_i <= w?",
                "options": [
                    "DP[i][w] = DP[i-1][w] + values[i]",
                    "DP[i][w] = max(DP[i-1][w], DP[i-1][w - weights[i]] + values[i])",
                    "DP[i][w] = DP[i][w - weights[i]] + values[i]",
                    "DP[i][w] = max(DP[i][w-1], DP[i-1][w])"
                ],
                "answer": 1,
                "explanation": "At item i, we evaluate the max between excluding item i (DP[i-1][w]) and including item i (DP[i-1][w - weights[i]] + values[i])."
            },
            {
                "q": "Why is the O(n * W) time complexity of 0/1 Knapsack termed 'pseudo-polynomial'?",
                "options": [
                    "Because it only works on floating point numbers",
                    "Because W is an integer value whose bit-length representation is log2(W), making the complexity exponential in the length of the input",
                    "Because the algorithm sometimes produces approximations",
                    "Because it requires quantum hardware"
                ],
                "answer": 1,
                "explanation": "In computational complexity, input size is measured in bits. An integer W takes log2(W) bits. Since 2^(log2 W) = W, O(n * W) is exponential in the number of bits representing W."
            },
            {
                "q": "When optimizing 0/1 Knapsack to use a single 1D array dp[w], why must the capacity loop run backwards from W down to weight_i?",
                "options": [
                    "To sort the items descending",
                    "To prevent using the same item multiple times in the same row (which would solve Unbounded Knapsack)",
                    "To avoid negative indices",
                    "It executes faster in CPU cache"
                ],
                "answer": 1,
                "explanation": "Running backwards ensures that dp[w - weight_i] represents the state from the PREVIOUS item iteration, preventing multiple inclusions of the same item."
            },
            {
                "q": "What two fundamental problem characteristics justify the use of Dynamic Programming for 0/1 Knapsack?",
                "options": [
                    "Greedy Choice Property and Polynomial Roots",
                    "Optimal Substructure and Overlapping Subproblems",
                    "Divide-and-Conquer and Amortization",
                    "Graph Planarity and Vertex Coloring"
                ],
                "answer": 1,
                "explanation": "Dynamic Programming is applicable when a problem possesses both Optimal Substructure (optimal subproblem solutions compose optimal overall solution) and Overlapping Subproblems (subproblems recur repeatedly)."
            }
        ],
        "summary": "0/1 Knapsack requires Dynamic Programming due to binary indivisibility and overlapping subproblems. The Bellman recurrence solves it in O(n * W) pseudo-polynomial time with backtracking."
    }
]

print(f"Loaded Part 4: {len(PART4_TOPICS)} topics")
