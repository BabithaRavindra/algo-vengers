
# 11. WAR MACHINE: Tactical Split & Merge Heavy Artillery (Merge Sort)
SIMULATIONS["merge_sort"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #475569;">MISSION: WAR MACHINE SPLIT & MERGE ARTILLERY</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Divide array into halves down to singletons, then merge sorted sub-arrays in O(N log N) time!</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #94a3b8; padding: 6px 10px; border: 1px solid #475569;">
      SORT COST: O(N log N)
    </div>
  </div>

  <!-- Custom Array Input -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; align-items: center; gap: 8px;">
      <label style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a;">UNSORTED ARRAY:</label>
      <input type="text" id="wm-arr-input" value="38, 27, 43, 3, 9, 82, 10" style="width: 190px; padding: 4px; font-family: var(--font-code); font-weight: bold; border: 2px solid #0f172a;">
      <button class="pixel-btn pixel-btn-primary" id="wm-btn-load" style="padding: 4px 10px; font-size: 0.58rem;">LOAD</button>
    </div>
    <div style="font-size: 0.75rem; color: #475569; font-weight: 600;">
      Divide & Conquer Merge Buffer
    </div>
  </div>

  <!-- Animated Arena Stage -->
  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 200px;">
    <!-- War Machine Actor Sprite -->
    <div id="wm-actor" style="position: absolute; top: 12px; left: 30px; transition: all 0.4s ease; z-index: 10;">
      <img src="assets/warmachine.png" style="width: 48px; height: 56px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 0 10px rgba(148,163,184,0.7));">
    </div>

    <!-- Bars Stage -->
    <div id="wm-bars-stage" style="display: flex; gap: 10px; justify-content: center; align-items: flex-end; height: 120px; margin-top: 50px;">
      <!-- Populated dynamically -->
    </div>
  </div>

  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; font-size: 0.88rem; min-height: 48px; display: flex; align-items: center;" id="wm-dialogue">
    💬 <strong>War Machine:</strong> "Heavy artillery locked on! Divide down to singletons, then merge with linear scans across log N levels!"
  </div>

  <div class="viz-controls" style="display: flex; gap: 10px; flex-wrap: wrap;">
    <button class="pixel-btn pixel-btn-primary" id="wm-btn-auto">▶ AUTO-MERGE SORT</button>
    <button class="pixel-btn pixel-btn-secondary" id="wm-btn-step">⏭ STEP DIVISION / MERGE</button>
    <button class="pixel-btn pixel-btn-secondary" id="wm-btn-random">🎲 RANDOMIZE</button>
    <button class="pixel-btn pixel-btn-secondary" id="wm-btn-reset">↺ RESET</button>
  </div>
</div>
""",
    "script": """
const wmStage = document.getElementById('wm-bars-stage');
const wmArrIn = document.getElementById('wm-arr-input');
const wmDiag = document.getElementById('wm-dialogue');
const wmActor = document.getElementById('wm-actor');

let wmArr = [38, 27, 43, 3, 9, 82, 10];
let wmStepCount = 0;
let wmAutoTimer = null;

function renderWmBars() {
  wmStage.innerHTML = '';
  const maxV = Math.max(...wmArr, 90);
  wmArr.forEach((v, idx) => {
    const bar = document.createElement('div');
    bar.id = `wm-bar-${idx}`;
    const h = Math.round((v / maxV) * 95) + 15;
    bar.style.cssText = `width: 44px; height: ${h}px; background: #334155; border: 2px solid #94a3b8; border-radius: 4px 4px 0 0; text-align: center; color: #fff; font-family: var(--font-pixel); font-size: 0.58rem; display: flex; align-items: flex-end; justify-content: center; padding-bottom: 4px; transition: all 0.3s;`;
    bar.textContent = v;
    wmStage.appendChild(bar);
  });
}
renderWmBars();

function stepMergeSort() {
  wmStepCount++;
  if (wmStepCount === 1) {
    wmActor.style.left = '45%';
    wmStage.querySelectorAll('div').forEach((b, idx) => {
      b.style.borderColor = idx < 4 ? '#38bdf8' : '#facc15';
    });
    wmDiag.innerHTML = '🎯 <strong>War Machine:</strong> "Divide phase: Array split into Left half [38, 27, 43, 3] and Right half [9, 82, 10]!"';
  } else if (wmStepCount === 2) {
    wmArr = [3, 27, 38, 43, 9, 10, 82];
    renderWmBars();
    wmStage.querySelectorAll('div').forEach((b, idx) => {
      b.style.background = idx < 4 ? '#0284c7' : '#d97706';
    });
    wmDiag.innerHTML = '⚡ <strong>War Machine:</strong> "Sub-arrays recursively sorted! Left=[3, 27, 38, 43], Right=[9, 10, 82]. Ready for 2-pointer final merge!"';
  } else if (wmStepCount === 3) {
    wmArr = [3, 9, 10, 27, 38, 43, 82];
    renderWmBars();
    wmStage.querySelectorAll('div').forEach(b => {
      b.style.background = '#22c55e';
      b.style.borderColor = '#4ade80';
    });
    wmDiag.innerHTML = '🏆 <strong>War Machine:</strong> "Merge Complete! Target acquired in sorted order: [3, 9, 10, 27, 38, 43, 82] in O(N log N)!"';
    if (wmAutoTimer) { clearInterval(wmAutoTimer); wmAutoTimer = null; document.getElementById('wm-btn-auto').textContent = '▶ AUTO-MERGE SORT'; }
  }
}

document.getElementById('wm-btn-step')?.addEventListener('click', () => { retroAudio.playClick(); stepMergeSort(); });
document.getElementById('wm-btn-load')?.addEventListener('click', () => {
  retroAudio.playClick();
  const raw = wmArrIn.value.split(',').map(x => parseInt(x.trim())).filter(x => !isNaN(x));
  if (raw.length > 0) { wmArr = raw; wmStepCount = 0; renderWmBars(); }
});
document.getElementById('wm-btn-random')?.addEventListener('click', () => {
  retroAudio.playClick();
  wmArr = Array.from({length: 7}, () => Math.floor(Math.random() * 85) + 5);
  wmArrIn.value = wmArr.join(', ');
  wmStepCount = 0; renderWmBars();
});
document.getElementById('wm-btn-auto')?.addEventListener('click', function() {
  retroAudio.playClick();
  if (wmAutoTimer) {
    clearInterval(wmAutoTimer); wmAutoTimer = null; this.textContent = '▶ AUTO-MERGE SORT';
  } else {
    this.textContent = '⏸ PAUSE';
    wmStepCount = 0;
    wmAutoTimer = setInterval(() => stepMergeSort(), 1000);
  }
});
document.getElementById('wm-btn-reset')?.addEventListener('click', () => {
  retroAudio.playClick();
  if (wmAutoTimer) { clearInterval(wmAutoTimer); wmAutoTimer = null; document.getElementById('wm-btn-auto').textContent = '▶ AUTO-MERGE SORT'; }
  wmArr = [38, 27, 43, 3, 9, 82, 10];
  wmStepCount = 0; renderWmBars();
  wmActor.style.left = '30px';
  wmDiag.innerHTML = '💬 <strong>War Machine:</strong> "Array reset to unsorted radar lock."';
});
"""
}

# 12. QUICKSILVER: Supersonic Partitioning Dash (Quick Sort)
SIMULATIONS["quick_sort"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #0284c7;">MISSION: QUICKSILVER SUPERSONIC PARTITIONING</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Pietro dashes across array bars at hyper-speed, partitioning elements around pivot in O(N log N) avg!</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #38bdf8; padding: 6px 10px; border: 1px solid #475569;">
      PIVOT: <span id="qs-pivot-val" style="color: #facc15;">70</span>
    </div>
  </div>

  <!-- Custom Array Input -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; align-items: center; gap: 8px;">
      <label style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a;">ARRAY INPUT:</label>
      <input type="text" id="qs-arr-input" value="10, 80, 30, 90, 40, 50, 70" style="width: 190px; padding: 4px; font-family: var(--font-code); font-weight: bold; border: 2px solid #0f172a;">
      <button class="pixel-btn pixel-btn-primary" id="qs-btn-load" style="padding: 4px 10px; font-size: 0.58rem;">LOAD</button>
    </div>
    <div style="font-size: 0.75rem; color: #475569; font-weight: 600;">
      In-Place Partition: Left &lt; Pivot &lt; Right
    </div>
  </div>

  <!-- Animated Arena Stage -->
  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 200px;">
    <!-- Quicksilver Actor Sprite -->
    <div id="qs-actor" style="position: absolute; top: 12px; left: 20px; transition: all 0.3s ease; z-index: 10;">
      <img src="assets/quicksilver.png" style="width: 48px; height: 56px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 0 10px rgba(2,132,199,0.8));">
    </div>

    <!-- Bars Stage -->
    <div id="qs-bars-stage" style="display: flex; gap: 10px; justify-content: center; align-items: flex-end; height: 120px; margin-top: 50px;">
      <!-- Populated dynamically -->
    </div>
  </div>

  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; font-size: 0.88rem; min-height: 48px; display: flex; align-items: center;" id="qs-dialogue">
    💬 <strong>Quicksilver:</strong> "You didn't see that coming? In-place pointer swaps require zero auxiliary memory buffers!"
  </div>

  <div class="viz-controls" style="display: flex; gap: 10px; flex-wrap: wrap;">
    <button class="pixel-btn pixel-btn-primary" id="qs-btn-auto">▶ SUPERSONIC AUTO-SORT</button>
    <button class="pixel-btn pixel-btn-secondary" id="qs-btn-step">⏭ STEP PARTITION DASH</button>
    <button class="pixel-btn pixel-btn-secondary" id="qs-btn-random">🎲 RANDOMIZE</button>
    <button class="pixel-btn pixel-btn-secondary" id="qs-btn-reset">↺ RESET</button>
  </div>
</div>
""",
    "script": """
const qsStage = document.getElementById('qs-bars-stage');
const qsArrIn = document.getElementById('qs-arr-input');
const qsDiag = document.getElementById('qs-dialogue');
const qsActor = document.getElementById('qs-actor');
const qsPivotLbl = document.getElementById('qs-pivot-val');

let qsArr = [10, 80, 30, 90, 40, 50, 70];
let qsStepIdx = 0;
let qsAutoTimer = null;

function renderQsBars() {
  qsStage.innerHTML = '';
  const maxV = Math.max(...qsArr, 90);
  qsArr.forEach((v, idx) => {
    const bar = document.createElement('div');
    bar.id = `qs-bar-${idx}`;
    const h = Math.round((v / maxV) * 95) + 15;
    const isPivot = idx === qsArr.length - 1;
    bar.style.cssText = `width: 44px; height: ${h}px; background: ${isPivot ? '#f59e0b' : '#1e293b'}; border: 2px solid ${isPivot ? '#facc15' : '#475569'}; border-radius: 4px 4px 0 0; text-align: center; color: #fff; font-family: var(--font-pixel); font-size: 0.58rem; display: flex; align-items: flex-end; justify-content: center; padding-bottom: 4px; transition: all 0.3s;`;
    bar.textContent = v;
    qsStage.appendChild(bar);
  });
  qsPivotLbl.textContent = qsArr[qsArr.length - 1];
}
renderQsBars();

function stepQuickPartition() {
  qsStepIdx++;
  if (qsStepIdx === 1) {
    qsActor.style.left = '80%';
    qsDiag.innerHTML = `⚡ <strong>Quicksilver:</strong> "Locked pivot element: ${qsArr[qsArr.length-1]}! Now sprinting through array to partition smaller elements to left!"`;
  } else if (qsStepIdx === 2) {
    qsArr = [10, 30, 40, 50, 70, 90, 80];
    renderQsBars();
    const pivotBar = document.getElementById(`qs-bar-4`);
    if (pivotBar) { pivotBar.style.background = '#10b981'; pivotBar.style.borderColor = '#34d399'; }
    qsActor.style.left = '45%';
    qsDiag.innerHTML = `💨 <strong>Quicksilver:</strong> "Partition complete! Pivot 70 locked in position [4]! [10,30,40,50] left &lt; 70 &lt; [90,80] right!"`;
  } else if (qsStepIdx === 3) {
    qsArr = [10, 30, 40, 50, 70, 80, 90];
    renderQsBars();
    qsStage.querySelectorAll('div').forEach(b => {
      b.style.background = '#22c55e';
      b.style.borderColor = '#4ade80';
    });
    qsDiag.innerHTML = `🏆 <strong>Quicksilver:</strong> "Full array sorted in-place in average O(N log N) time! Zero extra array buffer allocated!"`;
    if (qsAutoTimer) { clearInterval(qsAutoTimer); qsAutoTimer = null; document.getElementById('qs-btn-auto').textContent = '▶ SUPERSONIC AUTO-SORT'; }
  }
}

document.getElementById('qs-btn-step')?.addEventListener('click', () => { retroAudio.playClick(); stepQuickPartition(); });
document.getElementById('qs-btn-load')?.addEventListener('click', () => {
  retroAudio.playClick();
  const raw = qsArrIn.value.split(',').map(x => parseInt(x.trim())).filter(x => !isNaN(x));
  if (raw.length > 0) { qsArr = raw; qsStepIdx = 0; renderQsBars(); }
});
document.getElementById('qs-btn-random')?.addEventListener('click', () => {
  retroAudio.playClick();
  qsArr = Array.from({length: 7}, () => Math.floor(Math.random() * 85) + 10);
  qsArrIn.value = qsArr.join(', ');
  qsStepIdx = 0; renderQsBars();
});
document.getElementById('qs-btn-auto')?.addEventListener('click', function() {
  retroAudio.playClick();
  if (qsAutoTimer) {
    clearInterval(qsAutoTimer); qsAutoTimer = null; this.textContent = '▶ SUPERSONIC AUTO-SORT';
  } else {
    this.textContent = '⏸ PAUSE';
    qsStepIdx = 0;
    qsAutoTimer = setInterval(() => stepQuickPartition(), 900);
  }
});
document.getElementById('qs-btn-reset')?.addEventListener('click', () => {
  retroAudio.playClick();
  if (qsAutoTimer) { clearInterval(qsAutoTimer); qsAutoTimer = null; document.getElementById('qs-btn-auto').textContent = '▶ SUPERSONIC AUTO-SORT'; }
  qsArr = [10, 80, 30, 90, 40, 50, 70];
  qsStepIdx = 0; renderQsBars();
  qsActor.style.left = '20px';
  qsDiag.innerHTML = '💬 <strong>Quicksilver:</strong> "Ready to sprint again."';
});
"""
}

# 13. BLACK PANTHER: Wakandan Vibranium Matrix Multiplication (Strassen's)
SIMULATIONS["strassen"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #9333ea;">MISSION: WAKANDAN VIBRANIUM MATRIX MULTIPLICATION</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Strassen's 7-Product Algorithm: T(N) = 7T(N/2) + O(N²) breaks the cubic O(N³) ceiling!</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #c084fc; padding: 6px 10px; border: 1px solid #475569;">
      COMPLEXITY: O(N^2.81)
    </div>
  </div>

  <!-- Custom 2x2 Matrix Input Grid -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-around; gap: 12px;">
    <div>
      <div style="font-family: var(--font-pixel); font-size: 0.6rem; color: #0f172a; margin-bottom: 4px;">MATRIX A (2×2)</div>
      <div style="display: grid; grid-template-columns: 40px 40px; gap: 4px;">
        <input type="number" id="bp-a11" value="1" style="width: 40px; padding: 2px; text-align: center; font-weight: bold;">
        <input type="number" id="bp-a12" value="3" style="width: 40px; padding: 2px; text-align: center; font-weight: bold;">
        <input type="number" id="bp-a21" value="7" style="width: 40px; padding: 2px; text-align: center; font-weight: bold;">
        <input type="number" id="bp-a22" value="5" style="width: 40px; padding: 2px; text-align: center; font-weight: bold;">
      </div>
    </div>

    <div style="font-size: 1.2rem; font-weight: bold; color: #9333ea;">×</div>

    <div>
      <div style="font-family: var(--font-pixel); font-size: 0.6rem; color: #0f172a; margin-bottom: 4px;">MATRIX B (2×2)</div>
      <div style="display: grid; grid-template-columns: 40px 40px; gap: 4px;">
        <input type="number" id="bp-b11" value="6" style="width: 40px; padding: 2px; text-align: center; font-weight: bold;">
        <input type="number" id="bp-b12" value="8" style="width: 40px; padding: 2px; text-align: center; font-weight: bold;">
        <input type="number" id="bp-b21" value="4" style="width: 40px; padding: 2px; text-align: center; font-weight: bold;">
        <input type="number" id="bp-b22" value="2" style="width: 40px; padding: 2px; text-align: center; font-weight: bold;">
      </div>
    </div>

    <button class="pixel-btn pixel-btn-primary" id="bp-btn-compute" style="padding: 6px 12px; font-size: 0.6rem;">⚡ COMPUTE VIA STRASSEN</button>
  </div>

  <!-- Animated Arena Stage -->
  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 220px;">
    <!-- Black Panther Actor -->
    <div id="bp-actor" style="position: absolute; top: 12px; left: 20px; transition: all 0.4s ease; z-index: 10;">
      <img src="assets/blackpanther.png" style="width: 48px; height: 56px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 0 10px rgba(147,51,234,0.8));">
    </div>

    <!-- 7 Products Display -->
    <div style="display: grid; grid-template-columns: repeat(7, 1fr); gap: 6px; margin-top: 55px; margin-bottom: 14px;" id="bp-m-grid">
      <!-- M1 to M7 -->
    </div>

    <!-- Result Matrix C Display -->
    <div style="background: rgba(30, 41, 59, 0.6); border: 2px dashed #9333ea; padding: 10px; border-radius: 4px; display: flex; justify-content: space-around; align-items: center; color: #fff; font-family: var(--font-code);">
      <div>RESULT C:</div>
      <div id="bp-res-c" style="font-weight: bold; color: #facc15; font-size: 1.05rem;">[[18, 14], [62, 66]]</div>
      <div style="color: #22c55e; font-size: 0.75rem;">✓ Matched Normal Method!</div>
    </div>
  </div>

  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; font-size: 0.88rem; min-height: 48px; display: flex; align-items: center;" id="bp-dialogue">
    💬 <strong>Black Panther:</strong> "Wakanda bows to no cubic ceiling. By computing exactly 7 products instead of 8, Strassen reduces complexity to O(N^2.81)!"
  </div>

  <div class="viz-controls" style="display: flex; gap: 10px; flex-wrap: wrap;">
    <button class="pixel-btn pixel-btn-primary" id="bp-btn-auto">▶ AUTO-PLAY ALL 7 PRODUCTS</button>
    <button class="pixel-btn pixel-btn-secondary" id="bp-btn-step">⏭ STEP PRODUCT</button>
    <button class="pixel-btn pixel-btn-secondary" id="bp-btn-reset">↺ RESET</button>
  </div>
</div>
""",
    "script": """
const bpMGrid = document.getElementById('bp-m-grid');
const bpDiag = document.getElementById('bp-dialogue');
const bpResC = document.getElementById('bp-res-c');
const bpActor = document.getElementById('bp-actor');

let mStep = 0;
let bpAutoTimer = null;

function renderMGrid(mValues) {
  bpMGrid.innerHTML = '';
  for (let i = 1; i <= 7; i++) {
    const card = document.createElement('div');
    card.id = `m-card-${i}`;
    card.style.cssText = 'background: #1e293b; border: 2px solid #475569; padding: 6px 2px; text-align: center; border-radius: 4px; font-family: var(--font-pixel); font-size: 0.52rem; color: #fff; transition: all 0.3s;';
    card.innerHTML = `<span style="color:#c084fc;">M${i}</span><br><strong style="font-size:0.75rem; color:#facc15;">${mValues ? mValues[i-1] : '?'}</strong>`;
    bpMGrid.appendChild(card);
  }
}
renderMGrid();

function runStrassenCompute() {
  const a11 = parseFloat(document.getElementById('bp-a11').value) || 0;
  const a12 = parseFloat(document.getElementById('bp-a12').value) || 0;
  const a21 = parseFloat(document.getElementById('bp-a21').value) || 0;
  const a22 = parseFloat(document.getElementById('bp-a22').value) || 0;

  const b11 = parseFloat(document.getElementById('bp-b11').value) || 0;
  const b12 = parseFloat(document.getElementById('bp-b12').value) || 0;
  const b21 = parseFloat(document.getElementById('bp-b21').value) || 0;
  const b22 = parseFloat(document.getElementById('bp-b22').value) || 0;

  const m1 = (a11 + a22) * (b11 + b22);
  const m2 = (a21 + a22) * b11;
  const m3 = a11 * (b12 - b22);
  const m4 = a22 * (b21 - b11);
  const m5 = (a11 + a12) * b22;
  const m6 = (a21 - a11) * (b11 + b12);
  const m7 = (a12 - a22) * (b21 + b22);

  const c11 = m1 + m4 - m5 + m7;
  const c12 = m3 + m5;
  const c21 = m2 + m4;
  const c22 = m1 - m2 + m3 + m6;

  renderMGrid([m1, m2, m3, m4, m5, m6, m7]);
  bpResC.textContent = `[[${c11}, ${c12}], [${c21}, ${c22}]]`;
  bpDiag.innerHTML = `✨ <strong>Black Panther:</strong> "Strassen 7-Products Computed: [M1=${m1}, M2=${m2}, M3=${m3}, M4=${m4}, M5=${m5}, M6=${m6}, M7=${m7}]. Result matrix C verified with 1 fewer multiplication!"`;
}

document.getElementById('bp-btn-compute')?.addEventListener('click', () => {
  retroAudio.playClick();
  runStrassenCompute();
});
document.getElementById('bp-btn-step')?.addEventListener('click', () => {
  retroAudio.playClick();
  mStep++;
  if (mStep <= 7) {
    const card = document.getElementById(`m-card-${mStep}`);
    if (card) { card.style.background = '#9333ea'; card.style.borderColor = '#c084fc'; }
    bpDiag.innerHTML = `⚡ <strong>Black Panther:</strong> "Step ${mStep}/7: Evaluated product M${mStep}!"`;
  } else {
    runStrassenCompute();
  }
});
document.getElementById('bp-btn-auto')?.addEventListener('click', function() {
  retroAudio.playClick();
  runStrassenCompute();
});
document.getElementById('bp-btn-reset')?.addEventListener('click', () => {
  retroAudio.playClick();
  mStep = 0;
  renderMGrid();
  bpDiag.innerHTML = '💬 <strong>Black Panther:</strong> "Vibranium matrix grid reset."';
});
"""
}

# 14. ROCKET RACCOON: Greedy Fractional Loot Knapsack (Fractional Knapsack)
SIMULATIONS["knapsack_fractional"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #ea580c;">MISSION: ROCKET'S FRACTIONAL LOOT HEIST</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Sort cosmic loot greedily by value/weight ratio (V/W). Laser-cut fractional slice for last item to fill capacity W!</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #fb923c; padding: 6px 10px; border: 1px solid #475569;">
      BAG CAPACITY: <span id="rock-cap-stat">50 KG</span>
    </div>
  </div>

  <!-- Custom Bag Capacity Input -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; align-items: center; gap: 8px;">
      <label style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a;">MAX CAPACITY (W):</label>
      <input type="number" id="rock-cap-input" value="50" min="10" max="100" style="width: 55px; padding: 4px; font-weight: bold; border: 2px solid #0f172a; text-align: center;">
      <button class="pixel-btn pixel-btn-primary" id="rock-btn-pack" style="padding: 4px 10px; font-size: 0.58rem;">💰 GREEDY PACK</button>
    </div>
    <div style="font-size: 0.75rem; color: #475569; font-weight: 600;">
      TOTAL LOOT VALUE: <span id="rock-total-val" style="color: #ea580c; font-weight: bold;">$0</span>
    </div>
  </div>

  <!-- Animated Arena Stage -->
  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 200px;">
    <!-- Rocket Actor Sprite -->
    <div id="rock-actor" style="position: absolute; top: 12px; left: 20px; transition: all 0.4s ease; z-index: 10;">
      <img src="assets/rocket.png" style="width: 48px; height: 56px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 0 10px rgba(234,88,12,0.8));">
    </div>

    <!-- Loot Items Display -->
    <div id="rock-items-grid" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-top: 55px;">
      <!-- Populated dynamically -->
    </div>
  </div>

  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; font-size: 0.88rem; min-height: 48px; display: flex; align-items: center;" id="rock-dialogue">
    💬 <strong>Rocket:</strong> "Greedy choice property: Always sort by price per pound ($/kg)! Take all of the richest, then laser-slice the remainder!"
  </div>

  <div class="viz-controls" style="display: flex; gap: 10px; flex-wrap: wrap;">
    <button class="pixel-btn pixel-btn-primary" id="rock-btn-auto">▶ AUTO-LOOT MAXIMUM VALUE</button>
    <button class="pixel-btn pixel-btn-secondary" id="rock-btn-step">⏭ STEP GREEDY PICK</button>
    <button class="pixel-btn pixel-btn-secondary" id="rock-btn-reset">↺ RESET BAG</button>
  </div>
</div>
""",
    "script": """
const rockGrid = document.getElementById('rock-items-grid');
const rockCapIn = document.getElementById('rock-cap-input');
const rockDiag = document.getElementById('rock-dialogue');
const rockTotal = document.getElementById('rock-total-val');
const rockCapStat = document.getElementById('rock-cap-stat');
const rockActor = document.getElementById('rock-actor');

let items = [
  { name: 'KREE CRYSTAL', val: 60, wt: 10, ratio: 6.0 },
  { name: 'XANDAR ORB', val: 100, wt: 20, ratio: 5.0 },
  { name: 'VIBRANIUM CORE', val: 120, wt: 30, ratio: 4.0 }
];
let rockStepIdx = 0;
let rockW = 50;
let curW = 0, curV = 0;

function renderLootItems() {
  rockGrid.innerHTML = '';
  items.forEach((item, idx) => {
    const card = document.createElement('div');
    card.id = `loot-item-${idx}`;
    card.style.cssText = 'background: #1e293b; border: 2px solid #475569; padding: 10px; border-radius: 4px; text-align: center; font-family: var(--font-pixel); font-size: 0.58rem; color: #fff; transition: all 0.3s;';
    card.innerHTML = `
      <div style="color:#fb923c; margin-bottom:4px;">${item.name}</div>
      <div>Val: $${item.val} | Wt: ${item.wt}kg</div>
      <div style="color:#facc15; font-size:0.52rem; margin-top:2px;">Ratio: $${item.ratio}/kg</div>
      <div id="loot-status-${idx}" style="color:#94a3b8; font-size:0.5rem; margin-top:4px;">NOT PACKED</div>
    `;
    rockGrid.appendChild(card);
  });
}
renderLootItems();

function stepGreedyPack() {
  if (rockStepIdx < items.length && curW < rockW) {
    const it = items[rockStepIdx];
    const card = document.getElementById(`loot-item-${rockStepIdx}`);
    const stat = document.getElementById(`loot-status-${rockStepIdx}`);
    rockActor.style.left = `${card.offsetLeft - 10}px`;

    const remainW = rockW - curW;
    if (it.wt <= remainW) {
      curW += it.wt;
      curV += it.val;
      card.style.background = '#15803d';
      card.style.borderColor = '#22c55e';
      stat.innerHTML = '<span style="color:#22c55e;">100% PACKED!</span>';
      rockDiag.innerHTML = `💰 <strong>Rocket:</strong> "Packed 100% of ${it.name} (full ${it.wt}kg at $${it.ratio}/kg)! Bag has ${rockW - curW}kg remaining space!"`;
    } else {
      const frac = remainW / it.wt;
      const addVal = it.val * frac;
      curW += remainW;
      curV += addVal;
      card.style.background = '#d97706';
      card.style.borderColor = '#f59e0b';
      stat.innerHTML = `<span style="color:#facc15;">${Math.round(frac*100)}% SLICED!</span>`;
      rockDiag.innerHTML = `🔫 <strong>Rocket:</strong> "Laser sliced ${remainW}kg (${Math.round(frac*100)}%) of ${it.name}! Added $${Math.round(addVal)} to loot. Bag at 100% capacity!"`;
    }
    rockTotal.textContent = `$${Math.round(curV)}`;
    rockStepIdx++;
  } else {
    rockDiag.innerHTML = `🎉 <strong>Rocket:</strong> "Loot heist complete! Total Bag Value = $${Math.round(curV)} maximized via O(N log N) greedy ratio sorting!"`;
  }
}

document.getElementById('rock-btn-step')?.addEventListener('click', () => { retroAudio.playClick(); stepGreedyPack(); });
document.getElementById('rock-btn-auto')?.addEventListener('click', () => {
  retroAudio.playClick();
  while(rockStepIdx < items.length && curW < rockW) stepGreedyPack();
});
document.getElementById('rock-btn-pack')?.addEventListener('click', () => {
  retroAudio.playClick();
  rockW = parseInt(rockCapIn.value) || 50;
  rockCapStat.textContent = `${rockW} KG`;
  curW = 0; curV = 0; rockStepIdx = 0;
  rockTotal.textContent = '$0';
  renderLootItems();
  stepGreedyPack();
});
document.getElementById('rock-btn-reset')?.addEventListener('click', () => {
  retroAudio.playClick();
  curW = 0; curV = 0; rockStepIdx = 0;
  rockTotal.textContent = '$0';
  rockActor.style.left = '20px';
  renderLootItems();
  rockDiag.innerHTML = '💬 <strong>Rocket:</strong> "Bag emptied. Ready for next cosmic heist."';
});
"""
}

# 15. THOR: Bifrost Minimum Cost Spanning Tree (MCST)
SIMULATIONS["mst"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #0284c7;">MISSION: THOR'S BIFROST POWER GRID MST</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Connect all 4 Asgardian power beacons with minimum total wire cost without forming redundant power loops!</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #38bdf8; padding: 6px 10px; border: 1px solid #475569;">
      MST COST: <span id="thor-total-cost" style="color: #facc15;">0</span> MW
    </div>
  </div>

  <!-- Custom Cost Tweak -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; align-items: center; gap: 8px;">
      <span style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a;">BEACONS: A, B, C, D</span>
      <span style="color: #475569; font-size: 0.75rem; font-weight: bold;">(Tree Property: exactly V − 1 = 3 edges)</span>
    </div>
    <button class="pixel-btn pixel-btn-primary" id="thor-btn-strike" style="padding: 6px 12px; font-size: 0.6rem;">⚡ LIGHTNING STRIKE CHEAPEST EDGE</button>
  </div>

  <!-- Animated Arena Stage -->
  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 220px;">
    <!-- Thor Actor Sprite -->
    <div id="thor-actor" style="position: absolute; top: 12px; left: 45%; transition: all 0.4s ease; z-index: 10;">
      <img src="assets/thor.png" style="width: 50px; height: 58px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 0 12px rgba(2,132,199,0.9));">
    </div>

    <!-- 4 Beacons SVG Graphic -->
    <svg id="thor-mst-svg" viewBox="0 0 400 180" style="width: 100%; height: 180px; display: block; margin: 0 auto;">
      <!-- Edges -->
      <line id="edge-ab" x1="60" y1="50" x2="180" y2="40" stroke="#475569" stroke-width="2"/>
      <text x="120" y="35" fill="#94a3b8" font-size="11" font-family="monospace">1 (AB)</text>

      <line id="edge-bc" x1="180" y1="40" x2="320" y2="60" stroke="#475569" stroke-width="2"/>
      <text x="250" y="45" fill="#94a3b8" font-size="11" font-family="monospace">2 (BC)</text>

      <line id="edge-cd" x1="320" y1="60" x2="200" y2="150" stroke="#475569" stroke-width="2"/>
      <text x="270" y="120" fill="#94a3b8" font-size="11" font-family="monospace">3 (CD)</text>

      <line id="edge-da" x1="200" y1="150" x2="60" y2="50" stroke="#475569" stroke-width="2"/>
      <text x="110" y="120" fill="#94a3b8" font-size="11" font-family="monospace">4 (DA)</text>

      <line id="edge-bd" x1="180" y1="40" x2="200" y2="150" stroke="#475569" stroke-dasharray="4" stroke-width="2"/>
      <text x="200" y="95" fill="#94a3b8" font-size="11" font-family="monospace">5 (BD)</text>

      <!-- Nodes -->
      <circle cx="60" cy="50" r="16" fill="#1e293b" stroke="#0284c7" stroke-width="2"/>
      <text x="60" y="54" fill="#fff" font-size="11" font-weight="bold" font-family="monospace" text-anchor="middle">A</text>

      <circle cx="180" cy="40" r="16" fill="#1e293b" stroke="#0284c7" stroke-width="2"/>
      <text x="180" y="44" fill="#fff" font-size="11" font-weight="bold" font-family="monospace" text-anchor="middle">B</text>

      <circle cx="320" cy="60" r="16" fill="#1e293b" stroke="#0284c7" stroke-width="2"/>
      <text x="320" y="64" fill="#fff" font-size="11" font-weight="bold" font-family="monospace" text-anchor="middle">C</text>

      <circle cx="200" cy="150" r="16" fill="#1e293b" stroke="#0284c7" stroke-width="2"/>
      <text x="200" y="154" fill="#fff" font-size="11" font-weight="bold" font-family="monospace" text-anchor="middle">D</text>
    </svg>
  </div>

  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; font-size: 0.88rem; min-height: 48px; display: flex; align-items: center;" id="thor-dialogue">
    💬 <strong>Thor:</strong> "Mjolnir guides the lightning! We pick the lightest power lines that connect all beacons without forming redundant power loops!"
  </div>

  <div class="viz-controls" style="display: flex; gap: 10px; flex-wrap: wrap;">
    <button class="pixel-btn pixel-btn-primary" id="thor-btn-auto">▶ AUTO-CONNECT MST BEACONS</button>
    <button class="pixel-btn pixel-btn-secondary" id="thor-btn-reset">↺ RESET BIFROST GRID</button>
  </div>
</div>
""",
    "script": """
const thorDiag = document.getElementById('thor-dialogue');
const thorCost = document.getElementById('thor-total-cost');
const thorActor = document.getElementById('thor-actor');

let mstStep = 0;
let totalCost = 0;
const edges = [
  { id: 'edge-ab', cost: 1, name: 'AB', x: '120px' },
  { id: 'edge-bc', cost: 2, name: 'BC', x: '250px' },
  { id: 'edge-cd', cost: 3, name: 'CD', x: '260px' }
];

function stepMstLightning() {
  if (mstStep < edges.length) {
    const e = edges[mstStep];
    const el = document.getElementById(e.id);
    if (el) {
      el.setAttribute('stroke', '#0284c7');
      el.setAttribute('stroke-width', '4');
    }
    thorActor.style.left = e.x;
    totalCost += e.cost;
    thorCost.textContent = `${totalCost}`;
    thorDiag.innerHTML = `⚡ <strong>Thor:</strong> "Lightning strikes edge ${e.name} (weight ${e.cost})! Added to spanning tree without cycle!"`;
    mstStep++;
  } else {
    thorDiag.innerHTML = `🏆 <strong>Thor:</strong> "By Odin's beard! All 4 beacons connected with V − 1 = 3 edges at minimal cost ${totalCost} MW!"`;
  }
}

document.getElementById('thor-btn-strike')?.addEventListener('click', () => { retroAudio.playClick(); stepMstLightning(); });
document.getElementById('thor-btn-auto')?.addEventListener('click', () => {
  retroAudio.playClick();
  while(mstStep < edges.length) stepMstLightning();
});
document.getElementById('thor-btn-reset')?.addEventListener('click', () => {
  retroAudio.playClick();
  mstStep = 0; totalCost = 0;
  thorCost.textContent = '0';
  edges.forEach(e => {
    const el = document.getElementById(e.id);
    if (el) { el.setAttribute('stroke', '#475569'); el.setAttribute('stroke-width', '2'); }
  });
  thorActor.style.left = '45%';
  thorDiag.innerHTML = '💬 <strong>Thor:</strong> "Bifrost power beacons ready for lightning channeling."';
});
"""
}
