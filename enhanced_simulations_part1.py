# simulations.py - 19 Self-Running Interactive Marvel Retro Game Simulations
# Each simulation includes:
# - Animated Hero Sprite that moves/flies across the stage
# - Custom User Input support (user types custom numbers/arrays/parameters)
# - Self-running Auto-Play game mode with Pause/Step/Reset controls
# - Live battle log & Web Audio sound effects

SIMULATIONS = {}

# 1. ANT-MAN: Quantum Memory Regulator (Space Complexity)
SIMULATIONS["memory"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <!-- Simulation Header -->
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #ef4444;">MISSION: QUANTUM MEMORY REGULATOR</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Watch Scott Lang shrink to O(1) in-place swaps or clone into recursive O(N) heap frames.</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #22c55e; padding: 6px 10px; border: 1px solid #475569;">
      SUIT RAM: <span id="ant-mem-stat" style="color: #38bdf8;">O(1) CONSTANT</span>
    </div>
  </div>

  <!-- User Custom Input Bar -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; align-items: center; gap: 8px;">
      <label style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a;">ARRAY SIZE (N):</label>
      <input type="number" id="ant-input-n" value="6" min="2" max="12" style="width: 55px; padding: 4px; font-family: var(--font-code); font-weight: bold; border: 2px solid #0f172a; text-align: center;">
      <button class="pixel-btn pixel-btn-secondary" id="ant-btn-apply" style="padding: 4px 10px; font-size: 0.58rem;">APPLY N</button>
    </div>
    <div style="font-size: 0.75rem; color: #475569; font-weight: 600;">
      Compare: In-Place Swap vs Recursive Call Stack
    </div>
  </div>

  <!-- Animated Arena Stage -->
  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 200px;">
    <!-- RAM Meter Bar -->
    <div style="display: flex; justify-content: space-between; font-family: var(--font-pixel); font-size: 0.62rem; color: #94a3b8; margin-bottom: 6px;">
      <span>SUIT RAM CAPACITY (100 MB MAX)</span>
      <span id="ant-ram-pct" style="color: #22c55e;">10 MB / 100 MB (10%)</span>
    </div>
    <div style="width: 100%; height: 16px; background: #1e293b; border: 2px solid #475569; margin-bottom: 16px; overflow: hidden;">
      <div id="ant-ram-bar" style="width: 10%; height: 100%; background: #22c55e; transition: width 0.3s ease, background 0.3s ease;"></div>
    </div>

    <!-- Ant-Man Floating Actor -->
    <div id="ant-hero-actor" style="position: absolute; top: 75px; left: 40px; transition: all 0.35s cubic-bezier(0.34, 1.56, 0.64, 1); z-index: 10;">
      <img src="assets/antman.png" id="ant-hero-img" style="width: 44px; height: 50px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 4px 8px rgba(239,68,68,0.5)); transition: transform 0.3s ease;">
    </div>

    <!-- Active Memory Cells Corridor -->
    <div id="ant-cells-grid" style="display: flex; gap: 10px; min-height: 80px; align-items: center; justify-content: center; background: rgba(30, 41, 59, 0.5); border: 2px dashed #475569; padding: 14px; border-radius: 4px; overflow-x: auto;">
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
let antSize = 6;
let antStepIdx = 0;
let antAutoTimer = null;
let antIsRecursive = false;

function initAntGrid() {
  antGrid.innerHTML = '';
  antStepIdx = 0;
  for (let i = 0; i < antSize; i++) {
    const c = document.createElement('div');
    c.id = `ant-cell-${i}`;
    c.style.cssText = 'background: #1e293b; color: #fff; border: 2px solid #64748b; font-family: var(--font-pixel); font-size: 0.65rem; padding: 12px 14px; border-radius: 4px; text-align: center; min-width: 60px; transition: all 0.3s ease;';
    c.innerHTML = `[${i}]<br><small style="color:#38bdf8;">val:${(i+1)*7}</small>`;
    antGrid.appendChild(c);
  }
  antBar.style.width = '10%';
  antBar.style.background = '#22c55e';
  antPct.textContent = '10 MB / 100 MB (10%)';
  antStat.textContent = 'O(1) CONSTANT';
  antStat.style.color = '#22c55e';
  antHero.style.left = '40px';
  antHeroImg.style.transform = 'scale(1)';
  antDiag.innerHTML = `💬 <strong>Scott Lang:</strong> "Array of size N=${antSize} loaded in memory. Ready for tactical execution!"`;
}
initAntGrid();

document.getElementById('ant-btn-apply')?.addEventListener('click', () => {
  retroAudio.playClick();
  antSize = parseInt(antInputN.value) || 6;
  initAntGrid();
});

document.getElementById('ant-btn-step')?.addEventListener('click', () => {
  retroAudio.playClick();
  antIsRecursive = false;
  stepAntInplace();
});

function stepAntInplace() {
  if (antStepIdx < antSize) {
    const targetCell = document.getElementById(`ant-cell-${antStepIdx}`);
    if (targetCell) {
      targetCell.style.background = '#0284c7';
      targetCell.style.borderColor = '#38bdf8';
      const cellRect = targetCell.offsetLeft;
      antHero.style.left = `${cellRect + 15}px`;
      antHeroImg.style.transform = 'scale(0.65)'; // Ant-man shrinks into cell!
    }
    antDiag.innerHTML = `⚡ <strong>Scott Lang:</strong> "Shrank into Cell [${antStepIdx}]! In-place pointer swap uses zero extra space. Auxiliary memory remains O(1)!"`;
    antStepIdx++;
  } else {
    antDiag.innerHTML = `✨ <strong>Scott Lang:</strong> "Array traversed completely in-place! Memory stayed at strictly O(1) auxiliary space throughout!"`;
    if (antAutoTimer) { clearInterval(antAutoTimer); antAutoTimer = null; document.getElementById('ant-btn-auto').textContent = '▶ AUTO-RUN SIMULATION'; }
  }
}

document.getElementById('ant-btn-recurse')?.addEventListener('click', () => {
  retroAudio.playClick();
  antIsRecursive = true;
  antBar.style.width = '85%';
  antBar.style.background = '#ef4444';
  antPct.textContent = '85 MB / 100 MB (85%)';
  antStat.textContent = 'O(N) LINEAR ALLOCATION';
  antStat.style.color = '#ef4444';
  antHeroImg.style.transform = 'scale(1.25)'; // Ballooning
  antGrid.querySelectorAll('div').forEach((d, idx) => {
    d.style.background = '#7f1d1d';
    d.style.borderColor = '#ef4444';
  });
  antDiag.innerHTML = `⚠️ <strong>Hank Pym:</strong> "Warning! Recursive activation call stack frames created N=${antSize} stack frames! Space ballooned to O(N)!"`;
});

document.getElementById('ant-btn-auto')?.addEventListener('click', function() {
  retroAudio.playClick();
  if (antAutoTimer) {
    clearInterval(antAutoTimer);
    antAutoTimer = null;
    this.textContent = '▶ AUTO-RUN SIMULATION';
  } else {
    this.textContent = '⏸ PAUSE SIMULATION';
    antStepIdx = 0;
    antAutoTimer = setInterval(() => {
      stepAntInplace();
    }, 700);
  }
});

document.getElementById('ant-btn-reset')?.addEventListener('click', () => {
  retroAudio.playClick();
  if (antAutoTimer) { clearInterval(antAutoTimer); antAutoTimer = null; document.getElementById('ant-btn-auto').textContent = '▶ AUTO-RUN SIMULATION'; }
  initAntGrid();
});
"""
}

# 2. DOCTOR STRANGE: Time Realities (Time Complexity)
SIMULATIONS["time_growth"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #f59e0b;">MISSION: 14,000,605 TIME REALITIES</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Doctor Strange flies between mystic portals comparing step growth: O(1) vs O(log n) vs O(n) vs O(n²).</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #facc15; padding: 6px 10px; border: 1px solid #475569;">
      TIME STONE: <span id="ds-stone-stat">SYNCHRONIZED</span>
    </div>
  </div>

  <!-- User Custom Input Bar -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; align-items: center; gap: 8px;">
      <label style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a;">INPUT SIZE (N):</label>
      <input type="range" id="ds-slider-n" min="4" max="64" value="16" class="custom-range" style="width: 140px; accent-color: #f59e0b;">
      <span id="ds-n-readout" style="font-family: var(--font-code); font-weight: bold; font-size: 0.85rem; color: #0f172a;">N = 16</span>
    </div>
    <button class="pixel-btn pixel-btn-primary" id="ds-btn-eval" style="padding: 6px 12px; font-size: 0.6rem;">⚡ CAST TIME COMPARISON</button>
  </div>

  <!-- Animated Mystic Arena -->
  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 200px;">
    <!-- Doctor Strange Flying Actor -->
    <div id="ds-hero-actor" style="position: absolute; top: 15px; left: 30px; transition: all 0.5s ease-in-out; z-index: 10;">
      <img src="assets/doctorstrange.png" style="width: 50px; height: 56px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 0 10px rgba(245,158,11,0.7));">
    </div>

    <!-- 4 Portals Grid -->
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 12px; margin-top: 45px;">
      <div id="portal-c" style="background: rgba(16, 185, 129, 0.15); border: 2px dashed #10b981; padding: 14px 10px; border-radius: 6px; text-align: center;">
        <div style="font-family: var(--font-pixel); font-size: 0.6rem; color: #10b981; margin-bottom: 4px;">CONSTANT O(1)</div>
        <div id="ds-val-c" style="font-family: var(--font-code); font-size: 1.1rem; font-weight: bold; color: #fff;">1 step</div>
        <small style="color: #94a3b8; font-size: 0.7rem;">Fixed cost</small>
      </div>

      <div id="portal-log" style="background: rgba(2, 132, 199, 0.15); border: 2px dashed #0284c7; padding: 14px 10px; border-radius: 6px; text-align: center;">
        <div style="font-family: var(--font-pixel); font-size: 0.6rem; color: #38bdf8; margin-bottom: 4px;">LOGARITHMIC O(log N)</div>
        <div id="ds-val-log" style="font-family: var(--font-code); font-size: 1.1rem; font-weight: bold; color: #fff;">4 steps</div>
        <small style="color: #94a3b8; font-size: 0.7rem;">Tree halving</small>
      </div>

      <div id="portal-lin" style="background: rgba(245, 158, 11, 0.15); border: 2px dashed #f59e0b; padding: 14px 10px; border-radius: 6px; text-align: center;">
        <div style="font-family: var(--font-pixel); font-size: 0.6rem; color: #facc15; margin-bottom: 4px;">LINEAR O(N)</div>
        <div id="ds-val-lin" style="font-family: var(--font-code); font-size: 1.1rem; font-weight: bold; color: #fff;">16 steps</div>
        <small style="color: #94a3b8; font-size: 0.7rem;">Single scan</small>
      </div>

      <div id="portal-quad" style="background: rgba(239, 68, 68, 0.15); border: 2px dashed #ef4444; padding: 14px 10px; border-radius: 6px; text-align: center;">
        <div style="font-family: var(--font-pixel); font-size: 0.6rem; color: #ef4444; margin-bottom: 4px;">QUADRATIC O(N²)</div>
        <div id="ds-val-quad" style="font-family: var(--font-code); font-size: 1.1rem; font-weight: bold; color: #fff;">256 steps</div>
        <small style="color: #94a3b8; font-size: 0.7rem;">Nested loops</small>
      </div>
    </div>
  </div>

  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; font-size: 0.88rem; min-height: 48px; display: flex; align-items: center;" id="ds-dialogue">
    💬 <strong>Doctor Strange:</strong> "Move the N slider to see how asymptotic step counts diverge. Quadratic algorithms explode as N grows!"
  </div>

  <div class="viz-controls" style="display: flex; gap: 10px; flex-wrap: wrap;">
    <button class="pixel-btn pixel-btn-primary" id="ds-btn-fly">✨ FLY STRANGE TO SLOWEST REALITY</button>
    <button class="pixel-btn pixel-btn-secondary" id="ds-btn-fly-opt">🌟 FLY TO FASTEST REALITY</button>
  </div>
</div>
""",
    "script": """
const dsSlider = document.getElementById('ds-slider-n');
const dsReadout = document.getElementById('ds-n-readout');
const dsValC = document.getElementById('ds-val-c');
const dsValLog = document.getElementById('ds-val-log');
const dsValLin = document.getElementById('ds-val-lin');
const dsValQuad = document.getElementById('ds-val-quad');
const dsDiag = document.getElementById('ds-dialogue');
const dsHero = document.getElementById('ds-hero-actor');

function updateStrangeTimes() {
  const n = parseInt(dsSlider.value);
  dsReadout.textContent = `N = ${n}`;
  const logSteps = Math.round(Math.log2(n));
  const quadSteps = n * n;

  dsValC.textContent = '1 step';
  dsValLog.textContent = `${logSteps} steps`;
  dsValLin.textContent = `${n} steps`;
  dsValQuad.textContent = `${quadSteps.toLocaleString()} steps`;

  dsDiag.innerHTML = `🔮 <strong>Doctor Strange:</strong> "For N=${n}: O(log N) needs only ${logSteps} steps, while O(N²) burns ${quadSteps} operations! That is a ${Math.round(quadSteps/logSteps)}× efficiency gap!"`;
}

dsSlider?.addEventListener('input', () => {
  updateStrangeTimes();
});

document.getElementById('ds-btn-eval')?.addEventListener('click', () => {
  retroAudio.playClick();
  updateStrangeTimes();
});

document.getElementById('ds-btn-fly')?.addEventListener('click', () => {
  retroAudio.playClick();
  const quadPortal = document.getElementById('portal-quad');
  dsHero.style.left = `${quadPortal.offsetLeft + 40}px`;
  dsHero.style.top = '10px';
  dsDiag.innerHTML = `⚠️ <strong>Doctor Strange:</strong> "I have arrived at the Quadratic Dimension! At N=${dsSlider.value}, execution requires ${dsValQuad.textContent}. Dormammu would escape before this finishes!"`;
});

document.getElementById('ds-btn-fly-opt')?.addEventListener('click', () => {
  retroAudio.playClick();
  const logPortal = document.getElementById('portal-log');
  dsHero.style.left = `${logPortal.offsetLeft + 40}px`;
  dsHero.style.top = '10px';
  dsDiag.innerHTML = `✨ <strong>Doctor Strange:</strong> "In the Logarithmic Realm O(log n), step count is bounded by ${dsValLog.textContent}. Algorithmic mastery defies temporal barriers!"`;
});
"""
}

# 3. VISION: Mind Stone Bounding Containment (Asymptotic Notations)
SIMULATIONS["bounds"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #10b981;">MISSION: MIND STONE ASYMPTOTIC CONTAINMENT</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Trap Ultron's virus function f(n) between lower bound Ω(g(n)) and upper bound O(g(n)).</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #38bdf8; padding: 6px 10px; border: 1px solid #475569;">
      TARGET: Θ(n²)
    </div>
  </div>

  <!-- Custom Input Constants -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; align-items: center; gap: 12px;">
      <div>
        <label style="font-family: var(--font-pixel); font-size: 0.58rem; color: #38bdf8;">LOWER c1:</label>
        <input type="number" id="v-c1-input" value="2" min="1" max="10" style="width: 48px; padding: 4px; border: 2px solid #0f172a; text-align: center; font-weight: bold;">
      </div>
      <div>
        <label style="font-family: var(--font-pixel); font-size: 0.58rem; color: #ef4444;">UPPER c2:</label>
        <input type="number" id="v-c2-input" value="10" min="1" max="25" style="width: 48px; padding: 4px; border: 2px solid #0f172a; text-align: center; font-weight: bold;">
      </div>
    </div>
    <button class="pixel-btn pixel-btn-primary" id="v-btn-apply" style="padding: 6px 12px; font-size: 0.6rem;">⚡ VERIFY INEQUALITY</button>
  </div>

  <!-- Arena Stage -->
  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 180px;">
    <!-- Vision Actor -->
    <div id="v-hero-actor" style="position: absolute; top: 12px; right: 25px; z-index: 10;">
      <img src="assets/vision.png" style="width: 50px; height: 55px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 0 8px rgba(16,185,129,0.7));">
    </div>

    <!-- Beam Ceiling -->
    <div style="margin-bottom: 20px;">
      <div style="display: flex; justify-content: space-between; font-family: var(--font-pixel); font-size: 0.62rem; color: #ef4444; margin-bottom: 4px;">
        <span>BIG-O CEILING: c2 · n²</span>
        <span id="v-c2-label">c2 = 10</span>
      </div>
      <div id="v-beam-top" style="height: 4px; width: 80%; background: #ef4444; box-shadow: 0 0 8px #ef4444; transition: all 0.3s ease;"></div>
    </div>

    <!-- Function Wave -->
    <div id="v-wave-container" style="background: rgba(30, 41, 59, 0.6); border: 2px dashed #facc15; padding: 12px; text-align: center; font-family: var(--font-code); color: #facc15; font-size: 1rem; font-weight: bold; margin-bottom: 20px;">
      f(n) = 3n² + 5n [ULTRON VIRUS SIGNAL]
    </div>

    <!-- Beam Floor -->
    <div>
      <div style="display: flex; justify-content: space-between; font-family: var(--font-pixel); font-size: 0.62rem; color: #38bdf8; margin-bottom: 4px;">
        <span>BIG-OMEGA FLOOR: c1 · n²</span>
        <span id="v-c1-label">c1 = 2</span>
      </div>
      <div id="v-beam-bottom" style="height: 4px; width: 80%; background: #38bdf8; box-shadow: 0 0 8px #38bdf8; transition: all 0.3s ease;"></div>
    </div>
  </div>

  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; font-size: 0.88rem; min-height: 48px; display: flex; align-items: center;" id="v-dialogue">
    💬 <strong>Vision:</strong> "When c1·n² ≤ 3n² + 5n ≤ c2·n² holds for all n ≥ 1, the function is asymptotically bounded in tight Θ(n²)."
  </div>

  <div class="viz-controls" style="display: flex; gap: 10px; flex-wrap: wrap;">
    <button class="pixel-btn pixel-btn-primary" id="v-btn-auto">▶ AUTO-CONVERGE THETA BOUND</button>
    <button class="pixel-btn pixel-btn-accent" id="v-btn-breach">⚠️ TEST INVALID UPPER BOUND (c2=1)</button>
    <button class="pixel-btn pixel-btn-secondary" id="v-btn-reset">↺ RESET CONSTANTS</button>
  </div>
</div>
""",
    "script": """
const vC1In = document.getElementById('v-c1-input');
const vC2In = document.getElementById('v-c2-input');
const vC1Lbl = document.getElementById('v-c1-label');
const vC2Lbl = document.getElementById('v-c2-label');
const vWave = document.getElementById('v-wave-container');
const vDiag = document.getElementById('v-dialogue');

function evaluateBounds() {
  const c1 = parseFloat(vC1In.value);
  const c2 = parseFloat(vC2In.value);
  vC1Lbl.textContent = `c1 = ${c1}`;
  vC2Lbl.textContent = `c2 = ${c2}`;

  // For n >= 1: f(n) = 3n^2 + 5n.
  // c1*n^2 <= 3n^2 + 5n holds if c1 <= 3.
  // 3n^2 + 5n <= c2*n^2 holds for all n>=1 if c2 >= 8 (at n=1, 3+5=8).
  if (c1 <= 3 && c2 >= 8) {
    vWave.style.borderColor = '#10b981';
    vWave.style.color = '#10b981';
    vWave.innerHTML = '🔒 [PERFECT ASYMPTOTIC THETA ENCLOSURE: c1 ≤ 3, c2 ≥ 8] 🔒';
    vDiag.innerHTML = `✨ <strong>Vision:</strong> "Mind Stone containment locked! For all n ≥ 1, ${c1}n² ≤ 3n² + 5n ≤ ${c2}n². Ultron is tightly trapped in Θ(n²)!"`;
  } else if (c2 < 8) {
    vWave.style.borderColor = '#ef4444';
    vWave.style.color = '#ef4444';
    vWave.innerHTML = '💥 [UPPER BOUND BREACHED: c2 TOO SMALL!] 💥';
    vDiag.innerHTML = `⚠️ <strong>Vision:</strong> "Upper bound violated! At n=1, 3n²+5n = 8 > ${c2}n². Big-O condition fails! Increase c2."`;
  } else {
    vWave.style.borderColor = '#f59e0b';
    vWave.style.color = '#facc15';
    vWave.innerHTML = '⚠️ [LOWER BOUND VIOLATED: c1 TOO LARGE!] ⚠️';
    vDiag.innerHTML = `⚠️ <strong>Vision:</strong> "Lower bound violated! c1 = ${c1} exceeds the floor for large n. Adjust c1 ≤ 3."`;
  }
}

document.getElementById('v-btn-apply')?.addEventListener('click', () => {
  retroAudio.playClick();
  evaluateBounds();
});

document.getElementById('v-btn-auto')?.addEventListener('click', () => {
  retroAudio.playClick();
  vC1In.value = "3";
  vC2In.value = "8";
  evaluateBounds();
});

document.getElementById('v-btn-breach')?.addEventListener('click', () => {
  retroAudio.playClick();
  vC1In.value = "2";
  vC2In.value = "1";
  evaluateBounds();
});

document.getElementById('v-btn-reset')?.addEventListener('click', () => {
  retroAudio.playClick();
  vC1In.value = "2";
  vC2In.value = "10";
  evaluateBounds();
});
"""
}

# 4. CAPTAIN AMERICA: Vibranium Shield Bunker Defense (Stacks)
SIMULATIONS["stack"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #2563eb;">MISSION: VIBRANIUM SHIELD LIFO BUNKER</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Stack shields into the vertical launch shaft. Last shield pushed is the first shield ricocheted!</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #f8fafc; padding: 6px 10px; border: 1px solid #475569;">
      STACK SIZE: <span id="cap-size" style="color: #38bdf8;">3</span> / 5
    </div>
  </div>

  <!-- Custom Shield Push Input -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; align-items: center; gap: 8px;">
      <label style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a;">SHIELD ID / VALUE:</label>
      <input type="text" id="cap-shield-val" value="VIB-4" style="width: 80px; padding: 4px; font-family: var(--font-code); font-weight: bold; border: 2px solid #0f172a; text-align: center;">
      <button class="pixel-btn pixel-btn-primary" id="cap-btn-custom-push" style="padding: 4px 10px; font-size: 0.58rem;">PUSH CUSTOM</button>
    </div>
    <div style="font-size: 0.75rem; color: #475569; font-weight: 600;">
      TOP Pointer: <span id="cap-top-idx" style="color: #2563eb; font-weight: bold;">Index 2</span>
    </div>
  </div>

  <!-- Animated Arena Stage -->
  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; display: grid; grid-template-columns: 120px 1fr 140px; gap: 14px; align-items: center; min-height: 220px;">
    <!-- Cap Sprite Actor -->
    <div style="text-align: center;">
      <img src="assets/captainamerica.png" id="cap-hero-img" style="width: 60px; height: 70px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 4px 8px rgba(37,99,235,0.6)); transition: transform 0.2s ease;">
      <div style="font-family: var(--font-pixel); font-size: 0.55rem; color: #94a3b8; margin-top: 4px;">CAPTAIN AMERICA</div>
    </div>

    <!-- Vertical Shaft Stack Container -->
    <div style="background: #1e293b; border: 3px solid #475569; border-top: none; min-height: 180px; padding: 8px; display: flex; flex-direction: column-reverse; gap: 6px; border-radius: 0 0 6px 6px;" id="cap-shaft">
      <div class="cap-shield" style="background: #2563eb; color: #fff; font-family: var(--font-pixel); font-size: 0.6rem; padding: 8px; border: 2px solid #000; text-align: center;">SHIELD #1 (BASE)</div>
      <div class="cap-shield" style="background: #dc2626; color: #fff; font-family: var(--font-pixel); font-size: 0.6rem; padding: 8px; border: 2px solid #000; text-align: center;">SHIELD #2</div>
      <div class="cap-shield" style="background: #facc15; color: #000; font-family: var(--font-pixel); font-size: 0.6rem; padding: 8px; border: 2px solid #000; text-align: center;">SHIELD #3 [TOP]</div>
    </div>

    <!-- Hydra Target Arena -->
    <div id="cap-target-arena" style="background: rgba(220, 38, 38, 0.15); border: 2px dashed #dc2626; padding: 14px 10px; border-radius: 6px; text-align: center; font-family: var(--font-pixel); font-size: 0.65rem; color: #f87171; min-height: 100px; display: flex; align-items: center; justify-content: center;">
      HYDRA BOT PATROLLING...
    </div>
  </div>

  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; font-size: 0.88rem; min-height: 48px; display: flex; align-items: center;" id="cap-dialogue">
    💬 <strong>Captain America:</strong> "Stack top pointer is at Shield #3. Pushing adds to top in O(1); popping strikes targets in strict LIFO order!"
  </div>

  <div class="viz-controls" style="display: flex; gap: 10px; flex-wrap: wrap;">
    <button class="pixel-btn pixel-btn-primary" id="cap-btn-auto">▶ AUTO-PLAY BATTLE (PUSH & POP)</button>
    <button class="pixel-btn pixel-btn-secondary" id="cap-btn-push">🛡️ PUSH SHIELD [O(1)]</button>
    <button class="pixel-btn pixel-btn-accent" id="cap-btn-pop">💥 POP & RICOCHET [O(1)]</button>
    <button class="pixel-btn pixel-btn-secondary" id="cap-btn-reset">↺ RESET STACK</button>
  </div>
</div>
""",
    "script": """
const capShaft = document.getElementById('cap-shaft');
const capSize = document.getElementById('cap-size');
const capTopIdx = document.getElementById('cap-top-idx');
const capDiag = document.getElementById('cap-dialogue');
const capArena = document.getElementById('cap-target-arena');
const capHeroImg = document.getElementById('cap-hero-img');
const capShieldVal = document.getElementById('cap-shield-val');
let shieldCount = 3;
let capAutoTimer = null;

function updateTopLabels() {
  const children = capShaft.children;
  for (let i = 0; i < children.length; i++) {
    children[i].textContent = children[i].textContent.replace(' [TOP]', '');
  }
  if (children.length > 0) {
    children[children.length - 1].textContent += ' [TOP]';
    capTopIdx.textContent = `Index ${children.length - 1}`;
  } else {
    capTopIdx.textContent = 'EMPTY (-1)';
  }
  capSize.textContent = children.length;
}

function pushShield(label) {
  if (capShaft.children.length < 5) {
    shieldCount++;
    const s = document.createElement('div');
    s.className = 'cap-shield';
    const cols = ['#2563eb', '#dc2626', '#facc15', '#16a34a', '#9333ea'];
    const col = cols[shieldCount % cols.length];
    s.style.cssText = `background: ${col}; color: #fff; font-family: var(--font-pixel); font-size: 0.6rem; padding: 8px; border: 2px solid #000; text-align: center; animation: popIn 0.3s;`;
    s.textContent = label || `SHIELD #${shieldCount}`;
    capShaft.appendChild(s);
    updateTopLabels();
    capHeroImg.style.transform = 'scale(1.15) translateX(5px)';
    setTimeout(() => capHeroImg.style.transform = 'scale(1)', 200);
    capDiag.innerHTML = `🛡️ <strong>Captain America:</strong> "Pushed ${s.textContent} onto stack top in O(1) time!"`;
  } else {
    capDiag.innerHTML = '⚠️ <strong>Captain America:</strong> "STACK OVERFLOW! The corridor capacity is full at 5 shields!"';
  }
}

function popShield() {
  if (capShaft.children.length > 0) {
    const popped = capShaft.lastElementChild;
    const name = popped.textContent.replace(' [TOP]', '');
    capShaft.removeChild(popped);
    updateTopLabels();
    capArena.innerHTML = `<span style="color:#22c55e;">💥 HYDRA BOT HIT by ${name}!</span>`;
    capDiag.innerHTML = `💥 <strong>Captain America:</strong> "Popped ${name} from Top! Last-In, First-Out strikes with O(1) speed!"`;
    setTimeout(() => { if (capArena) capArena.innerHTML = 'HYDRA BOT PATROLLING...'; }, 1200);
  } else {
    capDiag.innerHTML = '⚠️ <strong>Captain America:</strong> "STACK UNDERFLOW! Cannot pop from an empty stack!"';
  }
}

document.getElementById('cap-btn-push')?.addEventListener('click', () => { retroAudio.playClick(); pushShield(); });
document.getElementById('cap-btn-custom-push')?.addEventListener('click', () => { retroAudio.playClick(); pushShield(capShieldVal.value || 'CUSTOM'); });
document.getElementById('cap-btn-pop')?.addEventListener('click', () => { retroAudio.playClick(); popShield(); });

document.getElementById('cap-btn-auto')?.addEventListener('click', function() {
  retroAudio.playClick();
  if (capAutoTimer) {
    clearInterval(capAutoTimer);
    capAutoTimer = null;
    this.textContent = '▶ AUTO-PLAY BATTLE (PUSH & POP)';
  } else {
    this.textContent = '⏸ PAUSE BATTLE';
    let flip = true;
    capAutoTimer = setInterval(() => {
      if (capShaft.children.length >= 5) flip = false;
      if (capShaft.children.length <= 1) flip = true;
      if (flip) pushShield(); else popShield();
    }, 900);
  }
});

document.getElementById('cap-btn-reset')?.addEventListener('click', () => {
  retroAudio.playClick();
  if (capAutoTimer) { clearInterval(capAutoTimer); capAutoTimer = null; document.getElementById('cap-btn-auto').textContent = '▶ AUTO-PLAY BATTLE (PUSH & POP)'; }
  capShaft.innerHTML = `
    <div class="cap-shield" style="background: #2563eb; color: #fff; font-family: var(--font-pixel); font-size: 0.6rem; padding: 8px; border: 2px solid #000; text-align: center;">SHIELD #1 (BASE)</div>
    <div class="cap-shield" style="background: #dc2626; color: #fff; font-family: var(--font-pixel); font-size: 0.6rem; padding: 8px; border: 2px solid #000; text-align: center;">SHIELD #2</div>
    <div class="cap-shield" style="background: #facc15; color: #000; font-family: var(--font-pixel); font-size: 0.6rem; padding: 8px; border: 2px solid #000; text-align: center;">SHIELD #3 [TOP]</div>
  `;
  shieldCount = 3;
  updateTopLabels();
});
"""
}

# 5. HULK: Gamma Smash Chitauri Conveyor (Queues)
SIMULATIONS["queue"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #16a34a;">MISSION: HULK GAMMA CHITAURI FIFO CONVEYOR</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Smash invading Chitauri assault chariots in strict First-In, First-Out (FIFO) queue order!</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #22c55e; padding: 6px 10px; border: 1px solid #475569;">
      QUEUE LENGTH: <span id="hulk-len" style="color: #22c55e;">3</span> / 5
    </div>
  </div>

  <!-- Custom Chariot Input -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; align-items: center; gap: 8px;">
      <label style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a;">CHARIOT NAME:</label>
      <input type="text" id="hulk-chariot-val" value="TITAN-4" style="width: 80px; padding: 4px; font-family: var(--font-code); font-weight: bold; border: 2px solid #0f172a; text-align: center;">
      <button class="pixel-btn pixel-btn-primary" id="hulk-btn-custom-enq" style="padding: 4px 10px; font-size: 0.58rem;">ENQUEUE CUSTOM</button>
    </div>
    <div style="font-size: 0.75rem; color: #475569; font-weight: 600;">
      REAR ➔ [FIFO Pipeline] ➔ FRONT
    </div>
  </div>

  <!-- Animated Arena Stage -->
  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative;">
    <div style="display: flex; justify-content: space-between; font-family: var(--font-pixel); font-size: 0.62rem; color: #94a3b8; margin-bottom: 8px;">
      <span style="color: #38bdf8;">[REAR (ENQUEUE)]</span>
      <span style="color: #22c55e;">CONVEYOR DIRECTION ➔ ➔ ➔</span>
      <span style="color: #ef4444;">[FRONT (NEXT TO SMASH)]</span>
    </div>

    <div style="display: flex; gap: 12px; align-items: center;">
      <div id="hulk-runway" style="flex: 1; display: flex; gap: 10px; min-height: 75px; background: #1e293b; border: 3px solid #475569; padding: 10px; border-radius: 4px; align-items: center; justify-content: flex-end; overflow-x: auto;">
        <div class="hulk-drone" style="background: #334155; color: #fff; font-family: var(--font-pixel); font-size: 0.6rem; padding: 10px; border: 2px solid #000;">CHARIOT #1 [FRONT]</div>
        <div class="hulk-drone" style="background: #475569; color: #fff; font-family: var(--font-pixel); font-size: 0.6rem; padding: 10px; border: 2px solid #000;">CHARIOT #2</div>
        <div class="hulk-drone" style="background: #16a34a; color: #fff; font-family: var(--font-pixel); font-size: 0.6rem; padding: 10px; border: 2px solid #000;">CHARIOT #3 [REAR]</div>
      </div>

      <!-- Hulk Smash Actor -->
      <div style="width: 70px; text-align: center; flex-shrink: 0;">
        <img src="assets/hulk.png" id="hulk-actor-img" style="width: 60px; height: 75px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 4px 8px rgba(22,163,74,0.7)); transition: transform 0.2s ease;">
      </div>
    </div>
  </div>

  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; font-size: 0.88rem; min-height: 48px; display: flex; align-items: center;" id="hulk-dialogue">
    💬 <strong>Hulk:</strong> "First chariot in line is first chariot Hulk smash! Enqueue adds to Rear; Dequeue smashes from Front in O(1) time!"
  </div>

  <div class="viz-controls" style="display: flex; gap: 10px; flex-wrap: wrap;">
    <button class="pixel-btn pixel-btn-primary" id="hulk-btn-auto">▶ AUTO-RUN SMASH CONVEYOR</button>
    <button class="pixel-btn pixel-btn-secondary" id="hulk-btn-enq">👾 ENQUEUE CHARIOT [O(1)]</button>
    <button class="pixel-btn pixel-btn-accent" id="hulk-btn-deq">💥 HULK SMASH FRONT [O(1)]</button>
    <button class="pixel-btn pixel-btn-secondary" id="hulk-btn-reset">↺ RESET CONVEYOR</button>
  </div>
</div>
""",
    "script": """
const hulkRunway = document.getElementById('hulk-runway');
const hulkLen = document.getElementById('hulk-len');
const hulkDiag = document.getElementById('hulk-dialogue');
const hulkImg = document.getElementById('hulk-actor-img');
const hulkVal = document.getElementById('hulk-chariot-val');
let hulkCount = 3;
let hulkAutoTimer = null;

function updateHulkLabels() {
  hulkLen.textContent = hulkRunway.children.length;
}

function enqueueChariot(label) {
  if (hulkRunway.children.length < 5) {
    hulkCount++;
    const d = document.createElement('div');
    d.className = 'hulk-drone';
    d.style.cssText = 'background: #16a34a; color: #fff; font-family: var(--font-pixel); font-size: 0.6rem; padding: 10px; border: 2px solid #000; animation: popIn 0.3s;';
    d.textContent = label || `CHARIOT #${hulkCount} [REAR]`;
    
    const firstChild = hulkRunway.firstElementChild;
    if (firstChild) firstChild.textContent = firstChild.textContent.replace(' [REAR]', '');
    hulkRunway.insertBefore(d, hulkRunway.firstChild);
    updateHulkLabels();
    hulkDiag.innerHTML = `👾 <strong>Hulk:</strong> "${d.textContent} enters Rear index in O(1) time! Waiting its turn in FIFO sequence!"`;
  } else {
    hulkDiag.innerHTML = '⚠️ <strong>Hulk:</strong> "QUEUE OVERFLOW! Conveyor is packed with 5 chariots!"';
  }
}

function dequeueChariot() {
  if (hulkRunway.children.length > 0) {
    const front = hulkRunway.lastElementChild;
    const name = front.textContent.replace(' [FRONT]', '');
    hulkRunway.removeChild(front);
    if (hulkRunway.lastElementChild) {
      hulkRunway.lastElementChild.textContent = hulkRunway.lastElementChild.textContent.replace(' [FRONT]', '') + ' [FRONT]';
    }
    updateHulkLabels();
    hulkImg.style.transform = 'scale(1.25) translateX(-8px)';
    setTimeout(() => hulkImg.style.transform = 'scale(1)', 200);
    hulkDiag.innerHTML = `💥 <strong>Hulk:</strong> "HULK SMASH ${name}! Dequeued from Front in O(1) time! FIFO order strictly respected!"`;
  } else {
    hulkDiag.innerHTML = '⚠️ <strong>Hulk:</strong> "QUEUE UNDERFLOW! No chariots left for Hulk to smash!"';
  }
}

document.getElementById('hulk-btn-enq')?.addEventListener('click', () => { retroAudio.playClick(); enqueueChariot(); });
document.getElementById('hulk-btn-custom-enq')?.addEventListener('click', () => { retroAudio.playClick(); enqueueChariot(hulkVal.value); });
document.getElementById('hulk-btn-deq')?.addEventListener('click', () => { retroAudio.playClick(); dequeueChariot(); });

document.getElementById('hulk-btn-auto')?.addEventListener('click', function() {
  retroAudio.playClick();
  if (hulkAutoTimer) {
    clearInterval(hulkAutoTimer);
    hulkAutoTimer = null;
    this.textContent = '▶ AUTO-RUN SMASH CONVEYOR';
  } else {
    this.textContent = '⏸ PAUSE CONVEYOR';
    let flip = true;
    hulkAutoTimer = setInterval(() => {
      if (hulkRunway.children.length >= 5) flip = false;
      if (hulkRunway.children.length <= 1) flip = true;
      if (flip) enqueueChariot(); else dequeueChariot();
    }, 900);
  }
});

document.getElementById('hulk-btn-reset')?.addEventListener('click', () => {
  retroAudio.playClick();
  if (hulkAutoTimer) { clearInterval(hulkAutoTimer); hulkAutoTimer = null; document.getElementById('hulk-btn-auto').textContent = '▶ AUTO-RUN SMASH CONVEYOR'; }
  hulkRunway.innerHTML = `
    <div class="hulk-drone" style="background: #334155; color: #fff; font-family: var(--font-pixel); font-size: 0.6rem; padding: 10px; border: 2px solid #000;">CHARIOT #1 [FRONT]</div>
    <div class="hulk-drone" style="background: #475569; color: #fff; font-family: var(--font-pixel); font-size: 0.6rem; padding: 10px; border: 2px solid #000;">CHARIOT #2</div>
    <div class="hulk-drone" style="background: #16a34a; color: #fff; font-family: var(--font-pixel); font-size: 0.6rem; padding: 10px; border: 2px solid #000;">CHARIOT #3 [REAR]</div>
  `;
  hulkCount = 3;
  updateHulkLabels();
});
"""
}
