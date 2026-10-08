# physical_sims_part2.py - Topics 6 to 10
# 6. Groot: Trees & BST (Root-to-Leaf Branching & In-Order Traversal)
# 7. Iron Man: Hash Tables (Direct Hash Jump & Linear Probing)
# 8. Scarlet Witch: Disjoint Sets (Path Compression & Union by Rank)
# 9. Hawkeye: Tournament Min-Max (Pairwise Bracket Shooting)
# 10. Spider-Man: Binary Search (LOW, MID, HIGH & Web Eliminating Halves)

PHYSICAL_SIMS_PART2 = {}

# 6. GROOT: Trees & BST
PHYSICAL_SIMS_PART2["tree"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #15803d;">MISSION: YGGDRASIL DATA CANOPY (BST)</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Watch Groot branch left (<) and right (>) from the root to insert and search keys.</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #facc15; padding: 6px 10px; border: 1px solid #475569;">
      TREE HEIGHT: <span id="groot-height" style="color: #38bdf8;">3</span> | NODES: <span id="groot-node-count" style="color: #22c55e;">5</span>
    </div>
  </div>

  <!-- Custom User Input Bar -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; align-items: center; gap: 10px;">
      <label style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a;">INSERT / SEARCH KEY:</label>
      <input type="number" id="groot-input-val" value="25" min="1" max="99" style="width: 60px; padding: 4px; font-family: var(--font-code); font-weight: bold; border: 2px solid #0f172a; text-align: center;">
    </div>
    <div style="font-family: var(--font-code); font-size: 0.8rem; font-weight: bold; color: #15803d;">
      INVARIANT: LEFT < NODE < RIGHT | TIME: O(log N)
    </div>
  </div>

  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 270px; overflow: hidden;">
    <!-- Groot Physical Actor -->
    <div id="groot-actor" style="position: absolute; top: 15px; left: 40px; transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1); z-index: 20; display: flex; flex-direction: column; align-items: center;">
      <div style="font-family: var(--font-pixel); font-size: 0.5rem; background: #15803d; color: #fff; padding: 1px 4px; border-radius: 2px; margin-bottom: 2px;">⸙ GROOT</div>
      <img src="assets/groot.png" style="width: 44px; height: 50px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 4px 8px rgba(21,128,61,0.6));">
    </div>

    <!-- Tree SVG Visualization Canvas -->
    <svg id="groot-tree-svg" style="width: 100%; height: 240px;">
      <!-- Connections -->
      <line x1="280" y1="40" x2="180" y2="100" stroke="#475569" stroke-width="2.5" id="line-root-left"/>
      <line x1="280" y1="40" x2="380" y2="100" stroke="#475569" stroke-width="2.5" id="line-root-right"/>
      <line x1="180" y1="100" x2="120" y2="170" stroke="#475569" stroke-width="2.5" id="line-l-left"/>
      <line x1="180" y1="100" x2="230" y2="170" stroke="#475569" stroke-width="2.5" id="line-l-right"/>
      
      <!-- Nodes -->
      <g id="node-50"><circle cx="280" cy="40" r="20" fill="#15803d" stroke="#facc15" stroke-width="2"/><text x="280" y="44" fill="#fff" font-family="'Press Start 2P'" font-size="9" text-anchor="middle">50</text></g>
      <g id="node-30"><circle cx="180" cy="100" r="18" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/><text x="180" y="104" fill="#fff" font-family="'Press Start 2P'" font-size="8" text-anchor="middle">30</text></g>
      <g id="node-70"><circle cx="380" cy="100" r="18" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/><text x="380" y="104" fill="#fff" font-family="'Press Start 2P'" font-size="8" text-anchor="middle">70</text></g>
      <g id="node-20"><circle cx="120" cy="170" r="16" fill="#1e293b" stroke="#64748b" stroke-width="2"/><text x="120" y="174" fill="#fff" font-family="'Press Start 2P'" font-size="7" text-anchor="middle">20</text></g>
      <g id="node-40"><circle cx="230" cy="170" r="16" fill="#1e293b" stroke="#64748b" stroke-width="2"/><text x="230" y="174" fill="#fff" font-family="'Press Start 2P'" font-size="7" text-anchor="middle">40</text></g>
    </svg>
  </div>

  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 12px 16px; margin-bottom: 14px; min-height: 52px; display: flex; align-items: center;" id="groot-dialogue">
    💬 <strong>Groot:</strong> "I am Groot. (Select an action to branch through Yggdrasil.)"
  </div>

  <div class="viz-controls" style="display: flex; gap: 10px; flex-wrap: wrap;">
    <button class="pixel-btn pixel-btn-primary" id="groot-btn-insert">🌱 INSERT KEY</button>
    <button class="pixel-btn pixel-btn-secondary" id="groot-btn-search">🔍 SEARCH KEY</button>
    <button class="pixel-btn pixel-btn-secondary" id="groot-btn-inorder">Asc IN-ORDER WALK</button>
    <button class="pixel-btn pixel-btn-secondary" id="groot-btn-reset">↺ RESET TREE</button>
  </div>
</div>
""",
    "script": """
const grootActor = document.getElementById('groot-actor');
const grootDiag = document.getElementById('groot-dialogue');
const grootInput = document.getElementById('groot-input-val');
let grootIsBusy = false;

// INSERT: Groot walks down tree comparing keys
document.getElementById('groot-btn-insert')?.addEventListener('click', () => {
  if (grootIsBusy) return;
  grootIsBusy = true;
  retroAudio.playClick();
  const val = parseInt(grootInput.value) || 25;
  
  // Start at root (node 50 at cx=280, cy=40)
  grootActor.style.left = '250px';
  grootActor.style.top = '10px';
  grootDiag.innerHTML = `⸙ <strong>Groot:</strong> "I am Groot! (At Root 50: Is ${val} < 50? Yes! Branching Left...)"`;
  
  setTimeout(() => {
    retroAudio.playHover();
    // Move to Node 30 (cx=180, cy=100)
    grootActor.style.left = '150px';
    grootActor.style.top = '70px';
    
    setTimeout(() => {
      if (val < 30) {
        grootDiag.innerHTML = `⸙ <strong>Groot:</strong> "I am Groot! (At Node 30: Is ${val} < 30? Yes! Branching Left to Leaf 20...)"`;
        // Move to Node 20 (cx=120, cy=170)
        setTimeout(() => {
          grootActor.style.left = '90px';
          grootActor.style.top = '140px';
          retroAudio.playSuccess();
          grootDiag.innerHTML = `
            <div style="border-left: 4px solid #15803d; padding-left: 8px;">
              <strong style="color: #15803d;">⸙ INSERTION COMPLETE</strong><br>
              <span>Key ${val} inserted as leaf in O(log N) time. Invariant preserved!</span>
            </div>
          `;
          setTimeout(() => { grootActor.style.left = '40px'; grootActor.style.top = '15px'; grootIsBusy = false; }, 800);
        }, 500);
      } else {
        grootDiag.innerHTML = `⸙ <strong>Groot:</strong> "I am Groot! (At Node 30: Is ${val} > 30? Yes! Branching Right to Node 40...)"`;
        setTimeout(() => {
          grootActor.style.left = '200px';
          grootActor.style.top = '140px';
          retroAudio.playSuccess();
          grootDiag.innerHTML = `
            <div style="border-left: 4px solid #15803d; padding-left: 8px;">
              <strong style="color: #15803d;">⸙ INSERTION COMPLETE</strong><br>
              <span>Key ${val} inserted into right branch in O(log N) time.</span>
            </div>
          `;
          setTimeout(() => { grootActor.style.left = '40px'; grootActor.style.top = '15px'; grootIsBusy = false; }, 800);
        }, 500);
      }
    }, 600);
  }, 600);
});

// SEARCH: Groot traverses node path
document.getElementById('groot-btn-search')?.addEventListener('click', () => {
  if (grootIsBusy) return;
  grootIsBusy = true;
  retroAudio.playClick();
  const target = parseInt(grootInput.value) || 40;
  
  grootActor.style.left = '250px'; grootActor.style.top = '10px';
  grootDiag.innerHTML = `🔍 <strong>Groot:</strong> "Searching for Key ${target}. Inspecting Root 50..."`;
  
  setTimeout(() => {
    if (target < 50) {
      grootActor.style.left = '150px'; grootActor.style.top = '70px';
      grootDiag.innerHTML = `🔍 <strong>Groot:</strong> "${target} < 50. Stepping into Left Subtree at Node 30..."`;
      setTimeout(() => {
        if (target === 40) {
          grootActor.style.left = '200px'; grootActor.style.top = '140px';
          retroAudio.playSuccess();
          grootDiag.innerHTML = `🎉 <strong>Groot:</strong> "I am Groot! (Found target key ${target} at Node 40 in 3 comparisons!)"`;
          setTimeout(() => { grootActor.style.left = '40px'; grootActor.style.top = '15px'; grootIsBusy = false; }, 800);
        } else {
          grootActor.style.left = '90px'; grootActor.style.top = '140px';
          retroAudio.playSuccess();
          grootDiag.innerHTML = `🎉 <strong>Groot:</strong> "Found target key ${target}!"`;
          setTimeout(() => { grootActor.style.left = '40px'; grootActor.style.top = '15px'; grootIsBusy = false; }, 800);
        }
      }, 600);
    } else {
      grootActor.style.left = '350px'; grootActor.style.top = '70px';
      grootDiag.innerHTML = `🔍 <strong>Groot:</strong> "${target} > 50. Stepping into Right Subtree at Node 70..."`;
      setTimeout(() => {
        retroAudio.playSuccess();
        grootDiag.innerHTML = `🎉 <strong>Groot:</strong> "Target evaluated at Node 70!"`;
        setTimeout(() => { grootActor.style.left = '40px'; grootActor.style.top = '15px'; grootIsBusy = false; }, 800);
      }, 600);
    }
  }, 600);
});

// IN-ORDER: Visually visits 20 -> 30 -> 40 -> 50 -> 70
document.getElementById('groot-btn-inorder')?.addEventListener('click', () => {
  if (grootIsBusy) return;
  grootIsBusy = true;
  retroAudio.playClick();
  grootDiag.innerHTML = `🌿 <strong>Groot:</strong> "Beginning In-Order Traversal: Left -> Root -> Right. Outputting ascending order..."`;
  
  const sequence = [
    { name: '20', left: '90px', top: '140px' },
    { name: '30', left: '150px', top: '70px' },
    { name: '40', left: '200px', top: '140px' },
    { name: '50', left: '250px', top: '10px' },
    { name: '70', left: '350px', top: '70px' }
  ];
  
  let i = 0;
  const timer = setInterval(() => {
    if (i < sequence.length) {
      retroAudio.playHover();
      grootActor.style.left = sequence[i].left;
      grootActor.style.top = sequence[i].top;
      grootDiag.innerHTML = `🌿 <strong>In-Order Step ${i+1}:</strong> Visited Node [<strong>${sequence[i].name}</strong>]`;
      i++;
    } else {
      clearInterval(timer);
      retroAudio.playSuccess();
      grootDiag.innerHTML = `✨ <strong>In-Order Result:</strong> [ 20, 30, 40, 50, 70 ] — Guaranteed strictly sorted order!`;
      setTimeout(() => { grootActor.style.left = '40px'; grootActor.style.top = '15px'; grootIsBusy = false; }, 800);
    }
  }, 600);
});

document.getElementById('groot-btn-reset')?.addEventListener('click', () => {
  retroAudio.playClick();
  grootActor.style.left = '40px';
  grootActor.style.top = '15px';
  grootDiag.innerHTML = `💬 <strong>Groot:</strong> "Tree reset to standard 5 nodes. Ready for traversal."`;
  grootIsBusy = false;
});
"""
}

# 7. IRON MAN: Dictionaries & Hash Tables
PHYSICAL_SIMS_PART2["hash"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #b91c1c;">MISSION: JARVIS TARGETING HASH TABLE</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Direct address jump: h(k) = k % 8. Watch Tony Stark fly straight to memory buckets in O(1) time.</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #facc15; padding: 6px 10px; border: 1px solid #475569;">
      LOAD FACTOR: <span id="stark-load" style="color: #38bdf8;">0.38</span> | BUCKETS: 8
    </div>
  </div>

  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; align-items: center; gap: 10px;">
      <label style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a;">KEY (INT):</label>
      <input type="number" id="stark-input-key" value="42" min="1" max="99" style="width: 60px; padding: 4px; font-family: var(--font-code); font-weight: bold; border: 2px solid #0f172a; text-align: center;">
      <label style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a;">VAL:</label>
      <input type="text" id="stark-input-val" value="Mark 42" style="width: 90px; padding: 4px; font-family: var(--font-code); font-weight: bold; border: 2px solid #0f172a; text-align: center;">
    </div>
    <div style="font-family: var(--font-code); font-size: 0.8rem; font-weight: bold; color: #b91c1c;">
      HASH FORMULA: h(k) = k % 8 | AVG: O(1)
    </div>
  </div>

  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 220px;">
    <div id="stark-actor" style="position: absolute; top: 15px; left: 30px; transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1); z-index: 20; display: flex; flex-direction: column; align-items: center;">
      <div style="font-family: var(--font-pixel); font-size: 0.5rem; background: #b91c1c; color: #fff; padding: 1px 4px; border-radius: 2px; margin-bottom: 2px;">◉ STARK</div>
      <img src="assets/ironman.png" style="width: 46px; height: 52px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 4px 8px rgba(185,28,28,0.7));">
    </div>

    <!-- 8 Hash Buckets Grid -->
    <div id="stark-buckets-grid" style="display: grid; grid-template-columns: repeat(8, 1fr); gap: 6px; margin-top: 85px;">
      <!-- Generated via JS -->
    </div>
  </div>

  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 12px 16px; margin-bottom: 14px; min-height: 52px; display: flex; align-items: center;" id="stark-dialogue">
    💬 <strong>Tony Stark:</strong> "Enter a key to watch JARVIS compute the hash index and jump directly to memory."
  </div>

  <div class="viz-controls" style="display: flex; gap: 10px; flex-wrap: wrap;">
    <button class="pixel-btn pixel-btn-primary" id="stark-btn-insert">◉ INSERT KEY</button>
    <button class="pixel-btn pixel-btn-secondary" id="stark-btn-search">🔍 SEARCH KEY</button>
    <button class="pixel-btn pixel-btn-secondary" id="stark-btn-reset">↺ RESET TABLE</button>
  </div>
</div>
""",
    "script": """
const starkGrid = document.getElementById('stark-buckets-grid');
const starkActor = document.getElementById('stark-actor');
const starkDiag = document.getElementById('stark-dialogue');
const starkKey = document.getElementById('stark-input-key');
const starkVal = document.getElementById('stark-input-val');
const starkLoad = document.getElementById('stark-load');

let starkBuckets = Array(8).fill(null);
starkBuckets[1] = { key: 9, val: 'Hulkbuster' };
starkBuckets[3] = { key: 11, val: 'NanoSuit' };
starkBuckets[7] = { key: 23, val: 'ArcReactor' };
let starkIsBusy = false;

function renderStarkBuckets() {
  starkGrid.innerHTML = '';
  let count = 0;
  for (let i = 0; i < 8; i++) {
    const b = document.createElement('div');
    b.id = `stark-bucket-${i}`;
    b.style.cssText = 'background: #1e293b; border: 2px solid #475569; padding: 8px 4px; text-align: center; border-radius: 4px; min-height: 70px; display: flex; flex-direction: column; justify-content: space-between; transition: all 0.25s ease;';
    const entry = starkBuckets[i];
    if (entry) {
      count++;
      b.innerHTML = `
        <span style="font-family: var(--font-pixel); font-size: 0.55rem; color: #facc15;">[${i}]</span>
        <div style="background: #b91c1c; color: #fff; font-family: var(--font-code); font-size: 0.65rem; padding: 2px; border-radius: 2px; font-weight: bold;">k:${entry.key}</div>
        <span style="font-size: 0.55rem; color: #94a3b8; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">${entry.val}</span>
      `;
    } else {
      b.innerHTML = `
        <span style="font-family: var(--font-pixel); font-size: 0.55rem; color: #64748b;">[${i}]</span>
        <span style="font-family: var(--font-pixel); font-size: 0.5rem; color: #475569;">EMPTY</span>
        <span></span>
      `;
    }
    starkGrid.appendChild(b);
  }
  starkLoad.textContent = (count / 8).toFixed(2);
}
renderStarkBuckets();

// INSERT: Tony computes hash k % 8, flies to bucket, probes on collision
document.getElementById('stark-btn-insert')?.addEventListener('click', () => {
  if (starkIsBusy) return;
  starkIsBusy = true;
  retroAudio.playClick();
  const k = parseInt(starkKey.value) || 42;
  const v = starkVal.value || 'Data';
  const initialHash = k % 8;
  
  starkDiag.innerHTML = `◉ <strong>Tony Stark:</strong> "Computing hash: h(${k}) = ${k} % 8 = ${initialHash}. Flying to Bucket [${initialHash}]..."`;
  
  const bEl = document.getElementById(`stark-bucket-${initialHash}`);
  if (bEl) {
    const rect = bEl.getBoundingClientRect();
    const parentRect = starkGrid.getBoundingClientRect();
    starkActor.style.left = `${rect.left - parentRect.left + 15}px`;
    bEl.style.borderColor = '#facc15';
  }
  
  setTimeout(() => {
    // Check collision
    if (starkBuckets[initialHash] === null || starkBuckets[initialHash].key === k) {
      retroAudio.playSuccess();
      starkBuckets[initialHash] = { key: k, val: v };
      renderStarkBuckets();
      starkDiag.innerHTML = `
        <div style="border-left: 4px solid #b91c1c; padding-left: 8px;">
          <strong style="color: #b91c1c;">◉ DIRECT HIT: BUCKET [${initialHash}] STORED</strong><br>
          <span>Key ${k} placed with zero collisions in strictly <strong>O(1)</strong> time!</span>
        </div>
      `;
      setTimeout(() => { starkActor.style.left = '30px'; starkIsBusy = false; }, 800);
    } else {
      // Collision! Linear probe
      retroAudio.playHover();
      starkDiag.innerHTML = `⚠️ <strong>Collision!</strong> Bucket [${initialHash}] occupied by Key ${starkBuckets[initialHash].key}. Linear probing to next slot...`;
      let nextSlot = (initialHash + 1) % 8;
      
      setTimeout(() => {
        const nextB = document.getElementById(`stark-bucket-${nextSlot}`);
        if (nextB) {
          const rect = nextB.getBoundingClientRect();
          const parentRect = starkGrid.getBoundingClientRect();
          starkActor.style.left = `${rect.left - parentRect.left + 15}px`;
        }
        starkBuckets[nextSlot] = { key: k, val: v };
        renderStarkBuckets();
        retroAudio.playSuccess();
        starkDiag.innerHTML = `
          <div style="border-left: 4px solid #facc15; padding-left: 8px;">
            <strong style="color: #b45309;">◉ COLLISION RESOLVED: BUCKET [${nextSlot}]</strong><br>
            <span>Linear probe placed key ${k} in next open slot.</span>
          </div>
        `;
        setTimeout(() => { starkActor.style.left = '30px'; starkIsBusy = false; }, 800);
      }, 700);
    }
  }, 600);
});

// SEARCH: Tony jumps directly to hash bucket
document.getElementById('stark-btn-search')?.addEventListener('click', () => {
  if (starkIsBusy) return;
  starkIsBusy = true;
  retroAudio.playClick();
  const k = parseInt(starkKey.value) || 42;
  const hashIdx = k % 8;
  
  starkDiag.innerHTML = `🔍 <strong>Tony Stark:</strong> "JARVIS jumping directly to calculated address: h(${k}) = ${hashIdx}..."`;
  const bEl = document.getElementById(`stark-bucket-${hashIdx}`);
  if (bEl) {
    const rect = bEl.getBoundingClientRect();
    const parentRect = starkGrid.getBoundingClientRect();
    starkActor.style.left = `${rect.left - parentRect.left + 15}px`;
    bEl.style.boxShadow = '0 0 12px #38bdf8';
  }
  
  setTimeout(() => {
    const item = starkBuckets[hashIdx];
    if (item && item.key === k) {
      retroAudio.playSuccess();
      starkDiag.innerHTML = `🎉 <strong>Target Acquired!</strong> Key ${k} found at Bucket [${hashIdx}] -> "${item.val}" in <strong>O(1)</strong>!`;
    } else {
      starkDiag.innerHTML = `⚠️ <strong>Key ${k} not at primary hash address.</strong> Probing sequence evaluated.`;
    }
    setTimeout(() => {
      if (bEl) bEl.style.boxShadow = 'none';
      starkActor.style.left = '30px';
      starkIsBusy = false;
    }, 800);
  }, 600);
});

document.getElementById('stark-btn-reset')?.addEventListener('click', () => {
  retroAudio.playClick();
  starkBuckets = Array(8).fill(null);
  starkBuckets[1] = { key: 9, val: 'Hulkbuster' };
  starkBuckets[3] = { key: 11, val: 'NanoSuit' };
  renderStarkBuckets();
  starkActor.style.left = '30px';
  starkDiag.innerHTML = `💬 <strong>Tony Stark:</strong> "Hash table reset to baseline cache."`;
  starkIsBusy = false;
});
"""
}

# 8. SCARLET WITCH: Sets & Disjoint Sets (DSU)
PHYSICAL_SIMS_PART2["disjoint_set"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #e11d48;">MISSION: MULTIVERSE NEXUS PARTITION (DSU)</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Find root universes and union disjoint components in O(α(N)) near-constant time.</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #facc15; padding: 6px 10px; border: 1px solid #475569;">
      COMPONENTS: <span id="wanda-comp-count" style="color: #38bdf8;">4</span>
    </div>
  </div>

  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; align-items: center; gap: 10px;">
      <label style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a;">UNION (U, V):</label>
      <input type="number" id="wanda-u" value="1" min="0" max="4" style="width: 45px; padding: 4px; font-family: var(--font-code); font-weight: bold; border: 2px solid #0f172a; text-align: center;">
      <span>⟷</span>
      <input type="number" id="wanda-v" value="3" min="0" max="4" style="width: 45px; padding: 4px; font-family: var(--font-code); font-weight: bold; border: 2px solid #0f172a; text-align: center;">
    </div>
    <div style="font-family: var(--font-code); font-size: 0.8rem; font-weight: bold; color: #e11d48;">
      HEURISTICS: UNION BY RANK + PATH COMPRESSION
    </div>
  </div>

  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 220px;">
    <div id="wanda-actor" style="position: absolute; top: 15px; left: 30px; transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1); z-index: 20; display: flex; flex-direction: column; align-items: center;">
      <div style="font-family: var(--font-pixel); font-size: 0.5rem; background: #e11d48; color: #fff; padding: 1px 4px; border-radius: 2px; margin-bottom: 2px;">✧ WANDA</div>
      <img src="assets/scarletwitch.png" style="width: 46px; height: 52px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 4px 8px rgba(225,29,72,0.7));">
    </div>

    <!-- 5 Nodes Representation -->
    <div id="wanda-nodes-grid" style="display: flex; gap: 16px; justify-content: center; margin-top: 85px;">
      <!-- Populated via JS -->
    </div>
  </div>

  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 12px 16px; margin-bottom: 14px; min-height: 52px; display: flex; align-items: center;" id="wanda-dialogue">
    💬 <strong>Scarlet Witch:</strong> "5 timeline realities initialized. Select two nodes to merge into a common nexus."
  </div>

  <div class="viz-controls" style="display: flex; gap: 10px; flex-wrap: wrap;">
    <button class="pixel-btn pixel-btn-primary" id="wanda-btn-union">✧ UNION(U, V)</button>
    <button class="pixel-btn pixel-btn-secondary" id="wanda-btn-find">🔍 FIND ROOT</button>
    <button class="pixel-btn pixel-btn-secondary" id="wanda-btn-reset">↺ RESET REALITIES</button>
  </div>
</div>
""",
    "script": """
const wandaGrid = document.getElementById('wanda-nodes-grid');
const wandaActor = document.getElementById('wanda-actor');
const wandaDiag = document.getElementById('wanda-dialogue');
const wandaU = document.getElementById('wanda-u');
const wandaV = document.getElementById('wanda-v');
const wandaComp = document.getElementById('wanda-comp-count');

let parent = [0, 0, 2, 2, 4];
let rank = [1, 0, 1, 0, 0];
let wandaBusy = false;

function findRoot(i) {
  if (parent[i] !== i) {
    parent[i] = findRoot(parent[i]); // Path compression
  }
  return parent[i];
}

function renderWandaNodes() {
  wandaGrid.innerHTML = '';
  const roots = new Set();
  for (let i = 0; i < 5; i++) {
    roots.add(findRoot(i));
    const n = document.createElement('div');
    n.id = `wanda-node-${i}`;
    const p = parent[i];
    n.style.cssText = 'background: #1e293b; border: 2px solid #e11d48; width: 65px; height: 65px; border-radius: 50%; display: flex; flex-direction: column; align-items: center; justify-content: center; font-family: var(--font-pixel); font-size: 0.65rem; color: #fff; transition: all 0.3s ease;';
    n.innerHTML = `
      <span>T-${i}</span>
      <small style="font-size:0.5rem; color:#facc15;">p:${p}</small>
    `;
    wandaGrid.appendChild(n);
  }
  wandaComp.textContent = roots.size;
}
renderWandaNodes();

document.getElementById('wanda-btn-union')?.addEventListener('click', () => {
  if (wandaBusy) return;
  wandaBusy = true;
  retroAudio.playClick();
  const u = Math.max(0, Math.min(4, parseInt(wandaU.value) || 0));
  const v = Math.max(0, Math.min(4, parseInt(wandaV.value) || 0));
  
  const rootU = findRoot(u);
  const rootV = findRoot(v);
  
  wandaActor.style.left = '200px';
  wandaDiag.innerHTML = `✧ <strong>Scarlet Witch:</strong> "Tracing roots: find(${u}) = ${rootU}, find(${v}) = ${rootV}..."`;
  
  setTimeout(() => {
    if (rootU === rootV) {
      retroAudio.playError();
      wandaDiag.innerHTML = `⚠️ <strong>Cycle Detected!</strong> Reality T-${u} and T-${v} already belong to Nexus ${rootU}. Union skipped!`;
      setTimeout(() => { wandaActor.style.left = '30px'; wandaBusy = false; }, 800);
    } else {
      retroAudio.playSuccess();
      // Union by rank
      if (rank[rootU] < rank[rootV]) {
        parent[rootU] = rootV;
      } else if (rank[rootU] > rank[rootV]) {
        parent[rootV] = rootU;
      } else {
        parent[rootV] = rootU;
        rank[rootU]++;
      }
      renderWandaNodes();
      wandaDiag.innerHTML = `
        <div style="border-left: 4px solid #e11d48; padding-left: 8px;">
          <strong style="color: #e11d48;">✧ UNION COMPLETE</strong><br>
          <span>Merged Nexus ${rootV} into Nexus ${rootU}. Near-constant time: <strong>O(α(N))</strong>!</span>
        </div>
      `;
      setTimeout(() => { wandaActor.style.left = '30px'; wandaBusy = false; }, 800);
    }
  }, 600);
});

document.getElementById('wanda-btn-find')?.addEventListener('click', () => {
  if (wandaBusy) return;
  wandaBusy = true;
  retroAudio.playClick();
  const u = Math.max(0, Math.min(4, parseInt(wandaU.value) || 0));
  const r = findRoot(u);
  
  const nEl = document.getElementById(`wanda-node-${u}`);
  if (nEl) nEl.style.boxShadow = '0 0 16px #e11d48';
  
  wandaDiag.innerHTML = `🔍 <strong>Scarlet Witch:</strong> "Path compression activated! Reality T-${u} now points directly to Root Nexus T-${r}."`;
  renderWandaNodes();
  setTimeout(() => {
    if (nEl) nEl.style.boxShadow = 'none';
    wandaBusy = false;
  }, 800);
});

document.getElementById('wanda-btn-reset')?.addEventListener('click', () => {
  retroAudio.playClick();
  parent = [0, 0, 2, 2, 4];
  rank = [1, 0, 1, 0, 0];
  renderWandaNodes();
  wandaDiag.innerHTML = `💬 <strong>Scarlet Witch:</strong> "Disjoint sets reset."`;
  wandaBusy = false;
});
"""
}

# 9. HAWKEYE: Maximum & Minimum (Tournament Method)
PHYSICAL_SIMS_PART2["min_max"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #7c3aed;">MISSION: TOURNAMENT EXTREMES TARGETING</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Pair elements into brackets. Find both Min and Max in optimal 3n/2 - 2 comparisons.</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #facc15; padding: 6px 10px; border: 1px solid #475569;">
      COMPARISONS: <span id="hawk-comps" style="color: #38bdf8;">0</span> / 7 (SAVED 3)
    </div>
  </div>

  <!-- Custom Input Array -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; align-items: center; gap: 10px;">
      <label style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a;">ARRAY (6 INTS):</label>
      <input type="text" id="hawk-input-arr" value="22, 13, 88, 7, 31, 99" style="width: 200px; padding: 4px; font-family: var(--font-code); font-weight: bold; border: 2px solid #0f172a; text-align: center;">
      <button class="pixel-btn pixel-btn-secondary" id="hawk-btn-apply" style="padding: 4px 8px; font-size: 0.58rem;">APPLY</button>
    </div>
    <div style="font-family: var(--font-code); font-size: 0.8rem; font-weight: bold; color: #7c3aed;">
      BOUND: (3n/2) - 2 COMPS
    </div>
  </div>

  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 220px;">
    <div id="hawk-actor" style="position: absolute; top: 15px; left: 30px; transition: all 0.35s ease; z-index: 20; display: flex; flex-direction: column; align-items: center;">
      <div style="font-family: var(--font-pixel); font-size: 0.5rem; background: #7c3aed; color: #fff; padding: 1px 4px; border-radius: 2px; margin-bottom: 2px;">🏹 HAWKEYE</div>
      <img src="assets/hawkeye.png" style="width: 46px; height: 52px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 4px 8px rgba(124,58,237,0.7));">
    </div>

    <!-- Brackets Display: Pairs -> Winners & Losers -> Final Min/Max -->
    <div id="hawk-brackets-display" style="display: flex; flex-direction: column; gap: 10px; margin-top: 75px; align-items: center;">
      <!-- Populated dynamically -->
    </div>
  </div>

  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 12px 16px; margin-bottom: 14px; min-height: 52px; display: flex; align-items: center;" id="hawk-dialogue">
    💬 <strong>Hawkeye:</strong> "Quiver armed! Click 'Step Bracket' to fire paired targeting arrows."
  </div>

  <div class="viz-controls" style="display: flex; gap: 10px; flex-wrap: wrap;">
    <button class="pixel-btn pixel-btn-primary" id="hawk-btn-step">🏹 STEP BRACKET</button>
    <button class="pixel-btn pixel-btn-secondary" id="hawk-btn-auto">▶ AUTO TOURNAMENT</button>
    <button class="pixel-btn pixel-btn-secondary" id="hawk-btn-reset">↺ RESET</button>
  </div>
</div>
""",
    "script": """
const hawkDisplay = document.getElementById('hawk-brackets-display');
const hawkActor = document.getElementById('hawk-actor');
const hawkDiag = document.getElementById('hawk-dialogue');
const hawkComps = document.getElementById('hawk-comps');
const hawkInput = document.getElementById('hawk-input-arr');

let hawkArr = [22, 13, 88, 7, 31, 99];
let hawkStep = 0;
let hawkCompsCount = 0;
let hawkTimer = null;
let winners = [], losers = [];

function initHawkDisplay() {
  hawkDisplay.innerHTML = `
    <div style="display:flex; gap:10px;">
      ${hawkArr.map((v, i) => `<div id="h-item-${i}" style="background:#1e293b; color:#fff; border:2px solid #64748b; padding:8px 12px; font-family:var(--font-pixel); font-size:0.65rem; border-radius:3px;">${v}</div>`).join('')}
    </div>
  `;
  hawkStep = 0;
  hawkCompsCount = 0;
  hawkComps.textContent = '0';
  winners = [];
  losers = [];
}
initHawkDisplay();

document.getElementById('hawk-btn-apply')?.addEventListener('click', () => {
  const parts = hawkInput.value.split(',').map(s => parseInt(s.trim())).filter(n => !isNaN(n));
  if (parts.length >= 4) {
    hawkArr = parts.slice(0, 8);
    initHawkDisplay();
  }
});

function stepHawkTournament() {
  if (hawkStep === 0) {
    // Pairwise step: compare (arr[0], arr[1]), (arr[2], arr[3]), etc.
    hawkActor.style.left = '120px';
    hawkCompsCount += Math.floor(hawkArr.length / 2);
    hawkComps.textContent = hawkCompsCount;
    retroAudio.playHover();
    
    winners = [];
    losers = [];
    for (let i = 0; i < hawkArr.length; i += 2) {
      if (i + 1 < hawkArr.length) {
        if (hawkArr[i] > hawkArr[i+1]) {
          winners.push(hawkArr[i]);
          losers.push(hawkArr[i+1]);
        } else {
          winners.push(hawkArr[i+1]);
          losers.push(hawkArr[i]);
        }
      }
    }
    
    hawkDisplay.innerHTML += `
      <div style="display:flex; gap:20px; margin-top:8px;">
        <div style="background:#064e3b; border:1.5px solid #22c55e; padding:6px 10px; font-size:0.7rem; color:#fff; font-family:var(--font-code);">
          WINNERS (MAX POOL): [ ${winners.join(', ')} ]
        </div>
        <div style="background:#7f1d1d; border:1.5px solid #ef4444; padding:6px 10px; font-size:0.7rem; color:#fff; font-family:var(--font-code);">
          LOSERS (MIN POOL): [ ${losers.join(', ')} ]
        </div>
      </div>
    `;
    hawkDiag.innerHTML = `🏹 <strong>Round 1 (Pairwise):</strong> Shot ${Math.floor(hawkArr.length / 2)} arrows. Partitioned into Winner and Loser pools!`;
    hawkStep = 1;
  } else if (hawkStep === 1) {
    // Round 2: Compare winners for max, losers for min
    hawkActor.style.left = '320px';
    const globalMax = Math.max(...winners);
    const globalMin = Math.min(...losers);
    hawkCompsCount += (winners.length - 1) + (losers.length - 1);
    hawkComps.textContent = hawkCompsCount;
    retroAudio.playSuccess();
    
    hawkDisplay.innerHTML += `
      <div style="display:flex; gap:14px; margin-top:8px;">
        <div style="background:#facc15; color:#0f172a; padding:6px 12px; font-family:var(--font-pixel); font-size:0.65rem; border:2px solid #000;">
          GLOBAL MAX = ${globalMax}
        </div>
        <div style="background:#38bdf8; color:#0f172a; padding:6px 12px; font-family:var(--font-pixel); font-size:0.65rem; border:2px solid #000;">
          GLOBAL MIN = ${globalMin}
        </div>
      </div>
    `;
    hawkDiag.innerHTML = `
      <div style="border-left: 4px solid #7c3aed; padding-left: 8px;">
        <strong style="color: #7c3aed;">🎯 BULLSEYE! TOURNAMENT CONCLUDED</strong><br>
        <span>Found Min (${globalMin}) and Max (${globalMax}) in only <strong>${hawkCompsCount}</strong> comparisons (vs ${2*hawkArr.length - 2} naive)!</span>
      </div>
    `;
    hawkStep = 2;
  }
}

document.getElementById('hawk-btn-step')?.addEventListener('click', () => {
  retroAudio.playClick();
  stepHawkTournament();
});

document.getElementById('hawk-btn-auto')?.addEventListener('click', () => {
  retroAudio.playClick();
  if (hawkTimer) {
    clearInterval(hawkTimer); hawkTimer = null;
    document.getElementById('hawk-btn-auto').textContent = '▶ AUTO TOURNAMENT';
  } else {
    document.getElementById('hawk-btn-auto').textContent = '⏸ PAUSE';
    hawkTimer = setInterval(() => {
      if (hawkStep >= 2) {
        clearInterval(hawkTimer); hawkTimer = null;
        document.getElementById('hawk-btn-auto').textContent = '▶ AUTO TOURNAMENT';
      } else {
        stepHawkTournament();
      }
    }, 700);
  }
});

document.getElementById('hawk-btn-reset')?.addEventListener('click', () => {
  retroAudio.playClick();
  if (hawkTimer) { clearInterval(hawkTimer); hawkTimer = null; }
  initHawkDisplay();
  hawkActor.style.left = '30px';
  hawkDiag.innerHTML = `💬 <strong>Hawkeye:</strong> "Tournament bracket reset."`;
});
"""
}

# 10. SPIDER-MAN: Binary Search (LOW, MID, HIGH & Web Eliminating Halves)
PHYSICAL_SIMS_PART2["binary_search"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #dc2626;">MISSION: GREEN GOBLIN FREQUENCY TRAP</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Spider-Man calculates MID and shoots webs over eliminated halves to isolate the target.</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #facc15; padding: 6px 10px; border: 1px solid #475569;">
      COMPARISONS: <span id="spidey-comp-count" style="color: #38bdf8;">0</span> | RANGE: <span id="spidey-range">[0..7]</span>
    </div>
  </div>

  <!-- Custom User Inputs for Array and Target -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; align-items: center; gap: 8px;">
      <label style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a;">TARGET:</label>
      <input type="number" id="spidey-target-val" value="60" min="10" max="99" style="width: 55px; padding: 4px; font-family: var(--font-code); font-weight: bold; border: 2px solid #0f172a; text-align: center;">
      <label style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a; margin-left: 6px;">ARRAY:</label>
      <input type="text" id="spidey-custom-arr" value="10, 20, 30, 40, 50, 60, 70, 80" style="width: 210px; padding: 4px; font-family: var(--font-code); font-size: 0.75rem; border: 2px solid #0f172a; text-align: center;">
      <button class="pixel-btn pixel-btn-secondary" id="spidey-btn-apply" style="padding: 4px 8px; font-size: 0.58rem;">APPLY</button>
    </div>
    <div style="font-family: var(--font-code); font-size: 0.8rem; font-weight: bold; color: #dc2626;">
      INVARIANT: arr[low] ≤ TARGET ≤ arr[high]
    </div>
  </div>

  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 240px; display: flex; flex-direction: column; justify-content: center;">
    <!-- Spidey Physical Actor with Web Line -->
    <div id="spidey-actor" style="position: absolute; top: 15px; left: 40px; transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1); z-index: 20; display: flex; flex-direction: column; align-items: center;">
      <div style="font-family: var(--font-pixel); font-size: 0.5rem; background: #dc2626; color: #fff; padding: 1px 4px; border-radius: 2px; margin-bottom: 2px;">🕸 SPIDEY</div>
      <img src="assets/spiderman.png" style="width: 46px; height: 52px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 4px 8px rgba(220,38,38,0.7));">
    </div>

    <!-- Sorted Array Blocks Grid with LOW, MID, HIGH Markers -->
    <div id="spidey-array-grid" style="display: flex; gap: 8px; justify-content: center; margin-top: 60px;">
      <!-- Populated via JS -->
    </div>
  </div>

  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 12px 16px; margin-bottom: 14px; min-height: 52px; display: flex; align-items: center;" id="spidey-dialogue">
    💬 <strong>Spider-Man:</strong> "Spider-sense tingling! Click 'Step Search' to calculate MID and eliminate half the spectrum."
  </div>

  <div class="viz-controls" style="display: flex; gap: 10px; flex-wrap: wrap;">
    <button class="pixel-btn pixel-btn-primary" id="spidey-btn-step">🕸 STEP SEARCH (HALVE)</button>
    <button class="pixel-btn pixel-btn-secondary" id="spidey-btn-auto">▶ AUTO-PLAY</button>
    <button class="pixel-btn pixel-btn-secondary" id="spidey-btn-reset">↺ RESET</button>
  </div>
</div>
""",
    "script": """
const spideyGrid = document.getElementById('spidey-array-grid');
const spideyActor = document.getElementById('spidey-actor');
const spideyDiag = document.getElementById('spidey-dialogue');
const spideyTarget = document.getElementById('spidey-target-val');
const spideyCustomArr = document.getElementById('spidey-custom-arr');
const spideyComp = document.getElementById('spidey-comp-count');
const spideyRange = document.getElementById('spidey-range');

let sArr = [10, 20, 30, 40, 50, 60, 70, 80];
let sLow = 0, sHigh = 7, sMid = 3;
let sComps = 0;
let sFound = false;
let sTimer = null;

function renderSpideyGrid() {
  spideyGrid.innerHTML = '';
  sArr.forEach((v, idx) => {
    const b = document.createElement('div');
    b.id = `spidey-cell-${idx}`;
    const isMid = idx === sMid;
    const isLow = idx === sLow;
    const isHigh = idx === sHigh;
    
    b.style.cssText = `
      background: ${isMid ? '#dc2626' : (idx >= sLow && idx <= sHigh ? '#1e293b' : '#334155')};
      color: #fff;
      border: 2px solid ${isMid ? '#facc15' : '#475569'};
      padding: 10px 8px;
      font-family: var(--font-pixel);
      font-size: 0.65rem;
      border-radius: 4px;
      text-align: center;
      min-width: 55px;
      transition: all 0.3s ease;
      opacity: ${idx < sLow || idx > sHigh ? '0.35' : '1'};
    `;
    
    let tag = '';
    if (isLow && isHigh) tag = 'LOW/HI';
    else if (isLow) tag = 'LOW';
    else if (isHigh) tag = 'HIGH';
    if (isMid) tag += (tag ? ' ' : '') + 'MID';
    
    b.innerHTML = `
      <span style="font-size:0.5rem; color:#94a3b8;">[${idx}]</span><br>
      <strong style="font-size:0.8rem; color:${isMid ? '#fff' : '#38bdf8'};">${v}</strong><br>
      <small style="font-size:0.5rem; color:#facc15;">${tag}</small>
    `;
    spideyGrid.appendChild(b);
  });
  spideyComp.textContent = sComps;
  spideyRange.textContent = `[${sLow}..${sHigh}]`;
}
renderSpideyGrid();

document.getElementById('spidey-btn-apply')?.addEventListener('click', () => {
  const parts = spideyCustomArr.value.split(',').map(s => parseInt(s.trim())).filter(n => !isNaN(n));
  if (parts.length >= 3) {
    sArr = parts.sort((a, b) => a - b);
    sLow = 0; sHigh = sArr.length - 1; sMid = Math.floor((sLow + sHigh) / 2);
    sComps = 0; sFound = false;
    renderSpideyGrid();
  }
});

function stepSpideyBinary() {
  if (sFound || sLow > sHigh) return;
  sComps++;
  sMid = Math.floor(sLow + (sHigh - sLow) / 2);
  const target = parseInt(spideyTarget.value) || 60;
  
  // Move Spidey over MID block
  const midCell = document.getElementById(`spidey-cell-${sMid}`);
  if (midCell) {
    const rect = midCell.getBoundingClientRect();
    const parentRect = spideyGrid.getBoundingClientRect();
    spideyActor.style.left = `${rect.left - parentRect.left + 5}px`;
    spideyActor.style.top = '10px';
  }
  
  renderSpideyGrid();
  retroAudio.playHover();
  
  if (sArr[sMid] === target) {
    sFound = true;
    retroAudio.playSuccess();
    if (midCell) {
      midCell.style.background = '#15803d';
      midCell.style.borderColor = '#22c55e';
      midCell.style.boxShadow = '0 0 20px #22c55e';
    }
    spideyDiag.innerHTML = `
      <div style="border-left: 4px solid #16a34a; padding-left: 8px;">
        <strong style="color: #16a34a;">🕸 TARGET ACQUIRED AT INDEX ${sMid}!</strong><br>
        <span>arr[${sMid}] == ${target}. Trap sprung in only <strong>${sComps}</strong> comparisons!</span>
      </div>
    `;
  } else if (target < sArr[sMid]) {
    spideyDiag.innerHTML = `🕸 <strong>Spider-Man:</strong> "Target ${target} < arr[mid] ${sArr[sMid]}. Webbing over right half [${sMid}..${sHigh}]!"`;
    setTimeout(() => {
      sHigh = sMid - 1;
      renderSpideyGrid();
    }, 400);
  } else {
    spideyDiag.innerHTML = `🕸 <strong>Spider-Man:</strong> "Target ${target} > arr[mid] ${sArr[sMid]}. Webbing over left half [${sLow}..${sMid}]!"`;
    setTimeout(() => {
      sLow = sMid + 1;
      renderSpideyGrid();
    }, 400);
  }
}

document.getElementById('spidey-btn-step')?.addEventListener('click', () => {
  retroAudio.playClick();
  stepSpideyBinary();
});

document.getElementById('spidey-btn-auto')?.addEventListener('click', () => {
  retroAudio.playClick();
  if (sTimer) {
    clearInterval(sTimer); sTimer = null;
    document.getElementById('spidey-btn-auto').textContent = '▶ AUTO-PLAY';
  } else {
    document.getElementById('spidey-btn-auto').textContent = '⏸ PAUSE';
    sTimer = setInterval(() => {
      if (sFound || sLow > sHigh) {
        clearInterval(sTimer); sTimer = null;
        document.getElementById('spidey-btn-auto').textContent = '▶ AUTO-PLAY';
      } else {
        stepSpideyBinary();
      }
    }, 800);
  }
});

document.getElementById('spidey-btn-reset')?.addEventListener('click', () => {
  retroAudio.playClick();
  if (sTimer) { clearInterval(sTimer); sTimer = null; }
  sLow = 0; sHigh = sArr.length - 1; sMid = Math.floor((sLow + sHigh) / 2);
  sComps = 0; sFound = false;
  spideyActor.style.left = '40px';
  renderSpideyGrid();
  spideyDiag.innerHTML = `💬 <strong>Spider-Man:</strong> "Search range reset to [0..${sArr.length - 1}]."`;
});
"""
}

print(f"Loaded Physical Simulations Part 2: {len(PHYSICAL_SIMS_PART2)} topics")
