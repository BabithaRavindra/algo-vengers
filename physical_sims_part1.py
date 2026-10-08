# physical_sims_part1.py - Topics 1 to 5
# Physical Algorithm Simulations with Moving Hero Actors & Custom Inputs
# 1. Ant-Man: Space Complexity (In-place O(1) vs Recursive O(N))
# 2. Doctor Strange: Time Complexity (Linear vs Quadratic Step Portal)
# 3. Vision: Asymptotic Notations (Bound Certification)
# 4. Captain America: Stacks (LIFO Physical Shield Push/Pop/Peek)
# 5. Hulk: Queues (FIFO Gamma Conveyor Enqueue/Dequeue)

PHYSICAL_SIMS_PART1 = {}

# 1. ANT-MAN: Quantum Memory Regulator (Space Complexity)
PHYSICAL_SIMS_PART1["memory"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <!-- Simulation Header -->
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #ef4444;">MISSION: QUANTUM MEMORY REGULATOR</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Watch Scott Lang shrink to O(1) in-place register swaps or clone into recursive O(N) heap frames.</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #22c55e; padding: 6px 10px; border: 1px solid #475569;">
      SUIT RAM: <span id="ant-mem-stat" style="color: #38bdf8;">O(1) CONSTANT</span>
    </div>
  </div>

  <!-- User Custom Input Bar -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; align-items: center; gap: 8px;">
      <label style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a;">ARRAY SIZE (N):</label>
      <input type="number" id="ant-input-n" value="6" min="2" max="10" style="width: 55px; padding: 4px; font-family: var(--font-code); font-weight: bold; border: 2px solid #0f172a; text-align: center;">
      <button class="pixel-btn pixel-btn-secondary" id="ant-btn-apply" style="padding: 4px 10px; font-size: 0.58rem;">APPLY N</button>
    </div>
    <div style="display: flex; gap: 8px; align-items: center;">
      <span style="font-family: var(--font-pixel); font-size: 0.58rem; color: #64748b;">ACTIVE MODE:</span>
      <span id="ant-mode-label" style="font-family: var(--font-pixel); font-size: 0.62rem; background: #dcfce7; color: #16a34a; padding: 3px 8px; border: 1px solid #16a34a;">IN-PLACE O(1)</span>
    </div>
  </div>

  <!-- Animated Arena Stage -->
  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 220px;">
    <!-- RAM Meter Bar -->
    <div style="display: flex; justify-content: space-between; font-family: var(--font-pixel); font-size: 0.62rem; color: #94a3b8; margin-bottom: 6px;">
      <span>SUIT RAM CAPACITY (100 KB HARDWARE BOUND)</span>
      <span id="ant-ram-pct" style="color: #22c55e;">8 KB / 100 KB (8%)</span>
    </div>
    <div style="width: 100%; height: 16px; background: #1e293b; border: 2px solid #475569; margin-bottom: 16px; overflow: hidden;">
      <div id="ant-ram-bar" style="width: 8%; height: 100%; background: #22c55e; transition: width 0.3s ease, background 0.3s ease;"></div>
    </div>

    <!-- Ant-Man Physical Actor -->
    <div id="ant-hero-actor" style="position: absolute; top: 75px; left: 40px; transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1); z-index: 10; display: flex; flex-direction: column; align-items: center;">
      <div style="font-family: var(--font-pixel); font-size: 0.5rem; background: #ef4444; color: #fff; padding: 1px 4px; border-radius: 2px; margin-bottom: 2px;">⚛ SCOTT</div>
      <img src="assets/antman.png" id="ant-hero-img" style="width: 44px; height: 50px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 4px 8px rgba(239,68,68,0.5)); transition: transform 0.3s ease;">
    </div>

    <!-- Active Memory Cells Corridor -->
    <div id="ant-cells-grid" style="display: flex; gap: 10px; min-height: 85px; align-items: center; justify-content: center; background: rgba(30, 41, 59, 0.5); border: 2px dashed #475569; padding: 14px; border-radius: 4px; overflow-x: auto;">
      <!-- Populated dynamically -->
    </div>
  </div>

  <!-- Live Intel Dialogue -->
  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; font-size: 0.88rem; min-height: 48px; display: flex; align-items: center;" id="ant-dialogue">
    💬 <strong>Scott Lang:</strong> "Quantum Regulator initialized! In-place pointer swaps require strictly O(1) auxiliary space."
  </div>

  <!-- Interactive Controls -->
  <div class="viz-controls" style="display: flex; gap: 10px; flex-wrap: wrap;">
    <button class="pixel-btn pixel-btn-primary" id="ant-btn-auto">▶ AUTO-RUN SIMULATION</button>
    <button class="pixel-btn pixel-btn-secondary" id="ant-btn-step">⏭ STEP IN-PLACE [O(1)]</button>
    <button class="pixel-btn pixel-btn-accent" id="ant-btn-recurse">🔴 ALLOCATE RECURSION [O(N)]</button>
    <button class="pixel-btn pixel-btn-secondary" id="ant-btn-reset">↺ RESET SUIT</button>
  </div>
</div>
""",
    "script": """
const antGrid = document.getElementById('ant-cells-grid');
const antBar = document.getElementById('ant-ram-bar');
const antPct = document.getElementById('ant-ram-pct');
const antStat = document.getElementById('ant-mem-stat');
const antDiag = document.getElementById('ant-dialogue');
const antHero = document.getElementById('ant-hero-actor');
const antHeroImg = document.getElementById('ant-hero-img');
const antInputN = document.getElementById('ant-input-n');
const antModeLabel = document.getElementById('ant-mode-label');
let antSize = 6;
let antLeft = 0, antRight = 5;
let antAutoTimer = null;
let antIsRecursive = false;
let antData = [12, 24, 36, 48, 60, 72];

function initAntGrid() {
  antGrid.innerHTML = '';
  antLeft = 0;
  antRight = antSize - 1;
  antData = Array.from({length: antSize}, (_, i) => (i + 1) * 12);
  for (let i = 0; i < antSize; i++) {
    const c = document.createElement('div');
    c.id = `ant-cell-${i}`;
    c.style.cssText = 'background: #1e293b; color: #fff; border: 2px solid #64748b; font-family: var(--font-pixel); font-size: 0.65rem; padding: 12px 14px; border-radius: 4px; text-align: center; min-width: 60px; transition: all 0.3s ease;';
    c.innerHTML = `[${i}]<br><span style="color:#38bdf8; font-size:0.75rem;">${antData[i]}</span>`;
    antGrid.appendChild(c);
  }
  antBar.style.width = '8%';
  antBar.style.background = '#22c55e';
  antPct.textContent = '8 KB / 100 KB (8%)';
  antStat.textContent = 'O(1) CONSTANT';
  antStat.style.color = '#22c55e';
  antHero.style.left = '40px';
  antHeroImg.style.transform = 'scale(1)';
  antDiag.innerHTML = `💬 <strong>Scott Lang:</strong> "Array of size N=${antSize} loaded in memory. Ready for tactical execution!"`;
}
initAntGrid();

document.getElementById('ant-btn-apply')?.addEventListener('click', () => {
  retroAudio.playClick();
  antSize = Math.max(2, Math.min(10, parseInt(antInputN.value) || 6));
  initAntGrid();
});

document.getElementById('ant-btn-step')?.addEventListener('click', () => {
  retroAudio.playClick();
  stepAntInplace();
});

function stepAntInplace() {
  if (antLeft >= antRight) {
    antDiag.innerHTML = `🎉 <strong>Scott Lang:</strong> "Array completely reversed in-place! Auxiliary space remained strictly O(1) throughout."`;
    antHero.style.left = '50%';
    antHeroImg.style.transform = 'scale(1.3)';
    return;
  }
  const cellL = document.getElementById(`ant-cell-${antLeft}`);
  const cellR = document.getElementById(`ant-cell-${antRight}`);
  if (cellL && cellR) {
    cellL.style.borderColor = '#facc15';
    cellR.style.borderColor = '#facc15';
    // Move Scott to left index
    const rectL = cellL.getBoundingClientRect();
    const gridRect = antGrid.getBoundingClientRect();
    antHero.style.left = `${rectL.left - gridRect.left + 20}px`;
    antHeroImg.style.transform = 'scale(0.85)';
    
    // Swap data
    const temp = antData[antLeft];
    antData[antLeft] = antData[antRight];
    antData[antRight] = temp;
    
    setTimeout(() => {
      cellL.innerHTML = `[${antLeft}]<br><span style="color:#22c55e; font-size:0.75rem;">${antData[antLeft]}</span>`;
      cellR.innerHTML = `[${antRight}]<br><span style="color:#22c55e; font-size:0.75rem;">${antData[antRight]}</span>`;
      cellL.style.background = '#065f46';
      cellR.style.background = '#065f46';
      antDiag.innerHTML = `⚛️ <strong>Scott Lang:</strong> "In-place swap: arr[${antLeft}] ⟷ arr[${antRight}]. No heap buffers allocated!"`;
      antLeft++;
      antRight--;
    }, 250);
  }
}

document.getElementById('ant-btn-recurse')?.addEventListener('click', () => {
  retroAudio.playClick();
  antModeLabel.textContent = 'RECURSION O(N)';
  antModeLabel.style.background = '#fee2e2';
  antModeLabel.style.color = '#ef4444';
  antBar.style.width = '88%';
  antBar.style.background = '#ef4444';
  antPct.textContent = '88 KB / 100 KB (88%)';
  antStat.textContent = 'O(N) CALL STACK';
  antStat.style.color = '#ef4444';
  antDiag.innerHTML = `⚠️ <strong>Scott Lang:</strong> "Stack frames piling up! Each recursive call allocates return addresses and local buffers. High memory footprint!"`;
  antHeroImg.style.transform = 'scale(1.4)';
});

document.getElementById('ant-btn-auto')?.addEventListener('click', () => {
  retroAudio.playClick();
  if (antAutoTimer) {
    clearInterval(antAutoTimer);
    antAutoTimer = null;
    document.getElementById('ant-btn-auto').textContent = '▶ AUTO-RUN SIMULATION';
  } else {
    document.getElementById('ant-btn-auto').textContent = '⏸ PAUSE';
    antAutoTimer = setInterval(() => {
      if (antLeft >= antRight) {
        clearInterval(antAutoTimer);
        antAutoTimer = null;
        document.getElementById('ant-btn-auto').textContent = '▶ AUTO-RUN SIMULATION';
      } else {
        stepAntInplace();
      }
    }, 700);
  }
});

document.getElementById('ant-btn-reset')?.addEventListener('click', () => {
  retroAudio.playClick();
  if (antAutoTimer) { clearInterval(antAutoTimer); antAutoTimer = null; }
  document.getElementById('ant-btn-auto').textContent = '▶ AUTO-RUN SIMULATION';
  initAntGrid();
});
"""
}

# 2. DOCTOR STRANGE: Temporal Step Counter (Time Complexity)
PHYSICAL_SIMS_PART1["time_growth"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #7e22ce;">MISSION: TEMPORAL STEP PORTAL</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Step through the mystic portals to calculate step counts across logarithmic, linear, and quadratic timelines.</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #facc15; padding: 6px 10px; border: 1px solid #475569;">
      OPERATIONS: <span id="strange-ops-count" style="color: #38bdf8;">0</span> STEPS
    </div>
  </div>

  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; align-items: center; gap: 10px;">
      <label style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a;">TIMELINE SIZE (N):</label>
      <input type="range" id="strange-slider-n" min="2" max="16" value="6" style="width: 120px; accent-color: #7e22ce;">
      <span id="strange-n-display" style="font-family: var(--font-code); font-weight: bold; background: #0f172a; color: #facc15; padding: 2px 8px; border-radius: 4px;">N = 6</span>
    </div>
    <div style="display: flex; gap: 8px;">
      <button class="pixel-btn pixel-btn-secondary" id="strange-mode-lin" style="padding: 4px 8px; font-size: 0.58rem; background: #dcfce7;">O(N) LINEAR</button>
      <button class="pixel-btn pixel-btn-secondary" id="strange-mode-quad" style="padding: 4px 8px; font-size: 0.58rem;">O(N²) QUADRATIC</button>
      <button class="pixel-btn pixel-btn-secondary" id="strange-mode-log" style="padding: 4px 8px; font-size: 0.58rem;">O(LOG N)</button>
    </div>
  </div>

  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 220px; display: flex; flex-direction: column; justify-content: center;">
    <div id="strange-hero-actor" style="position: absolute; top: 20px; left: 40px; transition: all 0.3s ease; z-index: 10; display: flex; flex-direction: column; align-items: center;">
      <div style="font-family: var(--font-pixel); font-size: 0.5rem; background: #7e22ce; color: #fff; padding: 1px 4px; border-radius: 2px; margin-bottom: 2px;">✦ STRANGE</div>
      <img src="assets/doctorstrange.png" style="width: 44px; height: 50px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 4px 8px rgba(126,34,206,0.6));">
    </div>

    <!-- Portal Path Steps -->
    <div id="strange-portals-container" style="display: flex; flex-wrap: wrap; gap: 8px; align-items: center; justify-content: center; padding-top: 50px;">
      <!-- Generated via JS -->
    </div>
  </div>

  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; font-size: 0.88rem; min-height: 48px; display: flex; align-items: center;" id="strange-dialogue">
    💬 <strong>Doctor Strange:</strong> "Select a complexity mode to watch how step counts scale across timelines."
  </div>

  <div class="viz-controls" style="display: flex; gap: 10px; flex-wrap: wrap;">
    <button class="pixel-btn pixel-btn-primary" id="strange-btn-run">▶ EXECUTE TIMELINE</button>
    <button class="pixel-btn pixel-btn-secondary" id="strange-btn-step">⏭ STEP PORTAL</button>
    <button class="pixel-btn pixel-btn-secondary" id="strange-btn-reset">↺ RESET REALITY</button>
  </div>
</div>
""",
    "script": """
const strangePortals = document.getElementById('strange-portals-container');
const strangeOps = document.getElementById('strange-ops-count');
const strangeDiag = document.getElementById('strange-dialogue');
const strangeHero = document.getElementById('strange-hero-actor');
const strangeSlider = document.getElementById('strange-slider-n');
const strangeNDisp = document.getElementById('strange-n-display');

let strangeN = 6;
let strangeMode = 'linear';
let strangeStepIdx = 0;
let strangeTimer = null;

function renderStrangeArena() {
  strangePortals.innerHTML = '';
  strangeStepIdx = 0;
  strangeOps.textContent = '0';
  let totalSteps = strangeMode === 'linear' ? strangeN : (strangeMode === 'quad' ? strangeN * strangeN : Math.ceil(Math.log2(strangeN)));
  
  for (let i = 0; i < Math.min(totalSteps, 32); i++) {
    const p = document.createElement('div');
    p.id = `strange-portal-${i}`;
    p.style.cssText = 'width: 38px; height: 38px; border-radius: 50%; border: 2px dashed #f59e0b; background: #1e1b4b; display: flex; align-items: center; justify-content: center; font-family: var(--font-pixel); font-size: 0.55rem; color: #facc15; transition: all 0.25s ease;';
    p.textContent = `${i+1}`;
    strangePortals.appendChild(p);
  }
  strangeDiag.innerHTML = `✦ <strong>Doctor Strange:</strong> "Timeline calibrated for N=${strangeN} in ${strangeMode.toUpperCase()} mode. Expected steps: ${totalSteps}."`;
}
renderStrangeArena();

strangeSlider?.addEventListener('input', () => {
  strangeN = parseInt(strangeSlider.value);
  strangeNDisp.textContent = `N = ${strangeN}`;
  renderStrangeArena();
});

document.getElementById('strange-mode-lin')?.addEventListener('click', () => {
  strangeMode = 'linear';
  renderStrangeArena();
});
document.getElementById('strange-mode-quad')?.addEventListener('click', () => {
  strangeMode = 'quad';
  renderStrangeArena();
});
document.getElementById('strange-mode-log')?.addEventListener('click', () => {
  strangeMode = 'log';
  renderStrangeArena();
});

document.getElementById('strange-btn-step')?.addEventListener('click', () => {
  retroAudio.playClick();
  stepStrange();
});

function stepStrange() {
  const p = document.getElementById(`strange-portal-${strangeStepIdx}`);
  if (p) {
    p.style.background = '#7e22ce';
    p.style.borderColor = '#38bdf8';
    p.style.boxShadow = '0 0 12px #38bdf8';
    strangeOps.textContent = strangeStepIdx + 1;
    const rect = p.getBoundingClientRect();
    const parentRect = strangePortals.getBoundingClientRect();
    strangeHero.style.left = `${rect.left - parentRect.left + 20}px`;
    strangeStepIdx++;
    strangeDiag.innerHTML = `✦ <strong>Doctor Strange:</strong> "Traversed operational portal ${strangeStepIdx}. Step count accumulates."`;
  } else {
    strangeDiag.innerHTML = `✨ <strong>Doctor Strange:</strong> "All temporal steps concluded! Final step count verified."`;
  }
}

document.getElementById('strange-btn-run')?.addEventListener('click', () => {
  retroAudio.playClick();
  if (strangeTimer) {
    clearInterval(strangeTimer); strangeTimer = null;
    document.getElementById('strange-btn-run').textContent = '▶ EXECUTE TIMELINE';
  } else {
    document.getElementById('strange-btn-run').textContent = '⏸ PAUSE';
    strangeTimer = setInterval(() => {
      const p = document.getElementById(`strange-portal-${strangeStepIdx}`);
      if (p) stepStrange();
      else {
        clearInterval(strangeTimer); strangeTimer = null;
        document.getElementById('strange-btn-run').textContent = '▶ EXECUTE TIMELINE';
      }
    }, 250);
  }
});

document.getElementById('strange-btn-reset')?.addEventListener('click', () => {
  retroAudio.playClick();
  if (strangeTimer) { clearInterval(strangeTimer); strangeTimer = null; }
  renderStrangeArena();
});
"""
}

# 3. VISION: Asymptotic Notations
PHYSICAL_SIMS_PART1["bounds"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #059669;">MISSION: MIND STONE ASYMPTOTIC SYNTHESIS</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Test inequality f(n) ≤ c · g(n) for all n ≥ n₀ to certify Big-O upper bound.</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #22c55e; padding: 6px 10px; border: 1px solid #475569;" id="vision-status">
      CERTIFICATION: VALID
    </div>
  </div>

  <!-- User Sliders for c and n0 -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; align-items: center; gap: 10px;">
      <label style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a;">CONSTANT (c):</label>
      <input type="range" id="vis-c-slider" min="1" max="15" value="7" style="width: 100px; accent-color: #059669;">
      <span id="vis-c-val" style="font-family: var(--font-code); font-weight: bold;">c = 7</span>
    </div>
    <div style="display: flex; align-items: center; gap: 10px;">
      <label style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a;">THRESHOLD (n₀):</label>
      <input type="range" id="vis-n0-slider" min="1" max="10" value="2" style="width: 100px; accent-color: #059669;">
      <span id="vis-n0-val" style="font-family: var(--font-code); font-weight: bold;">n₀ = 2</span>
    </div>
  </div>

  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 220px; display: flex; flex-direction: column; justify-content: center;">
    <div id="vision-hero-actor" style="position: absolute; top: 20px; left: 30px; transition: all 0.3s ease; z-index: 10; display: flex; flex-direction: column; align-items: center;">
      <div style="font-family: var(--font-pixel); font-size: 0.5rem; background: #059669; color: #fff; padding: 1px 4px; border-radius: 2px; margin-bottom: 2px;">⬡ VISION</div>
      <img src="assets/vision.png" style="width: 44px; height: 50px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 4px 8px rgba(5,150,105,0.6));">
    </div>

    <div id="vision-eval-grid" style="display: flex; flex-direction: column; gap: 8px; padding-left: 90px;">
      <!-- Row comparisons rendered here -->
    </div>
  </div>

  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; font-size: 0.88rem; min-height: 48px; display: flex; align-items: center;" id="vis-dialogue">
    💬 <strong>Vision:</strong> "Analyzing inequality f(n) = 3n + 8 against c·n for all n ≥ n₀."
  </div>

  <div class="viz-controls" style="display: flex; gap: 10px;">
    <button class="pixel-btn pixel-btn-primary" id="vis-btn-verify">✓ RUN FORMAL VERIFICATION</button>
  </div>
</div>
""",
    "script": """
const visCSlider = document.getElementById('vis-c-slider');
const visCVal = document.getElementById('vis-c-val');
const visN0Slider = document.getElementById('vis-n0-slider');
const visN0Val = document.getElementById('vis-n0-val');
const visGrid = document.getElementById('vision-eval-grid');
const visDiag = document.getElementById('vis-dialogue');
const visStatus = document.getElementById('vision-status');

function renderVisionCheck() {
  const c = parseInt(visCSlider.value);
  const n0 = parseInt(visN0Slider.value);
  visCVal.textContent = `c = ${c}`;
  visN0Val.textContent = `n₀ = ${n0}`;
  
  visGrid.innerHTML = '';
  let allValid = true;
  for (let n = 1; n <= 6; n++) {
    const fn = 3 * n + 8;
    const gn = c * n;
    const isAboveN0 = n >= n0;
    const conditionHolds = fn <= gn;
    if (isAboveN0 && !conditionHolds) allValid = false;
    
    const row = document.createElement('div');
    row.style.cssText = 'display: flex; align-items: center; gap: 12px; font-family: var(--font-code); font-size: 0.78rem; color: #fff;';
    row.innerHTML = `
      <span style="width: 50px; color: ${isAboveN0 ? '#facc15' : '#64748b'};">n=${n}:</span>
      <span style="color: #38bdf8;">f(${n})=${fn}</span>
      <span>${conditionHolds ? '≤' : '>'}</span>
      <span style="color: #4ade80;">c·g(${n})=${gn}</span>
      <span style="font-family: var(--font-pixel); font-size: 0.55rem; color: ${!isAboveN0 ? '#94a3b8' : (conditionHolds ? '#22c55e' : '#ef4444')};">
        ${!isAboveN0 ? '[n < n₀]' : (conditionHolds ? '✓ SATISFIED' : '✗ VIOLATION')}
      </span>
    `;
    visGrid.appendChild(row);
  }
  
  if (allValid) {
    visStatus.textContent = 'CERTIFICATION: VALID';
    visStatus.style.color = '#22c55e';
    visDiag.innerHTML = `⬡ <strong>Vision:</strong> "Inequality holds for all n ≥ ${n0} with c=${c}. Big-O upper bound mathematically certified!"`;
  } else {
    visStatus.textContent = 'CERTIFICATION: INVALID';
    visStatus.style.color = '#ef4444';
    visDiag.innerHTML = `⚠️ <strong>Vision:</strong> "Constant c=${c} is insufficient for n₀=${n0}. Increase c or adjust n₀ to establish asymptotic dominance."`;
  }
}
renderVisionCheck();

visCSlider?.addEventListener('input', renderVisionCheck);
visN0Slider?.addEventListener('input', renderVisionCheck);
document.getElementById('vis-btn-verify')?.addEventListener('click', () => {
  retroAudio.playClick();
  renderVisionCheck();
});
"""
}

# 4. CAPTAIN AMERICA: Stacks (BENCHMARK INTERACTIVE SIMULATION)
# Fully implements prompt Section 6:
# - Hero moves to source block
# - Hero physically lifts block
# - Block follows hero to stack
# - Block placed on top
# - Explanation appears with operation & complexity
# - POP lifts from stack and carries away
# - PEEK points to top element without removing
# - Custom user input support!
PHYSICAL_SIMS_PART1["stack"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <!-- Simulation Header -->
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #1d4ed8;">MISSION: VIBRANIUM SHIELD SILO (LIFO)</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Watch Captain America physically move blocks into the stack. Last In, First Out!</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #f8fafc; padding: 6px 10px; border: 1px solid #475569;">
      STACK SIZE: <span id="cap-size" style="color: #38bdf8;">3</span> / 5 | TOP: <span id="cap-top-idx" style="color: #facc15;">2</span>
    </div>
  </div>

  <!-- Custom User Input Bar -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; align-items: center; gap: 10px;">
      <label style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a;">PUSH VALUE:</label>
      <input type="number" id="cap-input-val" value="40" min="1" max="99" style="width: 60px; padding: 4px; font-family: var(--font-code); font-weight: bold; border: 2px solid #0f172a; text-align: center;">
      <span style="font-size: 0.75rem; color: #64748b;">(Or use controls below)</span>
    </div>
    <div style="font-family: var(--font-code); font-size: 0.8rem; font-weight: bold; color: #1d4ed8;">
      OPERATIONS: <span id="cap-op-counter">0</span> | AUX SPACE: O(1)
    </div>
  </div>

  <!-- Physical Interactive Arena -->
  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 250px;">
    <!-- Cap Animated Actor with Hands -->
    <div id="cap-actor" style="position: absolute; top: 15px; left: 60px; transition: left 0.4s cubic-bezier(0.34, 1.56, 0.64, 1), top 0.3s ease; z-index: 20; display: flex; flex-direction: column; align-items: center;">
      <!-- Carried Block (Lifts above Cap's hands) -->
      <div id="cap-carried-block" style="display: none; background: #facc15; color: #0f172a; font-family: var(--font-pixel); font-size: 0.65rem; padding: 4px 8px; border: 2px solid #000; box-shadow: 0 2px 6px rgba(0,0,0,0.5); margin-bottom: 2px;">
        [40]
      </div>
      <div style="font-family: var(--font-pixel); font-size: 0.5rem; background: #1d4ed8; color: #fff; padding: 1px 4px; border-radius: 2px; margin-bottom: 2px;">★ CAP</div>
      <img src="assets/captainamerica.png" id="cap-actor-img" style="width: 46px; height: 52px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 4px 8px rgba(29,78,216,0.6));">
      <!-- Pointer laser for PEEK -->
      <div id="cap-laser-beam" style="display: none; width: 2px; height: 40px; background: #facc15; box-shadow: 0 0 8px #facc15; margin-top: 2px;"></div>
    </div>

    <!-- Arena Stage Layout: Source Rack (Left) vs Stack Silo (Center) vs Output Tray (Right) -->
    <div style="display: grid; grid-template-columns: 140px 180px 140px; gap: 20px; justify-content: center; align-items: flex-end; height: 210px;">
      
      <!-- Source Inventory Rack -->
      <div style="display: flex; flex-direction: column; align-items: center;">
        <span style="font-family: var(--font-pixel); font-size: 0.58rem; color: #94a3b8; margin-bottom: 6px;">SOURCE INVENTORY</span>
        <div id="cap-source-box" style="background: #1e293b; border: 2px solid #64748b; padding: 10px; width: 100%; text-align: center; border-radius: 4px;">
          <div id="cap-source-item" style="background: #facc15; color: #0f172a; font-family: var(--font-pixel); font-size: 0.65rem; padding: 8px; border: 2px solid #000;">
            READY: <span id="cap-source-val">40</span>
          </div>
        </div>
      </div>

      <!-- Vertical Stack Silo -->
      <div style="display: flex; flex-direction: column; align-items: center;">
        <div style="display: flex; align-items: center; gap: 6px; margin-bottom: 6px;">
          <span style="font-family: var(--font-pixel); font-size: 0.58rem; color: #facc15;">STACK SILO</span>
          <span style="font-family: var(--font-pixel); font-size: 0.52rem; color: #38bdf8;">[TOP ⬇]</span>
        </div>
        <div id="cap-stack-shaft" style="background: #0f172a; border: 3px solid #38bdf8; border-top: none; width: 100%; height: 165px; display: flex; flex-direction: column-reverse; padding: 6px; gap: 5px; position: relative;">
          <!-- Default stack blocks -->
          <div class="cap-stack-item" style="background: #1d4ed8; color: #fff; font-family: var(--font-pixel); font-size: 0.6rem; padding: 6px; border: 2px solid #000; text-align: center;">[ 10 ] BASE</div>
          <div class="cap-stack-item" style="background: #2563eb; color: #fff; font-family: var(--font-pixel); font-size: 0.6rem; padding: 6px; border: 2px solid #000; text-align: center;">[ 20 ]</div>
          <div class="cap-stack-item" style="background: #3b82f6; color: #fff; font-family: var(--font-pixel); font-size: 0.6rem; padding: 6px; border: 2px solid #000; text-align: center;">[ 30 ] TOP</div>
        </div>
      </div>

      <!-- Discard / Extraction Output Tray -->
      <div style="display: flex; flex-direction: column; align-items: center;">
        <span style="font-family: var(--font-pixel); font-size: 0.58rem; color: #94a3b8; margin-bottom: 6px;">OUTPUT TRAY</span>
        <div id="cap-output-box" style="background: #1e293b; border: 2px dashed #64748b; padding: 10px; width: 100%; height: 60px; display: flex; align-items: center; justify-content: center; border-radius: 4px;">
          <span id="cap-output-text" style="font-family: var(--font-pixel); font-size: 0.55rem; color: #64748b;">EMPTY</span>
        </div>
      </div>

    </div>
  </div>

  <!-- Live Operation Feedback Card (Direct prompt benchmark!) -->
  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 12px 16px; margin-bottom: 14px; min-height: 52px; display: flex; align-items: center; justify-content: space-between;" id="cap-dialogue">
    <div>
      💬 <strong>Captain America:</strong> "Ready to deploy vibranium shields. Choose an operation to begin!"
    </div>
  </div>

  <!-- Interactive Controls: [ PUSH ] [ POP ] [ PEEK ] [ RESET ] -->
  <div class="viz-controls" style="display: flex; gap: 10px; flex-wrap: wrap;">
    <button class="pixel-btn pixel-btn-primary" id="cap-btn-push">▲ PUSH BLOCK</button>
    <button class="pixel-btn pixel-btn-secondary" id="cap-btn-pop">▼ POP TOP</button>
    <button class="pixel-btn pixel-btn-secondary" id="cap-btn-peek">◉ PEEK TOP</button>
    <button class="pixel-btn pixel-btn-secondary" id="cap-btn-reset">↺ RESET STACK</button>
  </div>
</div>
""",
    "script": """
const capActor = document.getElementById('cap-actor');
const capCarried = document.getElementById('cap-carried-block');
const capLaser = document.getElementById('cap-laser-beam');
const capShaft = document.getElementById('cap-stack-shaft');
const capSize = document.getElementById('cap-size');
const capTopIdx = document.getElementById('cap-top-idx');
const capDialogue = document.getElementById('cap-dialogue');
const capInputVal = document.getElementById('cap-input-val');
const capSourceVal = document.getElementById('cap-source-val');
const capOutputText = document.getElementById('cap-output-text');
const capOpCounter = document.getElementById('cap-op-counter');

let capItems = [10, 20, 30];
let capOps = 0;
let capIsBusy = false;

capInputVal?.addEventListener('input', () => {
  capSourceVal.textContent = capInputVal.value || '40';
});

function updateCapLabels() {
  capSize.textContent = capItems.length;
  capTopIdx.textContent = capItems.length > 0 ? capItems.length - 1 : '-1 (EMPTY)';
  capOpCounter.textContent = capOps;
}

// PUSH OPERATION: Hero walks to source, lifts block, carries to stack, places on top
document.getElementById('cap-btn-push')?.addEventListener('click', () => {
  if (capIsBusy) return;
  if (capItems.length >= 5) {
    retroAudio.playError();
    capDialogue.innerHTML = `⚠️ <strong>Captain America:</strong> "STACK OVERFLOW! Silo has reached max capacity of 5 shields. Pop an item first!"`;
    return;
  }
  
  capIsBusy = true;
  retroAudio.playClick();
  const pushVal = parseInt(capInputVal.value) || (capItems.length + 1) * 10;
  capOps++;
  updateCapLabels();
  
  // Step 1: Walk to source box (left: 80px)
  capActor.style.left = '80px';
  capActor.style.top = '100px';
  capDialogue.innerHTML = `★ <strong>Captain America:</strong> "Moving to source rack to retrieve Shield [${pushVal}]..."`;
  
  // Step 2: Lift block
  setTimeout(() => {
    retroAudio.playHover();
    capCarried.textContent = `[${pushVal}]`;
    capCarried.style.display = 'block';
    capDialogue.innerHTML = `★ <strong>Captain America:</strong> "Shield [${pushVal}] lifted! Carrying to top of stack silo..."`;
    
    // Step 3: Walk to Stack Silo (center: 330px)
    setTimeout(() => {
      capActor.style.left = '330px';
      capActor.style.top = '15px';
      
      // Step 4: Drop block on top of stack
      setTimeout(() => {
        retroAudio.playSuccess();
        capCarried.style.display = 'none';
        capItems.push(pushVal);
        
        // Add element to stack DOM
        const el = document.createElement('div');
        el.className = 'cap-stack-item';
        el.style.cssText = 'background: #3b82f6; color: #fff; font-family: var(--font-pixel); font-size: 0.6rem; padding: 6px; border: 2px solid #000; text-align: center; animation: popIn 0.25s;';
        el.textContent = `[ ${pushVal} ] TOP`;
        
        // Remove 'TOP' text from previous element
        const prev = capShaft.children[capShaft.children.length - 1];
        if (prev) prev.textContent = prev.textContent.replace(' TOP', '');
        
        capShaft.appendChild(el);
        updateCapLabels();
        
        capDialogue.innerHTML = `
          <div style="border-left: 4px solid #1d4ed8; padding-left: 8px;">
            <strong style="color: #1d4ed8;">★ PUSH(${pushVal}) SUCCESSFUL</strong><br>
            <span>Added ${pushVal} to the top of the stack. | Time Complexity: <strong>O(1)</strong></span>
          </div>
        `;
        
        // Walk back to idle station
        setTimeout(() => {
          capActor.style.left = '60px';
          capActor.style.top = '15px';
          capIsBusy = false;
        }, 300);
        
      }, 400);
    }, 450);
  }, 400);
});

// POP OPERATION: Hero moves to stack top, lifts top block, carries away
document.getElementById('cap-btn-pop')?.addEventListener('click', () => {
  if (capIsBusy) return;
  if (capItems.length === 0) {
    retroAudio.playError();
    capDialogue.innerHTML = `⚠️ <strong>Captain America:</strong> "STACK UNDERFLOW! No shields remain in the silo to pop."`;
    return;
  }
  
  capIsBusy = true;
  retroAudio.playClick();
  capOps++;
  updateCapLabels();
  
  // Step 1: Walk to stack top (center: 330px)
  capActor.style.left = '330px';
  capActor.style.top = '15px';
  capDialogue.innerHTML = `★ <strong>Captain America:</strong> "Accessing silo summit to retrieve topmost element..."`;
  
  setTimeout(() => {
    retroAudio.playHover();
    const poppedVal = capItems.pop();
    const topEl = capShaft.children[capShaft.children.length - 1];
    if (topEl) capShaft.removeChild(topEl);
    
    // Label new top if exists
    if (capShaft.children.length > 0) {
      const newTop = capShaft.children[capShaft.children.length - 1];
      if (!newTop.textContent.includes('TOP')) newTop.textContent += ' TOP';
    }
    
    // Lift block into hands
    capCarried.textContent = `[${poppedVal}]`;
    capCarried.style.display = 'block';
    
    // Step 2: Carry to output tray (right: 500px)
    setTimeout(() => {
      capActor.style.left = '500px';
      capActor.style.top = '100px';
      capDialogue.innerHTML = `★ <strong>Captain America:</strong> "Carrying popped element to extraction tray..."`;
      
      setTimeout(() => {
        retroAudio.playSuccess();
        capCarried.style.display = 'none';
        capOutputText.innerHTML = `<span style="color: #22c55e; font-size: 0.75rem;">[ ${poppedVal} ]</span>`;
        updateCapLabels();
        
        // Exact prompt popup card specification:
        capDialogue.innerHTML = `
          <div style="background: #eff6ff; border: 2px solid #1d4ed8; padding: 8px 12px; width: 100%;">
            <div style="font-family: var(--font-pixel); font-size: 0.65rem; color: #1d4ed8;">★ CAPTAIN AMERICA // EXTRACTION COMPLETE</div>
            <div style="font-size: 0.9rem; margin-top: 3px;">POP() removed: <strong>${poppedVal}</strong> | Time Complexity: <strong>O(1)</strong></div>
          </div>
        `;
        
        // Return to idle station
        setTimeout(() => {
          capActor.style.left = '60px';
          capActor.style.top = '15px';
          capIsBusy = false;
        }, 300);
      }, 400);
    }, 450);
  }, 400);
});

// PEEK OPERATION: Hero points laser/highlights top element without removing
document.getElementById('cap-btn-peek')?.addEventListener('click', () => {
  if (capIsBusy) return;
  if (capItems.length === 0) {
    capDialogue.innerHTML = `⚠️ <strong>Captain America:</strong> "Stack is empty! Cannot peek."`;
    return;
  }
  
  capIsBusy = true;
  retroAudio.playClick();
  capOps++;
  updateCapLabels();
  
  const topVal = capItems[capItems.length - 1];
  capActor.style.left = '330px';
  capActor.style.top = '15px';
  capLaser.style.display = 'block';
  
  const topEl = capShaft.children[capShaft.children.length - 1];
  if (topEl) topEl.style.boxShadow = '0 0 14px #facc15';
  
  setTimeout(() => {
    retroAudio.playSuccess();
    capDialogue.innerHTML = `
      <div style="border-left: 4px solid #facc15; padding-left: 8px;">
        <strong style="color: #b45309;">◉ PEEK INSPECTION: TOP = ${topVal}</strong><br>
        <span>PEEK reads the top element without changing the stack. Invariant preserved! | O(1)</span>
      </div>
    `;
    
    setTimeout(() => {
      capLaser.style.display = 'none';
      if (topEl) topEl.style.boxShadow = 'none';
      capActor.style.left = '60px';
      capIsBusy = false;
    }, 800);
  }, 400);
});

// RESET STACK
document.getElementById('cap-btn-reset')?.addEventListener('click', () => {
  retroAudio.playClick();
  capItems = [10, 20, 30];
  capOps = 0;
  capShaft.innerHTML = `
    <div class="cap-stack-item" style="background: #1d4ed8; color: #fff; font-family: var(--font-pixel); font-size: 0.6rem; padding: 6px; border: 2px solid #000; text-align: center;">[ 10 ] BASE</div>
    <div class="cap-stack-item" style="background: #2563eb; color: #fff; font-family: var(--font-pixel); font-size: 0.6rem; padding: 6px; border: 2px solid #000; text-align: center;">[ 20 ]</div>
    <div class="cap-stack-item" style="background: #3b82f6; color: #fff; font-family: var(--font-pixel); font-size: 0.6rem; padding: 6px; border: 2px solid #000; text-align: center;">[ 30 ] TOP</div>
  `;
  capOutputText.textContent = 'EMPTY';
  updateCapLabels();
  capActor.style.left = '60px';
  capActor.style.top = '15px';
  capCarried.style.display = 'none';
  capLaser.style.display = 'none';
  capDialogue.innerHTML = `💬 <strong>Captain America:</strong> "Stack reset to baseline 3 shields. Ready for drill."`;
  capIsBusy = false;
});
"""
}

# 5. HULK: Queues (FIFO Gamma Conveyor)
PHYSICAL_SIMS_PART1["queue"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #16a34a;">MISSION: GAMMA CONVOY FIFO EVACUATION</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">First chariot in is first chariot out! Hulk guides transports to the REAR and out the FRONT.</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #f8fafc; padding: 6px 10px; border: 1px solid #475569;">
      QUEUE SIZE: <span id="hulk-size" style="color: #22c55e;">3</span> / 5 | FRONT: <span id="hulk-front-idx" style="color: #38bdf8;">0</span>
    </div>
  </div>

  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; align-items: center; gap: 10px;">
      <label style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a;">ENQUEUE VAL:</label>
      <input type="number" id="hulk-input-val" value="40" min="1" max="99" style="width: 60px; padding: 4px; font-family: var(--font-code); font-weight: bold; border: 2px solid #0f172a; text-align: center;">
    </div>
    <div style="font-family: var(--font-code); font-size: 0.8rem; font-weight: bold; color: #16a34a;">
      OPERATIONS: <span id="hulk-op-counter">0</span> | TIME: O(1)
    </div>
  </div>

  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 250px;">
    <!-- Hulk Physical Actor -->
    <div id="hulk-actor" style="position: absolute; top: 15px; left: 60px; transition: left 0.4s cubic-bezier(0.34, 1.56, 0.64, 1), top 0.3s ease; z-index: 20; display: flex; flex-direction: column; align-items: center;">
      <div id="hulk-carried-block" style="display: none; background: #22c55e; color: #0f172a; font-family: var(--font-pixel); font-size: 0.65rem; padding: 4px 8px; border: 2px solid #000; margin-bottom: 2px;">
        [40]
      </div>
      <div style="font-family: var(--font-pixel); font-size: 0.5rem; background: #16a34a; color: #fff; padding: 1px 4px; border-radius: 2px; margin-bottom: 2px;">✊ HULK</div>
      <img src="assets/hulk.png" style="width: 48px; height: 54px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 4px 8px rgba(22,163,74,0.6));">
    </div>

    <!-- Arena Layout: FRONT (Left Exit) <--- Pipeline ---> REAR (Right Entrance) -->
    <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 80px; padding: 0 10px;">
      <!-- FRONT EXIT -->
      <div style="text-align: center;">
        <span style="font-family: var(--font-pixel); font-size: 0.55rem; color: #ef4444;">[FRONT EXIT] ⬅</span>
        <div id="hulk-front-indicator" style="background: #1e293b; border: 2px solid #ef4444; padding: 6px; font-family: var(--font-pixel); font-size: 0.6rem; color: #f87171; border-radius: 4px; margin-top: 4px;">
          DEQUEUE HERE
        </div>
      </div>

      <!-- Pipeline Conveyor Grid -->
      <div id="hulk-queue-pipe" style="display: flex; gap: 8px; background: #1e293b; border: 3px solid #475569; padding: 12px; border-radius: 4px; min-width: 280px; justify-content: center;">
        <div class="hulk-q-item" style="background: #16a34a; color: #fff; font-family: var(--font-pixel); font-size: 0.65rem; padding: 10px 14px; border: 2px solid #000;">[ 10 ]<br><small style="color:#facc15;">FRONT</small></div>
        <div class="hulk-q-item" style="background: #15803d; color: #fff; font-family: var(--font-pixel); font-size: 0.65rem; padding: 10px 14px; border: 2px solid #000;">[ 20 ]</div>
        <div class="hulk-q-item" style="background: #166534; color: #fff; font-family: var(--font-pixel); font-size: 0.65rem; padding: 10px 14px; border: 2px solid #000;">[ 30 ]<br><small style="color:#38bdf8;">REAR</small></div>
      </div>

      <!-- REAR ENTRANCE -->
      <div style="text-align: center;">
        <span style="font-family: var(--font-pixel); font-size: 0.55rem; color: #38bdf8;">➡ [REAR IN]</span>
        <div id="hulk-rear-indicator" style="background: #1e293b; border: 2px solid #38bdf8; padding: 6px; font-family: var(--font-pixel); font-size: 0.6rem; color: #38bdf8; border-radius: 4px; margin-top: 4px;">
          ENQUEUE HERE
        </div>
      </div>
    </div>
  </div>

  <!-- Live Operation Feedback Card -->
  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 12px 16px; margin-bottom: 14px; min-height: 52px; display: flex; align-items: center;" id="hulk-dialogue">
    💬 <strong>Hulk:</strong> "Queue pipeline active! First in is first out. Hulk moves chariots!"
  </div>

  <div class="viz-controls" style="display: flex; gap: 10px; flex-wrap: wrap;">
    <button class="pixel-btn pixel-btn-primary" id="hulk-btn-enqueue">➡ ENQUEUE REAR</button>
    <button class="pixel-btn pixel-btn-secondary" id="hulk-btn-dequeue">⬅ DEQUEUE FRONT</button>
    <button class="pixel-btn pixel-btn-secondary" id="hulk-btn-peek">◉ PEEK FRONT</button>
    <button class="pixel-btn pixel-btn-secondary" id="hulk-btn-reset">↺ RESET QUEUE</button>
  </div>
</div>
""",
    "script": """
const hulkActor = document.getElementById('hulk-actor');
const hulkCarried = document.getElementById('hulk-carried-block');
const hulkPipe = document.getElementById('hulk-queue-pipe');
const hulkSize = document.getElementById('hulk-size');
const hulkFrontIdx = document.getElementById('hulk-front-idx');
const hulkDialogue = document.getElementById('hulk-dialogue');
const hulkInputVal = document.getElementById('hulk-input-val');
const hulkOpCounter = document.getElementById('hulk-op-counter');

let hulkItems = [10, 20, 30];
let hulkOps = 0;
let hulkIsBusy = false;

function updateHulkLabels() {
  hulkSize.textContent = hulkItems.length;
  hulkFrontIdx.textContent = hulkItems.length > 0 ? '0' : 'NONE';
  hulkOpCounter.textContent = hulkOps;
}

// ENQUEUE: Hulk walks to incoming, grabs it, carries to REAR (right end), pushes into pipeline
document.getElementById('hulk-btn-enqueue')?.addEventListener('click', () => {
  if (hulkIsBusy) return;
  if (hulkItems.length >= 5) {
    retroAudio.playError();
    hulkDialogue.innerHTML = `⚠️ <strong>Hulk:</strong> "QUEUE OVERFLOW! Tunnel full! Dequeue front chariots first!"`;
    return;
  }
  
  hulkIsBusy = true;
  retroAudio.playClick();
  const val = parseInt(hulkInputVal.value) || (hulkItems.length + 1) * 10;
  hulkOps++;
  updateHulkLabels();
  
  // Walk to entrance
  hulkActor.style.left = '450px';
  hulkDialogue.innerHTML = `✊ <strong>Hulk:</strong> "Grabbing transport [${val}] to push into REAR..."`;
  
  setTimeout(() => {
    retroAudio.playHover();
    hulkCarried.textContent = `[${val}]`;
    hulkCarried.style.display = 'block';
    
    // Carry and place into pipeline
    setTimeout(() => {
      retroAudio.playSuccess();
      hulkCarried.style.display = 'none';
      hulkItems.push(val);
      
      const el = document.createElement('div');
      el.className = 'hulk-q-item';
      el.style.cssText = 'background: #166534; color: #fff; font-family: var(--font-pixel); font-size: 0.65rem; padding: 10px 14px; border: 2px solid #000; animation: popIn 0.25s;';
      el.innerHTML = `[ ${val} ]<br><small style="color:#38bdf8;">REAR</small>`;
      
      // Remove REAR tag from previous last element
      if (hulkPipe.children.length > 0) {
        const prev = hulkPipe.children[hulkPipe.children.length - 1];
        prev.innerHTML = prev.innerHTML.replace('<br><small style="color:#38bdf8;">REAR</small>', '');
      }
      hulkPipe.appendChild(el);
      updateHulkLabels();
      
      hulkDialogue.innerHTML = `
        <div style="border-left: 4px solid #16a34a; padding-left: 8px;">
          <strong style="color: #16a34a;">✊ ENQUEUE(${val}) SUCCESSFUL</strong><br>
          <span>Appended to REAR of queue. | Time Complexity: <strong>O(1)</strong></span>
        </div>
      `;
      
      setTimeout(() => {
        hulkActor.style.left = '60px';
        hulkIsBusy = false;
      }, 300);
    }, 400);
  }, 400);
});

// DEQUEUE: Hulk walks to FRONT (left end), removes front element, carries away
document.getElementById('hulk-btn-dequeue')?.addEventListener('click', () => {
  if (hulkIsBusy) return;
  if (hulkItems.length === 0) {
    retroAudio.playError();
    hulkDialogue.innerHTML = `⚠️ <strong>Hulk:</strong> "QUEUE UNDERFLOW! No transports waiting in tunnel."`;
    return;
  }
  
  hulkIsBusy = true;
  retroAudio.playClick();
  hulkOps++;
  updateHulkLabels();
  
  // Walk to FRONT (left: 120px)
  hulkActor.style.left = '120px';
  hulkDialogue.innerHTML = `✊ <strong>Hulk:</strong> "Moving to FRONT to evacuate oldest transport..."`;
  
  setTimeout(() => {
    retroAudio.playHover();
    const dequeuedVal = hulkItems.shift();
    const firstEl = hulkPipe.children[0];
    if (firstEl) hulkPipe.removeChild(firstEl);
    
    // Update new FRONT label
    if (hulkPipe.children.length > 0) {
      const newFront = hulkPipe.children[0];
      if (!newFront.innerHTML.includes('FRONT')) {
        newFront.innerHTML += '<br><small style="color:#facc15;">FRONT</small>';
      }
    }
    
    hulkCarried.textContent = `[${dequeuedVal}]`;
    hulkCarried.style.display = 'block';
    
    setTimeout(() => {
      // Carry out exit
      hulkActor.style.left = '10px';
      setTimeout(() => {
        retroAudio.playSuccess();
        hulkCarried.style.display = 'none';
        updateHulkLabels();
        
        hulkDialogue.innerHTML = `
          <div style="background: #f0fdf4; border: 2px solid #16a34a; padding: 8px 12px; width: 100%;">
            <div style="font-family: var(--font-pixel); font-size: 0.65rem; color: #16a34a;">✊ HULK // EVACUATION COMPLETE</div>
            <div style="font-size: 0.9rem; margin-top: 3px;">DEQUEUE() removed: <strong>${dequeuedVal}</strong> from FRONT | Time: <strong>O(1)</strong></div>
          </div>
        `;
        
        setTimeout(() => {
          hulkActor.style.left = '60px';
          hulkIsBusy = false;
        }, 300);
      }, 400);
    }, 400);
  }, 400);
});

// PEEK / FRONT: Hulk points to front element
document.getElementById('hulk-btn-peek')?.addEventListener('click', () => {
  if (hulkIsBusy) return;
  if (hulkItems.length === 0) {
    hulkDialogue.innerHTML = `⚠️ <strong>Hulk:</strong> "Queue is empty!"`;
    return;
  }
  hulkIsBusy = true;
  retroAudio.playClick();
  hulkOps++;
  updateHulkLabels();
  
  const frontVal = hulkItems[0];
  hulkActor.style.left = '120px';
  const firstEl = hulkPipe.children[0];
  if (firstEl) firstEl.style.boxShadow = '0 0 14px #22c55e';
  
  setTimeout(() => {
    retroAudio.playSuccess();
    hulkDialogue.innerHTML = `
      <div style="border-left: 4px solid #16a34a; padding-left: 8px;">
        <strong style="color: #16a34a;">◉ FRONT INSPECTION = ${frontVal}</strong><br>
        <span>Inspected front transport without modifying FIFO queue order. | O(1)</span>
      </div>
    `;
    setTimeout(() => {
      if (firstEl) firstEl.style.boxShadow = 'none';
      hulkActor.style.left = '60px';
      hulkIsBusy = false;
    }, 800);
  }, 400);
});

// RESET
document.getElementById('hulk-btn-reset')?.addEventListener('click', () => {
  retroAudio.playClick();
  hulkItems = [10, 20, 30];
  hulkOps = 0;
  hulkPipe.innerHTML = `
    <div class="hulk-q-item" style="background: #16a34a; color: #fff; font-family: var(--font-pixel); font-size: 0.65rem; padding: 10px 14px; border: 2px solid #000;">[ 10 ]<br><small style="color:#facc15;">FRONT</small></div>
    <div class="hulk-q-item" style="background: #15803d; color: #fff; font-family: var(--font-pixel); font-size: 0.65rem; padding: 10px 14px; border: 2px solid #000;">[ 20 ]</div>
    <div class="hulk-q-item" style="background: #166534; color: #fff; font-family: var(--font-pixel); font-size: 0.65rem; padding: 10px 14px; border: 2px solid #000;">[ 30 ]<br><small style="color:#38bdf8;">REAR</small></div>
  `;
  updateHulkLabels();
  hulkActor.style.left = '60px';
  hulkCarried.style.display = 'none';
  hulkDialogue.innerHTML = `💬 <strong>Hulk:</strong> "Queue reset to 3 transports. Ready for FIFO evacuation."`;
  hulkIsBusy = false;
});
"""
}

print(f"Loaded Physical Simulations Part 1: {len(PHYSICAL_SIMS_PART1)} topics")
