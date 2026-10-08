/**
 * ALGO-VENGERS — MISSIONS & TOPICS DATA REPOSITORY
 * Strictly contains the 5 Missions and 20 DAA Syllabus Topics
 */

const MISSIONS_DATA = [
  {
    id: "mission-01",
    num: "01",
    title: "FOUNDATIONS",
    codename: "PROJECT ODIN",
    hero: "Thor & Iron Man",
    badge: "CORE THEORY",
    desc: "Establish the mathematical bedrock of algorithmic efficiency, analyzing theoretical bounds, resource consumption, and asymptotic behavior.",
    topics: [
      {
        name: "Space Complexity",
        paradigm: "Complexity Theory",
        complexity: "S(n) = c + Sp(n)",
        summary: "Analyzing the memory footprint required by an algorithm as input size scales, differentiating auxiliary space from total space."
      },
      {
        name: "Time Complexity",
        paradigm: "Complexity Theory",
        complexity: "T(n) steps",
        summary: "Quantifying the execution step count relative to input length across best, average, and worst-case input permutations."
      },
      {
        name: "Asymptotic Notations",
        paradigm: "Mathematical Analysis",
        complexity: "O, Ω, Θ",
        summary: "Formal mathematical bounding of growth rates: Big-O (upper bound), Big-Omega (lower bound), and Big-Theta (tight bound)."
      }
    ]
  },
  {
    id: "mission-02",
    num: "02",
    title: "DATA STRUCTURES",
    codename: "VIBRANIUM ARCHIVES",
    hero: "Captain America",
    badge: "ABSTRACT TYPES",
    desc: "Master the structural organization of algorithmic data, memory representation, and optimal retrieval access patterns.",
    topics: [
      {
        name: "Stacks",
        paradigm: "Linear ADT",
        complexity: "Push/Pop: O(1)",
        summary: "Last-In-First-Out (LIFO) disciplined data structure foundational to recursion stacks, expression parsing, and backtracking."
      },
      {
        name: "Queues",
        paradigm: "Linear ADT",
        complexity: "Enqueue/Dequeue: O(1)",
        summary: "First-In-First-Out (FIFO) buffer structure critical for breadth-first graph explorations and asynchronous event handling."
      },
      {
        name: "Trees",
        paradigm: "Hierarchical ADT",
        complexity: "Search: O(log n) avg",
        summary: "Non-linear hierarchical node topologies including Binary Search Trees, AVL balance properties, and traversal algorithms."
      },
      {
        name: "Dictionaries",
        paradigm: "Associative Map",
        complexity: "Lookup: O(1) avg",
        summary: "Key-value indexing with hash functions, collision resolution strategies (chaining, open addressing), and load factor tuning."
      },
      {
        name: "Sets and Disjoint Sets",
        paradigm: "Union-Find ADT",
        complexity: "Find/Union: O(α(n))",
        summary: "Disjoint-set forests utilizing path compression and union by rank to manage dynamic equivalence relations and cycle detection."
      }
    ]
  },
  {
    id: "mission-03",
    num: "03",
    title: "SEARCH & SORT",
    codename: "QUANTUM VELOCITY",
    hero: "Hawkeye & Black Widow",
    badge: "BENCHMARK ALGORITHMS",
    desc: "Deconstruct ordering and target discovery mechanics, comparing linear vs logarithmic searches and recursive partitioned sorts.",
    topics: [
      {
        name: "Maximum and Minimum",
        paradigm: "Divide & Conquer",
        complexity: "Comparisons: ⌈3n/2⌉ - 2",
        summary: "Tournament and divide-and-conquer strategies to discover both extrema simultaneously with minimal element comparisons."
      },
      {
        name: "Binary Search",
        paradigm: "Decrease & Conquer",
        complexity: "O(log n)",
        summary: "Interval halving search over monotonic ordered arrays, eliminating half of remaining search space per iteration."
      },
      {
        name: "Merge Sort",
        paradigm: "Divide & Conquer",
        complexity: "O(n log n) stable",
        summary: "Stable divide-and-conquer sorting by recursive halving and linear merging; satisfies T(n) = 2T(n/2) + O(n)."
      },
      {
        name: "Quick Sort",
        paradigm: "Divide & Conquer",
        complexity: "O(n log n) avg, O(n²) worst",
        summary: "In-place partitioning around a chosen pivot element; dominant cache efficiency despite quadratic worst-case vulnerabilities."
      }
    ]
  },
  {
    id: "mission-04",
    num: "04",
    title: "ADVANCED ALGORITHMS",
    codename: "INFINITY ARSENAL",
    hero: "Iron Man & Hulk",
    badge: "PARADIGM MASTERY",
    desc: "Deploy sophisticated paradigms including sub-cubic matrix algebra, greedy selection strategies, and shortest-path tree generation.",
    topics: [
      {
        name: "Strassen's Matrix Multiplication",
        paradigm: "Divide & Conquer",
        complexity: "O(n^2.807)",
        summary: "Sub-cubic matrix multiplication reducing 8 sub-matrix multiplications down to 7 clever linear combinations."
      },
      {
        name: "Fractional Knapsack",
        paradigm: "Greedy Method",
        complexity: "O(n log n)",
        summary: "Optimal item fraction packing according to decreasing value-to-weight density ratios, proving greedy choice property."
      },
      {
        name: "Minimum Cost Spanning Trees",
        paradigm: "Graph Optimization",
        complexity: "V-1 edges",
        summary: "Acyclic subgraph selection spanning all vertices with minimal total edge weight in connected undirected networks."
      },
      {
        name: "Kruskal's and Prim's Algorithms",
        paradigm: "Greedy Method",
        complexity: "O(E log V) / O(E + V log V)",
        summary: "Two classic greedy approaches: edge-centric sorting with Disjoint Sets (Kruskal) vs vertex-centric priority queues (Prim)."
      },
      {
        name: "Single Source Shortest Paths — Dijkstra's Algorithm",
        paradigm: "Greedy Method",
        complexity: "O((V + E) log V)",
        summary: "Iterative relaxation of non-negative edge weights using a min-priority queue to compute shortest paths from a single source."
      }
    ]
  },
  {
    id: "mission-05",
    num: "05",
    title: "OPTIMIZATION",
    codename: "ENDGAME STRATEGY",
    hero: "Spider-Man",
    badge: "NP-HARD & DP",
    desc: "Attack intractable combinatorial challenges using dynamic programming state tables and exact combinatorial optimization techniques.",
    topics: [
      {
        name: "Traveling Salesman Problem",
        paradigm: "Branch & Bound / DP",
        complexity: "O(n² 2ⁿ) DP / O(n!) brute",
        summary: "Discovering the minimum-cost Hamiltonian cycle visiting every vertex exactly once and returning to the departure origin."
      },
      {
        name: "0/1 Knapsack Problem",
        paradigm: "Dynamic Programming",
        complexity: "O(n · W) pseudo-poly",
        summary: "Selecting discrete non-divisible items to maximize total profit without exceeding weight limit W using optimal substructure recurrence."
      }
    ]
  }
];

if (typeof window !== 'undefined') {
  window.MISSIONS_DATA = MISSIONS_DATA;
}
