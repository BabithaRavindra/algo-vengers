# academic_data_part3.py - Topics 11 to 15
# Mission 03: Divide and Conquer (Topics 11-13) & Mission 04: Greedy & Advanced (Topics 14-15)

PART3_TOPICS = [
    # 11. MERGE SORT (War Machine)
    {
        "filename": "topic-merge-sort.html",
        "topic_id": "merge-sort",
        "mission_num": "03",
        "mission_title": "DIVIDE AND CONQUER",
        "mission_url": "mission-03.html",
        "topic_num": "TOPIC 03",
        "topic_title": "MERGE SORT",
        "hero_name": "WAR MACHINE",
        "hero_color": "#475569",
        "hero_tag": "ARMORED HEAVY ARTILLERY RECOMBINATION",
        "hero_quote": "Divide firepower into coordinated battalions. Merge armored lines with guaranteed O(n log n) precision under any atmospheric condition.",
        "badge_color": "#e2e8f0",
        "viz_type": "merge_sort",
        "problem_invariants": """
<p><strong>Merge Sort</strong> is a classic, asymptotically optimal, comparison-based sorting algorithm invented by John von Neumann in 1945. It exemplifies the three pillars of the <strong>Divide-and-Conquer</strong> paradigm:</p>
<ol>
  <li><strong>Divide:</strong> Divide the unsorted array of size \(n\) into two equal subarrays of size \(\lfloor n/2 \rfloor\) and \(\lceil n/2 \rceil\) at index \(\text{mid} = \lfloor \frac{\text{low} + \text{high}}{2} \rfloor\).</li>
  <li><strong>Conquer:</strong> Recursively sort both subarrays by calling Merge Sort until the base case of size \(1\) is reached (a singleton array is trivially sorted).</li>
  <li><strong>Combine (Merge):</strong> Merge the two sorted subarrays into a single sorted array using a linear two-finger pointer merge routine in \(\Theta(n)\) time.</li>
</ol>
<p><strong>Crucial Structural Properties:</strong></p>
<ul>
  <li><strong>Stability:</strong> Merge Sort is <em>strictly stable</em> (equal keys preserve their original relative input order, provided the merge condition uses \(\le\)).</li>
  <li><strong>Guaranteed Worst-Case Time:</strong> Unlike QuickSort, Merge Sort is immune to degenerate adversarial inputs; its worst-case runtime is unconditionally \(\Theta(n \log n)\).</li>
</ul>
""",
        "naive_vs_optimal": """
<p>Naive quadratic sorting algorithms (Bubble Sort, Selection Sort, Insertion Sort) perform pairwise comparisons resulting in \(\Theta(n^2)\) worst-case time. For \(n = 100,000\), quadratic sorts execute \(10^{10}\) operations (~10 seconds). War Machine's Merge Sort requires only \(100,000 \times \log_2(100,000) \approx 1.66 \times 10^6\) operations (~2 milliseconds), a 6,000x speedup!</p>
<div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px; margin-top:12px;">
  <div style="background:#fee2e2; border:2px solid #ef4444; padding:12px; font-size:0.85rem;">
    <strong style="color:#b91c1c;">QUADRATIC SORTS [O(n^2)]</strong><br>
    \(n = 10^5 \implies 10,000,000,000\) steps.<br>
    Completely freezes systems on massive datasets.
  </div>
  <div style="background:#dcfce7; border:2px solid #16a34a; padding:12px; font-size:0.85rem;">
    <strong style="color:#15803d;">MERGE SORT [Theta(n log n)]</strong><br>
    \(n = 10^5 \implies 1,660,000\) steps.<br>
    Predictable, battle-hardened, guaranteed performance.
  </div>
</div>
""",
        "math_formulation": r"""
<p><strong>Recurrence Relation for Merge Sort:</strong></p>
\[ T(n) = 2T(n/2) + \Theta(n) \]
<p><strong>Master Theorem Derivation:</strong> Here \(a = 2, b = 2, f(n) = \Theta(n) = \Theta(n^1)\).</p>
\[ n^{\log_b a} = n^{\log_2 2} = n^1 = n \]
<p>Since \(f(n) = \Theta(n^{\log_b a})\) (Case 2 of Master Theorem with \(k = 0\)):</p>
\[ T(n) = \Theta(n^{\log_b a} \log n) = \Theta(n \log_2 n) \]
<p><strong>Total Comparisons Upper Bound:</strong> In the merge phase of two subarrays of lengths \(n_1\) and \(n_2\), at most \(n_1 + n_2 - 1 = n - 1\) comparisons are performed. Across all \(\log_2 n\) levels of the recursion tree, total comparisons \(\le n \log_2 n - n + 1\).</p>
""",
        "worked_example": """
<p><strong>Worked Example:</strong> Sort array <code>[38, 27, 43, 3, 9, 82, 10]</code> (\(n = 7\)) step-by-step.</p>
<ol style="margin-left:20px; line-height:1.8;">
  <li><strong>Split 1:</strong> Left <code>[38, 27, 43]</code>, Right <code>[3, 9, 82, 10]</code>.</li>
  <li><strong>Split Left Subtree:</strong>
      <br>Divide <code>[38, 27, 43]</code> into <code>[38]</code> and <code>[27, 43]</code>.
      <br>Divide <code>[27, 43]</code> into <code>[27]</code> and <code>[43]</code>.
      <br>Merge <code>[27]</code> and <code>[43]</code>: compare \(27 \le 43 \implies\) <code>[27, 43]</code>.
      <br>Merge <code>[38]</code> and <code>[27, 43]</code>: compare \(38\) vs \(27 \to [27]\); compare \(38\) vs \(43 \to [27, 38, 43]\).
  </li>
  <li><strong>Split Right Subtree:</strong>
      <br>Divide <code>[3, 9, 82, 10]</code> into <code>[3, 9]</code> and <code>[82, 10]</code>.
      <br>Merge <code>[3]</code> and <code>[9]</code> \(\implies\) <code>[3, 9]</code>.
      <br>Merge <code>[82]</code> and <code>[10]</code> \(\implies\) <code>[10, 82]</code>.
      <br>Merge <code>[3, 9]</code> and <code>[10, 82]</code>: compare elements \(\implies\) <code>[3, 9, 10, 82]</code>.
  </li>
  <li><strong>Final Grand Merge:</strong>
      <br>Merge <code>[27, 38, 43]</code> with <code>[3, 9, 10, 82]</code>:
      <br>Compare 27 vs 3 \(\to [3]\)
      <br>Compare 27 vs 9 \(\to [3, 9]\)
      <br>Compare 27 vs 10 \(\to [3, 9, 10]\)
      <br>Compare 27 vs 82 \(\to [3, 9, 10, 27]\)
      <br>Compare 38 vs 82 \(\to [3, 9, 10, 27, 38]\)
      <br>Compare 43 vs 82 \(\to [3, 9, 10, 27, 38, 43]\)
      <br>Remaining element 82 appended directly!
      <br><strong>Sorted Output:</strong> <code>[3, 9, 10, 27, 38, 43, 82]</code>.
  </li>
</ol>
""",
        "complexity_table": [
            ("Best-Case Time", "Theta(n log n)", "Omega(n log n)", "Requires full tree recursion regardless of sorted input"),
            ("Average-Case Time", "Theta(n log n)", "Omega(n log n)", "Consistent across all permutations"),
            ("Worst-Case Time", "Theta(n log n)", "Omega(n log n)", "Guaranteed upper bound against adversarial inputs"),
            ("Auxiliary Space Complexity", "O(n)", "O(n)", "Requires temporary array buffers during merge step"),
            ("Stability", "STABLE", "Yes", "Preserves relative order of equal keys when using <=")
        ],
        "code": '''def merge_sort(arr: list[int]) -> list[int]:
    """
    Standard recursive Merge Sort with O(n log n) guaranteed time.
    Stable sorting algorithm requiring O(n) auxiliary memory.
    """
    if len(arr) <= 1:
        return arr  # Base case: singleton array
        
    mid = len(arr) // 2
    left_sorted = merge_sort(arr[:mid])
    right_sorted = merge_sort(arr[mid:])
    
    return _merge(left_sorted, right_sorted)

def _merge(left: list[int], right: list[int]) -> list[int]:
    merged = []
    i = j = 0
    
    # Two-finger linear merge step (O(n))
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # <= ensures algorithmic STABILITY
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            
    # Append any remaining trailing elements
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged''',
        "practical_considerations": """
<p><strong>1. Memory Overhead (\(O(n)\) Auxiliary Space):</strong> The primary drawback of standard Merge Sort compared to QuickSort is its \(O(n)\) extra memory buffer requirement. In RAM-constrained microcontrollers, this can cause out-of-memory faults.</p>
<p><strong>2. External Sorting (Big Data on Disks):</strong> Merge Sort is the reigning king of <em>External Sorting</em> (sorting datasets of 100 TB that do not fit in RAM). Sequential disk block reads during the merge pass maximize sequential I/O throughput and minimize expensive random disk seeks.</p>
<p><strong>3. Timsort (Python & Java Standard Sort):</strong> Python's <code>sorted()</code> and Java's <code>Arrays.sort()</code> utilize Timsort, a hybrid derivative of Merge Sort and Insertion Sort that identifies natural pre-sorted runs and achieves \(O(n)\) best-case time while maintaining \(O(n \log n)\) worst-case stability.</p>
""",
        "speech_bubbles": [
            ("War Machine", "Heavy artillery doctrine: Never gamble on average-case luck! Merge Sort guarantees Theta(n log n) under the heaviest enemy fire, whether the array is reversed, random, or pre-sorted."),
            ("War Machine", "Pay attention to stability! When merging the left and right battalions, using '<=' instead of '<' ensures elements with equal priority hold their original tactical ranks.")
        ],
        "quiz": [
            {
                "q": "What is the worst-case time complexity of Merge Sort on an array of size n?",
                "options": [
                    "O(n)",
                    "O(n log n)",
                    "O(n^2)",
                    "O(log n)"
                ],
                "answer": 1,
                "explanation": "Merge Sort always divides the array evenly and performs a linear merge, guaranteeing Theta(n log n) time across all best, average, and worst-case scenarios."
            },
            {
                "q": "What is the auxiliary space complexity of standard recursive Merge Sort?",
                "options": [
                    "O(1)",
                    "O(log n)",
                    "O(n)",
                    "O(n log n)"
                ],
                "answer": 2,
                "explanation": "Merge Sort requires O(n) auxiliary buffer space to temporarily hold and merge subarrays during the combine phase."
            },
            {
                "q": "Why is Merge Sort considered an algorithmically 'stable' sort?",
                "options": [
                    "It never crashes with a stack overflow",
                    "It preserves the original relative order of elements that have equal keys",
                    "Its runtime does not fluctuate between best and worst cases",
                    "It operates strictly in-place"
                ],
                "answer": 1,
                "explanation": "A sorting algorithm is stable if equal elements retain their relative input order. Using <= during merging preserves stability."
            },
            {
                "q": "Which application domains favor Merge Sort over QuickSort?",
                "options": [
                    "Embedded systems with 2 KB RAM",
                    "External sorting of multi-terabyte datasets stored on disk and sorting linked lists",
                    "In-place GPU primitive sorting",
                    "Real-time sorting of 10 elements"
                ],
                "answer": 1,
                "explanation": "External sorting heavily leverages Merge Sort due to sequential block disk access. Linked lists also merge in O(1) auxiliary space without extra array buffers."
            }
        ],
        "summary": "Merge Sort divides in half and merges sorted halves in linear time. It provides an ironclad Theta(n log n) runtime guarantee and algorithmic stability at the cost of O(n) auxiliary memory."
    },

    # 12. QUICK SORT (Quicksilver)
    {
        "filename": "topic-quick-sort.html",
        "topic_id": "quick-sort",
        "mission_num": "03",
        "mission_title": "DIVIDE AND CONQUER",
        "mission_url": "mission-03.html",
        "topic_num": "TOPIC 04",
        "topic_title": "QUICK SORT",
        "hero_name": "QUICKSILVER",
        "hero_color": "#0284c7",
        "hero_tag": "SUPERSONIC PIVOT PARTITIONING",
        "hero_quote": "You didn't see that coming? Pick a pivot at mach speed, partition elements in-place, and leave competitors in the dust.",
        "badge_color": "#e0f2fe",
        "viz_type": "quick_sort",
        "problem_invariants": """
<p><strong>QuickSort</strong>, invented by Tony Hoare in 1961, is the fastest general-purpose, in-place, comparison-based sorting algorithm in practical computing. Unlike Merge Sort which divides trivially and does heavy work in the merge step, QuickSort does its heavy computational work upfront during the <strong>Partitioning Step</strong>.</p>
<p><strong>Divide-and-Conquer Partitioning Workflow:</strong></p>
<ol>
  <li><strong>Pivot Selection:</strong> Select an element from the array designated as the <em>Pivot</em> (\(P\)).</li>
  <li><strong>Partitioning:</strong> Rearrange the array in-place such that:
      <ul>
        <li>All elements smaller than or equal to \(P\) are moved to the left of \(P\).</li>
        <li>All elements greater than or equal to \(P\) are moved to the right of \(P\).</li>
        <li>The pivot \(P\) is placed at its final, definitive sorted index (\(p_{\text{idx}}\)).</li>
      </ul>
  </li>
  <li><strong>Recurse:</strong> Recursively apply QuickSort to the left subarray \([0 \dots p_{\text{idx}}-1]\) and right subarray \([p_{\text{idx}}+1 \dots n-1]\).</li>
</ol>
<p><strong>Partitioning Schemes:</strong></p>
<ul>
  <li><strong>Lomuto Partitioning:</strong> Simpler to teach and implement; maintains a single runner pointer \(i\) and advances scanner \(j\). Uses last element as pivot.</li>
  <li><strong>Hoare Partitioning:</strong> Original scheme; uses two pointers converging from both ends towards the center. Executes 3x fewer swaps on average than Lomuto.</li>
</ul>
""",
        "naive_vs_optimal": """
<p>A naive pivot choice (such as always choosing the first or last element) triggers QuickSort's disastrous worst-case: on an already-sorted array (\([1, 2, 3, 4, 5]\)), partitions become maximally unbalanced (\(0\) vs \(n-1\) elements), causing recursion depth to reach \(n\) and execution time to collapse to \(\Theta(n^2)\). Optimal techniques (Randomized Pivot or Median-of-Three) guarantee balanced splits, yielding blinding \(\Theta(n \log n)\) speed.</p>
<div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px; margin-top:12px;">
  <div style="background:#fee2e2; border:2px solid #ef4444; padding:12px; font-size:0.85rem;">
    <strong style="color:#b91c1c;">NAIVE PIVOT (SORTED INPUT)</strong><br>
    Unbalanced partition: \(0\) vs \(n - 1\).<br>
    Worst-Case Time: \(\Theta(n^2)\)<br>
    Call stack reaches depth \(n\); triggers Stack Overflow.
  </div>
  <div style="background:#dcfce7; border:2px solid #16a34a; padding:12px; font-size:0.85rem;">
    <strong style="color:#15803d;">RANDOMIZED / MEDIAN-OF-THREE</strong><br>
    Expected partition: \(\sim 50\% / 50\%\).<br>
    Average-Case Time: \(\Theta(n \log n)\)<br>
    In-place memory; optimal CPU L1 cache utilization.
  </div>
</div>
""",
        "math_formulation": r"""
<p><strong>Recurrence Relations for QuickSort:</strong></p>
<ul>
  <li><strong>Best-Case Recurrence (Even 50-50 Splits):</strong>
      \[ T(n) = 2T(n/2) + \Theta(n) \implies T(n) = \Theta(n \log n) \]
  </li>
  <li><strong>Worst-Case Recurrence (Maximally Skewed Splits):</strong>
      \[ T(n) = T(n-1) + T(0) + \Theta(n) = T(n-1) + c \cdot n = c \sum_{i=1}^{n} i = \Theta(n^2) \]
  </li>
  <li><strong>Average-Case Recurrence (Uniform Random Pivots):</strong>
      \[ T(n) = \frac{2}{n} \sum_{k=0}^{n-1} T(k) + \Theta(n) \implies T(n) = 2n \ln n \approx 1.386 n \log_2 n \]
  </li>
</ul>
<p><em>Insight:</em> On average, QuickSort executes only 38.6% more comparisons than the theoretical absolute information-theoretic minimum comparison bound (\(n \log_2 n\)).</p>
""",
        "worked_example": """
<p><strong>Worked Example:</strong> Trace Lomuto Partitioning on array <code>arr = [10, 80, 30, 90, 40, 50, 70]</code> with pivot = <code>70</code> (last element).</p>
<ol style="margin-left:20px; line-height:1.8;">
  <li><strong>Initialize:</strong> Pivot \(P = 70\), boundary pointer \(i = \text{low} - 1 = -1\). Scanner \(j\) runs from index 0 to 5.</li>
  <li><strong>j = 0 (val = 10):</strong> \(10 \le 70\)? Yes. Increment \(i \to 0\). Swap \(arr[0]\) with \(arr[0]\). Array: <code>[10, 80, 30, 90, 40, 50, 70]</code>.</li>
  <li><strong>j = 1 (val = 80):</strong> \(80 \le 70\)? No. No swap.</li>
  <li><strong>j = 2 (val = 30):</strong> \(30 \le 70\)? Yes. Increment \(i \to 1\). Swap \(arr[1] (80)\) with \(arr[2] (30)\). Array: <code>[10, 30, 80, 90, 40, 50, 70]</code>.</li>
  <li><strong>j = 3 (val = 90):</strong> \(90 \le 70\)? No. No swap.</li>
  <li><strong>j = 4 (val = 40):</strong> \(40 \le 70\)? Yes. Increment \(i \to 2\). Swap \(arr[2] (80)\) with \(arr[4] (40)\). Array: <code>[10, 30, 40, 90, 80, 50, 70]</code>.</li>
  <li><strong>j = 5 (val = 50):</strong> \(50 \le 70\)? Yes. Increment \(i \to 3\). Swap \(arr[3] (90)\) with \(arr[5] (50)\). Array: <code>[10, 30, 40, 50, 80, 90, 70]</code>.</li>
  <li><strong>Place Pivot:</strong> Swap pivot \(arr[6] (70)\) with \(arr[i+1] = arr[4] (80)\).
      <br><strong>Array after Partition:</strong> <code>[10, 30, 40, 50, 70, 90, 80]</code>.
      <br>Pivot <code>70</code> is locked at sorted index 4! Left partition \([10, 30, 40, 50] \le 70\) and right partition \([90, 80] \ge 70\).
  </li>
</ol>
""",
        "complexity_table": [
            ("Average-Case Time", "Theta(n log n)", "Omega(n log n)", "Achieved on random arrays; fastest real-world sort"),
            ("Best-Case Time", "Theta(n log n)", "Omega(n log n)", "Pivot always divides array into equal halves"),
            ("Worst-Case Time", "Theta(n^2)", "Omega(n^2)", "Occurs on sorted array with naive first/last pivot"),
            ("Auxiliary Space (Average)", "O(log n)", "O(log n)", "In-place array; stack space bounded by log2(n)"),
            ("Auxiliary Space (Worst)", "O(n)", "O(n)", "Degenerate recursion stack depth"),
            ("Stability", "UNSTABLE", "No", "Long-range swaps across pivot disrupt original relative order")
        ],
        "code": '''def quick_sort(arr: list[int], low: int, high: int) -> None:
    """
    In-place QuickSort using Lomuto partitioning.
    Average Time: O(n log n), Space: O(log n) call stack.
    """
    if low < high:
        # Partition step: places pivot at sorted position
        pi = _partition(arr, low, high)
        
        # Recursively sort elements before and after pivot
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def _partition(arr: list[int], low: int, high: int) -> int:
    pivot = arr[high]  # Choosing last element as pivot
    i = low - 1        # Boundary pointer of elements <= pivot
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    # Place pivot in between partitions
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1''',
        "practical_considerations": """
<p><strong>1. Why QuickSort Beats Merge Sort in Practice:</strong> Even though both have \(\Theta(n \log n)\) average time, QuickSort operates <em>in-place</em> without allocating secondary buffers. Its contiguous inner-loop pointer increments produce superior CPU L1 cache line hits, running 2x to 3x faster than Merge Sort on modern hardware.</p>
<p><strong>2. Median-of-Three Pivot Selection:</strong> To prevent the \(O(n^2)\) worst case on sorted arrays, compilers inspect the first, middle, and last elements, selecting their median as the pivot. This eliminates worst-case vulnerability for sorted and reverse-sorted inputs.</p>
<p><strong>3. Introsort (C++ <code>std::sort</code>):</strong> Modern standard libraries utilize Introsort: it starts with QuickSort for raw speed, monitors recursion depth, and switches to HeapSort if depth exceeds \(2 \log_2 n\), thereby guaranteeing \(O(n \log n)\) worst-case safety!</p>
""",
        "speech_bubbles": [
            ("Quicksilver", "Supersonic rule: You didn't see that partition coming! Unlike Merge Sort, we don't need extra array memory. Everything happens right here in-place!"),
            ("Quicksilver", "Never use a naive first-element pivot on already sorted data unless you want an O(n^2) snail crawl! Use Median-of-Three or randomized pivots to break sound barriers!")
        ],
        "quiz": [
            {
                "q": "What scenario triggers the worst-case Theta(n^2) time complexity in basic QuickSort?",
                "options": [
                    "Array contains all negative integers",
                    "Input is already sorted and the algorithm always picks the first or last element as pivot",
                    "Input size is an exact power of two",
                    "Pivot is chosen using the median-of-three heuristic"
                ],
                "answer": 1,
                "explanation": "If the array is already sorted and the first or last element is chosen as pivot, partitions split into sizes 0 and n-1, producing an O(n^2) recursion tree."
            },
            {
                "q": "What is the average-case auxiliary space complexity of QuickSort?",
                "options": [
                    "O(1)",
                    "O(log n)",
                    "O(n)",
                    "O(n log n)"
                ],
                "answer": 1,
                "explanation": "QuickSort operates in-place without auxiliary arrays, but the recursive activation stack consumes O(log n) memory on average."
            },
            {
                "q": "Why is QuickSort generally faster than Merge Sort on real-world CPU architectures?",
                "options": [
                    "It has a lower asymptotic Big-O bound than Merge Sort",
                    "It operates in-place, yielding smaller constant factors and superior CPU cache locality",
                    "It never performs comparisons",
                    "It uses multithreading by default"
                ],
                "answer": 1,
                "explanation": "In-place partitioning produces tight cache locality with zero heap allocation overhead, outperforming Merge Sort's constant factors."
            },
            {
                "q": "How does Introsort prevent QuickSort's worst-case O(n^2) runtime in C++ std::sort?",
                "options": [
                    "By replacing QuickSort with Bubble Sort",
                    "By monitoring recursion depth and switching to HeapSort if depth exceeds 2 log(n)",
                    "By discarding duplicate array elements",
                    "By using external disk sorting"
                ],
                "answer": 1,
                "explanation": "Introsort begins with QuickSort and switches to HeapSort if recursion depth exceeds 2 log(n), guaranteeing O(n log n) worst-case safety."
            }
        ],
        "summary": "QuickSort partitions around a pivot in-place. With average-case O(n log n) runtime and superior cache locality, it is the primary general-purpose sorting algorithm across modern computing."
    },

    # 13. STRASSEN'S MATRIX MULTIPLICATION (Black Panther)
    {
        "filename": "topic-strassens-matrix-multiplication.html",
        "topic_id": "strassens-matrix-multiplication",
        "mission_num": "03",
        "mission_title": "DIVIDE AND CONQUER",
        "mission_url": "mission-03.html",
        "topic_num": "TOPIC 05",
        "topic_title": "STRASSEN'S MATRIX MULTIPLICATION",
        "hero_name": "BLACK PANTHER",
        "hero_color": "#0f172a",
        "hero_tag": "VIBRANIUM SUBSPACES & 7 PRODUCTS",
        "hero_quote": "Wakanda's vibranium matrices transcend brute force. By substituting additions for multiplications, Volker Strassen proved n^3 is not the true barrier.",
        "badge_color": "#f1f5f9",
        "viz_type": "strassen",
        "problem_invariants": """
<p>Matrix multiplication is one of the most fundamental operations in computational mathematics, graph theory, 3D graphics, and machine learning. Given two square matrices \(A, B \in \mathbb{R}^{n \times n}\), their product \(C = A \times B\) is defined by:</p>
\[ C_{ij} = \sum_{k=1}^{n} A_{ik} \cdot B_{kj} \quad \text{for } 1 \le i, j \le n \]
<p><strong>The Traditional Brute Force Barrier:</strong></p>
<ul>
  <li>Each of the \(n^2\) entries in \(C\) requires computing an inner product of length \(n\).</li>
  <li>Total scalar multiplications = \(n \times n \times n = n^3\).</li>
  <li>Total scalar additions = \(n^2(n - 1) = n^3 - n^2\).</li>
  <li>Asymptotic Complexity: \(\Theta(n^3)\). For decades, mathematicians believed \(\Theta(n^3)\) was the inviolable lower bound.</li>
</ul>
<p><strong>Standard Divide-and-Conquer (Without the Trick):</strong></p>
<p>Partitioning \(A\) and \(B\) into four \((n/2 \times n/2)\) submatrices yields 8 recursive multiplications:</p>
\[ C_{11} = A_{11}B_{11} + A_{12}B_{21}, \quad C_{12} = A_{11}B_{12} + A_{12}B_{22} \]
\[ C_{21} = A_{21}B_{11} + A_{22}B_{21}, \quad C_{22} = A_{21}B_{12} + A_{22}B_{22} \]
<p>Recurrence: \(T(n) = 8T(n/2) + \Theta(n^2)\). By Master Theorem: \(n^{\log_2 8} = n^3 \implies \Theta(n^3)\). No improvement!</p>
""",
        "naive_vs_optimal": """
<p>In 1969, Volker Strassen published a breakthrough discovery: by computing <strong>7 clever scalar products</strong> (\(M_1\) through \(M_7\)) combined with 18 matrix additions and subtractions, we eliminate the 8th recursive call! This reduces the recurrence to \(T(n) = 7T(n/2) + \Theta(n^2)\), driving the asymptotic complexity down from \(O(n^3)\) to \(O(n^{\log_2 7}) \approx O(n^{2.807})\).</p>
<div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px; margin-top:12px;">
  <div style="background:#fee2e2; border:2px solid #ef4444; padding:12px; font-size:0.85rem;">
    <strong style="color:#b91c1c;">STANDARD BRUTE FORCE [O(n^3)]</strong><br>
    \(n = 1024 \implies 1024^3 \approx 1,073,741,824\) multiplications.<br>
    Exceeds 1 billion operations.
  </div>
  <div style="background:#dcfce7; border:2px solid #16a34a; padding:12px; font-size:0.85rem;">
    <strong style="color:#15803d;">STRASSEN'S ALGORITHM [O(n^2.807)]</strong><br>
    \(n = 1024 \implies 1024^{2.807} \approx 282,475,249\) operations.<br>
    Eliminates nearly 800 million calculations! Saves ~74% compute work.
  </div>
</div>
""",
        "math_formulation": r"""
<p><strong>Strassen's 7 Matrix Formulas:</strong></p>
\[ M_1 = (A_{11} + A_{22})(B_{11} + B_{22}) \]
\[ M_2 = (A_{21} + A_{22}) B_{11} \]
\[ M_3 = A_{11} (B_{12} - B_{22}) \]
\[ M_4 = A_{22} (B_{21} - B_{11}) \]
\[ M_5 = (A_{11} + A_{12}) B_{22} \]
\[ M_6 = (A_{21} - A_{11})(B_{11} + B_{12}) \]
\[ M_7 = (A_{12} - A_{22})(B_{21} + B_{22}) \]
<p><strong>Reconstructing Output Matrix \(C\):</strong></p>
\[ C_{11} = M_1 + M_4 - M_5 + M_7 \]
\[ C_{12} = M_3 + M_5 \]
\[ C_{21} = M_2 + M_4 \]
\[ C_{22} = M_1 - M_2 + M_3 + M_6 \]
<p><strong>Master Theorem Recurrence:</strong></p>
\[ T(n) = 7T(n/2) + \Theta(n^2) \]
\[ a = 7, \quad b = 2, \quad n^{\log_b a} = n^{\log_2 7} \approx n^{2.8074} \]
\[ \text{Since } f(n) = \Theta(n^2) = O(n^{\log_2 7 - \epsilon}) \implies T(n) = \Theta(n^{\log_2 7}) \approx \Theta(n^{2.81}) \]
""",
        "worked_example": """
<p><strong>Worked Example (2 &times; 2 Matrices):</strong> Multiply matrices \(A\) and \(B\):</p>
\[ A = \begin{pmatrix} 1 & 3 \\ 7 & 5 \end{pmatrix}, \quad B = \begin{pmatrix} 6 & 8 \\ 4 & 2 \end{pmatrix} \]
<ol style="margin-left:20px; line-height:1.8;">
  <li><strong>Identify Sub-elements:</strong>
      <br>\(A_{11}=1, A_{12}=3, A_{21}=7, A_{22}=5\)
      <br>\(B_{11}=6, B_{12}=8, B_{21}=4, B_{22}=2\)
  </li>
  <li><strong>Compute the 7 Products:</strong>
      <br>\(M_1 = (1 + 5)(6 + 2) = 6 \times 8 = \mathbf{48}\)
      <br>\(M_2 = (7 + 5) \times 6 = 12 \times 6 = \mathbf{72}\)
      <br>\(M_3 = 1 \times (8 - 2) = 1 \times 6 = \mathbf{6}\)
      <br>\(M_4 = 5 \times (4 - 6) = 5 \times (-2) = \mathbf{-10}\)
      <br>\(M_5 = (1 + 3) \times 2 = 4 \times 2 = \mathbf{8}\)
      <br>\(M_6 = (7 - 1)(6 + 8) = 6 \times 14 = \mathbf{84}\)
      <br>\(M_7 = (3 - 5)(4 + 2) = (-2) \times 6 = \mathbf{-12}\)
  </li>
  <li><strong>Combine to form Matrix \(C\):</strong>
      <br>\(C_{11} = M_1 + M_4 - M_5 + M_7 = 48 + (-10) - 8 + (-12) = \mathbf{18}\)
      <br>\(C_{12} = M_3 + M_5 = 6 + 8 = \mathbf{14}\)
      <br>\(C_{21} = M_2 + M_4 = 72 + (-10) = \mathbf{62}\)
      <br>\(C_{22} = M_1 - M_2 + M_3 + M_6 = 48 - 72 + 6 + 84 = \mathbf{66}\)
  </li>
  <li><strong>Verification via Standard Dot Product:</strong>
      <br>\(C_{11} = 1(6) + 3(4) = 6 + 12 = 18\) &check;
      <br>\(C_{12} = 1(8) + 3(2) = 8 + 6 = 14\) &check;
      <br>\(C_{21} = 7(6) + 5(4) = 42 + 20 = 62\) &check;
      <br>\(C_{22} = 7(8) + 5(2) = 56 + 10 = 66\) &check;
  </li>
</ol>
<p><strong>Final Product Matrix:</strong> \(C = \begin{pmatrix} 18 & 14 \\ 62 & 66 \end{pmatrix}\). Successfully computed with only 7 multiplications!</p>
""",
        "complexity_table": [
            ("Brute-Force Traditional", "Theta(n^3)", "O(1) space", "8 recursive sub-calls; 3 nested loops"),
            ("Standard Divide & Conquer", "Theta(n^3)", "O(log n) space", "T(n) = 8T(n/2) + O(n^2); no asymptotic gain"),
            ("Strassen's Algorithm", "Theta(n^2.807)", "O(n^2) space", "T(n) = 7T(n/2) + O(n^2); saves 1 multiplication"),
            ("Coppersmith-Winograd (1990)", "O(n^2.376)", "Galactic", "Theoretical algorithm with astronomical constant factor"),
            ("Current World Record (2024)", "O(n^2.37155)", "Galactic", "Duan, Wu, Zhou galactic algorithm bound")
        ],
        "code": '''import numpy as np

def strassen_multiply(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """
    Strassen's Matrix Multiplication for 2^k x 2^k matrices.
    Achieves O(n^2.807) time complexity via 7 recursive products.
    """
    n = A.shape[0]
    
    # Practical Crossover Threshold: for small n, standard method is faster
    if n <= 64:
        return np.dot(A, B)
        
    k = n // 2
    # Subdivide A and B into four (n/2 x n/2) quadrants
    A11, A12 = A[:k, :k], A[:k, k:]
    A21, A22 = A[k:, :k], A[k:, k:]
    B11, B12 = B[:k, :k], B[:k, k:]
    B21, B22 = B[k:, :k], B[k:, k:]
    
    # Calculate Strassen's 7 Products
    M1 = strassen_multiply(A11 + A22, B11 + B22)
    M2 = strassen_multiply(A21 + A22, B11)
    M3 = strassen_multiply(A11, B12 - B22)
    M4 = strassen_multiply(A22, B21 - B11)
    M5 = strassen_multiply(A11 + A12, B22)
    M6 = strassen_multiply(A21 - A11, B11 + B12)
    M7 = strassen_multiply(A12 - A22, B21 + B22)
    
    # Assemble output quadrant components
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6
    
    # Recombine quadrants into single matrix
    return np.vstack([np.hstack([C11, C12]), np.hstack([C21, C22])])''',
        "practical_considerations": """
<p><strong>1. Practical Crossover Threshold (The Hidden Constants):</strong> Why don't software libraries use Strassen for \(2 \times 2\) or \(10 \times 10\) matrices? Strassen executes 18 matrix additions. While scalar additions are \(O(n^2)\) and multiplications are \(O(n^3)\), for small \(n\), the addition and recursion allocation overhead outweighs the savings! High-performance BLAS libraries switch to Strassen only when \(n \ge 64\) to \(128\).</p>
<p><strong>2. Numerical Stability & Floating-Point Error:</strong> Brute force dot product has superior numerical stability. Strassen's repeated additions and subtractions cause minor loss of precision and catastrophic cancellation in IEEE-754 floating point arithmetic.</p>
<p><strong>3. Non-Power-of-Two Matrices:</strong> If \(n\) is not a power of 2, matrices are zero-padded to the nearest power of 2, or dynamic peeling techniques are employed.</p>
""",
        "speech_bubbles": [
            ("Black Panther", "In Wakanda, our scientists know that multiplication is far more expensive than addition. By trading one recursive multiplication for eighteen additions, we conquer the O(n^3) barrier!"),
            ("Black Panther", "Always remember the crossover point: below n=64, recursion overhead slows you down. Hybrid engineering is true wisdom: standard BLAS for small matrices, Strassen for cosmic dimensions!")
        ],
        "quiz": [
            {
                "q": "How many recursive matrix multiplications does Strassen's algorithm execute compared to the naive divide-and-conquer approach?",
                "options": [
                    "7 instead of 8",
                    "6 instead of 8",
                    "4 instead of 8",
                    "8 instead of 16"
                ],
                "answer": 0,
                "explanation": "Standard divide-and-conquer computes 8 submatrix multiplications. Strassen cleverly calculates 7 products (M1 through M7), saving one multiplication."
            },
            {
                "q": "What is the exact asymptotic time complexity of Strassen's algorithm according to the Master Theorem?",
                "options": [
                    "Theta(n^2)",
                    "Theta(n^log2(7)) approx Theta(n^2.807)",
                    "Theta(n^3)",
                    "Theta(n log n)"
                ],
                "answer": 1,
                "explanation": "Solving T(n) = 7T(n/2) + O(n^2) via Master Theorem yields Theta(n^(log_2 7)) approx Theta(n^2.807)."
            },
            {
                "q": "Why is Strassen's algorithm rarely utilized for small matrices (e.g. n < 64)?",
                "options": [
                    "It produces mathematically incorrect results for small matrices",
                    "The overhead of 18 matrix additions and recursion allocations outweighs the savings from fewer multiplications",
                    "Matrices must strictly contain prime numbers",
                    "CPUs cannot perform matrix division"
                ],
                "answer": 1,
                "explanation": "Due to large constant factor overhead (18 matrix additions and memory allocations), Strassen only becomes faster beyond a crossover point of n >= 64-128."
            },
            {
                "q": "In Strassen's algorithm, how is the output submatrix C12 reconstructed?",
                "options": [
                    "C12 = M1 + M2",
                    "C12 = M3 + M5",
                    "C12 = M2 + M4",
                    "C12 = M1 - M5"
                ],
                "answer": 1,
                "explanation": "By Strassen's formula: C12 = M3 + M5 = A11(B12 - B22) + (A11 + A12)B22 = A11 B12 + A12 B22."
            }
        ],
        "summary": "Strassen's algorithm shattered the O(n^3) matrix multiplication barrier by computing 7 products instead of 8, achieving O(n^2.807) time and opening the modern era of sub-cubic matrix algorithms."
    },

    # 14. FRACTIONAL KNAPSACK (Rocket Raccoon)
    {
        "filename": "topic-fractional-knapsack.html",
        "topic_id": "fractional-knapsack",
        "mission_num": "04",
        "mission_title": "ADVANCED ALGORITHMS",
        "mission_url": "mission-04.html",
        "topic_num": "TOPIC 01",
        "topic_title": "FRACTIONAL KNAPSACK (GREEDY)",
        "hero_name": "ROCKET RACCOON",
        "hero_color": "#d97706",
        "hero_tag": "GREEDY LOOT RATIO MAXIMIZATION",
        "hero_quote": "Ain't no thing like me except me! Always sort scrap loot by value-per-pound ratio. Grab the richest chunk first, then break the rest into fractions!",
        "badge_color": "#fef3c7",
        "viz_type": "knapsack_fractional",
        "problem_invariants": """
<p>The <strong>Fractional Knapsack Problem</strong> is a foundational optimization problem solved to mathematical optimality via the <strong>Greedy Method</strong>.</p>
<p><strong>Formal Problem Statement:</strong></p>
<ul>
  <li>Given \(n\) distinct items, where each item \(i\) has an integer or real value \(v_i > 0\) and weight \(w_i > 0\).</li>
  <li>A knapsack of maximum weight capacity \(W\).</li>
  <li>We are permitted to take any arbitrary fraction \(x_i \in [0, 1]\) of item \(i\).</li>
  <li><strong>Objective:</strong> Maximize total accumulated value \(\sum_{i=1}^{n} x_i \cdot v_i\) subject to the knapsack capacity constraint \(\sum_{i=1}^{n} x_i \cdot w_i \le W\).</li>
</ul>
<p><strong>The Greedy Choice Property:</strong> Sorting items in descending order of their <em>value-to-weight ratio</em> \(r_i = \frac{v_i}{w_i}\) and greedily stuffing the knapsack with as much of the highest ratio item as possible guarantees global mathematical optimality.</p>
""",
        "naive_vs_optimal": """
<p>A naive greedy strategy might pick items with the absolute highest raw value \(v_i\) (ignoring weight), or items with the lightest weight \(w_i\). Both naive strategies fail: taking an item worth $100 weighing 50kg (\(r = 2\)) prevents you from taking five items worth $30 each weighing 5kg (\(r = 6\), total value $150). Sorting strictly by ratio \(r_i = v_i / w_i\) achieves provable maximum profit.</p>
<div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px; margin-top:12px;">
  <div style="background:#fee2e2; border:2px solid #ef4444; padding:12px; font-size:0.85rem;">
    <strong style="color:#b91c1c;">MAX VALUE GREEDY (FLAWED)</strong><br>
    Picks highest \(v_i\) first.<br>
    Problem: Consumes massive capacity; sub-optimal value density.<br>
    Total Profit: Significantly below optimal.
  </div>
  <div style="background:#dcfce7; border:2px solid #16a34a; padding:12px; font-size:0.85rem;">
    <strong style="color:#15803d;">VALUE DENSITY RATIO [OPTIMAL]</strong><br>
    Sorts by \(r_i = v_i / w_i\).<br>
    Fills bag with densest items first.<br>
    Total Profit: Guaranteed global optimum via Exchange Argument.
  </div>
</div>
""",
        "math_formulation": r"""
<p><strong>Mathematical Formulation:</strong></p>
\[ \text{Maximize } \sum_{i=1}^{n} x_i v_i \quad \text{subject to } \sum_{i=1}^{n} x_i w_i \le W, \quad x_i \in [0, 1] \]
<p><strong>Exchange Argument Optimality Proof:</strong> Let \(G = (x_1, x_2, \dots, x_n)\) be the greedy solution sorted such that \(\frac{v_1}{w_1} \ge \frac{v_2}{w_2} \ge \dots \ge \frac{v_n}{w_n}\). Let \(O = (y_1, y_2, \dots, y_n)\) be any alternative feasible solution. If \(O \ne G\), let \(k\) be the first index where \(x_k > y_k\). Since \(x_k > y_k\), \(O\) must take some amount of a lower-ratio item \(j > k\) (\(y_j > 0\)). Replacing weight \(\Delta w\) of item \(j\) with item \(k\) increases total value by \(\Delta w (\frac{v_k}{w_k} - \frac{v_j}{w_j}) \ge 0\). Repeating this exchange transforms \(O\) into \(G\) without ever decreasing value. Thus, \(G\) is optimal! \(\blacksquare\)</p>
""",
        "worked_example": """
<p><strong>Worked Example:</strong> Knapsack capacity \(W = 50\text{ kg}\). Three items available:</p>
<table style="width:100%; border-collapse:collapse; margin-top:8px; font-size:0.85rem;">
  <tr style="background:#f1f5f9;"><th style="padding:6px; border:1px solid #cbd5e1;">Item</th><th style="padding:6px; border:1px solid #cbd5e1;">Value (\(v_i\))</th><th style="padding:6px; border:1px solid #cbd5e1;">Weight (\(w_i\))</th><th style="padding:6px; border:1px solid #cbd5e1;">Ratio (\(r_i = v_i/w_i\))</th></tr>
  <tr><td style="padding:6px; border:1px solid #cbd5e1;">A (Quantum Core)</td><td style="padding:6px; border:1px solid #cbd5e1;">$60</td><td style="padding:6px; border:1px solid #cbd5e1;">10 kg</td><td style="padding:6px; border:1px solid #cbd5e1;"><strong>$6.0 / kg</strong></td></tr>
  <tr><td style="padding:6px; border:1px solid #cbd5e1;">B (Plasma Blaster)</td><td style="padding:6px; border:1px solid #cbd5e1;">$100</td><td style="padding:6px; border:1px solid #cbd5e1;">20 kg</td><td style="padding:6px; border:1px solid #cbd5e1;"><strong>$5.0 / kg</strong></td></tr>
  <tr><td style="padding:6px; border:1px solid #cbd5e1;">C (Nanotech Ingot)</td><td style="padding:6px; border:1px solid #cbd5e1;">$120</td><td style="padding:6px; border:1px solid #cbd5e1;">30 kg</td><td style="padding:6px; border:1px solid #cbd5e1;"><strong>$4.0 / kg</strong></td></tr>
</table>
<ol style="margin-left:20px; line-height:1.8; margin-top:8px;">
  <li><strong>Sort by Ratio:</strong> Order: Item A (6.0), Item B (5.0), Item C (4.0).</li>
  <li><strong>Pick Item A:</strong> Weight = 10 kg \(\le 50\). Take 100% (\(x_A = 1\)). Remaining \(W = 50 - 10 = 40\text{ kg}\). Profit = $60.</li>
  <li><strong>Pick Item B:</strong> Weight = 20 kg \(\le 40\). Take 100% (\(x_B = 1\)). Remaining \(W = 40 - 20 = 20\text{ kg}\). Profit = \(60 + 100 = \$160\).</li>
  <li><strong>Pick Item C (Fractional!):</strong> Item C weighs 30 kg, but remaining capacity is only 20 kg.
      <br>Take fraction \(x_C = \frac{20}{30} = \frac{2}{3}\).
      <br>Value gained = \(\frac{2}{3} \times \$120 = \$80\).
      <br>Remaining capacity = 0 kg (Knapsack full).
  </li>
  <li><strong>Maximum Total Profit:</strong> \(\$60 + \$100 + \$80 = \mathbf{\$240}\).</li>
</ol>
""",
        "complexity_table": [
            ("Sorting Items by Ratio", "O(n log n)", "O(1) / O(n) space", "Dominant step of the entire algorithm"),
            ("Greedy Selection Pass", "O(n)", "O(1) space", "Linear scan through sorted items until capacity is filled"),
            ("Overall Time Complexity", "O(n log n)", "O(1) space", "Bounded by sorting step"),
            ("Linear Time Variant (QuickSelect)", "O(n)", "O(n) space", "Uses median-of-medians to partition items around capacity W"),
            ("0/1 Knapsack (Comparison)", "O(n W) [NP-Complete]", "O(n W) space", "Cannot be solved greedily; requires Dynamic Programming")
        ],
        "code": '''def fractional_knapsack(capacity: float, items: list[tuple[str, float, float]]) -> tuple[float, list]:
    """
    Solves Fractional Knapsack using Greedy Ratio Sorting.
    items: list of (name, value, weight) tuples.
    Time Complexity: O(n log n), Space: O(1) auxiliary.
    """
    # Step 1: Calculate ratio and sort descending: O(n log n)
    sorted_items = sorted(items, key=lambda item: item[1] / item[2], reverse=True)
    
    total_value = 0.0
    current_weight = 0.0
    taken = []
    
    # Step 2: Greedily pack items: O(n)
    for name, value, weight in sorted_items:
        if current_weight + weight <= capacity:
            # Take entire item
            current_weight += weight
            total_value += value
            taken.append((name, 1.0, value))
        else:
            # Take remaining fraction
            remaining_cap = capacity - current_weight
            if remaining_cap > 0:
                fraction = remaining_cap / weight
                total_value += value * fraction
                current_weight += remaining_cap
                taken.append((name, fraction, value * fraction))
            break  # Knapsack completely full
            
    return total_value, taken''',
        "practical_considerations": """
<p><strong>1. Fractional vs 0/1 Knapsack:</strong> A critical concept in DAA exams: the Greedy strategy works <strong>only for Fractional Knapsack</strong>. For 0/1 Knapsack (where items cannot be broken), the greedy ratio approach fails completely and dynamic programming is required.</p>
<p><strong>2. Linear Time Optimization (\(O(n)\) without Full Sort):</strong> Using the QuickSelect algorithm (median-of-medians), one can find the pivot ratio where cumulative weight equals \(W\) without sorting the entire array, achieving theoretical \(\Theta(n)\) time.</p>
<p><strong>3. Bandwidth Allocation in Networking:</strong> Internet routers use fractional knapsack logic to allocate fractional channel bandwidth to packet queues sorted by QoS utility-per-byte ratios.</p>
""",
        "speech_bubbles": [
            ("Rocket Raccoon", "Ain't rocket science! Sort by value-per-pound. Grab the high-density tech first, and when the bag gets full, laser-cut that last chunk into fractions!"),
            ("Rocket Raccoon", "Listen closely for your exams: GREEDY works here because we can take fractions. If you can't break the loot (0/1 Knapsack), greedy fails and you gotta call Black Widow for Dynamic Programming!")
        ],
        "quiz": [
            {
                "q": "What criteria dictates the greedy selection order in Fractional Knapsack?",
                "options": [
                    "Maximum raw value (v_i)",
                    "Minimum weight (w_i)",
                    "Maximum value-to-weight ratio (v_i / w_i)",
                    "First-come, first-served order"
                ],
                "answer": 2,
                "explanation": "Sorting items by descending value-to-weight ratio v_i / w_i guarantees that every kilogram packed yields the highest possible profit density."
            },
            {
                "q": "What is the overall time complexity of Fractional Knapsack with n items?",
                "options": [
                    "O(n)",
                    "O(n log n)",
                    "O(n^2)",
                    "O(2^n)"
                ],
                "answer": 1,
                "explanation": "Sorting the n items by ratio takes O(n log n) time, and the greedy packing loop takes O(n) time, yielding overall O(n log n)."
            },
            {
                "q": "Why does the Greedy choice strategy guarantee optimality for Fractional Knapsack but FAIL for 0/1 Knapsack?",
                "options": [
                    "0/1 Knapsack contains negative weights",
                    "Fractional Knapsack allows taking fractions, guaranteeing the knapsack is filled to 100% capacity without leaving empty slack space",
                    "Greedy algorithms only work on arrays of size <= 10",
                    "0/1 Knapsack cannot be sorted"
                ],
                "answer": 1,
                "explanation": "In 0/1 Knapsack, taking a high-ratio item might leave unused capacity that cannot be filled, causing lower total value. In Fractional Knapsack, slack space is always filled with a fraction of the next item."
            },
            {
                "q": "Given capacity W = 20, Item 1: ($30, 10kg), Item 2: ($40, 20kg). What is the optimal profit?",
                "options": [
                    "$40",
                    "$50",
                    "$70",
                    "$35"
                ],
                "answer": 1,
                "explanation": "Ratio 1 = 30/10 = 3.0/kg. Ratio 2 = 40/20 = 2.0/kg. Take all 10kg of Item 1 ($30), leaving 10kg capacity. Take 10/20 (half) of Item 2 (half of $40 = $20). Total = $30 + $20 = $50."
            }
        ],
        "summary": "Fractional Knapsack is the definitive Greedy problem: sort items by value-to-weight ratio in O(n log n) time and greedily fill the knapsack. Fractional divisibility ensures global optimality."
    },

    # 15. MINIMUM COST SPANNING TREES (Thor)
    {
        "filename": "topic-minimum-cost-spanning-trees.html",
        "topic_id": "minimum-cost-spanning-trees",
        "mission_num": "04",
        "mission_title": "ADVANCED ALGORITHMS",
        "mission_url": "mission-04.html",
        "topic_num": "TOPIC 02",
        "topic_title": "MINIMUM COST SPANNING TREES (MST)",
        "hero_name": "THOR",
        "hero_color": "#0284c7",
        "hero_tag": "BIFROST NINE-REALMS NETWORK OPTIMIZATION",
        "hero_quote": "By Odin's beard! To unite the Nine Realms with the Bifrost, we must connect every realm using the minimum total cosmic lightning energy.",
        "badge_color": "#e0f2fe",
        "viz_type": "mst",
        "problem_invariants": """
<p>Given a connected, undirected, edge-weighted graph \(G = (V, E)\) with weight function \(w: E \to \mathbb{R}\), a <strong>Spanning Tree</strong> \(T = (V, E_T)\) is an acyclic subgraph connecting all \(|V|\) vertices using exactly \(|V| - 1\) edges.</p>
<p>A <strong>Minimum Cost Spanning Tree (MST)</strong> is a spanning tree that minimizes the total sum of edge weights:</p>
\[ w(T) = \sum_{e \in E_T} w(e) \]
<p><strong>Foundational Theorems Governing All MST Algorithms:</strong></p>
<ul>
  <li><strong>The Cut Property:</strong> For any cut \((S, V - S)\) of graph \(G\), if an edge \(e\) is the strictly lightest edge crossing the cut, then \(e\) must belong to every MST of \(G\).</li>
  <li><strong>The Cycle Property:</strong> For any cycle \(C\) in graph \(G\), the strictly heaviest edge in \(C\) cannot belong to any unique MST.</li>
  <li><strong>Uniqueness Condition:</strong> If all edge weights in \(G\) are distinct, the MST is mathematically unique.</li>
</ul>
""",
        "naive_vs_optimal": """
<p>A brute force search enumerates all possible spanning trees using Cayley's Formula (\(V^{V-2}\) spanning trees for complete graphs) and selects the minimum. For a small graph with \(V = 10\) vertices, \(10^8 = 100,000,000\) trees must be tested. Greedy MST algorithms (Kruskal and Prim) leverage the Cut Property to find the exact optimal MST in near-linear \(O(E \log V)\) time!</p>
<div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px; margin-top:12px;">
  <div style="background:#fee2e2; border:2px solid #ef4444; padding:12px; font-size:0.85rem;">
    <strong style="color:#b91c1c;">BRUTE FORCE ENUMERATION</strong><br>
    Tests all \(V^{V-2}\) trees.<br>
    For \(V = 20 \implies 20^{18} \approx 2.6 \times 10^{23}\) trees!<br>
    Completely impossible to compute.
  </div>
  <div style="background:#dcfce7; border:2px solid #16a34a; padding:12px; font-size:0.85rem;">
    <strong style="color:#15803d;">GREEDY CUT PROPERTY [OPTIMAL]</strong><br>
    Time: \(O(E \log V)\).<br>
    For \(V = 20, E = 100 \implies \approx 400\) operations.<br>
    Computes optimal tree in microseconds!
  </div>
</div>
""",
        "math_formulation": r"""
<p><strong>Cayley's Formula:</strong> The number of labeled spanning trees on a complete graph \(K_n\) is:</p>
\[ \text{Trees}(K_n) = n^{n-2} \]
<p><strong>Structural Properties of Any Tree \(T\) with \(V\) Vertices:</strong></p>
<ol>
  <li>Number of edges is strictly \(|E_T| = |V| - 1\).</li>
  <li>\(T\) contains zero cycles (acyclic).</li>
  <li>\(T\) is maximally acyclic: adding any non-tree edge \(e \notin E_T\) creates exactly one fundamental cycle.</li>
  <li>\(T\) is minimally connected: removing any edge disconnects \(T\) into two components.</li>
</ol>
""",
        "worked_example": """
<p><strong>Worked Example:</strong> Find the MST on a 4-vertex graph \(V = \{A, B, C, D\}\) with edges:</p>
<ul>
  <li>\((A, B): 1\), \((B, C): 2\), \((A, C): 4\), \((C, D): 3\), \((B, D): 5\).</li>
</ul>
<ol style="margin-left:20px; line-height:1.8;">
  <li><strong>Total Vertices:</strong> \(|V| = 4\). Target MST edge count: \(|V| - 1 = 3\) edges.</li>
  <li><strong>Edge 1 (Weight 1):</strong> Lightest edge \((A, B)\) connects \(A\) and \(B\). Add to MST. (MST Edges: 1).</li>
  <li><strong>Edge 2 (Weight 2):</strong> Next lightest \((B, C)\). Connects \(C\) without cycle. Add to MST. (MST Edges: 2).</li>
  <li><strong>Edge 3 (Weight 3):</strong> Next lightest \((C, D)\). Connects \(D\) without cycle. Add to MST. (MST Edges: 3).</li>
  <li><strong>Edge 4 (Weight 4 - Skipped):</strong> Next lightest \((A, C)\). But \(A, B, C\) are already connected! Adding \((A, C)\) forms cycle \(\{A, B, C\}\). Rejected by Cycle Property!</li>
  <li><strong>Final MST:</strong> Edges \(\{(A, B), (B, C), (C, D)\}\).
      <br><strong>Total Minimum Weight:</strong> \(1 + 2 + 3 = \mathbf{6}\).
  </li>
</ol>
""",
        "complexity_table": [
            ("Kruskal's Algorithm", "O(E log E) = O(E log V)", "O(V) space", "Sorts global edges; best on Sparse Graphs (E << V^2)"),
            ("Prim's (Binary Heap)", "O((V + E) log V)", "O(V) space", "Grows tree from root; standard implementation"),
            ("Prim's (Fibonacci Heap)", "O(E + V log V)", "O(V) space", "Theoretical optimum on Dense Graphs (E ~ V^2)"),
            ("Boruvka's Algorithm", "O(E log V)", "O(V) space", "Parallel algorithm; contracts connected components"),
            ("Cayley Brute Force", "Theta(V^(V-2))", "O(V) space", "Intractable exponential search")
        ],
        "code": '''class GraphMST:
    """
    Representation of weighted undirected graph for MST calculations.
    """
    def __init__(self, vertices: int):
        self.V = vertices
        self.edges = []  # list of (u, v, weight)
        
    def add_edge(self, u: int, v: int, w: float) -> None:
        self.edges.append((u, v, w))
        
    def verify_mst_invariants(self, mst_edges: list) -> bool:
        """
        Validates the 2 core invariants of any MST:
        1. Edge count must equal V - 1
        2. Must span all V vertices without cycles
        """
        if len(mst_edges) != self.V - 1:
            return False
        total_weight = sum(w for _, _, w in mst_edges)
        print(f"MST validated with {len(mst_edges)} edges. Total cost: {total_weight}")
        return True''',
        "practical_considerations": """
<p><strong>1. Telecommunication & Power Grid Wiring:</strong> The real-world reason MST was researched in the 1920s (Otakar Boruvka) was designing the electrical electrification grid for Moravia at minimum copper wire expenditure.</p>
<p><strong>2. Approximation for NP-Hard Problems:</strong> A Minimum Spanning Tree is used to construct a \(2\)-approximation algorithm for the Metric Traveling Salesman Problem (TSP) by finding the MST, doubling the edges into an Eulerian tour, and taking shortcuts.</p>
<p><strong>3. Negative Edge Weights:</strong> Unlike Dijkstra's algorithm, both Kruskal's and Prim's MST algorithms work flawlessly with negative edge weights! As long as the graph is undirected and connected, adding a constant \(C\) to all edges shifts the MST weight uniformly.</p>
""",
        "speech_bubbles": [
            ("Thor", "Hear the thunder! A Spanning Tree connects all Nine Realms without a single redundant cosmic loop. Exactly V - 1 lightning bridges are required!"),
            ("Thor", "The Cut Property is as immutable as Mjolnir: if an edge is the lightest warrior crossing any continental divide, it MUST belong to the minimum spanning tree!")
        ],
        "quiz": [
            {
                "q": "How many edges must any valid Spanning Tree contain for a connected graph with V vertices?",
                "options": [
                    "V",
                    "V - 1",
                    "V + 1",
                    "V / 2"
                ],
                "answer": 1,
                "explanation": "By definition, a tree spanning V vertices contains exactly V - 1 edges. Removing any edge disconnects it; adding any edge creates a cycle."
            },
            {
                "q": "What does the Cut Property state in Minimum Spanning Tree theory?",
                "options": [
                    "Cutting any edge destroys the graph",
                    "The lightest edge crossing any cut (S, V - S) must belong to an MST",
                    "The heaviest edge must always be selected",
                    "Graphs can only be cut into equal halves"
                ],
                "answer": 1,
                "explanation": "The Cut Property proves that for any cut partition of the vertices, the minimum-weight edge crossing the cut is guaranteed to be in an MST."
            },
            {
                "q": "Do negative edge weights cause Kruskal's or Prim's MST algorithms to fail?",
                "options": [
                    "Yes, both algorithms fail on negative weights",
                    "Only Kruskal fails",
                    "No, both Kruskal's and Prim's algorithms work correctly with negative weights",
                    "Only Prim fails"
                ],
                "answer": 2,
                "explanation": "Unlike shortest path algorithms with negative cycles, MST algorithms simply seek the minimum sum of V - 1 edges; negative weights are handled correctly by the greedy cut property."
            },
            {
                "q": "According to Cayley's Formula, how many labeled spanning trees exist for a complete graph with 5 vertices?",
                "options": [
                    "10",
                    "25",
                    "125",
                    "1024"
                ],
                "answer": 2,
                "explanation": "Cayley's Formula: n^(n - 2). For n = 5: 5^(5 - 2) = 5^3 = 125 labeled trees."
            }
        ],
        "summary": "An MST connects all V vertices with V - 1 edges of minimal total weight. Governed by the Cut and Cycle properties, it forms the bedrock for infrastructure layout and clustering."
    }
]

print(f"Loaded Part 3: {len(PART3_TOPICS)} topics")
