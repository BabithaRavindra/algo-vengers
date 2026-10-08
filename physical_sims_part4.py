# physical_sims_part4.py - Topics 16 to 19
# Physical Algorithm Simulations with Moving Hero Actors & Custom Inputs
# 16. Wolverine: Kruskal's vs Prim's (Dual Strategy Adamantium Pipeline Cut)
# 17. Captain Marvel: Dijkstra's Algorithm (Interstellar Jumpgate Shortest Path Relaxation)
# 18. Loki: Traveling Salesman Problem (Multiverse Conquest Held-Karp Bitmask DP)
# 19. Black Widow: 0/1 Knapsack Problem (Red Room Mainframe Extraction 2D DP Table & Backtracking)

PHYSICAL_SIMS_PART4 = {}

# -----------------------------------------------------------------------------
# 16. WOLVERINE: Kruskal's vs Prim's Dual Strategy
# -----------------------------------------------------------------------------
PHYSICAL_SIMS_PART4["kruskal_prim"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #ca8a04;">MISSION: WEAPON X ADAMANTIUM PIPELINE NETWORK</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Watch Logan compare Kruskal's global edge sorting against Prim's growing vertex cluster.</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #facc15; padding: 6px 10px; border: 1px solid #475569;">
      STRATEGY: <span id="wolv-mode-badge" style="color: #38bdf8;">KRUSKAL (EDGE-CENTRIC)</span>
    </div>
  </div>

  <!-- Strategy Selector & Stats Bar -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; gap: 8px;">
      <button class="pixel-btn pixel-btn-primary" id="wolv-mode-kruskal" style="padding: 4px 10px; font-size: 0.58rem;">KRUSKAL'S (GLOBAL EDGES)</button>
      <button class="pixel-btn pixel-btn-secondary" id="wolv-mode-prim" style="padding: 4px 10px; font-size: 0.58rem;">PRIM'S (ROOT CLUSTER)</button>
    </div>
    <div style="font-family: var(--font-code); font-size: 0.75rem; color: #ca8a04; font-weight: bold;">
      PIPELINES SECURED: <span id="wolv-edges-count" style="color: #15803d;">0 / 4</span> | COST: <span id="wolv-cost" style="color: #0284c7;">0</span>
    </div>
  </div>

  <!-- Animated Arena Stage -->
  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 290px; overflow: hidden;">
    <!-- Wolverine Actor -->
    <div id="wolv-actor" style="position: absolute; top: 15px; left: 30px; transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1); z-index: 20; display: flex; flex-direction: column; align-items: center;">
      <div style="font-family: var(--font-pixel); font-size: 0.5rem; background: #ca8a04; color: #000; padding: 1px 4px; border-radius: 2px; margin-bottom: 2px; font-weight: bold;">⚔ LOGAN</div>
      <img src="assets/wolverine.png" style="width: 44px; height: 50px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 4px 8px rgba(202,138,4,0.7));">
    </div>

    <!-- Network Graph SVG -->
    <svg id="wolv-graph-svg" style="width: 100%; height: 260px;">
      <!-- Pipeline Edges -->
      <line id="w-edge-0" x1="120" y1="80" x2="280" y2="50" stroke="#475569" stroke-width="3"/>
      <line id="w-edge-1" x1="280" y1="50" x2="440" y2="90" stroke="#475569" stroke-width="3"/>
      <line id="w-edge-2" x1="120" y1="80" x2="180" y2="210" stroke="#475569" stroke-width="3"/>
      <line id="w-edge-3" x1="280" y1="50" x2="180" y2="210" stroke="#475569" stroke-width="3"/>
      <line id="w-edge-4" x1="280" y1="50" x2="400" y2="210" stroke="#475569" stroke-width="3"/>
      <line id="w-edge-5" x1="440" y1="90" x2="400" y2="210" stroke="#475569" stroke-width="3"/>
      <line id="w-edge-6" x1="180" y1="210" x2="400" y2="210" stroke="#475569" stroke-width="3"/>

      <!-- Edge Weight Labels -->
      <text x="200" y="55" fill="#facc15" font-family="'JetBrains Mono'" font-size="11" font-weight="bold">w:1</text>
      <text x="360" y="60" fill="#facc15" font-family="'JetBrains Mono'" font-size="11" font-weight="bold">w:2</text>
      <text x="130" y="150" fill="#facc15" font-family="'JetBrains Mono'" font-size="11" font-weight="bold">w:4</text>
      <text x="240" y="140" fill="#facc15" font-family="'JetBrains Mono'" font-size="11" font-weight="bold">w:3</text>
      <text x="330" y="140" fill="#facc15" font-family="'JetBrains Mono'" font-size="11" font-weight="bold">w:6</text>
      <text x="430" y="160" fill="#facc15" font-family="'JetBrains Mono'" font-size="11" font-weight="bold">w:5</text>
      <text x="280" y="230" fill="#facc15" font-family="'JetBrains Mono'" font-size="11" font-weight="bold">w:7</text>

      <!-- Facility Nodes -->
      <circle id="w-node-A" cx="120" cy="80" r="18" fill="#1e293b" stroke="#ca8a04" stroke-width="3"/>
      <text x="120" y="84" fill="#fff" font-family="'Press Start 2P'" font-size="8" text-anchor="middle">A</text>

      <circle id="w-node-B" cx="280" cy="50" r="18" fill="#1e293b" stroke="#ca8a04" stroke-width="3"/>
      <text x="280" y="54" fill="#fff" font-family="'Press Start 2P'" font-size="8" text-anchor="middle">B</text>

      <circle id="w-node-C" cx="440" cy="90" r="18" fill="#1e293b" stroke="#ca8a04" stroke-width="3"/>
      <text x="440" y="94" fill="#fff" font-family="'Press Start 2P'" font-size="8" text-anchor="middle">C</text>

      <circle id="w-node-D" cx="180" cy="210" r="18" fill="#1e293b" stroke="#ca8a04" stroke-width="3"/>
      <text x="180" y="214" fill="#fff" font-family="'Press Start 2P'" font-size="8" text-anchor="middle">D</text>

      <circle id="w-node-E" cx="400" cy="210" r="18" fill="#1e293b" stroke="#ca8a04" stroke-width="3"/>
      <text x="400" y="214" fill="#fff" font-family="'Press Start 2P'" font-size="8" text-anchor="middle">E</text>
    </svg>
  </div>

  <!-- Hero Telemetry Box -->
  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 12px 16px; margin-bottom: 14px; min-height: 52px; display: flex; align-items: center; box-shadow: 0 2px 0 #0f172a;" id="wolv-dialogue">
    💬 <strong>Wolverine:</strong> "Kruskal's sorts every pipeline globally across Canada. Prim's grows outward from Base A. Both slice down to the same minimal MST!"
  </div>

  <!-- Interactive Controls -->
  <div class="viz-controls" style="display: flex; flex-wrap: wrap; gap: 10px;">
    <button class="pixel-btn pixel-btn-primary" id="wolv-btn-step">⚔ CLAW SLICE NEXT EDGE</button>
    <button class="pixel-btn pixel-btn-accent" id="wolv-btn-all">▶ DISMANTLE FULL NETWORK</button>
    <button class="pixel-btn pixel-btn-secondary" id="wolv-btn-reset">↺ RESET FACILITY</button>
  </div>
</div>
""",
    "script": """
let wolvMode = 'kruskal'; // 'kruskal' or 'prim'
let wolvStep = 0;
let wolvTaken = 0;
let wolvTotalCost = 0;
let wolvDone = false;

// Kruskal Edge Sequence (Global sorted order)
const kruskalSeq = [
  { id: 0, u: 'A', v: 'B', w: 1, cycle: false, x: 200, y: 65 },
  { id: 1, u: 'B', v: 'C', w: 2, cycle: false, x: 360, y: 70 },
  { id: 3, u: 'B', v: 'D', w: 3, cycle: false, x: 230, y: 130 },
  { id: 2, u: 'A', v: 'D', w: 4, cycle: true,  x: 150, y: 145 },
  { id: 5, u: 'C', v: 'E', w: 5, cycle: false, x: 420, y: 150 },
  { id: 4, u: 'B', v: 'E', w: 6, cycle: true,  x: 340, y: 130 },
  { id: 6, u: 'D', v: 'E', w: 7, cycle: true,  x: 290, y: 210 }
];

// Prim Sequence starting from A
const primSeq = [
  { id: 0, u: 'A', v: 'B', w: 1, newNode: 'B', x: 200, y: 65 },
  { id: 1, u: 'B', v: 'C', w: 2, newNode: 'C', x: 360, y: 70 },
  { id: 3, u: 'B', v: 'D', w: 3, newNode: 'D', x: 230, y: 130 },
  { id: 5, u: 'C', v: 'E', w: 5, newNode: 'E', x: 420, y: 150 }
];

const wolvActor = document.getElementById('wolv-actor');
const wolvDialogue = document.getElementById('wolv-dialogue');
const wolvModeBadge = document.getElementById('wolv-mode-badge');
const wolvCountLabel = document.getElementById('wolv-edges-count');
const wolvCostLabel = document.getElementById('wolv-cost');

function stepWolv() {
  if (wolvDone || wolvTaken >= 4) {
    wolvDone = true;
    retroAudio.playSuccess();
    wolvDialogue.innerHTML = `<strong>✨ WEAPON X NETWORK COMPLETE!</strong> MST created with exactly 4 edges! Total Adamantium cost: ${wolvTotalCost}!`;
    return;
  }

  retroAudio.playClick();

  if (wolvMode === 'kruskal') {
    if (wolvStep >= kruskalSeq.length) return;
    const e = kruskalSeq[wolvStep];
    const lineEl = document.getElementById(`w-edge-${e.id}`);
    wolvActor.style.left = `${e.x}px`;
    wolvActor.style.top = `${e.y - 30}px`;

    setTimeout(() => {
      if (!e.cycle && wolvTaken < 4) {
        retroAudio.playSuccess();
        lineEl.setAttribute('stroke', '#ca8a04');
        lineEl.setAttribute('stroke-width', '5');
        wolvTaken++;
        wolvTotalCost += e.w;
        wolvDialogue.innerHTML = `⚔ <strong>Wolverine:</strong> "Kruskal picked lightest available edge ${e.u}-${e.v} (weight ${e.w}). Merges disjoint sets!"`;
      } else {
        retroAudio.playError();
        lineEl.setAttribute('stroke', '#ef4444');
        lineEl.setAttribute('stroke-dasharray', '5,5');
        wolvDialogue.innerHTML = `⚠️ <strong>Wolverine:</strong> "CYCLE DETECTED! ${e.u} and ${e.v} already in same set. Adamantium claw reject!"`;
      }
      wolvCountLabel.textContent = `${wolvTaken} / 4`;
      wolvCostLabel.textContent = wolvTotalCost;
      wolvStep++;
      if (wolvTaken >= 4) wolvDone = true;
    }, 300);

  } else {
    // Prim's
    if (wolvStep >= primSeq.length) return;
    const e = primSeq[wolvStep];
    const lineEl = document.getElementById(`w-edge-${e.id}`);
    const nodeEl = document.getElementById(`w-node-${e.newNode}`);
    wolvActor.style.left = `${e.x}px`;
    wolvActor.style.top = `${e.y - 30}px`;

    setTimeout(() => {
      retroAudio.playSuccess();
      lineEl.setAttribute('stroke', '#22c55e');
      lineEl.setAttribute('stroke-width', '5');
      if (nodeEl) nodeEl.setAttribute('stroke', '#22c55e');
      wolvTaken++;
      wolvTotalCost += e.w;
      wolvDialogue.innerHTML = `⚔ <strong>Wolverine:</strong> "Prim grows tree from cut! Lightest cut edge ${e.u}-${e.v} (weight ${e.w}) annexes Facility ${e.newNode}!"`;
      wolvCountLabel.textContent = `${wolvTaken} / 4`;
      wolvCostLabel.textContent = wolvTotalCost;
      wolvStep++;
      if (wolvTaken >= 4) wolvDone = true;
    }, 300);
  }
}

function resetWolv() {
  wolvStep = 0;
  wolvTaken = 0;
  wolvTotalCost = 0;
  wolvDone = false;
  wolvActor.style.left = '30px';
  wolvActor.style.top = '15px';
  wolvCountLabel.textContent = '0 / 4';
  wolvCostLabel.textContent = '0';
  for (let i = 0; i < 7; i++) {
    const el = document.getElementById(`w-edge-${i}`);
    if (el) {
      el.setAttribute('stroke', '#475569');
      el.setAttribute('stroke-width', '3');
      el.removeAttribute('stroke-dasharray');
    }
  }
  ['A','B','C','D','E'].forEach(n => {
    const el = document.getElementById(`w-node-${n}`);
    if (el) el.setAttribute('stroke', '#ca8a04');
  });
  wolvDialogue.innerHTML = `💬 <strong>Wolverine:</strong> "Facility reset. Active mode: ${wolvMode.toUpperCase()}. Ready to cut!"`;
}

document.getElementById('wolv-mode-kruskal')?.addEventListener('click', () => {
  wolvMode = 'kruskal';
  wolvModeBadge.textContent = 'KRUSKAL (EDGE-CENTRIC)';
  wolvModeBadge.style.color = '#38bdf8';
  resetWolv();
});

document.getElementById('wolv-mode-prim')?.addEventListener('click', () => {
  wolvMode = 'prim';
  wolvModeBadge.textContent = "PRIM (ROOT CUT GROWING)";
  wolvModeBadge.style.color = '#22c55e';
  resetWolv();
});

document.getElementById('wolv-btn-step')?.addEventListener('click', () => {
  stepWolv();
});

document.getElementById('wolv-btn-all')?.addEventListener('click', () => {
  while (!wolvDone && wolvTaken < 4) {
    stepWolv();
  }
});

document.getElementById('wolv-btn-reset')?.addEventListener('click', () => {
  resetWolv();
});
"""
}

# -----------------------------------------------------------------------------
# 17. CAPTAIN MARVEL: Dijkstra's Algorithm
# -----------------------------------------------------------------------------
PHYSICAL_SIMS_PART4["dijkstra"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #dc2626;">MISSION: KREE ARMADA RELAY INTERCEPTION</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Watch Captain Marvel channel photon beams across interstellar jumpgates to compute shortest paths.</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #facc15; padding: 6px 10px; border: 1px solid #475569;">
      CURRENT SECTOR: <span id="cm-cur-node" style="color: #38bdf8;">EARTH (S)</span>
    </div>
  </div>

  <!-- Priority Queue & Distances Bar -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; gap: 10px; align-items: center;">
      <span style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a;">PRIORITY QUEUE (DISTANCES):</span>
      <div id="cm-dist-tags" style="display: flex; gap: 6px; font-family: var(--font-code); font-size: 0.75rem;"></div>
    </div>
    <div style="font-family: var(--font-code); font-size: 0.8rem; font-weight: bold; color: #dc2626;">
      RELAXATION: d[v] = min(d[v], d[u] + w(u,v))
    </div>
  </div>

  <!-- Animated Arena Stage -->
  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 290px; overflow: hidden;">
    <!-- Captain Marvel Actor -->
    <div id="cm-actor" style="position: absolute; top: 70px; left: 110px; transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1); z-index: 20; display: flex; flex-direction: column; align-items: center;">
      <div style="font-family: var(--font-pixel); font-size: 0.5rem; background: #dc2626; color: #fff; padding: 1px 4px; border-radius: 2px; margin-bottom: 2px;">✴ DANVERS</div>
      <img src="assets/captainmarvel.png" style="width: 44px; height: 50px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 4px 8px rgba(220,38,38,0.7));">
    </div>

    <!-- Space Sectors Jumpgate Network SVG -->
    <svg id="cm-jump-svg" style="width: 100%; height: 260px;">
      <!-- Jumpgate Edges: S(130,120), X(260,50), K(260,190), H(420,120) -->
      <line id="cm-edge-sx" x1="130" y1="120" x2="260" y2="50" stroke="#475569" stroke-width="3"/>
      <line id="cm-edge-sk" x1="130" y1="120" x2="260" y2="190" stroke="#475569" stroke-width="3"/>
      <line id="cm-edge-xk" x1="260" y1="50" x2="260" y2="190" stroke="#475569" stroke-width="3"/>
      <line id="cm-edge-xh" x1="260" y1="50" x2="420" y2="120" stroke="#475569" stroke-width="3"/>
      <line id="cm-edge-kh" x1="260" y1="190" x2="420" y2="120" stroke="#475569" stroke-width="3"/>

      <!-- Weight Labels -->
      <text x="180" y="75" fill="#38bdf8" font-family="'JetBrains Mono'" font-size="11" font-weight="bold">w:4</text>
      <text x="180" y="170" fill="#38bdf8" font-family="'JetBrains Mono'" font-size="11" font-weight="bold">w:2</text>
      <text x="270" y="125" fill="#38bdf8" font-family="'JetBrains Mono'" font-size="11" font-weight="bold">w:1</text>
      <text x="350" y="75" fill="#38bdf8" font-family="'JetBrains Mono'" font-size="11" font-weight="bold">w:5</text>
      <text x="350" y="170" fill="#38bdf8" font-family="'JetBrains Mono'" font-size="11" font-weight="bold">w:3</text>

      <!-- Sector Nodes -->
      <!-- Earth (S) -->
      <circle id="cm-node-S" cx="130" cy="120" r="20" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
      <text x="130" y="124" fill="#fff" font-family="'Press Start 2P'" font-size="8" text-anchor="middle">S</text>

      <!-- Xandar (X) -->
      <circle id="cm-node-X" cx="260" cy="50" r="20" fill="#1e293b" stroke="#475569" stroke-width="3"/>
      <text x="260" y="54" fill="#fff" font-family="'Press Start 2P'" font-size="8" text-anchor="middle">X</text>

      <!-- Knowhere (K) -->
      <circle id="cm-node-K" cx="260" cy="190" r="20" fill="#1e293b" stroke="#475569" stroke-width="3"/>
      <text x="260" y="194" fill="#fff" font-family="'Press Start 2P'" font-size="8" text-anchor="middle">K</text>

      <!-- Hala (H) -->
      <circle id="cm-node-H" cx="420" cy="120" r="20" fill="#1e293b" stroke="#475569" stroke-width="3"/>
      <text x="420" y="124" fill="#fff" font-family="'Press Start 2P'" font-size="8" text-anchor="middle">H</text>
    </svg>
  </div>

  <!-- Hero Telemetry Box -->
  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 12px 16px; margin-bottom: 14px; min-height: 52px; display: flex; align-items: center; box-shadow: 0 2px 0 #0f172a;" id="cm-dialogue">
    💬 <strong>Captain Marvel:</strong> "Dijkstra's maintains a priority queue of tentative distances. We extract the closest unvisited star system and relax outgoing jumpgates!"
  </div>

  <!-- Interactive Controls -->
  <div class="viz-controls" style="display: flex; flex-wrap: wrap; gap: 10px;">
    <button class="pixel-btn pixel-btn-primary" id="cm-btn-step">✴ RELAX OUTGOING JUMPGATES</button>
    <button class="pixel-btn pixel-btn-accent" id="cm-btn-all">▶ FULL COSMIC FLIGHT SWEEP</button>
    <button class="pixel-btn pixel-btn-secondary" id="cm-btn-reset">↺ RESET FLIGHT PLAN</button>
  </div>
</div>
""",
    "script": """
let cmStep = 0;
let cmVisited = new Set();
let cmDist = { S: 0, X: 4, K: 2, H: Infinity };
let cmDone = false;

const cmActor = document.getElementById('cm-actor');
const cmDialogue = document.getElementById('cm-dialogue');
const cmDistTags = document.getElementById('cm-dist-tags');
const cmCurNode = document.getElementById('cm-cur-node');

function renderCMDist() {
  cmDistTags.innerHTML = '';
  Object.keys(cmDist).forEach(k => {
    const el = document.createElement('span');
    const isVis = cmVisited.has(k);
    el.style.cssText = `
      background: ${isVis ? '#15803d' : '#1e293b'}; color: #fff;
      border: 1px solid ${isVis ? '#22c55e' : '#475569'}; padding: 3px 6px; border-radius: 3px;
    `;
    const dStr = cmDist[k] === Infinity ? '∞' : cmDist[k];
    el.textContent = `${k}: ${dStr}${isVis ? ' [✓]' : ''}`;
    cmDistTags.appendChild(el);
  });
}

function stepCM() {
  if (cmDone) return;
  retroAudio.playClick();

  if (cmStep === 0) {
    // Start at S, relax outgoing to K and X
    cmVisited.add('S');
    cmCurNode.textContent = 'EARTH (S)';
    document.getElementById('cm-node-S').setAttribute('stroke', '#22c55e');
    cmDialogue.innerHTML = `✴ <strong>Captain Marvel:</strong> "Starting at Earth (S). Relax outgoing: S->K is cost 2; S->X is cost 4. K is next closest!"`;
    cmStep = 1;
    renderCMDist();
  } else if (cmStep === 1) {
    // Move to K (cost 2)
    cmVisited.add('K');
    cmCurNode.textContent = 'KNOWHERE (K)';
    cmActor.style.left = '240px';
    cmActor.style.top = '140px';
    document.getElementById('cm-node-K').setAttribute('stroke', '#22c55e');
    document.getElementById('cm-edge-sk').setAttribute('stroke', '#22c55e');
    document.getElementById('cm-edge-sk').setAttribute('stroke-width', '5');

    // Relax K->X (2 + 1 = 3 < 4), K->H (2 + 3 = 5)
    cmDist.X = Math.min(cmDist.X, cmDist.K + 1);
    cmDist.H = Math.min(cmDist.H, cmDist.K + 3);

    retroAudio.playHover();
    cmDialogue.innerHTML = `✴ <strong>Captain Marvel:</strong> "At Knowhere (K). RELAXATION: K->X improves distance from 4 to 3! K->H establishes distance 5!"`;
    cmStep = 2;
    renderCMDist();
  } else if (cmStep === 2) {
    // Move to X (cost 3)
    cmVisited.add('X');
    cmCurNode.textContent = 'XANDAR (X)';
    cmActor.style.left = '240px';
    cmActor.style.top = '10px';
    document.getElementById('cm-node-X').setAttribute('stroke', '#22c55e');
    document.getElementById('cm-edge-xk').setAttribute('stroke', '#22c55e');
    document.getElementById('cm-edge-xk').setAttribute('stroke-width', '5');

    // Relax X->H: 3 + 5 = 8 (does not beat 5)
    retroAudio.playHover();
    cmDialogue.innerHTML = `✴ <strong>Captain Marvel:</strong> "At Xandar (X, dist 3). Outgoing X->H cost 3+5=8 does NOT improve existing route (dist 5)."`;
    cmStep = 3;
    renderCMDist();
  } else if (cmStep === 3) {
    // Finalize H (cost 5)
    cmVisited.add('H');
    cmCurNode.textContent = 'HALA (H) [DESTINATION]';
    cmActor.style.left = '400px';
    cmActor.style.top = '70px';
    document.getElementById('cm-node-H').setAttribute('stroke', '#22c55e');
    document.getElementById('cm-edge-kh').setAttribute('stroke', '#22c55e');
    document.getElementById('cm-edge-kh').setAttribute('stroke-width', '5');

    cmDone = true;
    retroAudio.playSuccess();
    cmDialogue.innerHTML = `<strong>✨ DESTINATION REACHED!</strong> Shortest path from Earth to Hala finalized via S -> K -> H with total cost 5!`;
    renderCMDist();
  }
}

document.getElementById('cm-btn-step')?.addEventListener('click', () => {
  stepCM();
});

document.getElementById('cm-btn-all')?.addEventListener('click', () => {
  while (!cmDone) {
    stepCM();
  }
});

document.getElementById('cm-btn-reset')?.addEventListener('click', () => {
  cmStep = 0;
  cmVisited = new Set();
  cmDist = { S: 0, X: 4, K: 2, H: Infinity };
  cmDone = false;
  cmActor.style.left = '110px';
  cmActor.style.top = '70px';
  cmCurNode.textContent = 'EARTH (S)';
  ['S','X','K','H'].forEach(id => {
    document.getElementById(`cm-node-${id}`).setAttribute('stroke', '#475569');
  });
  document.getElementById('cm-node-S').setAttribute('stroke', '#38bdf8');
  ['sx','sk','xk','xh','kh'].forEach(e => {
    const el = document.getElementById(`cm-edge-${e}`);
    el.setAttribute('stroke', '#475569');
    el.setAttribute('stroke-width', '3');
  });
  renderCMDist();
  cmDialogue.innerHTML = `💬 <strong>Captain Marvel:</strong> "Flight plan reset. Ready to relax interstellar jumpgates!"`;
});

renderCMDist();
"""
}

# -----------------------------------------------------------------------------
# 18. LOKI: Traveling Salesman Problem (TSP) Held-Karp DP
# -----------------------------------------------------------------------------
PHYSICAL_SIMS_PART4["tsp"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #15803d;">MISSION: THE MULTIVERSE CONQUEST GRAND TOUR</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Watch Loki avoid factorial explosion using Held-Karp subset bitmask memoization.</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #facc15; padding: 6px 10px; border: 1px solid #475569;">
      TOUR: <span id="loki-tour-path" style="color: #38bdf8;">A -> ... -> A</span> | COST: <span id="loki-tour-cost" style="color: #22c55e;">0</span>
    </div>
  </div>

  <!-- Tour Comparison Header Bar -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a;">
      CITIES: 4 (Asgard [0], Midgard [1], Jotunheim [2], Sakaar [3])
    </div>
    <div style="font-family: var(--font-code); font-size: 0.8rem; font-weight: bold; color: #15803d;">
      HELD-KARP: O(n^2 * 2^n) vs BRUTE FORCE: O(n!)
    </div>
  </div>

  <!-- Animated Arena Stage -->
  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 290px; overflow: hidden;">
    <!-- Loki Actor -->
    <div id="loki-actor" style="position: absolute; top: 15px; left: 160px; transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1); z-index: 20; display: flex; flex-direction: column; align-items: center;">
      <div style="font-family: var(--font-pixel); font-size: 0.5rem; background: #15803d; color: #fff; padding: 1px 4px; border-radius: 2px; margin-bottom: 2px;">♜ LOKI</div>
      <img src="assets/loki.png" style="width: 44px; height: 50px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 4px 8px rgba(21,128,61,0.7));">
    </div>

    <!-- Planetary Cities Tour Graph SVG -->
    <svg id="loki-tour-svg" style="width: 100%; height: 260px;">
      <!-- Realm Coordinates: A(180,60), M(380,60), S(380,200), J(180,200) -->
      <!-- Outer Cycle Lines -->
      <line id="tsp-edge-am" x1="180" y1="60" x2="380" y2="60" stroke="#475569" stroke-width="3"/>
      <line id="tsp-edge-ms" x1="380" y1="60" x2="380" y2="200" stroke="#475569" stroke-width="3"/>
      <line id="tsp-edge-sj" x1="380" y1="200" x2="180" y2="200" stroke="#475569" stroke-width="3"/>
      <line id="tsp-edge-ja" x1="180" y1="200" x2="180" y2="60" stroke="#475569" stroke-width="3"/>
      <!-- Diagonal Lines -->
      <line id="tsp-edge-as" x1="180" y1="60" x2="380" y2="200" stroke="#475569" stroke-width="2" stroke-dasharray="4,4"/>
      <line id="tsp-edge-mj" x1="380" y1="60" x2="180" y2="200" stroke="#475569" stroke-width="2" stroke-dasharray="4,4"/>

      <!-- Edge Weight Labels -->
      <text x="270" y="50" fill="#38bdf8" font-family="'JetBrains Mono'" font-size="11" font-weight="bold">10</text>
      <text x="395" y="135" fill="#38bdf8" font-family="'JetBrains Mono'" font-size="11" font-weight="bold">15</text>
      <text x="270" y="225" fill="#38bdf8" font-family="'JetBrains Mono'" font-size="11" font-weight="bold">20</text>
      <text x="145" y="135" fill="#38bdf8" font-family="'JetBrains Mono'" font-size="11" font-weight="bold">25</text>
      <text x="300" y="115" fill="#94a3b8" font-family="'JetBrains Mono'" font-size="10">35</text>
      <text x="250" y="115" fill="#94a3b8" font-family="'JetBrains Mono'" font-size="10">30</text>

      <!-- Planetary Nodes -->
      <circle id="tsp-node-A" cx="180" cy="60" r="20" fill="#1e293b" stroke="#facc15" stroke-width="3"/>
      <text x="180" y="64" fill="#fff" font-family="'Press Start 2P'" font-size="8" text-anchor="middle">A</text>

      <circle id="tsp-node-M" cx="380" cy="60" r="20" fill="#1e293b" stroke="#475569" stroke-width="3"/>
      <text x="380" y="64" fill="#fff" font-family="'Press Start 2P'" font-size="8" text-anchor="middle">M</text>

      <circle id="tsp-node-S" cx="380" cy="200" r="20" fill="#1e293b" stroke="#475569" stroke-width="3"/>
      <text x="380" y="204" fill="#fff" font-family="'Press Start 2P'" font-size="8" text-anchor="middle">S</text>

      <circle id="tsp-node-J" cx="180" cy="200" r="20" fill="#1e293b" stroke="#475569" stroke-width="3"/>
      <text x="180" y="204" fill="#fff" font-family="'Press Start 2P'" font-size="8" text-anchor="middle">J</text>
    </svg>
  </div>

  <!-- Hero Telemetry Box -->
  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 12px 16px; margin-bottom: 14px; min-height: 52px; display: flex; align-items: center; box-shadow: 0 2px 0 #0f172a;" id="loki-dialogue">
    💬 <strong>Loki:</strong> "Brute force evaluates (n-1)! / 2 tours. With the Tesseract and Held-Karp DP, we memoize sub-tours by subset bitmask!"
  </div>

  <!-- Interactive Controls -->
  <div class="viz-controls" style="display: flex; flex-wrap: wrap; gap: 10px;">
    <button class="pixel-btn pixel-btn-primary" id="loki-btn-step">♜ ADVANCE TOUR LEG</button>
    <button class="pixel-btn pixel-btn-accent" id="loki-btn-all">▶ EXECUTE FULL TOUR</button>
    <button class="pixel-btn pixel-btn-secondary" id="loki-btn-reset">↺ RETURN TO ASGARD</button>
  </div>
</div>
""",
    "script": """
let lokiStep = 0;
let lokiCost = 0;
let lokiDone = false;

// Optimal Tour: A -> M (10) -> S (15) -> J (20) -> A (25) = 70
const tourSteps = [
  { from: 'A', to: 'M', cost: 10, edge: 'tsp-edge-am', actorX: 360, actorY: 15 },
  { from: 'M', to: 'S', cost: 15, edge: 'tsp-edge-ms', actorX: 360, actorY: 150 },
  { from: 'S', to: 'J', cost: 20, edge: 'tsp-edge-sj', actorX: 160, actorY: 150 },
  { from: 'J', to: 'A', cost: 25, edge: 'tsp-edge-ja', actorX: 160, actorY: 15 }
];

const lokiActor = document.getElementById('loki-actor');
const lokiDialogue = document.getElementById('loki-dialogue');
const lokiPathLabel = document.getElementById('loki-tour-path');
const lokiCostLabel = document.getElementById('loki-tour-cost');

function stepLoki() {
  if (lokiDone || lokiStep >= tourSteps.length) {
    lokiDone = true;
    retroAudio.playSuccess();
    lokiDialogue.innerHTML = `<strong>✨ GLORIOUS PURPOSE FULFILLED!</strong> Minimal round-trip Hamiltonian cycle complete! Total cost: 70!`;
    return;
  }

  retroAudio.playClick();
  const step = tourSteps[lokiStep];
  const lineEl = document.getElementById(step.edge);
  const targetNode = document.getElementById(`tsp-node-${step.to}`);

  lokiActor.style.left = `${step.actorX}px`;
  lokiActor.style.top = `${step.actorY}px`;

  setTimeout(() => {
    retroAudio.playHover();
    lineEl.setAttribute('stroke', '#15803d');
    lineEl.setAttribute('stroke-width', '5');
    if (targetNode) targetNode.setAttribute('stroke', '#22c55e');

    lokiCost += step.cost;
    lokiStep++;

    const visitedNodes = ['A'];
    for (let i = 0; i < lokiStep; i++) visitedNodes.push(tourSteps[i].to);
    lokiPathLabel.textContent = visitedNodes.join(' -> ');
    lokiCostLabel.textContent = lokiCost;

    lokiDialogue.innerHTML = `♜ <strong>Loki:</strong> "Teleported from ${step.from} to ${step.to} (+${step.cost} energy). Bitmask updated!"`;

    if (lokiStep === tourSteps.length) {
      lokiDone = true;
      setTimeout(() => {
        retroAudio.playSuccess();
        lokiDialogue.innerHTML = `<strong>✨ TOUR COMPLETE!</strong> Round-trip cycle A->M->S->J->A verified optimal via Dynamic Programming!`;
      }, 300);
    }
  }, 300);
}

document.getElementById('loki-btn-step')?.addEventListener('click', () => {
  stepLoki();
});

document.getElementById('loki-btn-all')?.addEventListener('click', () => {
  while (!lokiDone && lokiStep < tourSteps.length) {
    stepLoki();
  }
});

document.getElementById('loki-btn-reset')?.addEventListener('click', () => {
  lokiStep = 0;
  lokiCost = 0;
  lokiDone = false;
  lokiActor.style.left = '160px';
  lokiActor.style.top = '15px';
  lokiPathLabel.textContent = 'A -> ... -> A';
  lokiCostLabel.textContent = '0';
  ['am','ms','sj','ja'].forEach(e => {
    const el = document.getElementById(`tsp-edge-${e}`);
    el.setAttribute('stroke', '#475569');
    el.setAttribute('stroke-width', '3');
  });
  ['M','S','J'].forEach(n => {
    document.getElementById(`tsp-node-${n}`).setAttribute('stroke', '#475569');
  });
  document.getElementById('tsp-node-A').setAttribute('stroke', '#facc15');
  lokiDialogue.innerHTML = `💬 <strong>Loki:</strong> "Returned to Asgard. Ready to conquer the multiverse once more!"`;
});
"""
}

# -----------------------------------------------------------------------------
# 19. BLACK WIDOW: 0/1 Knapsack Problem (2D Dynamic Programming Table)
# -----------------------------------------------------------------------------
PHYSICAL_SIMS_PART4["knapsack_01"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #be123c;">MISSION: RED ROOM COVERT EXTRACTION (0/1 KNAPSACK)</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Watch Natasha Romanoff evaluate binary take-or-leave choices across a 2D Bellman recurrence grid.</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #f43f5e; padding: 6px 10px; border: 1px solid #475569;">
      HARNESS: <span id="bw-cap-text" style="color: #38bdf8;">W = 6 KG</span> | OPTIMAL VAL: <span id="bw-opt-val" style="color: #22c55e;">0</span>
    </div>
  </div>

  <!-- User Knapsack Items & Invariant Bar -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; gap: 8px; font-family: var(--font-code); font-size: 0.75rem;">
      <span style="background: #fee2e2; color: #991b1b; padding: 2px 6px; border: 1px solid #991b1b;">Item 1: [w:1, v:3]</span>
      <span style="background: #fee2e2; color: #991b1b; padding: 2px 6px; border: 1px solid #991b1b;">Item 2: [w:2, v:4]</span>
      <span style="background: #fee2e2; color: #991b1b; padding: 2px 6px; border: 1px solid #991b1b;">Item 3: [w:3, v:6]</span>
    </div>
    <div style="font-family: var(--font-code); font-size: 0.75rem; font-weight: bold; color: #be123c;">
      DP[i][w] = max(DP[i-1][w], DP[i-1][w - w_i] + v_i)
    </div>
  </div>

  <!-- Animated Arena Stage (2D DP Table) -->
  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 290px; overflow-x: auto;">
    <!-- Black Widow Actor -->
    <div id="bw-actor" style="position: absolute; top: 15px; left: 20px; transition: all 0.35s cubic-bezier(0.34, 1.56, 0.64, 1); z-index: 20; display: flex; flex-direction: column; align-items: center;">
      <div style="font-family: var(--font-pixel); font-size: 0.5rem; background: #be123c; color: #fff; padding: 1px 4px; border-radius: 2px; margin-bottom: 2px;">⧗ NATASHA</div>
      <img src="assets/blackwidow.png" style="width: 44px; height: 50px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 4px 8px rgba(190,18,60,0.7));">
    </div>

    <!-- 2D Dynamic Programming Table Display -->
    <div style="margin-top: 30px;">
      <div style="font-family: var(--font-pixel); font-size: 0.58rem; color: #94a3b8; margin-bottom: 8px;">2D DP MEMOIZATION TABLE [ROWS: ITEMS (i) | COLS: CAPACITY (w = 0..6)]</div>
      <table id="bw-dp-table" style="width: 100%; border-collapse: collapse; text-align: center; font-family: var(--font-code); font-size: 0.8rem; color: #fff;">
        <!-- Filled dynamically -->
      </table>
    </div>
  </div>

  <!-- Hero Telemetry Box -->
  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 12px 16px; margin-bottom: 14px; min-height: 52px; display: flex; align-items: center; box-shadow: 0 2px 0 #0f172a;" id="bw-dialogue">
    💬 <strong>Black Widow:</strong> "Unlike fractional knapsack, drives cannot be fragmented. We evaluate binary choices (take or leave) via 2D Bellman recurrence!"
  </div>

  <!-- Interactive Controls -->
  <div class="viz-controls" style="display: flex; flex-wrap: wrap; gap: 10px;">
    <button class="pixel-btn pixel-btn-primary" id="bw-btn-step">⧗ EVALUATE NEXT CELL</button>
    <button class="pixel-btn pixel-btn-accent" id="bw-btn-all">▶ AUTO-FILL DP TABLE</button>
    <button class="pixel-btn pixel-btn-secondary" id="bw-btn-backtrack">🔍 BACKTRACK EXTRACTION</button>
    <button class="pixel-btn pixel-btn-secondary" id="bw-btn-reset">↺ RESET MAINFRAME</button>
  </div>
</div>
""",
    "script": """
const bwItems = [
  { name: "Drive 1", wt: 1, val: 3 },
  { name: "Drive 2", wt: 2, val: 4 },
  { name: "Drive 3", wt: 3, val: 6 }
];
const bwCap = 6;
let dpTable = [];
let curI = 1;
let curW = 0;
let bwDone = false;

const bwActor = document.getElementById('bw-actor');
const bwDialogue = document.getElementById('bw-dialogue');
const bwTableEl = document.getElementById('bw-dp-table');
const bwOptLabel = document.getElementById('bw-opt-val');

function initBWTable() {
  dpTable = [];
  for (let i = 0; i <= bwItems.length; i++) {
    dpTable.push(new Array(bwCap + 1).fill(0));
  }
  curI = 1;
  curW = 0;
  bwDone = false;
  renderBWTable();
}

function renderBWTable() {
  bwTableEl.innerHTML = '';

  // Header row
  let headerHtml = '<tr><th style="padding:6px; border:1px solid #475569; background:#1e293b; color:#94a3b8;">i \\ w</th>';
  for (let w = 0; w <= bwCap; w++) {
    headerHtml += `<th style="padding:6px; border:1px solid #475569; background:#1e293b; color:#38bdf8;">w=${w}</th>`;
  }
  headerHtml += '</tr>';
  bwTableEl.innerHTML += headerHtml;

  // Data rows
  for (let i = 0; i <= bwItems.length; i++) {
    let rowHtml = `<tr><td style="padding:6px; border:1px solid #475569; background:#1e293b; font-weight:bold; color:#facc15;">${i === 0 ? '0 (None)' : `i=${i} [${bwItems[i-1].name}]`}</td>`;
    for (let w = 0; w <= bwCap; w++) {
      const isCur = (i === curI && w === curW && !bwDone);
      const isFilled = (i < curI || (i === curI && w <= curW) || bwDone);
      rowHtml += `
        <td id="dp-cell-${i}-${w}" style="padding:6px; border:1px solid #475569; background:${isCur ? '#be123c' : (isFilled ? '#0f172a' : '#1e293b')}; color:${isCur ? '#fff' : (isFilled ? '#22c55e' : '#64748b')}; font-weight:bold; transition:all 0.2s;">
          ${isFilled ? dpTable[i][w] : '-'}
        </td>
      `;
    }
    rowHtml += '</tr>';
    bwTableEl.innerHTML += rowHtml;
  }
}

function stepBW() {
  if (bwDone) return;
  retroAudio.playClick();

  const item = bwItems[curI - 1];
  const w = curW;
  const i = curI;

  let chosenVal = 0;
  let reason = '';

  if (item.wt > w) {
    // Cannot take
    chosenVal = dpTable[i - 1][w];
    reason = `Weight ${item.wt} > capacity ${w}. Must leave: DP[${i-1}][${w}] = ${chosenVal}`;
  } else {
    const leaveVal = dpTable[i - 1][w];
    const takeVal = dpTable[i - 1][w - item.wt] + item.val;
    if (takeVal > leaveVal) {
      chosenVal = takeVal;
      reason = `TAKE Drive ${i}! (${takeVal} > ${leaveVal}): +${item.val} value`;
    } else {
      chosenVal = leaveVal;
      reason = `LEAVE Drive ${i}: (${leaveVal} >= ${takeVal})`;
    }
  }

  dpTable[i][w] = chosenVal;

  const targetX = Math.min(500, 60 + w * 65);
  bwActor.style.left = `${targetX}px`;
  bwActor.style.top = `${60 + i * 35}px`;

  bwDialogue.innerHTML = `⧗ <strong>Black Widow:</strong> "Cell [${i}, ${w}]: ${reason}"`;

  curW++;
  if (curW > bwCap) {
    curW = 0;
    curI++;
    if (curI > bwItems.length) {
      bwDone = true;
      retroAudio.playSuccess();
      bwOptLabel.textContent = dpTable[bwItems.length][bwCap];
      bwDialogue.innerHTML = `<strong>✨ TABLE COMPLETE!</strong> Optimal maximum value = ${dpTable[bwItems.length][bwCap]}! Click 'BACKTRACK EXTRACTION' to recover payload!`;
    }
  }

  renderBWTable();
}

document.getElementById('bw-btn-step')?.addEventListener('click', () => {
  stepBW();
});

document.getElementById('bw-btn-all')?.addEventListener('click', () => {
  while (!bwDone) {
    stepBW();
  }
});

document.getElementById('bw-btn-backtrack')?.addEventListener('click', () => {
  if (!bwDone) {
    while (!bwDone) stepBW();
  }
  retroAudio.playSuccess();

  let w = bwCap;
  let selected = [];
  for (let i = bwItems.length; i > 0; i--) {
    if (dpTable[i][w] !== dpTable[i - 1][w]) {
      selected.push(bwItems[i - 1].name);
      w -= bwItems[i - 1].wt;
      const cell = document.getElementById(`dp-cell-${i}-${w + bwItems[i - 1].wt}`);
      if (cell) cell.style.background = '#ca8a04';
    }
  }

  bwDialogue.innerHTML = `🔍 <strong>Black Widow Backtrack:</strong> "Payload recovered: <strong>${selected.join(' + ')}</strong>! Total value = ${dpTable[bwItems.length][bwCap]} within W = 6 kg!"`;
});

document.getElementById('bw-btn-reset')?.addEventListener('click', () => {
  initBWTable();
  bwActor.style.left = '20px';
  bwActor.style.top = '15px';
  bwOptLabel.textContent = '0';
  bwDialogue.innerHTML = `💬 <strong>Black Widow:</strong> "Mainframe reset. 2D DP recurrence table ready to populate."`;
});

initBWTable();
"""
}
