# academic_data_part1.py - Topics 1 to 5
# Mission 01: Foundations (Topics 1-3) & Mission 02: Data Structures (Topics 4-5)

PART1_TOPICS = [
    # 1. SPACE COMPLEXITY (Ant-Man)
    {
        "filename": "topic-space-complexity.html",
        "topic_id": "space-complexity",
        "mission_num": "01",
        "mission_title": "FOUNDATIONS",
        "mission_url": "mission-01.html",
        "topic_num": "TOPIC 01",
        "topic_title": "SPACE COMPLEXITY",
        "hero_name": "ANT-MAN",
        "hero_color": "#ef4444",
        "hero_tag": "QUANTUM STORAGE EFFICIENCY",
        "hero_quote": "Just like shrinking into the Quantum Realm, space complexity analyzes how much physical and virtual memory an algorithm requires as input grows.",
        "badge_color": "#fee2e2",
        "viz_type": "memory",
        "problem_invariants": """
<p>Space Complexity measures the total amount of memory space an algorithm requires during its lifecycle as a function of the input length \(n\). Unlike execution speed, memory consumption is constrained by finite hardware bounds (L1/L2/L3 CPU caches, RAM limits, and OS thread stack allocations).</p>
<p>Formally, the total space \(S(P)\) required by program \(P\) is decomposed into two foundational components:</p>
<ul>
  <li><strong>Fixed Space Requirement (\(c\)):</strong> Memory independent of the characteristics of the inputs and outputs (e.g., instruction space, simple variables, fixed constants, and struct descriptors).</li>
  <li><strong>Variable Space Requirement (\(S_A(n)\)):</strong> Dynamic space dependent on instance characteristics, including dynamic array allocations, reference pointers, and recursion call stack frames.</li>
</ul>
<p><strong>Crucial Distinction:</strong> In technical interviews and DAA university examinations, always distinguish between <em>Total Space Complexity</em> (input buffer + working workspace) and <em>Auxiliary Space Complexity</em> (extra temporary workspace allocated beyond the input itself).</p>
""",
        "naive_vs_optimal": """
<p>Consider the problem of reversing an array of size \(n\). A naive implementation allocates a secondary mirror array, copying elements backwards. While simple, it requires \(\Theta(n)\) auxiliary memory. An optimal algorithm uses two convergent pointers to perform in-place swaps, shrinking auxiliary memory down to \(O(1)\) constant space.</p>
<div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px; margin-top:12px;">
  <div style="background:#fee2e2; border:2px solid #ef4444; padding:12px; font-size:0.85rem;">
    <strong style="color:#b91c1c;">NAIVE APPROACH</strong><br>
    Allocates new array \(B[n]\).<br>
    Auxiliary Space: \(O(n)\)<br>
    Memory Waste: Doubles RAM footprint; risks out-of-memory faults on embedded microcontrollers.
  </div>
  <div style="background:#dcfce7; border:2px solid #16a34a; padding:12px; font-size:0.85rem;">
    <strong style="color:#15803d;">OPTIMAL IN-PLACE SWAP</strong><br>
    Pointers \(i=0, j=n-1\) swap elements.<br>
    Auxiliary Space: \(O(1)\)<br>
    Memory Efficiency: Conserves L1 cache; 0 heap allocations.
  </div>
</div>
""",
        "math_formulation": r"""
\[ S(P) = c + S_A(n) \]
<p>For recursive algorithms, the variable space is dominated by the activation records pushed onto the execution call stack:</p>
\[ S_{\text{stack}}(n) = \text{Maximum Recursion Depth} \times \text{Size of Single Activation Frame} \]
<p>For Divide-and-Conquer binary subdivision (e.g., standard Binary Search):</p>
\[ S(n) = S(n/2) + O(1) \implies S(n) = O(\log_2 n) \]
<p>For naive linear recursion (e.g., recursive factorial or unoptimized Fibonacci):</p>
\[ S(n) = S(n-1) + O(1) \implies S(n) = O(n) \]
""",
        "worked_example": """
<p><strong>Scenario:</strong> Calculating memory footprints for an integer array processing routine handling \(N = 10,000\) elements on a 64-bit architecture (each integer = 4 bytes, pointer = 8 bytes).</p>
<ol style="margin-left:20px; line-height:1.8;">
  <li><strong>Fixed Space:</strong> Base variables (loop index <code>i</code>, accumulator <code>total</code>, return pointer) = \(3 \times 8 = 24\) bytes.</li>
  <li><strong>Input Array Space:</strong> \(10,000 \times 4 = 40,000\) bytes \(\approx 39.06 \text{ KB}\).</li>
  <li><strong>Algorithm A (Recursive with \(N\) frames):</strong> Call stack depth = 10,000. Each frame stores return address (8B), frame pointer (8B), and local parameters (16B) = 32 bytes.
      <br>\(S_{\text{aux}} = 10,000 \times 32 = 320,000 \text{ bytes} \approx 312.5 \text{ KB}\).</li>
  <li><strong>Algorithm B (Iterative Two-Pointer):</strong> Only 2 local indices stored in CPU registers.
      <br>\(S_{\text{aux}} = 2 \times 4 = 8 \text{ bytes} = O(1)\).</li>
</ol>
<p><em>Conclusion:</em> Algorithm B reduces auxiliary memory consumption by a factor of 40,000x!</p>
""",
        "complexity_table": [
            ("In-Place Two-Pointer Reverse", "O(1)", "O(1) Auxiliary", "Strictly loop registers and temporary swap variable"),
            ("Binary Search (Iterative)", "O(1)", "O(1) Auxiliary", "Three index pointers (low, mid, high) only"),
            ("Binary Search (Recursive)", "O(log n)", "O(log n) Auxiliary", "Call stack depth bounded by tree height log2(n)"),
            ("Merge Sort", "O(n)", "O(n) Auxiliary", "Temporary merge buffers proportional to array slice size"),
            ("Dynamic Programming (2D Table)", "O(n^2)", "O(n^2) Auxiliary", "Full memoization table of size n * n")
        ],
        "code": '''def reverse_array_inplace(arr: list[int]) -> None:
    """
    Reverses an array in-place with O(1) auxiliary space.
    Space Complexity: O(1) Auxiliary, O(n) Total
    Time Complexity: O(n)
    """
    left = 0
    right = len(arr) - 1
    
    # In-place convergent two-pointer swap
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

def recursive_sum(arr: list[int], index: int = 0) -> int:
    """
    Recursive summation demonstrating O(n) call-stack space.
    Space Complexity: O(n) Auxiliary (Stack Depth = len(arr))
    """
    if index >= len(arr):
        return 0
    # Each call pushes a new activation frame onto the call stack
    return arr[index] + recursive_sum(arr, index + 1)''',
        "practical_considerations": """
<p><strong>1. Thread Stack Limits & Stack Overflow:</strong> In OS environments like Linux and Windows, the default thread stack is typically 8 MB or 1 MB. An unoptimized recursion with \(N = 10^6\) frames will violently crash with <code>SIGSEGV (Stack Overflow)</code>, while heap memory could comfortably hold gigabytes.</p>
<p><strong>2. CPU Cache Locality:</strong> In-place algorithms with \(O(1)\) auxiliary memory preserve CPU cache lines (L1/L2 caches). Allocating secondary heap buffers introduces cache misses, pointer indirection overhead, and triggers garbage collector pauses.</p>
<p><strong>3. Space-Time Trade-offs:</strong> Often algorithms trade auxiliary space to reduce time complexity (e.g., Hash Tables achieve \(O(1)\) lookup by utilizing \(O(n)\) memory, whereas linear scan takes \(O(1)\) space but \(O(n)\) time).</p>
""",
        "speech_bubbles": [
            ("Scott Lang", "Pym particles teach us that shrinking your memory footprint is what separates a rookie coder from an Avenger. Keep auxiliary variables down to O(1) in-place swaps to save the quantum realm!"),
            ("Scott Lang", "Beware recursive depth traps! A 1MB thread stack will shatter into a stack overflow if your base case is missing. Tail-call optimization or iterative loops are your best shields.")
        ],
        "quiz": [
            {
                "q": "What is the primary difference between Total Space Complexity and Auxiliary Space Complexity?",
                "options": [
                    "Auxiliary space includes the input buffer, whereas total space does not",
                    "Auxiliary space is only the extra or temporary workspace used beyond the input size",
                    "Total space only counts heap allocations, ignoring call stacks",
                    "They are identical terms with no distinction in DAA"
                ],
                "answer": 1,
                "explanation": "Auxiliary space measures only the extra temporary memory allocated by the algorithm to solve the problem, excluding the input data itself."
            },
            {
                "q": "What is the auxiliary space complexity of standard recursive Merge Sort on an array of size n?",
                "options": [
                    "O(1)",
                    "O(log n)",
                    "O(n)",
                    "O(n^2)"
                ],
                "answer": 2,
                "explanation": "Merge Sort requires O(n) auxiliary space to store elements during the merge phase across temporary buffers."
            },
            {
                "q": "If a recursive function halves the input size at each level and performs O(1) work, what is its call stack space complexity?",
                "options": [
                    "O(1)",
                    "O(log n)",
                    "O(n)",
                    "O(n log n)"
                ],
                "answer": 1,
                "explanation": "Halving the input at each step yields a recursion tree of height log2(n), requiring O(log n) activation frames on the stack."
            },
            {
                "q": "Which data structure technique achieves O(1) space reversal of an array?",
                "options": [
                    "Allocating a secondary copy queue",
                    "Two-pointer convergent in-place element swapping",
                    "Using recursive post-order traversal",
                    "Creating a Hash Map index"
                ],
                "answer": 1,
                "explanation": "Convergent two-pointer swap operates strictly in-place, allocating only two index variables in registers (O(1) auxiliary space)."
            }
        ],
        "summary": "Always distinguish between total memory (input + working) and auxiliary memory (extra workspace). In competitive programming and memory-constrained microcontrollers, reducing auxiliary space from O(n) to O(1) prevents stack overflows and out-of-memory faults."
    },

    # 2. TIME COMPLEXITY (Doctor Strange)
    {
        "filename": "topic-time-complexity.html",
        "topic_id": "time-complexity",
        "mission_num": "01",
        "mission_title": "FOUNDATIONS",
        "mission_url": "mission-01.html",
        "topic_num": "TOPIC 02",
        "topic_title": "TIME COMPLEXITY",
        "hero_name": "DOCTOR STRANGE",
        "hero_color": "#f59e0b",
        "hero_tag": "TEMPORAL PATH EXPANSION",
        "hero_quote": "I viewed 14,000,605 algorithmic timelines. In every reality, asymptotic step count dictates victory.",
        "badge_color": "#fef3c7",
        "viz_type": "time_growth",
        "problem_invariants": """
<p>Time Complexity quantifies the number of elementary operational steps executed by an algorithm as a function of the input size \(n\). Rather than measuring clock milliseconds (which vary widely based on hardware architecture, CPU clock speed, compiler optimizations, and background operating system processes), Design and Analysis of Algorithms counts primitive operations (comparisons, arithmetic operations, assignments, and pointer dereferences).</p>
<p>DAA classifies execution complexity across three canonical scenarios:</p>
<ul>
  <li><strong>Worst-Case Time (\(T_{\text{worst}}(n)\)):</strong> The maximum number of steps executed over any input of length \(n\). Provides a mathematical guarantee that the algorithm will never exceed this bound.</li>
  <li><strong>Best-Case Time (\(T_{\text{best}}(n)\)):</strong> The minimum number of steps executed on the most favorable input configuration.</li>
  <li><strong>Average-Case Time (\(T_{\text{avg}}(n)\)):</strong> The expected step count averaged over all valid inputs according to a defined probability distribution (commonly uniform).</li>
</ul>
""",
        "naive_vs_optimal": """
<p>Consider locating a target element inside a sorted sequence of \(n = 1,000,000\) elements. A naive Linear Scan inspects each index one by one, requiring up to \(1,000,000\) steps in the worst case. Doctor Strange's Binary Search halves the temporal dimension on every comparison, finding any element in at most \(\lceil \log_2(1,000,000) \rceil = 20\) steps.</p>
<div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px; margin-top:12px;">
  <div style="background:#fef3c7; border:2px solid #f59e0b; padding:12px; font-size:0.85rem;">
    <strong style="color:#b45309;">LINEAR SEARCH [O(n)]</strong><br>
    \(n = 10^6 \implies 1,000,000 \text{ steps}\)<br>
    Unbearable latency on big data pipelines; redundant scans through sorted sequences.
  </div>
  <div style="background:#dcfce7; border:2px solid #16a34a; padding:12px; font-size:0.85rem;">
    <strong style="color:#15803d;">BINARY SEARCH [O(log n)]</strong><br>
    \(n = 10^6 \implies 20 \text{ steps}\)<br>
    Exponential speedup; instantaneous lookup even across billions of records.
  </div>
</div>
""",
        "math_formulation": r"""
\[ T(n) = \sum_{i=1}^{k} c_i \cdot \text{step}_i(n) \]
<p>For nested loop structures where inner loops execute \(j\) times:</p>
\[ T(n) = \sum_{i=1}^{n} \sum_{j=1}^{i} c = c \cdot \sum_{i=1}^{n} i = c \cdot \frac{n(n+1)}{2} = \frac{c}{2}n^2 + \frac{c}{2}n \implies \Theta(n^2) \]
<p>Asymptotic Dominance Hierarchy (from fastest to slowest):</p>
\[ O(1) < O(\log \log n) < O(\log n) < O(\sqrt{n}) < O(n) < O(n \log n) < O(n^2) < O(n^3) < O(2^n) < O(n!) \]
""",
        "worked_example": """
<p><strong>Scenario:</strong> Calculating exact operations for a 2-level nested loop matrix comparison routine with \(n = 500\).</p>
<ol style="margin-left:20px; line-height:1.8;">
  <li><strong>Outer Loop:</strong> Executes \(i\) from \(0\) to \(n-1\) (\(500\) iterations).</li>
  <li><strong>Inner Loop:</strong> For each \(i\), executes \(j\) from \(i+1\) to \(n-1\).</li>
  <li><strong>Total Step Sum:</strong>
      \[ \sum_{i=0}^{n-1} (n - 1 - i) = (n-1) + (n-2) + \dots + 1 + 0 = \frac{(n-1)n}{2} \]
  </li>
  <li><strong>Plugging in \(n = 500\):</strong>
      \[ \text{Operations} = \frac{499 \times 500}{2} = 124,750 \text{ comparisons}. \]
  </li>
  <li><strong>Asymptotic Term:</strong> Dropping lower-order components (\(-\frac{n}{2}\)) and coefficients yields \(\Theta(n^2)\).</li>
</ol>
""",
        "complexity_table": [
            ("Array Index Access / Push", "O(1)", "Omega(1)", "Single offset memory calculation"),
            ("Binary Search", "O(log n)", "Omega(1)", "Halves problem size at each step; best case target at mid"),
            ("Linear Scan", "O(n)", "Omega(1)", "Inspects up to n elements sequentially"),
            ("Merge Sort / Heap Sort", "O(n log n)", "Omega(n log n)", "Optimal comparison-based sorting lower bound"),
            ("Bubble Sort / Selection Sort", "O(n^2)", "Omega(n) / Omega(n^2)", "Pairwise element comparisons across nested loops"),
            ("Subset Sum (Brute Force)", "O(2^n)", "Omega(2^n)", "Examines power set of all 2^n combinations")
        ],
        "code": '''def find_pair_with_sum(arr: list[int], target: int) -> tuple[int, int] | None:
    """
    Demonstrating O(n) Two-Pointer Time vs O(n^2) Nested Loop Time.
    Assumes sorted input array.
    """
    # OPTIMAL O(n) TWO-POINTER APPROACH:
    low = 0
    high = len(arr) - 1
    
    while low < high:
        current_sum = arr[low] + arr[high]
        if current_sum == target:
            return arr[low], arr[high]  # O(1) best case
        elif current_sum < target:
            low += 1                    # Move lower boundary up
        else:
            high -= 1                   # Move upper boundary down
            
    return None  # Worst case O(n) steps''',
        "practical_considerations": """
<p><strong>1. Constants Matter in Real Life:</strong> Asymptotic Big-O notation suppresses constant factors (\(c\)). An \(O(n)\) algorithm with \(c = 10,000\) may run slower than an \(O(n^2)\) algorithm with \(c = 1\) for \(n < 10,000\). The crossover point dictates algorithm selection in high-performance engines.</p>
<p><strong>2. Worst-Case Guarantees in Mission-Critical Systems:</strong> In real-time aviation, pacemaker controls, and Marvel defense grids, average-case time is insufficient. One must guarantee worst-case polynomial bounds (\(T_{\text{worst}}\)) to prevent deadlocks.</p>
<p><strong>3. Amortized Time Analysis:</strong> Operations like dynamic array resizing (<code>vector.push_back</code>) take \(O(n)\) occasionally to reallocate memory, but \(O(1)\) across \(n\) sequential calls, yielding an amortized time of \(O(1)\).</p>
""",
        "speech_bubbles": [
            ("Doctor Strange", "By the Eye of Agamotto, counting clock milliseconds on an unstable CPU is foolish! True sorcerers measure asymptotic step counts across all timelines."),
            ("Doctor Strange", "Notice how O(n^2) explodes exponentially as N passes 10,000? Master the time stone by breaking problems into O(n log n) divide-and-conquer portals.")
        ],
        "quiz": [
            {
                "q": "Why does DAA count elementary operations rather than recording wall-clock milliseconds?",
                "options": [
                    "Millisecond timers are deprecated in modern programming languages",
                    "Clock time varies with CPU hardware, background OS load, and compiler optimizations",
                    "Elementary operations are always powers of two",
                    "Counting clock time requires quantum computing hardware"
                ],
                "answer": 1,
                "explanation": "Wall-clock measurements fluctuate across operating systems, processor loads, and CPU models. Elementary operation counting provides hardware-independent mathematical truth."
            },
            {
                "q": "Which time complexity class represents the slowest rate of growth (fastest execution) for large n?",
                "options": [
                    "O(n)",
                    "O(n log n)",
                    "O(log n)",
                    "O(sqrt(n))"
                ],
                "answer": 2,
                "explanation": "Logarithmic time O(log n) grows far slower than linear O(n) or square root O(sqrt(n)) as n scales towards infinity."
            },
            {
                "q": "What is the worst-case time complexity of finding an element in an unsorted array of size n?",
                "options": [
                    "O(1)",
                    "O(log n)",
                    "O(n)",
                    "O(n^2)"
                ],
                "answer": 2,
                "explanation": "In an unsorted array, the target element may reside at the final index or not be present, requiring an inspection of all n elements (O(n))."
            },
            {
                "q": "If an algorithm executes 3n^2 + 50n + 1000 operations, what is its asymptotic tight bound?",
                "options": [
                    "Theta(n)",
                    "Theta(n^2)",
                    "Theta(n^3)",
                    "Theta(1000)"
                ],
                "answer": 1,
                "explanation": "In asymptotic analysis, the highest order term (n^2) dominates as n grows large; constant coefficients and lower-order terms (50n + 1000) are dropped."
            }
        ],
        "summary": "Mastering time complexity allows you to predict whether an algorithm will complete in microseconds or require centuries. In technical interviews and exams, always define the dominant term and ignore lower-order coefficients."
    },

    # 3. ASYMPTOTIC NOTATIONS (Vision)
    {
        "filename": "topic-asymptotic-notations.html",
        "topic_id": "asymptotic-notations",
        "mission_num": "01",
        "mission_title": "FOUNDATIONS",
        "mission_url": "mission-01.html",
        "topic_num": "TOPIC 03",
        "topic_title": "ASYMPTOTIC NOTATIONS",
        "hero_name": "VISION",
        "hero_color": "#10b981",
        "hero_tag": "MATHEMATICAL SYNTHESIS",
        "hero_quote": "A function is merely arbitrary code until bounded from above and below by rigorous asymptotic limits.",
        "badge_color": "#d1fae5",
        "viz_type": "bounds",
        "problem_invariants": """
<p>Asymptotic Notation provides the formal mathematical language used in computer science to classify and compare the limiting behavior of functions as input size \(n \to \infty\). Rather than dealing with messy exact polynomials, asymptotic bounds capture the core rate of growth.</p>
<p>The three fundamental asymptotic bounds are defined mathematically as:</p>
<ul>
  <li><strong>Big-O Notation (\(O\)) — Asymptotic Upper Bound:</strong> \(f(n) = O(g(n))\) if there exist positive constants \(c > 0\) and \(n_0 \ge 1\) such that \(0 \le f(n) \le c \cdot g(n)\) for all \(n \ge n_0\).</li>
  <li><strong>Big-Omega Notation (\(\Omega\)) — Asymptotic Lower Bound:</strong> \(f(n) = \Omega(g(n))\) if there exist positive constants \(c > 0\) and \(n_0 \ge 1\) such that \(0 \le c \cdot g(n) \le f(n)\) for all \(n \ge n_0\).</li>
  <li><strong>Big-Theta Notation (\(\Theta\)) — Asymptotically Tight Bound:</strong> \(f(n) = \Theta(g(n))\) if and only if \(f(n) = O(g(n))\) and \(f(n) = \Omega(g(n))\). That is, \(c_1 \cdot g(n) \le f(n) \le c_2 \cdot g(n)\) for all \(n \ge n_0\).</li>
  <li><strong>Little-o (\(o\)) & Little-omega (\(\omega\)):</strong> Represent strict, non-tight upper and lower bounds respectively, where the ratio limit approaches \(0\) or \(\infty\).</li>
</ul>
""",
        "naive_vs_optimal": """
<p>A common error in computer science exams is conflating Big-O with 'worst case'. Big-O is an upper bound on <em>any</em> function, not necessarily the worst case. Saying QuickSort takes \(O(n^3)\) is mathematically true (since \(n^2 \le n^3\)), but loose and uninformative. The optimal specification is \(\Theta(n \log n)\) average case and \(\Theta(n^2)\) worst case.</p>
<div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px; margin-top:12px;">
  <div style="background:#fee2e2; border:2px solid #ef4444; padding:12px; font-size:0.85rem;">
    <strong style="color:#b91c1c;">LOOSE / MISLEADING BOUNDS</strong><br>
    Stating: Linear Search = \(O(n^2)\).<br>
    While mathematically valid (\(f(n) \le c \cdot n^2\)), it fails to convey tight operational characteristics.
  </div>
  <div style="background:#dcfce7; border:2px solid #16a34a; padding:12px; font-size:0.85rem;">
    <strong style="color:#15803d;">TIGHT THETA BOUND</strong><br>
    Stating: Linear Search = \(\Theta(n)\).<br>
    Sandwiches growth between \(c_1 n\) and \(c_2 n\), giving complete mathematical certitude.
  </div>
</div>
""",
        "math_formulation": r"""
<p><strong>Formal Limits for Asymptotic Comparison:</strong></p>
\[ L = \lim_{n \to \infty} \frac{f(n)}{g(n)} \]
<ul>
  <li>If \(L = 0 \implies f(n) = o(g(n))\) and \(f(n) = O(g(n))\).</li>
  <li>If \(0 < L < \infty \implies f(n) = \Theta(g(n))\).</li>
  <li>If \(L = \infty \implies f(n) = \omega(g(n))\) and \(f(n) = \Omega(g(n))\).</li>
</ul>
<p><strong>Limit Ratio Theorem Example:</strong> Let \(f(n) = 7n^2 + 3n\) and \(g(n) = n^2\):</p>
\[ L = \lim_{n \to \infty} \frac{7n^2 + 3n}{n^2} = \lim_{n \to \infty} \left(7 + \frac{3}{n}\right) = 7 \implies f(n) = \Theta(n^2) \]
""",
        "worked_example": """
<p><strong>Formal Proof Example:</strong> Prove that \(f(n) = 3n + 8\) is \(O(n)\) using formal definition constants \((c, n_0)\).</p>
<ol style="margin-left:20px; line-height:1.8;">
  <li><strong>Target Inequality:</strong> We must find \(c > 0\) and \(n_0 \ge 1\) such that \(3n + 8 \le c \cdot n\) for all \(n \ge n_0\).</li>
  <li><strong>Manipulate Inequality:</strong>
      \[ 3n + 8 \le 3n + 8n = 11n \quad (\text{for all } n \ge 1) \]
  </li>
  <li><strong>Select Constants:</strong> Choose \(c = 11\) and \(n_0 = 1\).</li>
  <li><strong>Verification:</strong>
      <br>For \(n = 1\): \(3(1) + 8 = 11 \le 11(1) = 11\) (True).
      <br>For \(n = 2\): \(3(2) + 8 = 14 \le 11(2) = 22\) (True).
      <br>For \(n = 10\): \(3(10) + 8 = 38 \le 11(10) = 110\) (True).
  </li>
  <li><strong>Conclusion:</strong> Since the condition holds for \(c = 11, n_0 = 1\), by definition \(3n + 8 \in O(n)\). \(\blacksquare\)</li>
</ol>
""",
        "complexity_table": [
            ("Big-O (O)", "Upper Bound", "f(n) <= c * g(n)", "Worst-case ceiling; guarantees run time won't exceed curve"),
            ("Big-Omega (Omega)", "Lower Bound", "f(n) >= c * g(n)", "Best-case floor; algorithm takes at least this many steps"),
            ("Big-Theta (Theta)", "Tight Bound", "c1 * g(n) <= f(n) <= c2 * g(n)", "Both upper and lower bound; exact rate of growth"),
            ("Little-o (o)", "Strict Upper Bound", "f(n) < c * g(n) for all c > 0", "Ratio limit approaches 0 as n -> infinity"),
            ("Little-omega (omega)", "Strict Lower Bound", "f(n) > c * g(n) for all c > 0", "Ratio limit approaches infinity as n -> infinity")
        ],
        "code": '''def demonstrate_bounds_check(f_val: float, g_val: float, c: float) -> bool:
    """
    Verifies if f(n) <= c * g(n) for a chosen constant c.
    Returns True if the upper bound invariant holds.
    """
    return f_val <= c * g_val

# Testing f(n) = 3n + 8 vs g(n) = n with c = 11
n_values = [1, 5, 10, 50, 100, 1000]
c = 11.0

for n in n_values:
    fn = 3 * n + 8
    gn = c * n
    is_valid = demonstrate_bounds_check(fn, n, c)
    # Guaranteed to evaluate True for all n >= 1''',
        "practical_considerations": """
<p><strong>1. Asymptotic Equivalence vs Real Hardware:</strong> Two algorithms with \(\Theta(n \log n)\) complexity can exhibit radically different runtimes. For example, QuickSort and HeapSort are both \(\Theta(n \log n)\), but QuickSort's sequential memory access yields cache hits, making it 2x-3x faster in practice.</p>
<p><strong>2. Invariance to Multiplicative Constants:</strong> Multiplying an algorithm's speed by upgrading CPU clock frequency from 2 GHz to 4 GHz cuts execution time in half, but does not alter its asymptotic notation. Asymptotic notation measures structural algorithmic scalability, not hardware raw speed.</p>
<p><strong>3. Transitivity & Symmetry:</strong> If \(f(n) = O(g(n))\) and \(g(n) = O(h(n))\), then \(f(n) = O(h(n))\). Furthermore, \(f(n) = \Theta(g(n)) \iff g(n) = \Theta(f(n))\).</p>
""",
        "speech_bubbles": [
            ("Vision", "I calculate a 99.8% probability of confusion among students between Big-O and worst case. Remember: Big-O is an upper bound on any metric, not exclusively the worst case."),
            ("Vision", "When f(n) is tightly bound between c1*g(n) and c2*g(n), we achieve Big-Theta equilibrium. The Mind Stone perceives perfection in exact tight bounds.")
        ],
        "quiz": [
            {
                "q": "What condition must be satisfied for f(n) to be Theta(g(n))?",
                "options": [
                    "f(n) must be strictly less than g(n) for all n",
                    "f(n) must be both O(g(n)) and Omega(g(n)) simultaneously",
                    "The limit of f(n)/g(n) as n -> infinity must equal 0",
                    "f(n) must be a polynomial of degree strictly less than g(n)"
                ],
                "answer": 1,
                "explanation": "Theta(g(n)) denotes an asymptotically tight bound, which by definition requires f(n) to be bounded from above by O(g(n)) and from below by Omega(g(n))."
            },
            {
                "q": "If f(n) = 2^(n+1), which of the following is true?",
                "options": [
                    "f(n) is O(2^n)",
                    "f(n) is Theta(2^(2n))",
                    "f(n) is o(2^n)",
                    "f(n) is Omega(3^n)"
                ],
                "answer": 0,
                "explanation": "2^(n+1) = 2 * 2^n. Setting c = 2 satisfies 2^(n+1) <= c * 2^n for all n >= 1, meaning f(n) = O(2^n)."
            },
            {
                "q": "What does Little-o notation (f(n) = o(g(n))) imply about the limit ratio lim f(n)/g(n)?",
                "options": [
                    "The limit equals 1",
                    "The limit equals infinity",
                    "The limit equals 0",
                    "The limit does not exist"
                ],
                "answer": 2,
                "explanation": "Little-o represents a strictly smaller asymptotic growth rate, meaning lim_{n->infty} f(n)/g(n) = 0."
            },
            {
                "q": "Which of the following constants (c, n_0) correctly proves 4n^2 + 5 <= c * n^2 for all n >= n_0?",
                "options": [
                    "c = 4, n_0 = 1",
                    "c = 9, n_0 = 1",
                    "c = 2, n_0 = 5",
                    "c = 3, n_0 = 10"
                ],
                "answer": 1,
                "explanation": "For n >= 1, 5 <= 5n^2. Thus 4n^2 + 5 <= 4n^2 + 5n^2 = 9n^2. Setting c = 9 and n_0 = 1 satisfies the inequality."
            }
        ],
        "summary": "Mastering asymptotic notations is the cornerstone of algorithm design. Big-O gives the ceiling, Big-Omega provides the floor, and Big-Theta pinpoints the exact rate of asymptotic growth."
    },

    # 4. STACKS (Captain America)
    {
        "filename": "topic-stacks.html",
        "topic_id": "stacks",
        "mission_num": "02",
        "mission_title": "DATA STRUCTURES",
        "mission_url": "mission-02.html",
        "topic_num": "TOPIC 01",
        "topic_title": "STACKS",
        "hero_name": "CAPTAIN AMERICA",
        "hero_color": "#2563eb",
        "hero_tag": "LIFO VIBRANIUM SHIELD DISCIPLINE",
        "hero_quote": "Discipline wins battles. The last shield deployed into combat is the first shield recovered from the front line.",
        "badge_color": "#dbeafe",
        "viz_type": "stack",
        "problem_invariants": """
<p>A <strong>Stack</strong> is a fundamental linear data structure adhering strictly to the <strong>LIFO (Last-In, First-Out)</strong> or <strong>FILO (First-In, Last-Out)</strong> structural invariant. All insertions and deletions take place exclusively at a single designated terminal end termed the <strong>TOP</strong> of the stack.</p>
<p>Core Stack Primitive Operations:</p>
<ul>
  <li><code>push(x)</code>: Places item \(x\) onto the top of the stack. Requires bounds checking against maximum capacity (preventing <em>Stack Overflow</em>). Time Complexity: \(O(1)\).</li>
  <li><code>pop()</code>: Removes and returns the topmost element. Requires checking if the stack is non-empty (preventing <em>Stack Underflow</em>). Time Complexity: \(O(1)\).</li>
  <li><code>peek()</code> / <code>top()</code>: Returns the topmost item without removing it. Time Complexity: \(O(1)\).</li>
  <li><code>isEmpty()</code>: Returns boolean status indicating whether the stack contains 0 items. Time Complexity: \(O(1)\).</li>
</ul>
<p><strong>Primary Applications in DAA:</strong> Function call stack management in recursion, balanced parentheses matching in compilers, expression evaluation (Infix to Postfix conversion), and Depth-First Search (DFS) graph traversal.</p>
""",
        "naive_vs_optimal": """
<p>Implementing a stack using a raw naive array with element shifting results in disastrous performance: inserting at index 0 requires shifting \(n\) elements, causing \(O(n)\) push operations. The optimal design maintains a single integer pointer <code>top</code> initialized to \(-1\), executing push and pop in strictly \(O(1)\) time without shifting a single byte.</p>
<div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px; margin-top:12px;">
  <div style="background:#fee2e2; border:2px solid #ef4444; padding:12px; font-size:0.85rem;">
    <strong style="color:#b91c1c;">NAIVE SHIFTING ARRAY</strong><br>
    Inserts at index 0 and shifts elements right.<br>
    Push Time: \(O(n)\)<br>
    Pop Time: \(O(n)\)<br>
    Severe cache thrashing on massive sequences.
  </div>
  <div style="background:#dcfce7; border:2px solid #16a34a; padding:12px; font-size:0.85rem;">
    <strong style="color:#15803d;">OPTIMAL TOP-POINTER STACK</strong><br>
    Maintains <code>top</code> index tracking stack summit.<br>
    Push Time: \(\Theta(1)\)<br>
    Pop Time: \(\Theta(1)\)<br>
    Zero memory movements; optimal CPU register utilization.
  </div>
</div>
""",
        "math_formulation": r"""
<p><strong>Stack Capacity Constraints:</strong></p>
\[ \text{Let array size be } N. \quad \text{Empty Condition: } \text{top} = -1. \quad \text{Full Condition: } \text{top} = N - 1 \]
<p><strong>Catalan Number Permutations:</strong> Given \(n\) distinct elements pushed into a stack in fixed order, the number of distinct valid pop permutation sequences is given by the \(n\)-th Catalan Number:</p>
\[ C_n = \frac{1}{n+1} \binom{2n}{n} = \frac{(2n)!}{(n+1)! n!} \]
<p>For \(n = 3\) items \(\{A, B, C\}\):</p>
\[ C_3 = \frac{1}{4} \binom{6}{3} = \frac{20}{4} = 5 \text{ valid permutation sequences out of } 3! = 6 \text{ total permutations}. \]
""",
        "worked_example": """
<p><strong>Worked Example:</strong> Evaluating Postfix Expression <code>5 3 + 8 2 - *</code> using a Stack.</p>
<ol style="margin-left:20px; line-height:1.8;">
  <li><strong>Read '5':</strong> Push <code>5</code>. Stack: <code>[5]</code>.</li>
  <li><strong>Read '3':</strong> Push <code>3</code>. Stack: <code>[5, 3]</code>.</li>
  <li><strong>Read '+':</strong> Pop <code>op2 = 3</code>, Pop <code>op1 = 5</code>. Compute \(5 + 3 = 8\). Push <code>8</code>. Stack: <code>[8]</code>.</li>
  <li><strong>Read '8':</strong> Push <code>8</code>. Stack: <code>[8, 8]</code>.</li>
  <li><strong>Read '2':</strong> Push <code>2</code>. Stack: <code>[8, 8, 2]</code>.</li>
  <li><strong>Read '-':</strong> Pop <code>op2 = 2</code>, Pop <code>op1 = 8</code>. Compute \(8 - 2 = 6\). Push <code>6</code>. Stack: <code>[8, 6]</code>.</li>
  <li><strong>Read '*':</strong> Pop <code>op2 = 6</code>, Pop <code>op1 = 8</code>. Compute \(8 \times 6 = 48\). Push <code>48</code>. Stack: <code>[48]</code>.</li>
</ol>
<p><strong>Final Result:</strong> Pop last element = <strong>48</strong>. Total operations: 7 steps, strictly \(\Theta(N)\) time and \(O(N)\) auxiliary space.</p>
""",
        "complexity_table": [
            ("Push Operation", "O(1)", "O(1) Auxiliary", "Direct array assignment at top++ without shifting"),
            ("Pop Operation", "O(1)", "O(1) Auxiliary", "Retrieval at top followed by top-- decrement"),
            ("Peek / Top", "O(1)", "O(1) Auxiliary", "Single memory read access at arr[top]"),
            ("Is Empty / Size", "O(1)", "O(1) Auxiliary", "Direct comparison top == -1"),
            ("Search Element (Unrestricted)", "O(n)", "O(n) Auxiliary", "Must pop elements to reach internal targets")
        ],
        "code": '''class VibraniumStack:
    """
    Fixed-size array stack implementation with Captain America discipline.
    Guarantees strict O(1) push, pop, and peek operations.
    """
    def __init__(self, capacity: int = 10):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.top = -1  # Invariant: points to active top item
        
    def push(self, shield_id: str) -> bool:
        if self.top >= self.capacity - 1:
            raise OverflowError("STACK OVERFLOW: Vibranium rack at max capacity!")
        self.top += 1
        self.storage[self.top] = shield_id
        return True
        
    def pop(self) -> str:
        if self.top == -1:
            raise IndexError("STACK UNDERFLOW: No shields remaining in rack!")
        item = self.storage[self.top]
        self.storage[self.top] = None  # Prevent memory leak
        self.top -= 1
        return item
        
    def peek(self) -> str | None:
        return self.storage[self.top] if self.top != -1 else None''',
        "practical_considerations": """
<p><strong>1. Static Array vs Dynamic Linked List:</strong> Static array stacks provide blazing speed and optimal cache locality because elements are contiguous in memory. Linked list stacks eliminate fixed capacity limits but incur extra pointer memory (8 bytes per node on 64-bit systems) and heap allocation overhead.</p>
<p><strong>2. CPU Hardware Support:</strong> Modern CPUs possess dedicated hardware stack support via registers (<code>RSP</code> in x86-64) and machine instructions (<code>PUSH</code>, <code>POP</code>, <code>CALL</code>, <code>RET</code>), making stack operations faster than any other dynamic memory structure.</p>
<p><strong>3. Monotonic Stack Technique:</strong> Advanced DAA competitive programming problems (such as 'Next Greater Element', 'Largest Rectangle in Histogram') use monotonic stacks to reduce \(O(n^2)\) brute force searching down to \(\Theta(n)\) amortized linear time.</p>
""",
        "speech_bubbles": [
            ("Captain America", "Attention team! A stack respects military order: Last-In, First-Out. Never try to pull a shield from the bottom unless you want a stack underflow disaster!"),
            ("Captain America", "When evaluating arithmetic expressions or unwinding function recursion, the stack is your most loyal ally. Keep operations at O(1) time and hold the line.")
        ],
        "quiz": [
            {
                "q": "Which principle governs the order of elements entering and exiting a Stack?",
                "options": [
                    "FIFO (First-In, First-Out)",
                    "LIFO (Last-In, First-Out)",
                    "Priority Selection",
                    "Random Access Order"
                ],
                "answer": 1,
                "explanation": "Stacks follow LIFO (Last-In, First-Out): the most recently inserted element is always the first one to be removed."
            },
            {
                "q": "What runtime error occurs when executing pop() on an empty stack?",
                "options": [
                    "Stack Overflow",
                    "Stack Underflow",
                    "Segmentation Fault",
                    "Deadlock Exception"
                ],
                "answer": 1,
                "explanation": "Attempting to remove or pop an element from an already empty stack results in a Stack Underflow error."
            },
            {
                "q": "How many valid pop permutations can be formed from 3 distinct elements pushed into a stack in sequence 1, 2, 3?",
                "options": [
                    "6",
                    "5",
                    "4",
                    "3"
                ],
                "answer": 1,
                "explanation": "The number of valid permutations is given by the 3rd Catalan number C_3 = (1/4) * binom(6,3) = 5. (The sequence 3, 1, 2 is impossible)."
            },
            {
                "q": "What is the worst-case time complexity of peek() in an optimal array-based stack?",
                "options": [
                    "O(n)",
                    "O(log n)",
                    "O(1)",
                    "O(n^2)"
                ],
                "answer": 2,
                "explanation": "Peek accesses the element directly at arr[top] using the top pointer in O(1) constant time without modifying the stack."
            }
        ],
        "summary": "Stacks enforce LIFO discipline with O(1) push and pop operations. They form the foundational architecture for compiler expression parsing, recursive call stacks, and backtracking algorithms."
    },

    # 5. QUEUES (Hulk)
    {
        "filename": "topic-queues.html",
        "topic_id": "queues",
        "mission_num": "02",
        "mission_title": "DATA STRUCTURES",
        "mission_url": "mission-02.html",
        "topic_num": "TOPIC 02",
        "topic_title": "QUEUES",
        "hero_name": "HULK",
        "hero_color": "#16a34a",
        "hero_tag": "FIFO SMASH BUFFER PIPELINE",
        "hero_quote": "Hulk smash queue bottlenecks! First chariot into Gamma arena is first chariot to strike target!",
        "badge_color": "#dcfce7",
        "viz_type": "queue",
        "problem_invariants": """
<p>A <strong>Queue</strong> is a linear data structure governed by the <strong>FIFO (First-In, First-Out)</strong> structural invariant. Elements are added at one end called the <strong>REAR</strong> (or Tail) and deleted from the opposite end called the <strong>FRONT</strong> (or Head).</p>
<p>Core Queue Primitive Operations:</p>
<ul>
  <li><code>enqueue(x)</code>: Appends item \(x\) to the rear of the queue. Time Complexity: \(O(1)\).</li>
  <li><code>dequeue()</code>: Removes and returns the item from the front of the queue. Time Complexity: \(O(1)\).</li>
  <li><code>front()</code>: Inspects the front item without extraction. Time Complexity: \(O(1)\).</li>
  <li><code>isFull()</code> & <code>isEmpty()</code>: Validates capacity limits to prevent overflow and underflow faults.</li>
</ul>
<p><strong>Primary Applications in DAA:</strong> Breadth-First Search (BFS) graph traversal, CPU process scheduling (Round-Robin), asynchronous printer spooling buffers, and network packet routing.</p>
""",
        "naive_vs_optimal": """
<p>A linear array queue suffers from <em>False Overflow</em>: as elements are enqueued and dequeued, the front and rear pointers march towards the end of the array. Even if the front of the array is completely empty, <code>rear == capacity - 1</code> triggers overflow! The optimal solution is the <strong>Circular Queue</strong>, wrapping pointers back to index 0 using modulo arithmetic: <code>(rear + 1) % capacity</code>.</p>
<div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px; margin-top:12px;">
  <div style="background:#fee2e2; border:2px solid #ef4444; padding:12px; font-size:0.85rem;">
    <strong style="color:#b91c1c;">LINEAR QUEUE (FALSE OVERFLOW)</strong><br>
    Front and rear advance linearly.<br>
    Problem: Dequeued slots at array beginning become dead, unusable memory.<br>
    Requires expensive \(O(n)\) array sliding or re-centering.
  </div>
  <div style="background:#dcfce7; border:2px solid #16a34a; padding:12px; font-size:0.85rem;">
    <strong style="color:#15803d;">CIRCULAR QUEUE (MODULO RING)</strong><br>
    Wrap-around via <code>(idx + 1) % N</code>.<br>
    Recycles freed memory seamlessly.<br>
    Guarantees strict \(\Theta(1)\) enqueue and dequeue forever.
  </div>
</div>
""",
        "math_formulation": r"""
<p><strong>Circular Queue Ring Modulo Arithmetic:</strong></p>
\[ \text{Next Rear Index: } \text{rear} = (\text{rear} + 1) \pmod N \]
\[ \text{Next Front Index: } \text{front} = (\text{front} + 1) \pmod N \]
<p><strong>Full and Empty State Invariants:</strong></p>
\[ \text{Queue Empty: } \text{count} = 0 \quad (\text{or } \text{front} == -1) \]
\[ \text{Queue Full: } \text{count} == N \quad (\text{or } (\text{rear} + 1) \pmod N == \text{front}) \]
<p><strong>Current Queue Size:</strong></p>
\[ \text{Size} = (\text{rear} - \text{front} + N) \pmod N \]
""",
        "worked_example": """
<p><strong>Worked Example:</strong> Step-by-step trace of a Circular Queue of capacity \(N = 4\).</p>
<ol style="margin-left:20px; line-height:1.8;">
  <li><strong>Initial State:</strong> <code>front = 0, rear = 0, count = 0</code>, Array = <code>[_, _, _, _]</code>.</li>
  <li><strong>Enqueue(10):</strong> Store at <code>arr[0] = 10</code>. <code>rear = (0+1)%4 = 1</code>. <code>count = 1</code>. Array: <code>[10, _, _, _]</code>.</li>
  <li><strong>Enqueue(20):</strong> Store at <code>arr[1] = 20</code>. <code>rear = (1+1)%4 = 2</code>. <code>count = 2</code>. Array: <code>[10, 20, _, _]</code>.</li>
  <li><strong>Enqueue(30):</strong> Store at <code>arr[2] = 30</code>. <code>rear = (2+1)%4 = 3</code>. <code>count = 3</code>. Array: <code>[10, 20, 30, _]</code>.</li>
  <li><strong>Dequeue():</strong> Retrieve <code>arr[0] = 10</code>. <code>front = (0+1)%4 = 1</code>. <code>count = 2</code>. Array: <code>[_, 20, 30, _]</code>.</li>
  <li><strong>Enqueue(40):</strong> Store at <code>arr[3] = 40</code>. <code>rear = (3+1)%4 = 0</code>. <code>count = 3</code>. Array: <code>[_, 20, 30, 40]</code>.</li>
  <li><strong>Enqueue(50):</strong> Wrap around! Store at <code>arr[0] = 50</code>. <code>rear = (0+1)%4 = 1</code>. <code>count = 4 (FULL)</code>. Array: <code>[50, 20, 30, 40]</code>.</li>
</ol>
<p><em>Observation:</em> Slot 0 was recycled cleanly without shifting any elements!</p>
""",
        "complexity_table": [
            ("Enqueue (Circular)", "O(1)", "O(1) Auxiliary", "Direct assignment at rear, followed by modular index bump"),
            ("Dequeue (Circular)", "O(1)", "O(1) Auxiliary", "Direct read at front, followed by modular index bump"),
            ("Peek / Front", "O(1)", "O(1) Auxiliary", "Single memory read access at arr[front]"),
            ("Linear Queue (Naive Dequeue)", "O(n)", "O(1) Auxiliary", "Requires shifting all remaining elements left"),
            ("Search Queue", "O(n)", "O(n) Auxiliary", "Requires scanning elements sequentially")
        ],
        "code": '''class GammaCircularQueue:
    """
    Circular Queue buffer preventing False Overflow with O(1) FIFO speed.
    """
    def __init__(self, capacity: int = 5):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.front = 0
        self.rear = 0
        self.count = 0
        
    def enqueue(self, item: str) -> bool:
        if self.count == self.capacity:
            raise OverflowError("QUEUE OVERFLOW: Hulk buffer completely full!")
        self.storage[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity  # Modulo wrap-around
        self.count += 1
        return True
        
    def dequeue(self) -> str:
        if self.count == 0:
            raise IndexError("QUEUE UNDERFLOW: No items in Gamma queue!")
        item = self.storage[self.front]
        self.storage[self.front] = None  # Clear slot
        self.front = (self.front + 1) % self.capacity  # Modulo wrap-around
        self.count -= 1
        return item''',
        "practical_considerations": """
<p><strong>1. Double-Ended Queues (Deque):</strong> A Deque allows insertion and deletion at both ends in \(O(1)\) time. Python's <code>collections.deque</code> is implemented as a doubly-linked list of blocks, optimizing both queue and stack workflows.</p>
<p><strong>2. Priority Queues:</strong> In scenarios like Dijkstra's algorithm and Prim's MST, FIFO order is replaced by key-based priority extraction, requiring Min-Heaps with \(O(\log n)\) insertion and extraction.</p>
<p><strong>3. Lock-Free Ring Buffers:</strong> In high-throughput operating systems and audio DSP pipelines, circular queues implemented as atomic single-producer single-consumer (SPSC) ring buffers provide lock-free concurrency with zero mutex locking overhead.</p>
""",
        "speech_bubbles": [
            ("Hulk", "Hulk hate false overflow! Linear array wastes slots in front. Always use circular modulo ring so Hulk can recycle memory and smash forever!"),
            ("Hulk", "In BFS graph exploration, Queue holds wavefront frontier! First vertex discovered is first vertex expanded. Keep order clean and smash villains!")
        ],
        "quiz": [
            {
                "q": "What problem does a Circular Queue solve compared to a basic linear array queue?",
                "options": [
                    "Stack Overflow errors",
                    "False Overflow where front slots are freed but unusable",
                    "Priority inversion in thread schedulers",
                    "Infinite recursion loops"
                ],
                "answer": 1,
                "explanation": "A basic linear queue allows rear to reach capacity while front has moved forward, leaving dead space. Circular queues wrap indices around using modulo arithmetic to reuse freed slots."
            },
            {
                "q": "If a circular queue has capacity N=6, front=3, and count=4, what is the rear index for the next insertion?",
                "options": [
                    "0",
                    "1",
                    "2",
                    "5"
                ],
                "answer": 1,
                "explanation": "rear = (front + count) % N = (3 + 4) % 6 = 7 % 6 = 1."
            },
            {
                "q": "Which graph traversal algorithm fundamentally relies on a FIFO Queue?",
                "options": [
                    "Depth-First Search (DFS)",
                    "Breadth-First Search (BFS)",
                    "Tarjan's Strongly Connected Components",
                    "Kosaraju's Algorithm"
                ],
                "answer": 1,
                "explanation": "Breadth-First Search (BFS) explores vertices level-by-level using a FIFO Queue to maintain the frontier."
            },
            {
                "q": "What is the time complexity of dequeue in an optimal Circular Queue?",
                "options": [
                    "O(1)",
                    "O(log n)",
                    "O(n)",
                    "O(n^2)"
                ],
                "answer": 0,
                "explanation": "Circular queue dequeue directly accesses the element at arr[front] and advances front by (front + 1) % N in O(1) constant time."
            }
        ],
        "summary": "Queues uphold FIFO order, making them indispensable for BFS tree/graph exploration, thread job scheduling, and hardware buffer pipelines. Circular queues prevent false overflow via modulo arithmetic."
    }
]

print(f"Loaded Part 1: {len(PART1_TOPICS)} topics")
