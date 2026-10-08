
# 6. GROOT: Yggdrasil Binary Search Tree Canopy
SIMULATIONS["tree"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #16a34a;">MISSION: GROOT'S YGGDRASIL BST CANOPY</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Grow branches left (< smaller) and right (> greater). Groot navigates tree depth in O(log N)!</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #22c55e; padding: 6px 10px; border: 1px solid #475569;">
      SEARCH COST: <span id="groot-cost" style="color: #38bdf8;">O(LOG N)</span>
    </div>
  </div>

  <!-- Custom Node Insert / Search Input -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; align-items: center; gap: 8px;">
      <label style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a;">SEARCH / INSERT KEY:</label>
      <input type="number" id="groot-key-input" value="65" style="width: 60px; padding: 4px; font-family: var(--font-code); font-weight: bold; border: 2px solid #0f172a; text-align: center;">
      <button class="pixel-btn pixel-btn-primary" id="groot-btn-search" style="padding: 4px 10px; font-size: 0.58rem;">🔍 SEARCH TREE</button>
    </div>
    <div style="font-size: 0.75rem; color: #475569; font-weight: 600;">
      Invariant: Left &lt; Root &lt; Right
    </div>
  </div>

  <!-- Animated Tree Stage -->
  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 220px;">
    <!-- Groot Actor Sprite -->
    <div id="groot-actor" style="position: absolute; top: 10px; left: 20px; transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1); z-index: 10;">
      <img src="assets/groot.png" style="width: 48px; height: 56px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 4px 8px rgba(22,163,74,0.7));">
    </div>

    <!-- Tree SVG Render Stage -->
    <div style="display: flex; flex-direction: column; align-items: center; gap: 14px; font-family: var(--font-pixel); font-size: 0.65rem; color: #fff;">
      <div id="tn-root" style="background: #16a34a; padding: 8px 18px; border: 2px solid #fff; border-radius: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.5); transition: all 0.3s;">ROOT: [50]</div>
      <div style="display: flex; gap: 90px; align-items: center;">
        <div id="tn-l" style="background: #15803d; padding: 8px 14px; border: 2px solid #fff; border-radius: 20px; transition: all 0.3s;">L: [25]</div>
        <div id="tn-r" style="background: #15803d; padding: 8px 14px; border: 2px solid #fff; border-radius: 20px; transition: all 0.3s;">R: [75]</div>
      </div>
      <div style="display: flex; gap: 35px; align-items: center; font-size: 0.58rem;">
        <div id="tn-ll" style="background: #14532d; padding: 6px 10px; border: 1px solid #fff; border-radius: 16px; transition: all 0.3s;">LL: [12]</div>
        <div id="tn-lr" style="background: #14532d; padding: 6px 10px; border: 1px solid #fff; border-radius: 16px; transition: all 0.3s;">LR: [38]</div>
        <div id="tn-rl" style="background: #14532d; padding: 6px 10px; border: 1px solid #fff; border-radius: 16px; transition: all 0.3s;">RL: [65]</div>
        <div id="tn-rr" style="background: #14532d; padding: 6px 10px; border: 1px solid #fff; border-radius: 16px; transition: all 0.3s;">RR: [90]</div>
      </div>
    </div>
  </div>

  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; font-size: 0.88rem; min-height: 48px; display: flex; align-items: center;" id="groot-dialogue">
    💬 <strong>Groot:</strong> "I am Groot! (At every node, comparing target with root eliminates half the tree. Search cost is O(log n).)"
  </div>

  <div class="viz-controls" style="display: flex; gap: 10px; flex-wrap: wrap;">
    <button class="pixel-btn pixel-btn-primary" id="groot-btn-auto">▶ AUTO-SEARCH SAMPLE [65]</button>
    <button class="pixel-btn pixel-btn-secondary" id="groot-btn-search-min">🌿 FIND MINIMUM [12]</button>
    <button class="pixel-btn pixel-btn-secondary" id="groot-btn-search-max">🌳 FIND MAXIMUM [90]</button>
    <button class="pixel-btn pixel-btn-secondary" id="groot-btn-reset">↺ RESET TREE</button>
  </div>
</div>
""",
    "script": """
const grootActor = document.getElementById('groot-actor');
const grootDiag = document.getElementById('groot-dialogue');
const grootKeyIn = document.getElementById('groot-key-input');
const nodes = {
  root: document.getElementById('tn-root'),
  l: document.getElementById('tn-l'),
  r: document.getElementById('tn-r'),
  ll: document.getElementById('tn-ll'),
  lr: document.getElementById('tn-lr'),
  rl: document.getElementById('tn-rl'),
  rr: document.getElementById('tn-rr')
};

function clearGrootHighlights() {
  Object.values(nodes).forEach(n => {
    n.style.background = '';
    n.style.borderColor = '#fff';
    n.style.boxShadow = '';
  });
}

function searchTreeVal(val) {
  clearGrootHighlights();
  nodes.root.style.background = '#f59e0b';
  grootActor.style.top = `${nodes.root.offsetTop - 15}px`;
  grootActor.style.left = `${nodes.root.offsetLeft - 50}px`;
  grootDiag.innerHTML = `💬 <strong>Groot:</strong> "I am Groot! Comparing target ${val} with Root [50]..."`;

  setTimeout(() => {
    if (val < 50) {
      nodes.root.style.background = '#1e293b';
      nodes.l.style.background = '#f59e0b';
      grootActor.style.top = `${nodes.l.offsetTop - 15}px`;
      grootActor.style.left = `${nodes.l.offsetLeft - 50}px`;
      grootDiag.innerHTML = `💬 <strong>Groot:</strong> "${val} &lt; 50! Branch left to node [25]! Right subtree pruned in O(1) step!"`;
      setTimeout(() => {
        const leaf = val < 25 ? nodes.ll : nodes.lr;
        nodes.l.style.background = '#1e293b';
        leaf.style.background = '#22c55e';
        leaf.style.boxShadow = '0 0 12px #22c55e';
        grootActor.style.top = `${leaf.offsetTop - 15}px`;
        grootActor.style.left = `${leaf.offsetLeft - 45}px`;
        grootDiag.innerHTML = `✨ <strong>Groot:</strong> "I am Groot! Target found or positioned at leaf in just 2 steps = O(log n)!"`;
      }, 900);
    } else {
      nodes.root.style.background = '#1e293b';
      nodes.r.style.background = '#f59e0b';
      grootActor.style.top = `${nodes.r.offsetTop - 15}px`;
      grootActor.style.left = `${nodes.r.offsetLeft - 50}px`;
      grootDiag.innerHTML = `💬 <strong>Groot:</strong> "${val} &gt; 50! Branch right to node [75]! Left subtree eliminated!"`;
      setTimeout(() => {
        const leaf = val < 75 ? nodes.rl : nodes.rr;
        nodes.r.style.background = '#1e293b';
        leaf.style.background = '#22c55e';
        leaf.style.boxShadow = '0 0 12px #22c55e';
        grootActor.style.top = `${leaf.offsetTop - 15}px`;
        grootActor.style.left = `${leaf.offsetLeft - 45}px`;
        grootDiag.innerHTML = `✨ <strong>Groot:</strong> "I am Groot! Leaf node accessed with logarithmic height bound!"`;
      }, 900);
    }
  }, 900);
}

document.getElementById('groot-btn-search')?.addEventListener('click', () => {
  retroAudio.playClick();
  searchTreeVal(parseInt(grootKeyIn.value) || 65);
});
document.getElementById('groot-btn-auto')?.addEventListener('click', () => { retroAudio.playClick(); searchTreeVal(65); });
document.getElementById('groot-btn-search-min')?.addEventListener('click', () => { retroAudio.playClick(); searchTreeVal(12); });
document.getElementById('groot-btn-search-max')?.addEventListener('click', () => { retroAudio.playClick(); searchTreeVal(90); });
document.getElementById('groot-btn-reset')?.addEventListener('click', () => {
  retroAudio.playClick();
  clearGrootHighlights();
  grootActor.style.top = '10px';
  grootActor.style.left = '20px';
  grootDiag.innerHTML = '💬 <strong>Groot:</strong> "I am Groot! (Tree reset to nominal canopy state.)"';
});
"""
}

# 7. IRON MAN: J.A.R.V.I.S. Arc Reactor Hash Table (Dictionaries)
SIMULATIONS["hash"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #dc2626;">MISSION: J.A.R.V.I.S. ARC REACTOR HASH TABLE</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Map key strings directly to memory slots in O(1) average time via hash function h(k) = sum(k) mod 7.</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #facc15; padding: 6px 10px; border: 1px solid #475569;">
      SLOTS: 7 BUCKETS
    </div>
  </div>

  <!-- Custom Key Input Bar -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; align-items: center; gap: 8px;">
      <label style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a;">INSERT KEY / THREAT:</label>
      <input type="text" id="iron-key-input" value="ULTRON" style="width: 100px; padding: 4px; font-family: var(--font-code); font-weight: bold; border: 2px solid #0f172a; text-align: center; text-transform: uppercase;">
      <button class="pixel-btn pixel-btn-primary" id="iron-btn-insert" style="padding: 4px 10px; font-size: 0.58rem;">⚡ HASH & INSERT</button>
    </div>
    <div style="font-size: 0.75rem; color: #475569; font-weight: 600;">
      Avg Search/Insert: O(1)
    </div>
  </div>

  <!-- Animated Arena Stage -->
  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 200px;">
    <!-- Iron Man Actor Sprite -->
    <div id="iron-actor" style="position: absolute; top: 12px; left: 20px; transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1); z-index: 10;">
      <img src="assets/ironman.png" style="width: 48px; height: 56px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 0 10px rgba(220,38,38,0.7));">
    </div>

    <!-- 7 Hash Buckets Array -->
    <div id="iron-buckets-grid" style="display: grid; grid-template-columns: repeat(7, 1fr); gap: 6px; margin-top: 55px;">
      <!-- Populated dynamically -->
    </div>
  </div>

  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; font-size: 0.88rem; min-height: 48px; display: flex; align-items: center;" id="iron-dialogue">
    💬 <strong>Tony Stark:</strong> "J.A.R.V.I.S., initialize Arc Hash Matrix. Direct address indexing yields pure O(1) lookup speed!"
  </div>

  <div class="viz-controls" style="display: flex; gap: 10px; flex-wrap: wrap;">
    <button class="pixel-btn pixel-btn-primary" id="iron-btn-sample1">INSERT "THANOS"</button>
    <button class="pixel-btn pixel-btn-secondary" id="iron-btn-sample2">INSERT "LOKI"</button>
    <button class="pixel-btn pixel-btn-accent" id="iron-btn-collide">FORCE COLLISION</button>
    <button class="pixel-btn pixel-btn-secondary" id="iron-btn-reset">↺ RESET HASH TABLE</button>
  </div>
</div>
""",
    "script": """
const ironGrid = document.getElementById('iron-buckets-grid');
const ironKeyIn = document.getElementById('iron-key-input');
const ironDiag = document.getElementById('iron-dialogue');
const ironActor = document.getElementById('iron-actor');

let buckets = [[], [], [], [], [], [], []];

function renderBuckets() {
  ironGrid.innerHTML = '';
  for (let i = 0; i < 7; i++) {
    const b = document.createElement('div');
    b.id = `bucket-slot-${i}`;
    b.style.cssText = 'background: #1e293b; border: 2px solid #475569; padding: 8px 4px; border-radius: 4px; text-align: center; font-family: var(--font-pixel); font-size: 0.58rem; min-height: 80px; display: flex; flex-direction: column; gap: 4px; justify-content: flex-start; transition: all 0.3s;';
    b.innerHTML = `<span style="color:#facc15; border-bottom: 1px solid #475569; padding-bottom: 2px;">SLOT [${i}]</span>`;
    
    buckets[i].forEach(item => {
      const chip = document.createElement('div');
      chip.style.cssText = 'background: #dc2626; color: #fff; padding: 3px 2px; border-radius: 2px; font-size: 0.52rem; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; border: 1px solid #000; animation: popIn 0.3s;';
      chip.textContent = item;
      b.appendChild(chip);
    });
    ironGrid.appendChild(b);
  }
}
renderBuckets();

function insertKey(key) {
  if (!key) return;
  const upperKey = key.toUpperCase();
  let asciiSum = 0;
  for (let c of upperKey) asciiSum += c.charCodeAt(0);
  const slot = asciiSum % 7;

  const targetSlot = document.getElementById(`bucket-slot-${slot}`);
  if (targetSlot) {
    targetSlot.style.borderColor = '#facc15';
    targetSlot.style.background = '#451a03';
    ironActor.style.left = `${targetSlot.offsetLeft - 10}px`;
  }

  buckets[slot].push(upperKey);
  renderBuckets();

  if (buckets[slot].length > 1) {
    ironDiag.innerHTML = `⚡ <strong>J.A.R.V.I.S.:</strong> "Hash h('${upperKey}') = ${asciiSum} mod 7 = ${slot}. <strong>Collision detected!</strong> Chained to linked list in Slot [${slot}]. Avg lookup still O(1)!"`;
  } else {
    ironDiag.innerHTML = `🎯 <strong>Tony Stark:</strong> "Repulsor beam mapped '${upperKey}' directly to Slot [${slot}] in O(1) time flat!"`;
  }
}

document.getElementById('iron-btn-insert')?.addEventListener('click', () => {
  retroAudio.playClick();
  insertKey(ironKeyIn.value);
});
document.getElementById('iron-btn-sample1')?.addEventListener('click', () => { retroAudio.playClick(); insertKey('THANOS'); });
document.getElementById('iron-btn-sample2')?.addEventListener('click', () => { retroAudio.playClick(); insertKey('LOKI'); });
document.getElementById('iron-btn-collide')?.addEventListener('click', () => {
  retroAudio.playClick();
  insertKey('HYDRA');
  setTimeout(() => insertKey('KANG'), 500);
});
document.getElementById('iron-btn-reset')?.addEventListener('click', () => {
  retroAudio.playClick();
  buckets = [[], [], [], [], [], [], []];
  renderBuckets();
  ironActor.style.left = '20px';
  ironDiag.innerHTML = '💬 <strong>Tony Stark:</strong> "Arc Reactor Hash Table purged and reset."';
});
"""
}

# 8. SCARLET WITCH: Chaos Magic Disjoint Sets (Sets & Disjoint Sets)
SIMULATIONS["disjoint_set"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #be123c;">MISSION: CHAOS MAGIC UNION-FIND DISJOINT SETS</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Partition heroes into sets. Path compression flattens trees directly to representative root in O(α(N))!</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #f43f5e; padding: 6px 10px; border: 1px solid #475569;">
      COST: O(α(N)) ≈ O(1)
    </div>
  </div>

  <!-- Custom Union Input -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; align-items: center; gap: 8px;">
      <label style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a;">UNION NODES:</label>
      <input type="number" id="wanda-u-1" value="0" min="0" max="4" style="width: 44px; padding: 4px; font-weight: bold; border: 2px solid #0f172a; text-align: center;">
      <span style="font-weight: bold;">&</span>
      <input type="number" id="wanda-u-2" value="1" min="0" max="4" style="width: 44px; padding: 4px; font-weight: bold; border: 2px solid #0f172a; text-align: center;">
      <button class="pixel-btn pixel-btn-primary" id="wanda-btn-custom-union" style="padding: 4px 10px; font-size: 0.58rem;">🔮 UNION(X, Y)</button>
    </div>
    <div style="font-size: 0.75rem; color: #475569; font-weight: 600;">
      Find(x) Representative: Parent Array
    </div>
  </div>

  <!-- Animated Arena Stage -->
  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 200px;">
    <!-- Wanda Actor Sprite -->
    <div id="wanda-actor" style="position: absolute; top: 12px; right: 25px; z-index: 10;">
      <img src="assets/scarletwitch.png" style="width: 48px; height: 56px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 0 12px rgba(225,29,72,0.8));">
    </div>

    <!-- Nodes Display -->
    <div id="wanda-nodes-row" style="display: flex; justify-content: space-around; align-items: center; margin-top: 55px;">
      <!-- Populated dynamically -->
    </div>
  </div>

  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; font-size: 0.88rem; min-height: 48px; display: flex; align-items: center;" id="wanda-dialogue">
    💬 <strong>Scarlet Witch:</strong> "Chaos Magic partitions reality. Path compression flattens trees directly to the set root in inverse Ackermann O(α(N))!"
  </div>

  <div class="viz-controls" style="display: flex; gap: 10px; flex-wrap: wrap;">
    <button class="pixel-btn pixel-btn-primary" id="wanda-btn-union-sample">🔮 UNION(0, 1) & UNION(2, 3)</button>
    <button class="pixel-btn pixel-btn-accent" id="wanda-btn-merge-all">✨ UNION ALL TO ROOT [0]</button>
    <button class="pixel-btn pixel-btn-secondary" id="wanda-btn-compress">⚡ RUN PATH COMPRESSION</button>
    <button class="pixel-btn pixel-btn-secondary" id="wanda-btn-reset">↺ RESET SETS</button>
  </div>
</div>
""",
    "script": """
const wandaRow = document.getElementById('wanda-nodes-row');
const wandaDiag = document.getElementById('wanda-dialogue');
const wandaU1 = document.getElementById('wanda-u-1');
const wandaU2 = document.getElementById('wanda-u-2');

let parent = [0, 1, 2, 3, 4];
let rank = [0, 0, 0, 0, 0];

function findRoot(i) {
  if (parent[i] === i) return i;
  return parent[i] = findRoot(parent[i]); // Path compression
}

function unionNodes(x, y) {
  const rx = findRoot(x);
  const ry = findRoot(y);
  if (rx !== ry) {
    if (rank[rx] < rank[ry]) parent[rx] = ry;
    else if (rank[rx] > rank[ry]) parent[ry] = rx;
    else { parent[ry] = rx; rank[rx]++; }
    renderDisjointSets();
    wandaDiag.innerHTML = `🔮 <strong>Scarlet Witch:</strong> "Chaos bond forged! Union(${x}, ${y}) attached root [${ry}] under root [${rx}]. Set representative is [${findRoot(x)}]!"`;
  } else {
    wandaDiag.innerHTML = `⚠️ <strong>Scarlet Witch:</strong> "Nodes ${x} and ${y} are already in the same disjoint set under root [${rx}]! Cycle avoided!"`;
  }
}

function renderDisjointSets() {
  wandaRow.innerHTML = '';
  const colors = ['#dc2626', '#2563eb', '#16a34a', '#f59e0b', '#9333ea'];
  for (let i = 0; i < 5; i++) {
    const root = findRoot(i);
    const n = document.createElement('div');
    n.style.cssText = `background: ${colors[root]}; color: #fff; border: 3px solid #fff; border-radius: 50%; width: 55px; height: 55px; display: flex; flex-direction: column; align-items: center; justify-content: center; font-family: var(--font-pixel); font-size: 0.65rem; box-shadow: 0 4px 8px rgba(0,0,0,0.5); transition: all 0.3s;`;
    n.innerHTML = `Node ${i}<br><span style="font-size:0.5rem; color:#facc15;">R:[${root}]</span>`;
    wandaRow.appendChild(n);
  }
}
renderDisjointSets();

document.getElementById('wanda-btn-custom-union')?.addEventListener('click', () => {
  retroAudio.playClick();
  const u1 = parseInt(wandaU1.value) || 0;
  const u2 = parseInt(wandaU2.value) || 1;
  unionNodes(u1, u2);
});

document.getElementById('wanda-btn-union-sample')?.addEventListener('click', () => {
  retroAudio.playClick();
  unionNodes(0, 1);
  setTimeout(() => unionNodes(2, 3), 400);
});

document.getElementById('wanda-btn-merge-all')?.addEventListener('click', () => {
  retroAudio.playClick();
  for (let i = 1; i < 5; i++) unionNodes(0, i);
});

document.getElementById('wanda-btn-compress')?.addEventListener('click', () => {
  retroAudio.playClick();
  for (let i = 0; i < 5; i++) findRoot(i);
  renderDisjointSets();
  wandaDiag.innerHTML = '⚡ <strong>Scarlet Witch:</strong> "Path compression executed! Tree depth flattened directly to root representative!"';
});

document.getElementById('wanda-btn-reset')?.addEventListener('click', () => {
  retroAudio.playClick();
  parent = [0, 1, 2, 3, 4];
  rank = [0, 0, 0, 0, 0];
  renderDisjointSets();
  wandaDiag.innerHTML = '💬 <strong>Scarlet Witch:</strong> "Disjoint sets reset to 5 singleton independent partitions."';
});
"""
}

# 9. HAWKEYE: Min-Max Tournament Bracket (Maximum & Minimum)
SIMULATIONS["min_max"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #7c3aed;">MISSION: HAWKEYE PAIRWISE MIN-MAX TOURNAMENT</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Pair elements together to find Min and Max in theoretical lower bound ⌊3N/2⌋ − 2 comparisons!</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #c084fc; padding: 6px 10px; border: 1px solid #475569;">
      COMPARISONS: <span id="hawk-cmp-count" style="color: #22c55e;">0</span> (SAVED 25%)
    </div>
  </div>

  <!-- Custom Array Input -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; align-items: center; gap: 8px;">
      <label style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a;">CUSTOM ARRAY:</label>
      <input type="text" id="hawk-arr-input" value="28, 14, 95, 42, 7, 63" style="width: 180px; padding: 4px; font-family: var(--font-code); font-weight: bold; border: 2px solid #0f172a;">
      <button class="pixel-btn pixel-btn-primary" id="hawk-btn-load" style="padding: 4px 10px; font-size: 0.58rem;">LOAD ARRAY</button>
    </div>
    <div style="font-size: 0.75rem; color: #475569; font-weight: 600;">
      Current [MIN, MAX]: <span id="hawk-result-box" style="color: #7c3aed; font-weight: bold;">[?, ?]</span>
    </div>
  </div>

  <!-- Animated Arena Stage -->
  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 200px;">
    <!-- Hawkeye Actor Sprite -->
    <div id="hawk-actor" style="position: absolute; top: 12px; left: 20px; transition: all 0.4s ease; z-index: 10;">
      <img src="assets/hawkeye.png" style="width: 48px; height: 56px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 0 10px rgba(124,58,237,0.7));">
    </div>

    <!-- Array Bars Arena -->
    <div id="hawk-bars-arena" style="display: flex; gap: 12px; justify-content: center; align-items: flex-end; height: 120px; margin-top: 50px;">
      <!-- Populated dynamically -->
    </div>
  </div>

  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; font-size: 0.88rem; min-height: 48px; display: flex; align-items: center;" id="hawk-dialogue">
    💬 <strong>Hawkeye:</strong> "I never miss. Pairwise comparisons eliminate redundant scans, saving 25% comparisons over naive 2n − 2."
  </div>

  <div class="viz-controls" style="display: flex; gap: 10px; flex-wrap: wrap;">
    <button class="pixel-btn pixel-btn-primary" id="hawk-btn-auto">▶ AUTO-RUN TOURNAMENT</button>
    <button class="pixel-btn pixel-btn-secondary" id="hawk-btn-step">⏭ STEP PAIR COMPARISON</button>
    <button class="pixel-btn pixel-btn-secondary" id="hawk-btn-random">🎲 RANDOMIZE ARRAY</button>
    <button class="pixel-btn pixel-btn-secondary" id="hawk-btn-reset">↺ RESET</button>
  </div>
</div>
""",
    "script": """
const hawkArena = document.getElementById('hawk-bars-arena');
const hawkArrIn = document.getElementById('hawk-arr-input');
const hawkDiag = document.getElementById('hawk-dialogue');
const hawkRes = document.getElementById('hawk-result-box');
const hawkCmp = document.getElementById('hawk-cmp-count');
const hawkActor = document.getElementById('hawk-actor');

let arr = [28, 14, 95, 42, 7, 63];
let curMin = null, curMax = null;
let pairIdx = 0;
let comparisons = 0;
let hawkAutoTimer = null;

function renderHawkBars() {
  hawkArena.innerHTML = '';
  const maxVal = Math.max(...arr, 100);
  arr.forEach((val, idx) => {
    const bar = document.createElement('div');
    bar.id = `hawk-bar-${idx}`;
    const h = Math.round((val / maxVal) * 90) + 15;
    bar.style.cssText = `width: 44px; height: ${h}px; background: #334155; border: 2px solid #64748b; border-radius: 4px 4px 0 0; text-align: center; color: #fff; font-family: var(--font-pixel); font-size: 0.58rem; display: flex; align-items: flex-end; justify-content: center; padding-bottom: 4px; transition: all 0.3s;`;
    bar.textContent = val;
    hawkArena.appendChild(bar);
  });
}
renderHawkBars();

function stepPair() {
  if (pairIdx < arr.length - 1) {
    const i1 = pairIdx;
    const i2 = pairIdx + 1;
    const b1 = document.getElementById(`hawk-bar-${i1}`);
    const b2 = document.getElementById(`hawk-bar-${i2}`);

    b1.style.background = '#7c3aed';
    b2.style.background = '#7c3aed';
    hawkActor.style.left = `${b1.offsetLeft - 10}px`;

    comparisons++; // 1 comparison between the pair
    let localMin, localMax;
    if (arr[i1] < arr[i2]) { localMin = arr[i1]; localMax = arr[i2]; }
    else { localMin = arr[i2]; localMax = arr[i1]; }

    if (curMin === null || localMin < curMin) { curMin = localMin; comparisons++; }
    if (curMax === null || localMax > curMax) { curMax = localMax; comparisons++; }

    hawkCmp.textContent = comparisons;
    hawkRes.textContent = `[${curMin}, ${curMax}]`;
    hawkDiag.innerHTML = `🎯 <strong>Hawkeye:</strong> "Paired [${arr[i1]}, ${arr[i2]}]: winner ${localMax} compared with Max; loser ${localMin} compared with Min! 3 comparisons for 2 elements!"`;

    pairIdx += 2;
  } else {
    hawkDiag.innerHTML = `🏆 <strong>Hawkeye:</strong> "Tournament complete! MIN = ${curMin}, MAX = ${curMax} found in just ${comparisons} comparisons (theoretical lower bound ⌊3N/2⌋ − 2)!"`;
    if (hawkAutoTimer) { clearInterval(hawkAutoTimer); hawkAutoTimer = null; document.getElementById('hawk-btn-auto').textContent = '▶ AUTO-RUN TOURNAMENT'; }
  }
}

document.getElementById('hawk-btn-step')?.addEventListener('click', () => { retroAudio.playClick(); stepPair(); });
document.getElementById('hawk-btn-load')?.addEventListener('click', () => {
  retroAudio.playClick();
  const raw = hawkArrIn.value.split(',').map(x => parseInt(x.trim())).filter(x => !isNaN(x));
  if (raw.length > 0) { arr = raw; pairIdx = 0; comparisons = 0; curMin = null; curMax = null; renderHawkBars(); }
});
document.getElementById('hawk-btn-random')?.addEventListener('click', () => {
  retroAudio.playClick();
  arr = Array.from({length: 6}, () => Math.floor(Math.random() * 90) + 10);
  hawkArrIn.value = arr.join(', ');
  pairIdx = 0; comparisons = 0; curMin = null; curMax = null;
  renderHawkBars();
});
document.getElementById('hawk-btn-auto')?.addEventListener('click', function() {
  retroAudio.playClick();
  if (hawkAutoTimer) {
    clearInterval(hawkAutoTimer); hawkAutoTimer = null; this.textContent = '▶ AUTO-RUN TOURNAMENT';
  } else {
    this.textContent = '⏸ PAUSE TOURNAMENT';
    hawkAutoTimer = setInterval(() => stepPair(), 800);
  }
});
document.getElementById('hawk-btn-reset')?.addEventListener('click', () => {
  retroAudio.playClick();
  if (hawkAutoTimer) { clearInterval(hawkAutoTimer); hawkAutoTimer = null; document.getElementById('hawk-btn-auto').textContent = '▶ AUTO-RUN TOURNAMENT'; }
  pairIdx = 0; comparisons = 0; curMin = null; curMax = null;
  hawkCmp.textContent = '0';
  hawkRes.textContent = '[?, ?]';
  renderHawkBars();
});
"""
}

# 10. SPIDER-MAN: Web-Zipping Binary Search (Binary Search)
SIMULATIONS["binary_search"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #dc2626;">MISSION: SPIDER-MAN WEB-SLINGING BINARY SEARCH</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Watch Spidey web-zip to mid=(low+high)//2 on each step, halving the search space in O(log N)!</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #38bdf8; padding: 6px 10px; border: 1px solid #475569;">
      SEARCH COST: O(log₂ N)
    </div>
  </div>

  <!-- Custom Sorted Array & Target Input -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; align-items: center; gap: 8px;">
      <label style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a;">SORTED ARRAY:</label>
      <input type="text" id="spidey-arr-input" value="4, 12, 19, 27, 35, 48, 62, 75, 88" style="width: 190px; padding: 4px; font-family: var(--font-code); font-weight: bold; border: 2px solid #0f172a;">
    </div>
    <div style="display: flex; align-items: center; gap: 8px;">
      <label style="font-family: var(--font-pixel); font-size: 0.62rem; color: #dc2626;">TARGET:</label>
      <input type="number" id="spidey-target-input" value="48" style="width: 55px; padding: 4px; font-family: var(--font-code); font-weight: bold; border: 2px solid #0f172a; text-align: center;">
      <button class="pixel-btn pixel-btn-primary" id="spidey-btn-load" style="padding: 4px 10px; font-size: 0.58rem;">LOAD & SEEK</button>
    </div>
  </div>

  <!-- Animated Arena Stage -->
  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 220px;">
    <!-- Spider-Man Web-Zip Actor -->
    <div id="spidey-actor" style="position: absolute; top: 15px; left: 40px; transition: all 0.45s cubic-bezier(0.34, 1.56, 0.64, 1); z-index: 10;">
      <img src="assets/spiderman.png" style="width: 48px; height: 56px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 0 12px rgba(220,38,38,0.8));">
    </div>

    <!-- Pointers Indicator Bar -->
    <div style="display: flex; justify-content: space-between; font-family: var(--font-pixel); font-size: 0.62rem; color: #94a3b8; margin-top: 50px; margin-bottom: 8px;">
      <span id="spidey-low-lbl" style="color: #38bdf8;">LOW: 0</span>
      <span id="spidey-mid-lbl" style="color: #facc15;">MID: ?</span>
      <span id="spidey-high-lbl" style="color: #ef4444;">HIGH: 8</span>
    </div>

    <!-- Array Elements Grid -->
    <div id="spidey-elements-row" style="display: flex; gap: 8px; justify-content: center; overflow-x: auto; padding: 8px 0;">
      <!-- Populated dynamically -->
    </div>
  </div>

  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; font-size: 0.88rem; min-height: 48px; display: flex; align-items: center;" id="spidey-dialogue">
    💬 <strong>Spider-Man:</strong> "My Spidey-Sense halves the search grid with every web-zip! Click Auto-Run or Step!"
  </div>

  <div class="viz-controls" style="display: flex; gap: 10px; flex-wrap: wrap;">
    <button class="pixel-btn pixel-btn-primary" id="spidey-btn-auto">▶ AUTO WEB-ZIP SEARCH</button>
    <button class="pixel-btn pixel-btn-secondary" id="spidey-btn-step">⏭ STEP WEB-ZIP</button>
    <button class="pixel-btn pixel-btn-secondary" id="spidey-btn-reset">↺ RESET SEARCH</button>
  </div>
</div>
""",
    "script": """
const spideyRow = document.getElementById('spidey-elements-row');
const spideyArrIn = document.getElementById('spidey-arr-input');
const spideyTargetIn = document.getElementById('spidey-target-input');
const spideyDiag = document.getElementById('spidey-dialogue');
const spideyActor = document.getElementById('spidey-actor');
const spideyLowLbl = document.getElementById('spidey-low-lbl');
const spideyMidLbl = document.getElementById('spidey-mid-lbl');
const spideyHighLbl = document.getElementById('spidey-high-lbl');

let sArr = [4, 12, 19, 27, 35, 48, 62, 75, 88];
let sTarget = 48;
let sLow = 0, sHigh = sArr.length - 1;
let sStepDone = false;
let sAutoTimer = null;

function renderSpideyGrid() {
  spideyRow.innerHTML = '';
  sArr.forEach((val, idx) => {
    const el = document.createElement('div');
    el.id = `spidey-cell-${idx}`;
    el.style.cssText = 'background: #1e293b; color: #fff; border: 2px solid #475569; padding: 12px 10px; border-radius: 4px; font-family: var(--font-pixel); font-size: 0.65rem; min-width: 48px; text-align: center; transition: all 0.3s;';
    el.innerHTML = `[${idx}]<br><strong style="font-size:0.8rem; color:#facc15;">${val}</strong>`;
    spideyRow.appendChild(el);
  });
  spideyLowLbl.textContent = `LOW: ${sLow}`;
  spideyHighLbl.textContent = `HIGH: ${sHigh}`;
  spideyMidLbl.textContent = 'MID: ?';
}
renderSpideyGrid();

function stepSpideyBinary() {
  if (sLow <= sHigh && !sStepDone) {
    const mid = Math.floor((sLow + sHigh) / 2);
    spideyLowLbl.textContent = `LOW: ${sLow}`;
    spideyHighLbl.textContent = `HIGH: ${sHigh}`;
    spideyMidLbl.textContent = `MID: ${mid}`;

    const midCell = document.getElementById(`spidey-cell-${mid}`);
    if (midCell) {
      midCell.style.background = '#0284c7';
      midCell.style.borderColor = '#38bdf8';
      spideyActor.style.left = `${midCell.offsetLeft + 10}px`;
    }

    if (sArr[mid] === sTarget) {
      midCell.style.background = '#22c55e';
      midCell.style.boxShadow = '0 0 14px #22c55e';
      spideyDiag.innerHTML = `🎉 <strong>Spider-Man:</strong> "TARGET ${sTarget} ACQUIRED AT INDEX [${mid}]! Found in O(log n) web-zips!"`;
      sStepDone = true;
      if (sAutoTimer) { clearInterval(sAutoTimer); sAutoTimer = null; document.getElementById('spidey-btn-auto').textContent = '▶ AUTO WEB-ZIP SEARCH'; }
    } else if (sArr[mid] < sTarget) {
      // Discard left half
      for (let i = sLow; i <= mid; i++) {
        const c = document.getElementById(`spidey-cell-${i}`);
        if (c) c.style.opacity = '0.3';
      }
      spideyDiag.innerHTML = `🕸️ <strong>Spider-Man:</strong> "Array[${mid}] = ${sArr[mid]} &lt; ${sTarget}. Webbed up and discarded left half! New LOW = ${mid + 1}."`;
      sLow = mid + 1;
    } else {
      // Discard right half
      for (let i = mid; i <= sHigh; i++) {
        const c = document.getElementById(`spidey-cell-${i}`);
        if (c) c.style.opacity = '0.3';
      }
      spideyDiag.innerHTML = `🕸️ <strong>Spider-Man:</strong> "Array[${mid}] = ${sArr[mid]} &gt; ${sTarget}. Webbed up and discarded right half! New HIGH = ${mid - 1}."`;
      sHigh = mid - 1;
    }
  } else if (!sStepDone) {
    spideyDiag.innerHTML = `⚠️ <strong>Spider-Man:</strong> "Target ${sTarget} not present in sorted array! Low crossed High."`;
    sStepDone = true;
    if (sAutoTimer) { clearInterval(sAutoTimer); sAutoTimer = null; document.getElementById('spidey-btn-auto').textContent = '▶ AUTO WEB-ZIP SEARCH'; }
  }
}

document.getElementById('spidey-btn-step')?.addEventListener('click', () => { retroAudio.playClick(); stepSpideyBinary(); });
document.getElementById('spidey-btn-load')?.addEventListener('click', () => {
  retroAudio.playClick();
  const raw = spideyArrIn.value.split(',').map(x => parseInt(x.trim())).filter(x => !isNaN(x));
  if (raw.length > 0) {
    sArr = raw.sort((a,b) => a-b);
    spideyArrIn.value = sArr.join(', ');
    sTarget = parseInt(spideyTargetIn.value) || sArr[0];
    sLow = 0; sHigh = sArr.length - 1; sStepDone = false;
    renderSpideyGrid();
  }
});
document.getElementById('spidey-btn-auto')?.addEventListener('click', function() {
  retroAudio.playClick();
  if (sAutoTimer) {
    clearInterval(sAutoTimer); sAutoTimer = null; this.textContent = '▶ AUTO WEB-ZIP SEARCH';
  } else {
    this.textContent = '⏸ PAUSE SEARCH';
    sAutoTimer = setInterval(() => stepSpideyBinary(), 900);
  }
});
document.getElementById('spidey-btn-reset')?.addEventListener('click', () => {
  retroAudio.playClick();
  if (sAutoTimer) { clearInterval(sAutoTimer); sAutoTimer = null; document.getElementById('spidey-btn-auto').textContent = '▶ AUTO WEB-ZIP SEARCH'; }
  sLow = 0; sHigh = sArr.length - 1; sStepDone = false;
  spideyActor.style.left = '40px';
  renderSpideyGrid();
});
"""
}
