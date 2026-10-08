# ALGO-VENGERS: Earth's Mightiest Algorithms

> **Design and Analysis of Algorithms (DAA) — CIA Project**  
> An interactive light-themed pixelated Avengers command center learning platform.

---

## ⚡ Project Overview

**ALGO-VENGERS** bridges the thematic visual identity of the Avengers with the rigorous academic curriculum of **Design and Analysis of Algorithms (DAA)**.

- **Theme Identity:** Avengers Command Center × Chibi Pixel Game Art × Modern Academic DAA Platform
- **Total Suite:** **26 Self-Contained HTML Pages**
  - 1 Home Page: [`index.html`](file:///C:/Users/Babitha%20Ravindra/.gemini/antigravity/scratch/algo-vengers/index.html)
  - 1 S.H.I.E.L.D. Directory: [`missions.html`](file:///C:/Users/Babitha%20Ravindra/.gemini/antigravity/scratch/algo-vengers/missions.html)
  - 5 Mission Hubs: [`mission-01.html`](file:///C:/Users/Babitha%20Ravindra/.gemini/antigravity/scratch/algo-vengers/mission-01.html) through [`mission-05.html`](file:///C:/Users/Babitha%20Ravindra/.gemini/antigravity/scratch/algo-vengers/mission-05.html)
  - 19 Dedicated Topic Pages: [`topic-*.html`](file:///C:/Users/Babitha%20Ravindra/.gemini/antigravity/scratch/algo-vengers/)
- **Visual Style:** Light technical background (`#f8fafc`) with blueprint grid lines, crisp white cards, stepped pixel borders (`3px solid #0f172a`), and high-contrast typography.
- **Figures:** Chibi pixel-art sprites matching reference proportions with thick outlines.
- **Audio Synthesizer:** Pure Web Audio API gentle tones (sine bubble hover, tactile triangle clicks).
- **Custom Cursors:** Dynamic cursor follower morphing into hero-specific pixel icons on hover.
- **Zero External Dependencies:** CSS & JS are embedded directly inside every HTML file.

---

## 🗺️ Complete Mission & Topic Matrix (26 Pages)

```text
S.H.I.E.L.D. HQ (index.html)
   │
   └──► MISSIONS DIRECTORY (missions.html)
         │
         ├──► MISSION 01: FOUNDATIONS (mission-01.html)
         │     ├── Topic 01: Space Complexity (Ant-Man) [topic-space-complexity.html]
         │     ├── Topic 02: Time Complexity (Doctor Strange) [topic-time-complexity.html]
         │     └── Topic 03: Asymptotic Notations (Vision) [topic-asymptotic-notations.html]
         │
         ├──► MISSION 02: DATA STRUCTURES (mission-02.html)
         │     ├── Topic 01: Stacks (Captain America) [topic-stacks.html]
         │     ├── Topic 02: Queues (Falcon) [topic-queues.html]
         │     ├── Topic 03: Trees & BST (Groot) [topic-trees.html]
         │     ├── Topic 04: Dictionaries & Hash Tables (Iron Man) [topic-dictionaries.html]
         │     └── Topic 05: Sets & Disjoint Sets (Scarlet Witch) [topic-sets-and-disjoint-sets.html]
         │
         ├──► MISSION 03: SEARCH & SORT (mission-03.html)
         │     ├── Topic 01: Maximum & Minimum (Hawkeye) [topic-maximum-and-minimum.html]
         │     ├── Topic 02: Binary Search (Spider-Man) [topic-binary-search.html]
         │     ├── Topic 03: Merge Sort (War Machine) [topic-merge-sort.html]
         │     └── Topic 04: Quick Sort (Quicksilver) [topic-quick-sort.html]
         │
         ├──► MISSION 04: ADVANCED ALGORITHMS (mission-04.html)
         │     ├── Topic 01: Strassen's Matrix Mult. (Black Panther) [topic-strassens-matrix-multiplication.html]
         │     ├── Topic 02: Fractional Knapsack (Rocket Raccoon) [topic-fractional-knapsack.html]
         │     ├── Topic 03: Minimum Cost Spanning Trees (Thor) [topic-minimum-cost-spanning-trees.html]
         │     ├── Topic 04: Kruskal's & Prim's Algorithms (Wolverine) [topic-kruskals-and-prims.html]
         │     └── Topic 05: Dijkstra's Algorithm (Captain Marvel) [topic-dijkstras-algorithm.html]
         │
         └──► MISSION 05: OPTIMIZATION (mission-05.html)
               ├── Topic 01: Traveling Salesman Problem (Loki) [topic-traveling-salesman-problem.html]
               └── Topic 02: 0/1 Knapsack Problem (Black Widow) [topic-0-1-knapsack-problem.html]
```

---

## 🎨 Integrating Custom SVG Icons

You can add your own SVG files at any time! Drop them in the `assets/` directory:

```text
assets/
  ├── ironman.svg
  ├── captainamerica.svg
  ├── thor.svg
  ├── hulk.svg
  ├── blackwidow.svg
  ├── hawkeye.svg
  ├── spiderman.svg
  ├── antman.svg
  ├── doctorstrange.svg
  ├── vision.svg
  ├── falcon.svg
  ├── groot.svg
  ├── scarletwitch.svg
  ├── warmachine.svg
  ├── quicksilver.svg
  ├── blackpanther.svg
  ├── rocket.svg
  ├── wolverine.svg
  ├── captainmarvel.svg
  └── loki.svg
```

### Integration Methods
1. **Direct File Reference:** Load via `<img src="assets/ironman.svg">` or CSS `background-image`.
2. **Inline Vector SVG:** Embed directly into the HTML to keep files completely standalone and offline-ready.
3. **Cursor Integration:** Plug SVG code directly into `templates[heroKey]` inside the `<script>` cursor follower.

---

## 🚀 How to Run Locally

```bash
cd "C:\Users\Babitha Ravindra\.gemini\antigravity\scratch\algo-vengers"
python -m http.server 8000
```
Open **`http://localhost:8000`** or open [`index.html`](file:///C:/Users/Babitha%20Ravindra/.gemini/antigravity/scratch/algo-vengers/index.html) directly in any browser.
