
# 16. WOLVERINE: Adamantium Claw Slicing (Kruskal's & Prim's)
SIMULATIONS["kruskal_prim"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #eab308;">MISSION: WOLVERINE KRUSKAL VS PRIM CLAW SLICER</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Kruskal sorts all edges and checks cycles via Disjoint Sets; Prim grows a connected tree from a vertex!</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #facc15; padding: 6px 10px; border: 1px solid #475569;">
      MODE: <span id="wolv-mode">KRUSKAL'S (E log E)</span>
    </div>
  </div>

  <!-- Mode Selector Bar -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; gap: 8px;">
      <button class="pixel-btn pixel-btn-primary" id="wolv-btn-mode-k">MODE: KRUSKAL</button>
      <button class="pixel-btn pixel-btn-secondary" id="wolv-btn-mode-p">MODE: PRIM</button>
    </div>
    <div style="font-size: 0.75rem; color: #475569; font-weight: 600;">
      Edges Added: <span id="wolv-edge-count" style="color: #eab308; font-weight: bold;">0 / 3</span>
    </div>
  </div>

  <!-- Animated Arena Stage -->
  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 200px;">
    <!-- Wolverine Actor -->
    <div id="wolv-actor" style="position: absolute; top: 12px; left: 20px; transition: all 0.4s ease; z-index: 10;">
      <img src="assets/wolverine.png" style="width: 48px; height: 56px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 0 10px rgba(234,179,8,0.8));">
    </div>

    <!-- Graph Visual -->
    <div style="display: flex; gap: 12px; justify-content: space-around; margin-top: 55px; align-items: center;" id="wolv-edges-list">
      <div id="wedge-1" style="background: #1e293b; border: 2px solid #475569; padding: 10px; border-radius: 4px; color: #fff; font-family: var(--font-pixel); font-size: 0.6rem; text-align: center;">EDGE (1-2)<br>WT: 1</div>
      <div id="wedge-2" style="background: #1e293b; border: 2px solid #475569; padding: 10px; border-radius: 4px; color: #fff; font-family: var(--font-pixel); font-size: 0.6rem; text-align: center;">EDGE (2-3)<br>WT: 2</div>
      <div id="wedge-3" style="background: #1e293b; border: 2px solid #475569; padding: 10px; border-radius: 4px; color: #fff; font-family: var(--font-pixel); font-size: 0.6rem; text-align: center;">EDGE (3-4)<br>WT: 3</div>
      <div id="wedge-4" style="background: #1e293b; border: 2px solid #475569; padding: 10px; border-radius: 4px; color: #fff; font-family: var(--font-pixel); font-size: 0.6rem; text-align: center; opacity: 0.5;">EDGE (1-4)<br>WT: 8 (CYCLE)</div>
    </div>
  </div>

  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; font-size: 0.88rem; min-height: 48px; display: flex; align-items: center;" id="wolv-dialogue">
    💬 <strong>Wolverine:</strong> "Adamantium claws ready. Kruskal sorts all edges globally; Prim cuts edges crossing the active cut!"
  </div>

  <div class="viz-controls" style="display: flex; gap: 10px; flex-wrap: wrap;">
    <button class="pixel-btn pixel-btn-primary" id="wolv-btn-step">⚔️ CLAW SLICE NEXT EDGE</button>
    <button class="pixel-btn pixel-btn-secondary" id="wolv-btn-auto">▶ AUTO-BUILD MST</button>
    <button class="pixel-btn pixel-btn-secondary" id="wolv-btn-reset">↺ RESET GRAPH</button>
  </div>
</div>
""",
    "script": """
const wolvDiag = document.getElementById('wolv-dialogue');
const wolvMode = document.getElementById('wolv-mode');
const wolvActor = document.getElementById('wolv-actor');
const wolvCount = document.getElementById('wolv-edge-count');

let wStep = 0;
let isPrim = false;

function stepWolvEdge() {
  wStep++;
  if (wStep === 1) {
    document.getElementById('wedge-1').style.background = '#15803d';
    document.getElementById('wedge-1').style.borderColor = '#22c55e';
    wolvActor.style.left = '20%';
    wolvCount.textContent = '1 / 3';
    wolvDiag.innerHTML = '⚔️ <strong>Wolverine:</strong> "Edge (1-2) with weight 1 added to MST! No cycle formed!"';
  } else if (wStep === 2) {
    document.getElementById('wedge-2').style.background = '#15803d';
    document.getElementById('wedge-2').style.borderColor = '#22c55e';
    wolvActor.style.left = '45%';
    wolvCount.textContent = '2 / 3';
    wolvDiag.innerHTML = '⚔️ <strong>Wolverine:</strong> "Edge (2-3) with weight 2 sliced into MST! Both sets merged!"';
  } else if (wStep === 3) {
    document.getElementById('wedge-3').style.background = '#15803d';
    document.getElementById('wedge-3').style.borderColor = '#22c55e';
    wolvActor.style.left = '70%';
    wolvCount.textContent = '3 / 3';
    wolvDiag.innerHTML = '🏆 <strong>Wolverine:</strong> "MST complete with 3 edges! Edge (1-4) with weight 8 is rejected because both ends are already connected (cycle prevention)!"';
  }
}

document.getElementById('wolv-btn-step')?.addEventListener('click', () => { retroAudio.playClick(); stepWolvEdge(); });
document.getElementById('wolv-btn-auto')?.addEventListener('click', () => {
  retroAudio.playClick();
  while(wStep < 3) stepWolvEdge();
});
document.getElementById('wolv-btn-mode-k')?.addEventListener('click', () => {
  retroAudio.playClick();
  isPrim = false;
  wolvMode.textContent = "KRUSKAL'S (E log E)";
  wolvDiag.innerHTML = '💬 <strong>Wolverine:</strong> "Switched to Kruskal: Global edge sort + Disjoint Set cycle detection."';
});
document.getElementById('wolv-btn-mode-p')?.addEventListener('click', () => {
  retroAudio.playClick();
  isPrim = true;
  wolvMode.textContent = "PRIM'S (V² or E + V log V)";
  wolvDiag.innerHTML = '💬 <strong>Wolverine:</strong> "Switched to Prim: Grow spanning tree outward from a seed vertex."';
});
document.getElementById('wolv-btn-reset')?.addEventListener('click', () => {
  retroAudio.playClick();
  wStep = 0;
  wolvCount.textContent = '0 / 3';
  for(let i=1; i<=3; i++) {
    const el = document.getElementById(`wedge-${i}`);
    if (el) { el.style.background = '#1e293b'; el.style.borderColor = '#475569'; }
  }
  wolvActor.style.left = '20px';
  wolvDiag.innerHTML = '💬 <strong>Wolverine:</strong> "Ready to slice edges."';
});
"""
}

# 17. CAPTAIN MARVEL: Interstellar Warp Navigation (Dijkstra's)
SIMULATIONS["dijkstra"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #dc2626;">MISSION: CAPTAIN MARVEL HYPERSPACE WARP DIJKSTRA</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Fly photon speed across cosmic jump nodes. Priority queue relaxes distances to find shortest path!</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #facc15; padding: 6px 10px; border: 1px solid #475569;">
      WARP PATH: S ➔ A ➔ D
    </div>
  </div>

  <!-- Custom Destination Input -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; align-items: center; gap: 8px;">
      <label style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a;">SOURCE: S</label>
      <span style="color:#475569; font-size:0.75rem; font-weight:bold;">➔ DESTINATION: D (WARP JUMP)</span>
    </div>
    <button class="pixel-btn pixel-btn-primary" id="cm-btn-fly" style="padding: 6px 12px; font-size: 0.6rem;">⚡ RELAX EDGES & FLY</button>
  </div>

  <!-- Animated Arena Stage -->
  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 220px;">
    <!-- Carol Danvers Actor Sprite -->
    <div id="cm-actor" style="position: absolute; top: 75px; left: 40px; transition: all 0.6s cubic-bezier(0.34, 1.56, 0.64, 1); z-index: 10;">
      <img src="assets/captainmarvel.png" style="width: 50px; height: 56px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 0 14px rgba(250,204,21,0.9));">
    </div>

    <!-- Planetary Nodes SVG -->
    <svg viewBox="0 0 420 180" style="width: 100%; height: 180px; display: block; margin: 0 auto;">
      <line id="cm-line-sa" x1="60" y1="90" x2="160" y2="40" stroke="#475569" stroke-width="2"/>
      <text x="100" y="55" fill="#94a3b8" font-size="11" font-family="monospace">4</text>

      <line id="cm-line-sb" x1="60" y1="90" x2="160" y2="140" stroke="#475569" stroke-width="2"/>
      <text x="100" y="130" fill="#94a3b8" font-size="11" font-family="monospace">7</text>

      <line id="cm-line-ab" x1="160" y1="40" x2="160" y2="140" stroke="#475569" stroke-width="2"/>
      <text x="170" y="95" fill="#94a3b8" font-size="11" font-family="monospace">1</text>

      <line id="cm-line-ad" x1="160" y1="40" x2="320" y2="90" stroke="#475569" stroke-width="2"/>
      <text x="240" y="55" fill="#94a3b8" font-size="11" font-family="monospace">3</text>

      <line id="cm-line-bd" x1="160" y1="140" x2="320" y2="90" stroke="#475569" stroke-width="2"/>
      <text x="240" y="130" fill="#94a3b8" font-size="11" font-family="monospace">6</text>

      <!-- Nodes -->
      <circle id="cmn-s" cx="60" cy="90" r="18" fill="#1e293b" stroke="#facc15" stroke-width="2"/>
      <text x="60" y="94" fill="#fff" font-size="11" font-weight="bold" font-family="monospace" text-anchor="middle">S[0]</text>

      <circle id="cmn-a" cx="160" cy="40" r="18" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
      <text x="160" y="44" fill="#fff" font-size="11" font-weight="bold" font-family="monospace" text-anchor="middle">A[∞]</text>

      <circle id="cmn-b" cx="160" cy="140" r="18" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
      <text x="160" y="144" fill="#fff" font-size="11" font-weight="bold" font-family="monospace" text-anchor="middle">B[∞]</text>

      <circle id="cmn-d" cx="320" cy="90" r="18" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
      <text x="320" y="94" fill="#fff" font-size="11" font-weight="bold" font-family="monospace" text-anchor="middle">D[∞]</text>
    </svg>
  </div>

  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; font-size: 0.88rem; min-height: 48px; display: flex; align-items: center;" id="cm-dialogue">
    💬 <strong>Captain Marvel:</strong> "Higher, further, faster! Priority queue selects closest unvisited node, relaxing neighbor distances in O((V + E) log V)!"
  </div>

  <div class="viz-controls" style="display: flex; gap: 10px; flex-wrap: wrap;">
    <button class="pixel-btn pixel-btn-primary" id="cm-btn-auto">▶ AUTO-NAVIGATE SHORTEST PATH</button>
    <button class="pixel-btn pixel-btn-secondary" id="cm-btn-reset">↺ RESET GALAXY</button>
  </div>
</div>
""",
    "script": """
const cmActor = document.getElementById('cm-actor');
const cmDiag = document.getElementById('cm-dialogue');

let cmStep = 0;

function stepDijkstra() {
  cmStep++;
  if (cmStep === 1) {
    document.getElementById('cm-line-sa').setAttribute('stroke', '#facc15');
    document.getElementById('cm-line-sa').setAttribute('stroke-width', '4');
    document.getElementById('cmn-a').nextElementSibling.textContent = 'A[4]';
    cmActor.style.top = '25px';
    cmActor.style.left = '140px';
    cmDiag.innerHTML = '⚡ <strong>Captain Marvel:</strong> "Relaxed Node A: Dist(S, A) = 0 + 4 = 4! Node A is now minimal in Priority Queue!"';
  } else if (cmStep === 2) {
    document.getElementById('cm-line-ad').setAttribute('stroke', '#facc15');
    document.getElementById('cm-line-ad').setAttribute('stroke-width', '4');
    document.getElementById('cmn-d').nextElementSibling.textContent = 'D[7]';
    cmActor.style.top = '75px';
    cmActor.style.left = '300px';
    cmDiag.innerHTML = '🏆 <strong>Captain Marvel:</strong> "Destination D reached! Shortest Path: S ➔ A ➔ D with total warp cost = 4 + 3 = 7!"';
  }
}

document.getElementById('cm-btn-fly')?.addEventListener('click', () => { retroAudio.playClick(); stepDijkstra(); });
document.getElementById('cm-btn-auto')?.addEventListener('click', () => {
  retroAudio.playClick();
  stepDijkstra();
  setTimeout(() => stepDijkstra(), 700);
});
document.getElementById('cm-btn-reset')?.addEventListener('click', () => {
  retroAudio.playClick();
  cmStep = 0;
  cmActor.style.top = '75px';
  cmActor.style.left = '40px';
  document.getElementById('cm-line-sa').setAttribute('stroke', '#475569');
  document.getElementById('cm-line-sa').setAttribute('stroke-width', '2');
  document.getElementById('cm-line-ad').setAttribute('stroke', '#475569');
  document.getElementById('cm-line-ad').setAttribute('stroke-width', '2');
  document.getElementById('cmn-a').nextElementSibling.textContent = 'A[∞]';
  document.getElementById('cmn-d').nextElementSibling.textContent = 'D[∞]';
  cmDiag.innerHTML = '💬 <strong>Captain Marvel:</strong> "Hyperspace jump coordinates reset."';
});
"""
}

# 18. LOKI: Multiverse Traveling Salesman Tour (TSP)
SIMULATIONS["tsp"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #15803d;">MISSION: LOKI MULTIVERSE TSP PRUNING</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Visit all 4 Asgardian realms exactly once and return home. Prune sub-paths that exceed best bound!</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #4ade80; padding: 6px 10px; border: 1px solid #475569;">
      OPTIMAL TOUR: 35 REALM UNITS
    </div>
  </div>

  <!-- Custom Realm Count / Path Bar -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="font-size: 0.75rem; color: #0f172a; font-weight: bold;">
      REALMS: [1: ASGARD, 2: MIDGARD, 3: JOTUNHEIM, 4: VANAHEIM]
    </div>
    <button class="pixel-btn pixel-btn-primary" id="loki-btn-prune" style="padding: 6px 12px; font-size: 0.6rem;">👑 BRANCH & BOUND PRUNE</button>
  </div>

  <!-- Animated Arena Stage -->
  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 220px;">
    <!-- Loki Actor Sprite -->
    <div id="loki-actor" style="position: absolute; top: 15px; left: 60px; transition: all 0.5s ease-in-out; z-index: 10;">
      <img src="assets/loki.png" style="width: 48px; height: 58px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 0 12px rgba(21,128,61,0.9));">
    </div>

    <!-- 4 Realms Layout -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; width: 280px; margin: 40px auto 10px;">
      <div id="realm-1" style="background: #1e293b; border: 2px solid #22c55e; padding: 12px; border-radius: 6px; text-align: center; color: #fff; font-family: var(--font-pixel); font-size: 0.6rem;">1: ASGARD (HOME)</div>
      <div id="realm-2" style="background: #1e293b; border: 2px solid #475569; padding: 12px; border-radius: 6px; text-align: center; color: #fff; font-family: var(--font-pixel); font-size: 0.6rem;">2: MIDGARD</div>
      <div id="realm-4" style="background: #1e293b; border: 2px solid #475569; padding: 12px; border-radius: 6px; text-align: center; color: #fff; font-family: var(--font-pixel); font-size: 0.6rem;">4: VANAHEIM</div>
      <div id="realm-3" style="background: #1e293b; border: 2px solid #475569; padding: 12px; border-radius: 6px; text-align: center; color: #fff; font-family: var(--font-pixel); font-size: 0.6rem;">3: JOTUNHEIM</div>
    </div>
  </div>

  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; font-size: 0.88rem; min-height: 48px; display: flex; align-items: center;" id="loki-dialogue">
    💬 <strong>Loki:</strong> "Brute force evaluates (N−1)! / 2 = exponential explosion. Branch and Bound prunes suboptimal illusion timelines in O(N² 2^N)!"
  </div>

  <div class="viz-controls" style="display: flex; gap: 10px; flex-wrap: wrap;">
    <button class="pixel-btn pixel-btn-primary" id="loki-btn-auto">▶ AUTO-TOUR OPTIMAL HAMILTONIAN CYCLE</button>
    <button class="pixel-btn pixel-btn-secondary" id="loki-btn-reset">↺ RESET REALMS</button>
  </div>
</div>
""",
    "script": """
const lokiActor = document.getElementById('loki-actor');
const lokiDiag = document.getElementById('loki-dialogue');

let lokiStep = 0;
const pathPositions = [
  { left: '60px', top: '15px', name: '1: Asgard' },
  { left: '200px', top: '15px', name: '2: Midgard' },
  { left: '200px', top: '120px', name: '3: Jotunheim' },
  { left: '60px', top: '120px', name: '4: Vanaheim' },
  { left: '60px', top: '15px', name: '1: Asgard (Returned Home)' }
];

function stepLokiTour() {
  lokiStep = (lokiStep + 1) % pathPositions.length;
  const pos = pathPositions[lokiStep];
  lokiActor.style.left = pos.left;
  lokiActor.style.top = pos.top;
  lokiDiag.innerHTML = `👑 <strong>Loki:</strong> "Teleported to ${pos.name}! Total tour cost = 35 minimal realm units!"`;
}

document.getElementById('loki-btn-prune')?.addEventListener('click', () => { retroAudio.playClick(); stepLokiTour(); });
document.getElementById('loki-btn-auto')?.addEventListener('click', () => {
  retroAudio.playClick();
  let count = 0;
  const timer = setInterval(() => {
    stepLokiTour();
    count++;
    if (count >= 4) clearInterval(timer);
  }, 600);
});
document.getElementById('loki-btn-reset')?.addEventListener('click', () => {
  retroAudio.playClick();
  lokiStep = 0;
  lokiActor.style.left = '60px';
  lokiActor.style.top = '15px';
  lokiDiag.innerHTML = '💬 <strong>Loki:</strong> "Realms reset. Ready for glorious purpose."';
});
"""
}

# 19. BLACK WIDOW: Discrete Infiltration Vault (0/1 Knapsack)
SIMULATIONS["knapsack_01"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #e11d48;">MISSION: BLACK WIDOW 0/1 DISCRETE VAULT HEIST</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Items CANNOT be broken. Dynamic Programming fills 2D table DP[i, w] = max(DP[i-1,w], val + DP[i-1, w-wt]) in O(NW)!</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #fb7185; padding: 6px 10px; border: 1px solid #475569;">
      MAX VALUE: <span id="bw-max-val">$0</span>
    </div>
  </div>

  <!-- Custom Capacity Bar -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; align-items: center; gap: 8px;">
      <label style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a;">KNAPSACK CAPACITY W:</label>
      <input type="number" id="bw-cap-input" value="7" min="3" max="10" style="width: 50px; padding: 4px; border: 2px solid #0f172a; text-align: center; font-weight: bold;">
      <button class="pixel-btn pixel-btn-primary" id="bw-btn-solve" style="padding: 4px 10px; font-size: 0.58rem;">⚡ SOLVE 0/1 DP</button>
    </div>
    <div style="font-size: 0.75rem; color: #475569; font-weight: 600;">
      Items: #1(w:1, v:1), #2(w:3, v:4), #3(w:4, v:5), #4(w:5, v:7)
    </div>
  </div>

  <!-- Animated Arena Stage -->
  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 220px;">
    <!-- Black Widow Actor -->
    <div id="bw-actor" style="position: absolute; top: 12px; left: 20px; transition: all 0.4s ease; z-index: 10;">
      <img src="assets/blackwidow.png" style="width: 48px; height: 56px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 0 10px rgba(225,29,72,0.8));">
    </div>

    <!-- 2D DP Table Visual -->
    <div style="overflow-x: auto; margin-top: 50px;">
      <table style="width: 100%; border-collapse: collapse; font-family: var(--font-pixel); font-size: 0.55rem; color: #fff; text-align: center;" id="bw-dp-table">
        <!-- Generated dynamically -->
      </table>
    </div>
  </div>

  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; font-size: 0.88rem; min-height: 48px; display: flex; align-items: center;" id="bw-dialogue">
    💬 <strong>Black Widow:</strong> "0/1 Knapsack allows no fractional cuts. Either take an item completely or leave it. DP table memoizes optimal sub-problems in O(N·W)!"
  </div>

  <div class="viz-controls" style="display: flex; gap: 10px; flex-wrap: wrap;">
    <button class="pixel-btn pixel-btn-primary" id="bw-btn-auto">▶ AUTO-FILL DP TABLE CELL-BY-CELL</button>
    <button class="pixel-btn pixel-btn-secondary" id="bw-btn-step">⏭ STEP DP ROW</button>
    <button class="pixel-btn pixel-btn-secondary" id="bw-btn-reset">↺ RESET VAULT</button>
  </div>
</div>
""",
    "script": """
const bwTable = document.getElementById('bw-dp-table');
const bwDiag = document.getElementById('bw-dialogue');
const bwMaxVal = document.getElementById('bw-max-val');
const bwCapIn = document.getElementById('bw-cap-input');
const bwActor = document.getElementById('bw-actor');

let bwItems = [
  { w: 1, v: 1 },
  { w: 3, v: 4 },
  { w: 4, v: 5 },
  { w: 5, v: 7 }
];
let bwW = 7;
let dp = [];
let curRow = 0;

function buildDpTable() {
  bwW = parseInt(bwCapIn.value) || 7;
  dp = Array.from({length: bwItems.length + 1}, () => Array(bwW + 1).fill(0));

  for (let i = 1; i <= bwItems.length; i++) {
    for (let w = 0; w <= bwW; w++) {
      if (bwItems[i-1].w <= w) {
        dp[i][w] = Math.max(dp[i-1][w], bwItems[i-1].v + dp[i-1][w - bwItems[i-1].w]);
      } else {
        dp[i][w] = dp[i-1][w];
      }
    }
  }

  // Render Table Shell
  bwTable.innerHTML = '';
  let headerHtml = '<tr><th style="border:1px solid #475569; padding:4px;">Item \\ W</th>';
  for (let w = 0; w <= bwW; w++) headerHtml += `<th style="border:1px solid #475569; padding:4px; color:#facc15;">${w}</th>`;
  headerHtml += '</tr>';
  bwTable.innerHTML = headerHtml;

  for (let i = 0; i <= bwItems.length; i++) {
    let rowHtml = `<tr id="dp-row-${i}"><td style="border:1px solid #475569; padding:4px; color:#fb7185;">i=${i}</td>`;
    for (let w = 0; w <= bwW; w++) {
      rowHtml += `<td id="dp-cell-${i}-${w}" style="border:1px solid #334155; padding:4px; min-width:24px;">0</td>`;
    }
    rowHtml += '</tr>';
    bwTable.innerHTML += rowHtml;
  }
}
buildDpTable();

function fillRow(row) {
  if (row <= bwItems.length) {
    for (let w = 0; w <= bwW; w++) {
      const cell = document.getElementById(`dp-cell-${row}-${w}`);
      if (cell) {
        cell.textContent = dp[row][w];
        cell.style.background = '#15803d';
      }
    }
    bwActor.style.left = `${30 + row * 45}px`;
    bwDiag.innerHTML = `🕷️ <strong>Black Widow:</strong> "Filled DP row i=${row} for item with weight ${bwItems[row-1]?.w || 0} and value $${bwItems[row-1]?.v || 0}!"`;
  }
  if (row === bwItems.length) {
    const finalVal = dp[bwItems.length][bwW];
    bwMaxVal.textContent = `$${finalVal}`;
    bwDiag.innerHTML = `🏆 <strong>Black Widow:</strong> "Vault infiltration optimal: Max value = $${finalVal} under capacity W=${bwW} in O(NW)!"`;
  }
}

document.getElementById('bw-btn-step')?.addEventListener('click', () => {
  retroAudio.playClick();
  curRow++;
  if (curRow <= bwItems.length) fillRow(curRow);
});
document.getElementById('bw-btn-auto')?.addEventListener('click', () => {
  retroAudio.playClick();
  for (let i = 1; i <= bwItems.length; i++) fillRow(i);
});
document.getElementById('bw-btn-solve')?.addEventListener('click', () => {
  retroAudio.playClick();
  buildDpTable();
  for (let i = 1; i <= bwItems.length; i++) fillRow(i);
});
document.getElementById('bw-btn-reset')?.addEventListener('click', () => {
  retroAudio.playClick();
  curRow = 0;
  bwMaxVal.textContent = '$0';
  buildDpTable();
  bwActor.style.left = '20px';
  bwDiag.innerHTML = '💬 <strong>Black Widow:</strong> "Vault DP table reset."';
});
"""
}
