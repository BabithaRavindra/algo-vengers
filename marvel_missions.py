# marvel_missions.py - 19 Coherent Marvel Mission Stories for DAA Topics
# Follows the sequence: STORY -> PROBLEM -> ALGORITHM -> INTERACTION -> RESULT -> COMPLEXITY

MISSIONS_DATA = {
    "space-complexity": {
        "mission_code": "OP-ANT-01",
        "mission_title": "OPERATION SUBATOMIC CONTAINMENT",
        "story_intro": "Hank Pym's regulator suit has entered the subatomic Quantum Realm. In this micro-dimension, suit RAM is strictly throttled to a finite hardware register limit. Scott Lang must reverse a critical coordinate array of quantum particles before temporal shear destroys the suit.",
        "problem_statement": "Reversing an array of size N using a naive algorithm allocates a secondary copy array, consuming O(N) auxiliary space. In subatomic registers, this triggers a catastrophic stack overflow.",
        "why_algorithm": "In-place two-pointer algorithm operates directly on the existing memory buffer using convergent indices (left and right), shrinking auxiliary memory to strictly O(1) constant space.",
        "objective": "Help Ant-Man swap particle coordinates in-place without exceeding the 100 KB suit RAM threshold.",
        "success_state": "Quantum array reversed! Suit RAM consumption held at O(1) constant space. Temporal shear averted!"
    },
    "time-complexity": {
        "mission_code": "OP-STRANGE-02",
        "mission_title": "THE 14,000,605 TIMELINES CRUCIBLE",
        "story_intro": "Dormammu's Dark Dimension is expanding through temporal fractures. Dr. Stephen Strange has projected consciousness into the Eye of Agamotto, calculating defense barriers across thousands of reality timelines. In every timeline, the total operational step count decides survival.",
        "problem_statement": "Measuring defense efficiency using clock milliseconds fluctuates wildly due to dimensional turbulence and CPU background interference. Strange needs hardware-independent mathematical step counting.",
        "why_algorithm": "Asymptotic Time Complexity counts primitive operational steps (comparisons, arithmetic steps) across best, average, and worst-case scenarios, bounding growth as N scales to infinity.",
        "objective": "Observe how elementary operations scale across different spell complexity classes as input size N grows.",
        "success_state": "Temporal pathways analyzed! Asymptotic upper guarantee locked in before dimensional collapse!"
    },
    "asymptotic-notations": {
        "mission_code": "OP-VISION-03",
        "mission_title": "MIND STONE ASYMPTOTIC SYNTHESIS",
        "story_intro": "Ultron has unleashed polymorphic cyber-tendrils whose execution speed fluctuates dynamically. Vision must calibrate the Avengers perimeter firewall by establishing formal mathematical boundaries on threat growth rates.",
        "problem_statement": "Loose boundaries leave blind spots. Stating an algorithm is O(n^3) when it executes in linear time gives zero practical certitude.",
        "why_algorithm": "Vision applies Big-O (upper ceiling), Big-Omega (lower floor), and Big-Theta (tight sandwich bound). When c1*g(n) <= f(n) <= c2*g(n), mathematical certitude is achieved.",
        "objective": "Adjust constants c and n0 to mathematically verify that threat growth is securely bounded.",
        "success_state": "Mind Stone equilibrium achieved! Growth rate strictly bounded by Big-Theta limits!"
    },
    "stacks": {
        "mission_code": "OP-CAP-04",
        "mission_title": "VIBRANIUM SHIELD DEFENSE SILO",
        "story_intro": "Hydra shock troops are bombarding the Brooklyn command bunker. Tactical vibranium energy shields are stored inside a vertical pneumatic launch silo with only ONE top access hatch. Shields must be deployed and retrieved with absolute military discipline.",
        "problem_statement": "Accessing items from the bottom or middle of a pneumatic silo causes mechanical jamming. The system must operate under strict Last-In, First-Out (LIFO) order.",
        "why_algorithm": "The Stack data structure provides O(1) time push, pop, and peek operations exclusively at the TOP pointer, guaranteeing instantaneous access with zero element shifting.",
        "objective": "Help Captain America push incoming shields into the silo, pop the active shield for combat, and inspect the top shield without disturbing the rack.",
        "success_state": "Silo discipline maintained! Shields deployed in exact LIFO sequence with O(1) constant speed!"
    },
    "queues": {
        "mission_code": "OP-HULK-05",
        "mission_title": "GAMMA CONVOY FIFO EVACUATION",
        "story_intro": "A Chitauri orbital bombardment has compromised the Manhattan bridge. Hulk is stationed at the Stark tunnel terminal to guide civilian evacuation transports. To prevent civil chaos and gridlock, transports must be evacuated in the exact order they arrive: First-In, First-Out (FIFO).",
        "problem_statement": "In a linear array queue, dequeued front slots become dead, unusable memory, causing False Overflow even when capacity remains. Hulk cannot allow memory bottlenecks during evacuation!",
        "why_algorithm": "A Circular Queue wraps rear and front indices using modulo arithmetic (idx + 1) % N, recycling freed slots endlessly in O(1) enqueue and dequeue time.",
        "objective": "Help Hulk enqueue arriving transport chariots at the REAR and dequeue evacuated transports from the FRONT.",
        "success_state": "All transports evacuated safely! Queue pipeline cycled with zero False Overflow deadlocks!"
    },
    "trees": {
        "mission_code": "OP-GROOT-06",
        "mission_title": "THE SACRED YGGDRASIL DATA CANOPY",
        "story_intro": "The High Evolutionary has scrambled the galactic botanical genetic archive. Groot must restore the ancestral species records into the Yggdrasil Tree. The records must allow rapid logarithmic searching and sequential ordered retrieval.",
        "problem_statement": "Linear lists require O(N) search time across millions of alien plant species. An unsorted hierarchy leads to disorientation.",
        "why_algorithm": "A Binary Search Tree (BST) enforces the ordering invariant: keys smaller than a node branch Left, keys greater branch Right. In-Order traversal extracts records in strictly ascending sorted order.",
        "objective": "Guide Groot to insert species keys into the BST by branching left and right, then run In-Order traversal.",
        "success_state": "Yggdrasil archive restored! In-order traversal produced perfectly sorted botanical taxonomy!"
    },
    "dictionaries": {
        "mission_code": "OP-IRON-07",
        "mission_title": "JARVIS ARC REACTOR TARGETING CACHE",
        "story_intro": "Ultron sentries are swarming the Stark Tower airspace. Tony Stark's targeting HUD needs instantaneous, sub-millisecond retrieval of enemy armor weakness coordinates. Scanning an array in O(n) time is far too slow during supersonic combat.",
        "problem_statement": "Searching unsorted records requires O(n) scans; sorted arrays take O(log n) search and O(n) insertion. Tony cannot wait for arrays to shift while under heavy fire.",
        "why_algorithm": "A Hash Table uses an arithmetic hash function h(k) = k % size to map keys directly to memory bucket addresses in O(1) average time, resolving collisions via linear probing.",
        "objective": "Help Iron Man compute hash bucket indices, insert threat coordinates, and probe past collisions in O(1) time.",
        "success_state": "All Ultron targets acquired! Hash table lookups completed in O(1) constant time!"
    },
    "sets-and-disjoint-sets": {
        "mission_code": "OP-WANDA-08",
        "mission_title": "MULTIVERSE NEXUS REALM PARTITION",
        "story_intro": "The Darkhold has shattered reality into isolated timeline pockets across the multiverse. Wanda Maximoff must monitor which alternate realities are connected and merge them into unified nexus realms without creating paradox cycles.",
        "problem_statement": "Testing whether two dimensions are already connected using naive graph searches takes O(V + E) time per query. Unifying large timelines causes tall tree chains that degrade to O(N).",
        "why_algorithm": "Disjoint-Set Union (Union-Find) with Union by Rank and Path Compression flattens component trees during every Find query, driving amortized time down to near-constant O(alpha(N)).",
        "objective": "Help Scarlet Witch find root nexus representatives and union timelines without forming temporal paradox loops.",
        "success_state": "Multiverse stabilized! Connected components resolved in near-constant inverse Ackermann time!"
    },
    "maximum-and-minimum": {
        "mission_code": "OP-HAWKEYE-09",
        "mission_title": "CHITAURI LEVIATHAN EXTREMES TOURNAMENT",
        "story_intro": "A wave of Chitauri combat drones is descending on Central Park. Hawkeye has a limited quiver of high-yield acoustic arrows and must identify both the weakest scout drone (minimum armor) and the flagship leviathan (maximum threat) simultaneously.",
        "problem_statement": "A naive linear scan compares each element against both min and max, requiring 2n - 2 comparisons. Clint cannot afford to waste arrows on redundant checks.",
        "why_algorithm": "The Divide-and-Conquer Tournament Method pairs elements up into brackets: the winners compete for Maximum and losers compete for Minimum, slashing comparisons to exactly 3n/2 - 2.",
        "objective": "Help Hawkeye pair targets into tournament matches and identify both extremes in optimal 1.5n comparisons.",
        "success_state": "Both extremes locked in! Armada neutralized with 25% fewer targeting comparisons!"
    },
    "binary-search": {
        "mission_code": "OP-SPIDEY-10",
        "mission_title": "GREEN GOBLIN GLIDER FREQUENCY TRAP",
        "story_intro": "Norman Osborn's gliders are broadcasting interference across a sorted radio frequency spectrum of 1,000,000 channels. Peter Parker must pinpoint Goblin's exact broadcast channel before bombs detonate across Times Square.",
        "problem_statement": "Linear scan across one million channels takes up to 1,000,000 checks (too slow!). But the radio spectrum is strictly SORTED.",
        "why_algorithm": "Binary Search probes the midpoint MID. If the target is greater, the entire lower half is eliminated; if smaller, the upper half is discarded. The search space shrinks by 50% on every probe, finding any channel in <= 20 steps.",
        "objective": "Guide Spider-Man to calculate MID, evaluate comparisons, shoot web lines over eliminated intervals, and trap Goblin's frequency.",
        "success_state": "Goblin glider frequency trapped! Search space halved on every web zip in O(log n) time!"
    },
    "merge-sort": {
        "mission_code": "OP-WARMACHINE-11",
        "mission_title": "ARMORED BATTALION TELEMETRY MERGE",
        "story_intro": "Col. James Rhodes is coordinating dispersed armored defense squads along the eastern seaboard. Sensor telemetry feeds have arrived in scrambled, fragmented batches. War Machine must sort all battalion coordinates with guaranteed, predictable runtime.",
        "problem_statement": "Unstable sorting algorithms like QuickSort can degrade to O(N^2) under adversarial attacks. In military logistics, worst-case guarantees are required.",
        "why_algorithm": "Merge Sort recursively divides the array into halves and merges sorted subarrays in linear time, guaranteeing ironclad Theta(n log n) runtime under all input conditions with algorithmic stability.",
        "objective": "Help War Machine split the scrambled array into sub-battalions and execute the two-pointer merge sweep.",
        "success_state": "Battalion telemetry sorted! Guaranteed Theta(n log n) precision maintained under heavy fire!"
    },
    "quick-sort": {
        "mission_code": "OP-QUICKSILVER-12",
        "mission_title": "SUPERSONIC RAILGUN PROJECTILE SORT",
        "story_intro": "Ultron infiltrators have scrambled the magnetic projectile magazine of the Avengers defense railgun. Quicksilver must sort the ammunition canisters in ascending caliber order before the railgun capacitor drains.",
        "problem_statement": "Allocating secondary memory buffers for sorting wastes valuable milliseconds. The canisters must be sorted in-place at supersonic speed.",
        "why_algorithm": "QuickSort chooses a pivot element, partitions the array in-place so all smaller elements move left and larger move right, and recurses. In-place partitioning maximizes CPU cache line hits.",
        "objective": "Guide Quicksilver to lock onto a pivot, scan the array, swap elements in-place at mach speed, and lock the pivot into its final position.",
        "success_state": "Railgun magazine sorted in-place! In-place swaps completed at supersonic speed!"
    },
    "strassens-matrix-multiplication": {
        "mission_code": "OP-PANTHER-13",
        "mission_title": "WAKANDAN VIBRANIUM SHIELD MATRIX",
        "story_intro": "Shuri's planetary defense shield mesh requires real-time block matrix transformations to deflect Thanos's orbital kinetic bombardments. The textbook brute force matrix multiplication takes O(n^3) scalar multiplications—too slow to recalculate between kinetic pulses.",
        "problem_statement": "Standard matrix multiplication performs 8 recursive multiplications for 2x2 block quadrants, hitting the cubic O(n^3) barrier. Multiplying large matrices overwhelms the Vibranium power grid.",
        "why_algorithm": "Volker Strassen's algorithm computes 7 clever products (M1 through M7) and 18 matrix additions, breaking the cubic barrier down to O(n^log2(7)) = O(n^2.807) operations.",
        "objective": "Help Black Panther compute the 7 Strassen products and reconstruct the output matrix C before the next kinetic wave strikes.",
        "success_state": "Vibranium grid updated! Cubic barrier conquered with only 7 multiplications!"
    },
    "fractional-knapsack": {
        "mission_code": "OP-ROCKET-14",
        "mission_title": "KNOWHERE SCRAP SALVAGE HEIST",
        "story_intro": "The Collector's vault on Knowhere is collapsing! Rocket Raccoon has an escape cargo harness with a strict weight capacity W. The vault contains high-tech alien components with varying weights and black-market values that can be laser-sliced into fractional pieces.",
        "problem_statement": "Taking items blindly based on high raw value fills the pack with heavy junk. Rocket needs maximum credits per pound.",
        "why_algorithm": "The Greedy Method sorts items by value-to-weight ratio (v/w). Packing 100% of the densest items and cutting the final item into a fraction guarantees global mathematical optimality.",
        "objective": "Help Rocket sort scrap items by profit ratio, pack whole items, and laser-slice the final item to fill capacity W to 100%.",
        "success_state": "Cargo harness packed to 100% capacity! Maximum credit profit achieved via greedy ratio sorting!"
    },
    "minimum-cost-spanning-trees": {
        "mission_code": "OP-THOR-15",
        "mission_title": "RESTORING THE NINE REALMS BIFROST GRID",
        "story_intro": "Hela's dark magic has shattered the cosmic rainbow bridges connecting Asgard, Midgard, Vanaheim, and the outer realms. Thor must reconnect all V realms using exactly V - 1 Bifrost lightning bridges with minimum total cosmic energy expenditure.",
        "problem_statement": "Brute-force checking all V^(V-2) spanning trees is computationally impossible. Redundant cosmic bridges create destructive feedback cycles.",
        "why_algorithm": "The Cut Property dictates that the lightest edge crossing any partition must belong to the Minimum Spanning Tree. Selecting V - 1 lightest acyclic edges minimizes total network cost.",
        "objective": "Help Thor examine planetary bridges, channel Mjolnir lightning along lightest edges, and reject cycle-forming bridges.",
        "success_state": "All Nine Realms connected! Exactly V - 1 Bifrost bridges activated with minimal lightning energy!"
    },
    "kruskals-and-prims": {
        "mission_code": "OP-WOLVERINE-16",
        "mission_title": "WEAPON X ADAMANTIUM PIPELINE NETWORK",
        "story_intro": "Col. Stryker has established underground Weapon X research facilities connected by subterranean pipelines. Logan must dismantle the network using two distinct adamantium cutting strategies: Kruskal's global claw slice vs. Prim's base expansion.",
        "problem_statement": "Sparse wilderness pipelines require global edge sorting; dense urban facility hubs have too many edges to sort efficiently.",
        "why_algorithm": "Kruskal's algorithm sorts all edges globally and uses Union-Find to avoid cycles (best for sparse graphs). Prim's algorithm grows a single tree outward from a starting root using a priority queue (best for dense graphs).",
        "objective": "Guide Wolverine through Kruskal's edge-centric forest merging and Prim's vertex-centric growing tree.",
        "success_state": "Weapon X network mapped and dismantled! Both Kruskal and Prim produced the optimal MST!"
    },
    "dijkstras-algorithm": {
        "mission_code": "OP-MARVEL-17",
        "mission_title": "KREE ARMADA RELAY INTERCEPTION",
        "story_intro": "Supreme Intelligence has dispatched Kree war cruisers across a network of interstellar jumpgates. Carol Danvers must compute the shortest flight path from Earth to Hala through non-negative hyperspace coordinates before the Kree armada launches.",
        "problem_statement": "Exploring every possible interstellar path takes exponential time. Negative cosmic anomalies would break greedy assumptions.",
        "why_algorithm": "Dijkstra's Algorithm maintains a tentative distance table and priority queue. It greedily finalizes the closest unvisited star system and relaxes all outgoing jumpgates in O((V + E) log V) time.",
        "objective": "Help Captain Marvel channel her photon beam: extract minimum tentative jumpgates, finalize star systems, and relax outgoing routes.",
        "success_state": "Shortest cosmic route locked! Captain Marvel intercepted the Kree fleet in minimal hyperspace jumps!"
    },
    "traveling-salesman-problem": {
        "mission_code": "OP-LOKI-18",
        "mission_title": "THE MULTIVERSE CONQUEST GRAND TOUR",
        "story_intro": "Loki has acquired the Tesseract and intends to establish glorious dominion over 5 planetary capitals. He must depart from Asgard, visit every capital exactly once, and return to Asgard while expending minimum Tesseract energy.",
        "problem_statement": "Finding the minimum Hamiltonian cycle across N cities suffers from factorial explosion: (n - 1)! / 2 tours. For even 20 cities, brute force takes billions of years.",
        "why_algorithm": "The Held-Karp Dynamic Programming algorithm uses subset bitmask memoization g(i, S), reducing time from O(n!) to O(n^2 * 2^n), solving the problem in seconds.",
        "objective": "Help Loki evaluate tour legs, avoid redundant permutations with bitmasks, and lock in the minimal Hamiltonian cycle.",
        "success_state": "Glorious purpose fulfilled! Minimal Hamiltonian round-trip cycle mapped without factorial explosion!"
    },
    "0-1-knapsack-problem": {
        "mission_code": "OP-WIDOW-19",
        "mission_title": "RED ROOM COVERT EXTRACTION",
        "story_intro": "Natasha Romanoff has infiltrated Gen. Dreykov's fortified Red Room mainframe. Her extraction harness has a strict weight limit W. The server rack holds encrypted intelligence drives with distinct values and weights that CANNOT be fragmented.",
        "problem_statement": "Because items cannot be broken into fractions, the Greedy ratio method fails. Brute force recursion evaluates 2^N binary combinations, which is impossible during an alarm countdown.",
        "why_algorithm": "Dynamic Programming uses the Bellman recurrence DP[i][w] = max(DP[i-1][w], DP[i-1][w - w_i] + v_i) to evaluate binary take-or-leave choices in O(N * W) pseudo-polynomial time.",
        "objective": "Help Black Widow populate the 2D DP table cell by cell and backtrack to recover the exact binary drive payload.",
        "success_state": "Red Room mainframe extracted! Maximum intelligence value secured within weight limit W!"
    }
}
