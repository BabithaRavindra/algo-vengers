# physical_sims_part3.py - Topics 11 to 15
# Physical Algorithm Simulations with Moving Hero Actors & Custom Inputs
# 11. War Machine: Merge Sort (Divide & Two-Pointer Merge Sweep)
# 12. Quicksilver: QuickSort (Supersonic In-Place Pivot Partitioning)
# 13. Black Panther: Strassen's Matrix (7 Vibranium Products Sub-Cubic Multiplier)
# 14. Rocket Raccoon: Fractional Knapsack (Greedy Loot Density & Laser Slicing)
# 15. Thor: Minimum Cost Spanning Trees (Nine-Realms Bifrost Lightning Grid & Cycle Deflection)

PHYSICAL_SIMS_PART3 = {}

# -----------------------------------------------------------------------------
# 11. WAR MACHINE: Heavy Artillery Merge Sort
# -----------------------------------------------------------------------------
PHYSICAL_SIMS_PART3["merge_sort"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #475569;">MISSION: BATTALION TELEMETRY MERGE SORT</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Watch Col. Rhodes divide encrypted ammunition crates and merge them via two-pointer comparison.</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #38bdf8; padding: 6px 10px; border: 1px solid #475569;">
      DIVIDE: <span id="wm-depth" style="color: #facc15;">LEVEL 0</span> | SWEEPS: <span id="wm-ops" style="color: #22c55e;">0</span>
    </div>
  </div>

  <!-- Custom User Input Bar -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; align-items: center; gap: 10px;">
      <label style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a;">AMMO CRATES (6-8 NUMS):</label>
      <input type="text" id="wm-input-arr" value="38, 27, 43, 3, 9, 82" style="width: 190px; padding: 4px 8px; font-family: var(--font-code); font-weight: bold; border: 2px solid #0f172a; text-align: center;">
      <button class="pixel-btn pixel-btn-secondary" id="wm-btn-apply" style="padding: 4px 10px; font-size: 0.58rem;">LOAD BATTALION</button>
    </div>
    <div style="font-family: var(--font-code); font-size: 0.8rem; font-weight: bold; color: #475569;">
      RECURRENCE: T(n) = 2T(n/2) + Theta(n) = Theta(n log n)
    </div>
  </div>

  <!-- Animated Arena Stage -->
  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 270px; overflow: hidden;">
    <!-- War Machine Actor -->
    <div id="wm-actor" style="position: absolute; top: 15px; left: 40px; transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1); z-index: 20; display: flex; flex-direction: column; align-items: center;">
      <div style="font-family: var(--font-pixel); font-size: 0.5rem; background: #475569; color: #fff; padding: 1px 4px; border-radius: 2px; margin-bottom: 2px;">⛨ RHODEY</div>
      <img src="assets/warmachine.png" style="width: 44px; height: 50px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 4px 8px rgba(71,85,105,0.7));">
      <div id="wm-carried" style="display: none; background: #f59e0b; color: #000; font-family: var(--font-pixel); font-size: 0.55rem; padding: 2px 5px; border: 1.5px solid #000; margin-top: 2px;"></div>
    </div>

    <!-- Pointers Display -->
    <div style="display: flex; justify-content: space-around; margin-bottom: 8px; font-family: var(--font-pixel); font-size: 0.6rem; color: #94a3b8;">
      <div id="wm-left-tag" style="color: #38bdf8;">LEFT SUB-ARRAY [i]</div>
      <div id="wm-right-tag" style="color: #ec4899;">RIGHT SUB-ARRAY [j]</div>
    </div>

    <!-- Active Comparison Arena -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 18px;">
      <!-- Left Subarray Tray -->
      <div style="background: rgba(15, 23, 42, 0.8); border: 2px dashed #0284c7; padding: 10px; border-radius: 4px; min-height: 60px;">
        <div style="font-family: var(--font-pixel); font-size: 0.55rem; color: #38bdf8; margin-bottom: 6px;">LEFT PLATOON [POINTER i]</div>
        <div id="wm-left-box" style="display: flex; gap: 8px; justify-content: center; min-height: 40px; align-items: center;"></div>
      </div>
      <!-- Right Subarray Tray -->
      <div style="background: rgba(15, 23, 42, 0.8); border: 2px dashed #db2777; padding: 10px; border-radius: 4px; min-height: 60px;">
        <div style="font-family: var(--font-pixel); font-size: 0.55rem; color: #f472b6; margin-bottom: 6px;">RIGHT PLATOON [POINTER j]</div>
        <div id="wm-right-box" style="display: flex; gap: 8px; justify-content: center; min-height: 40px; align-items: center;"></div>
      </div>
    </div>

    <!-- Sorted Output Conveyor -->
    <div style="background: rgba(30, 41, 59, 0.7); border: 2px solid #22c55e; padding: 10px; border-radius: 4px; min-height: 70px;">
      <div style="font-family: var(--font-pixel); font-size: 0.58rem; color: #22c55e; margin-bottom: 6px; display: flex; justify-content: space-between;">
        <span>MERGED CONVEYOR (SORTED OUTPUT)</span>
        <span id="wm-merge-status" style="color: #94a3b8;">AWAITING COMPARISON</span>
      </div>
      <div id="wm-output-box" style="display: flex; gap: 8px; justify-content: center; min-height: 42px; align-items: center;"></div>
    </div>
  </div>

  <!-- Hero Telemetry & Invariant Dialogue -->
  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 12px 16px; margin-bottom: 14px; min-height: 52px; display: flex; align-items: center; box-shadow: 0 2px 0 #0f172a;" id="wm-dialogue">
    💬 <strong>War Machine:</strong> "Array loaded. Merge sort uses divide-and-conquer: split into halves until singletons, then merge back with linear comparisons!"
  </div>

  <!-- Interactive Controls -->
  <div class="viz-controls" style="display: flex; flex-wrap: wrap; gap: 10px;">
    <button class="pixel-btn pixel-btn-primary" id="wm-btn-step">⏭ STEP MERGE COMPARISON</button>
    <button class="pixel-btn pixel-btn-accent" id="wm-btn-auto">▶ AUTO-MERGE BATTALION</button>
    <button class="pixel-btn pixel-btn-secondary" id="wm-btn-split">✂ RE-DIVIDE SUBARRAYS</button>
    <button class="pixel-btn pixel-btn-secondary" id="wm-btn-reset">↺ RESET</button>
  </div>
</div>
""",
    "script": """
// War Machine Merge Sort Simulation Engine
let wmLeftArr = [27, 38, 43];
let wmRightArr = [3, 9, 82];
let wmOutArr = [];
let wmI = 0;
let wmJ = 0;
let wmOps = 0;
let wmIsBusy = false;
let wmAutoTimer = null;

const wmActor = document.getElementById('wm-actor');
const wmCarried = document.getElementById('wm-carried');
const wmLeftBox = document.getElementById('wm-left-box');
const wmRightBox = document.getElementById('wm-right-box');
const wmOutBox = document.getElementById('wm-output-box');
const wmDialogue = document.getElementById('wm-dialogue');
const wmOpsLabel = document.getElementById('wm-ops');
const wmStatus = document.getElementById('wm-merge-status');

function renderWMBars() {
  wmLeftBox.innerHTML = '';
  wmRightBox.innerHTML = '';
  wmOutBox.innerHTML = '';

  wmLeftArr.forEach((v, idx) => {
    const el = document.createElement('div');
    el.style.cssText = `background: ${idx === wmI ? '#0284c7' : '#1e293b'}; color: #fff; border: 2px solid ${idx === wmI ? '#38bdf8' : '#475569'}; padding: 6px 10px; font-family: var(--font-pixel); font-size: 0.65rem; border-radius: 3px; transition: all 0.2s;`;
    if (idx < wmI) {
      el.style.opacity = '0.3';
      el.style.textDecoration = 'line-through';
    }
    el.textContent = v;
    wmLeftBox.appendChild(el);
  });

  wmRightArr.forEach((v, idx) => {
    const el = document.createElement('div');
    el.style.cssText = `background: ${idx === wmJ ? '#be185d' : '#1e293b'}; color: #fff; border: 2px solid ${idx === wmJ ? '#f472b6' : '#475569'}; padding: 6px 10px; font-family: var(--font-pixel); font-size: 0.65rem; border-radius: 3px; transition: all 0.2s;`;
    if (idx < wmJ) {
      el.style.opacity = '0.3';
      el.style.textDecoration = 'line-through';
    }
    el.textContent = v;
    wmRightBox.appendChild(el);
  });

  wmOutArr.forEach(v => {
    const el = document.createElement('div');
    el.style.cssText = 'background: #15803d; color: #fff; border: 2px solid #22c55e; padding: 6px 10px; font-family: var(--font-pixel); font-size: 0.65rem; border-radius: 3px; animation: popIn 0.2s;';
    el.textContent = v;
    wmOutBox.appendChild(el);
  });

  wmOpsLabel.textContent = wmOps;
}

function parseWMInput() {
  const raw = document.getElementById('wm-input-arr').value;
  const nums = raw.split(',').map(s => parseInt(s.trim())).filter(n => !isNaN(n));
  if (nums.length < 2) return;
  const mid = Math.floor(nums.length / 2);
  wmLeftArr = nums.slice(0, mid).sort((a,b) => a - b);
  wmRightArr = nums.slice(mid).sort((a,b) => a - b);
  resetWMSim();
}

function resetWMSim() {
  clearInterval(wmAutoTimer);
  wmAutoTimer = null;
  wmI = 0;
  wmJ = 0;
  wmOutArr = [];
  wmOps = 0;
  wmIsBusy = false;
  wmActor.style.left = '40px';
  wmActor.style.top = '15px';
  wmCarried.style.display = 'none';
  wmStatus.textContent = 'AWAITING COMPARISON';
  renderWMBars();
  wmDialogue.innerHTML = `💬 <strong>War Machine:</strong> "Subarrays reset. Left: [${wmLeftArr.join(', ')}], Right: [${wmRightArr.join(', ')}]. Ready to merge!"`;
}

function stepWMMerge() {
  if (wmIsBusy) return;
  if (wmI >= wmLeftArr.length && wmJ >= wmRightArr.length) {
    wmStatus.textContent = 'MERGE COMPLETE!';
    wmDialogue.innerHTML = `<strong>✨ BATTALION SORTED!</strong> All elements merged in linear time O(n) = ${wmOps} operations. Stable order preserved!`;
    retroAudio.playSuccess();
    if (wmAutoTimer) { clearInterval(wmAutoTimer); wmAutoTimer = null; }
    return;
  }

  wmIsBusy = true;
  wmOps++;
  retroAudio.playClick();

  let takeLeft = false;
  let chosenVal = null;

  if (wmI < wmLeftArr.length && wmJ < wmRightArr.length) {
    const valL = wmLeftArr[wmI];
    const valR = wmRightArr[wmJ];
    if (valL <= valR) {
      takeLeft = true;
      chosenVal = valL;
      wmDialogue.innerHTML = `⛨ <strong>War Machine:</strong> "COMPARE: Left[${valL}] <= Right[${valR}]. Stability rule: take left element!"`;
    } else {
      takeLeft = false;
      chosenVal = valR;
      wmDialogue.innerHTML = `⛨ <strong>War Machine:</strong> "COMPARE: Right[${valR}] < Left[${valL}]. Take smaller right element!"`;
    }
  } else if (wmI < wmLeftArr.length) {
    takeLeft = true;
    chosenVal = wmLeftArr[wmI];
    wmDialogue.innerHTML = `⛨ <strong>War Machine:</strong> "Right subarray exhausted. Append remaining Left[${chosenVal}]!"`;
  } else {
    takeLeft = false;
    chosenVal = wmRightArr[wmJ];
    wmDialogue.innerHTML = `⛨ <strong>War Machine:</strong> "Left subarray exhausted. Append remaining Right[${chosenVal}]!"`;
  }

  // Move actor to chosen box
  wmActor.style.left = takeLeft ? '180px' : '480px';
  wmActor.style.top = '65px';

  setTimeout(() => {
    retroAudio.playHover();
    wmCarried.textContent = `[${chosenVal}]`;
    wmCarried.style.display = 'block';

    if (takeLeft) wmI++;
    else wmJ++;

    renderWMBars();

    // Carry to output conveyor
    setTimeout(() => {
      wmActor.style.left = '330px';
      wmActor.style.top = '175px';

      setTimeout(() => {
        retroAudio.playSuccess();
        wmCarried.style.display = 'none';
        wmOutArr.push(chosenVal);
        renderWMBars();

        setTimeout(() => {
          wmActor.style.left = '40px';
          wmActor.style.top = '15px';
          wmIsBusy = false;
        }, 200);
      }, 300);
    }, 350);
  }, 300);
}

document.getElementById('wm-btn-apply')?.addEventListener('click', () => {
  parseWMInput();
  retroAudio.playClick();
});

document.getElementById('wm-btn-step')?.addEventListener('click', () => {
  stepWMMerge();
});

document.getElementById('wm-btn-auto')?.addEventListener('click', () => {
  if (wmAutoTimer) {
    clearInterval(wmAutoTimer);
    wmAutoTimer = null;
    wmDialogue.innerHTML = `⏸ <strong>War Machine:</strong> "Auto-merge paused."`;
  } else {
    wmAutoTimer = setInterval(() => {
      if (wmI >= wmLeftArr.length && wmJ >= wmRightArr.length) {
        clearInterval(wmAutoTimer);
        wmAutoTimer = null;
      } else {
        stepWMMerge();
      }
    }, 1300);
    wmDialogue.innerHTML = `▶ <strong>War Machine:</strong> "Auto-merging battalion at rapid cadence..."`;
  }
});

document.getElementById('wm-btn-split')?.addEventListener('click', () => {
  parseWMInput();
});

document.getElementById('wm-btn-reset')?.addEventListener('click', () => {
  resetWMSim();
});

renderWMBars();
"""
}

# -----------------------------------------------------------------------------
# 12. QUICKSILVER: Supersonic QuickSort
# -----------------------------------------------------------------------------
PHYSICAL_SIMS_PART3["quick_sort"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #0284c7;">MISSION: SUPERSONIC RAILGUN PROJECTILE SORT</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Watch Quicksilver partition the railgun magazine in-place around a pivot at supersonic speed.</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #38bdf8; padding: 6px 10px; border: 1px solid #475569;">
      PIVOT: <span id="qs-pivot-val" style="color: #facc15;">32</span> | SWAPS: <span id="qs-swaps" style="color: #22c55e;">0</span>
    </div>
  </div>

  <!-- User Custom Input Bar -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; align-items: center; gap: 10px;">
      <label style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a;">PROJECTILE CALIBERS (6-8 NUMS):</label>
      <input type="text" id="qs-input-arr" value="50, 23, 9, 18, 61, 32" style="width: 180px; padding: 4px 8px; font-family: var(--font-code); font-weight: bold; border: 2px solid #0f172a; text-align: center;">
      <button class="pixel-btn pixel-btn-secondary" id="qs-btn-apply" style="padding: 4px 10px; font-size: 0.58rem;">LOAD MAGAZINE</button>
    </div>
    <div style="font-family: var(--font-code); font-size: 0.8rem; font-weight: bold; color: #0284c7;">
      LOMUTO PARTITION: i (boundary) & j (scanner)
    </div>
  </div>

  <!-- Animated Arena Stage -->
  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 250px; overflow: hidden;">
    <!-- Quicksilver Actor -->
    <div id="qs-actor" style="position: absolute; top: 15px; left: 40px; transition: all 0.25s cubic-bezier(0.34, 1.56, 0.64, 1); z-index: 20; display: flex; flex-direction: column; align-items: center;">
      <div style="font-family: var(--font-pixel); font-size: 0.5rem; background: #0284c7; color: #fff; padding: 1px 4px; border-radius: 2px; margin-bottom: 2px;">⚡ PIETRO</div>
      <img src="assets/quicksilver.png" style="width: 44px; height: 50px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 4px 8px rgba(2,132,199,0.7));">
    </div>

    <!-- Magazine Tray Indicator -->
    <div style="display: flex; justify-content: space-between; font-family: var(--font-pixel); font-size: 0.6rem; color: #94a3b8; margin-bottom: 12px;">
      <span>RAILGUN AMMUNITION MAGAZINE (IN-PLACE MEMORY)</span>
      <span id="qs-partition-phase" style="color: #38bdf8;">PHASE: INITIALIZING</span>
    </div>

    <!-- Projectile Cells Conveyor -->
    <div id="qs-cells-box" style="display: flex; gap: 10px; justify-content: center; align-items: center; min-height: 100px; background: rgba(30, 41, 59, 0.5); border: 2px dashed #475569; padding: 14px; border-radius: 4px; margin-top: 30px;"></div>
  </div>

  <!-- Hero Telemetry Box -->
  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 12px 16px; margin-bottom: 14px; min-height: 52px; display: flex; align-items: center; box-shadow: 0 2px 0 #0f172a;" id="qs-dialogue">
    💬 <strong>Quicksilver:</strong> "You didn't see that coming? QuickSort partitions in-place: elements smaller than pivot sprint left, larger stay right!"
  </div>

  <!-- Interactive Controls -->
  <div class="viz-controls" style="display: flex; flex-wrap: wrap; gap: 10px;">
    <button class="pixel-btn pixel-btn-primary" id="qs-btn-step">⚡ SUPERSONIC STEP SCAN</button>
    <button class="pixel-btn pixel-btn-accent" id="qs-btn-run">▶ FULL MACH PARTITION</button>
    <button class="pixel-btn pixel-btn-secondary" id="qs-btn-reset">↺ RELOAD MAGAZINE</button>
  </div>
</div>
""",
    "script": """
let qsArr = [50, 23, 9, 18, 61, 32];
let qsI = -1;
let qsJ = 0;
let qsPivotIdx = 5;
let qsSwaps = 0;
let qsDone = false;
let qsBusy = false;
let qsAutoTimer = null;

const qsActor = document.getElementById('qs-actor');
const qsCellsBox = document.getElementById('qs-cells-box');
const qsDialogue = document.getElementById('qs-dialogue');
const qsPivotLabel = document.getElementById('qs-pivot-val');
const qsSwapsLabel = document.getElementById('qs-swaps');
const qsPhaseLabel = document.getElementById('qs-partition-phase');

function renderQSGrid() {
  qsCellsBox.innerHTML = '';
  const pivotVal = qsArr[qsPivotIdx];
  qsPivotLabel.textContent = pivotVal;

  qsArr.forEach((val, idx) => {
    const el = document.createElement('div');
    el.style.cssText = `
      display: flex; flex-direction: column; align-items: center; gap: 4px;
      padding: 10px 14px; border: 2px solid #000; border-radius: 4px; min-width: 55px; text-align: center;
      font-family: var(--font-pixel); font-size: 0.75rem; transition: all 0.25s ease;
    `;

    if (idx === qsPivotIdx) {
      el.style.background = '#facc15';
      el.style.color = '#000';
      el.style.borderColor = '#ca8a04';
      el.innerHTML = `<span>${val}</span><span style="font-size:0.5rem; color:#713f12;">PIVOT</span>`;
    } else if (idx === qsJ && !qsDone) {
      el.style.background = '#38bdf8';
      el.style.color = '#000';
      el.style.borderColor = '#0284c7';
      el.innerHTML = `<span>${val}</span><span style="font-size:0.5rem; color:#0369a1;">SCAN [j]</span>`;
    } else if (idx <= qsI && !qsDone) {
      el.style.background = '#dcfce7';
      el.style.color = '#15803d';
      el.style.borderColor = '#16a34a';
      el.innerHTML = `<span>${val}</span><span style="font-size:0.5rem; color:#166534;"><= PIV</span>`;
    } else {
      el.style.background = '#1e293b';
      el.style.color = '#f8fafc';
      el.style.borderColor = '#475569';
      el.innerHTML = `<span>${val}</span><span style="font-size:0.5rem; color:#64748b;">[${idx}]</span>`;
    }

    qsCellsBox.appendChild(el);
  });

  qsSwapsLabel.textContent = qsSwaps;
}

function parseQSInput() {
  const raw = document.getElementById('qs-input-arr').value;
  const nums = raw.split(',').map(s => parseInt(s.trim())).filter(n => !isNaN(n));
  if (nums.length < 2) return;
  qsArr = nums;
  resetQSSim();
}

function resetQSSim() {
  clearInterval(qsAutoTimer);
  qsAutoTimer = null;
  qsI = -1;
  qsJ = 0;
  qsPivotIdx = qsArr.length - 1;
  qsSwaps = 0;
  qsDone = false;
  qsBusy = false;
  qsActor.style.left = '40px';
  qsActor.style.top = '15px';
  qsPhaseLabel.textContent = 'PHASE: SCANNING';
  renderQSGrid();
  qsDialogue.innerHTML = `💬 <strong>Quicksilver:</strong> "Magazine reloaded! Pivot chosen at index [${qsPivotIdx}] = ${qsArr[qsPivotIdx]}. Ready to sprint!"`;
}

function stepQSPartition() {
  if (qsBusy || qsDone) return;
  qsBusy = true;
  retroAudio.playClick();

  const pivotVal = qsArr[qsPivotIdx];

  // If scanner reached pivot, swap pivot into i+1
  if (qsJ >= qsPivotIdx) {
    qsActor.style.left = '480px';
    qsActor.style.top = '50px';

    setTimeout(() => {
      const finalIdx = qsI + 1;
      qsDialogue.innerHTML = `⚡ <strong>Quicksilver:</strong> "Scan complete! Swapping pivot [${pivotVal}] into its final sorted position at index [${finalIdx}]!"`;
      retroAudio.playSuccess();

      // Swap
      const tmp = qsArr[finalIdx];
      qsArr[finalIdx] = qsArr[qsPivotIdx];
      qsArr[qsPivotIdx] = tmp;
      qsPivotIdx = finalIdx;
      qsSwaps++;
      qsDone = true;
      qsPhaseLabel.textContent = 'PARTITION COMPLETE!';

      renderQSGrid();

      setTimeout(() => {
        qsActor.style.left = '40px';
        qsActor.style.top = '15px';
        qsBusy = false;
        if (qsAutoTimer) { clearInterval(qsAutoTimer); qsAutoTimer = null; }
      }, 300);
    }, 300);
    return;
  }

  // Scanning element j
  const curVal = qsArr[qsJ];
  const targetX = Math.min(500, 100 + qsJ * 70);
  qsActor.style.left = `${targetX}px`;
  qsActor.style.top = '45px';

  setTimeout(() => {
    if (curVal <= pivotVal) {
      qsI++;
      qsDialogue.innerHTML = `⚡ <strong>Quicksilver:</strong> "ARR[${qsJ}] = ${curVal} <= PIVOT ${pivotVal}! Advance boundary i to [${qsI}] and SWAP!"`;
      retroAudio.playHover();

      // Swap arr[i] and arr[j]
      const tmp = qsArr[qsI];
      qsArr[qsI] = qsArr[qsJ];
      qsArr[qsJ] = tmp;
      qsSwaps++;
    } else {
      qsDialogue.innerHTML = `⚡ <strong>Quicksilver:</strong> "ARR[${qsJ}] = ${curVal} > PIVOT ${pivotVal}! Stays in upper partition."`;
    }

    qsJ++;
    renderQSGrid();

    setTimeout(() => {
      qsBusy = false;
    }, 200);
  }, 250);
}

document.getElementById('qs-btn-apply')?.addEventListener('click', () => {
  parseQSInput();
  retroAudio.playClick();
});

document.getElementById('qs-btn-step')?.addEventListener('click', () => {
  stepQSPartition();
});

document.getElementById('qs-btn-run')?.addEventListener('click', () => {
  if (qsAutoTimer) {
    clearInterval(qsAutoTimer);
    qsAutoTimer = null;
    qsDialogue.innerHTML = `⏸ <strong>Quicksilver:</strong> "Partition paused."`;
  } else {
    qsAutoTimer = setInterval(() => {
      if (qsDone) {
        clearInterval(qsAutoTimer);
        qsAutoTimer = null;
      } else {
        stepQSPartition();
      }
    }, 600);
  }
});

document.getElementById('qs-btn-reset')?.addEventListener('click', () => {
  resetQSSim();
});

renderQSGrid();
"""
}

# -----------------------------------------------------------------------------
# 13. BLACK PANTHER: Strassen's Matrix Multiplication
# -----------------------------------------------------------------------------
PHYSICAL_SIMS_PART3["strassen"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #6b21a8;">MISSION: WAKANDAN VIBRANIUM SHIELD MATRIX</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Watch King T'Challa conquer the cubic multiplication barrier using Strassen's 7 products.</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #a855f7; padding: 6px 10px; border: 1px solid #475569;">
      PRODUCTS COMPUTED: <span id="strassen-prod-count" style="color: #22c55e;">0 / 7</span>
    </div>
  </div>

  <!-- User Custom 2x2 Matrix Inputs -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 14px;">
    <!-- Matrix A -->
    <div style="display: flex; align-items: center; gap: 8px;">
      <span style="font-family: var(--font-pixel); font-size: 0.65rem; color: #6b21a8;">MATRIX A:</span>
      <div style="display: grid; grid-template-columns: 40px 40px; gap: 4px;">
        <input type="number" id="a11" value="2" style="padding: 2px; text-align: center; font-family: var(--font-code); font-weight: bold; border: 1.5px solid #000;">
        <input type="number" id="a12" value="3" style="padding: 2px; text-align: center; font-family: var(--font-code); font-weight: bold; border: 1.5px solid #000;">
        <input type="number" id="a21" value="1" style="padding: 2px; text-align: center; font-family: var(--font-code); font-weight: bold; border: 1.5px solid #000;">
        <input type="number" id="a22" value="4" style="padding: 2px; text-align: center; font-family: var(--font-code); font-weight: bold; border: 1.5px solid #000;">
      </div>
    </div>

    <!-- Matrix B -->
    <div style="display: flex; align-items: center; gap: 8px;">
      <span style="font-family: var(--font-pixel); font-size: 0.65rem; color: #0284c7;">MATRIX B:</span>
      <div style="display: grid; grid-template-columns: 40px 40px; gap: 4px;">
        <input type="number" id="b11" value="5" style="padding: 2px; text-align: center; font-family: var(--font-code); font-weight: bold; border: 1.5px solid #000;">
        <input type="number" id="b12" value="6" style="padding: 2px; text-align: center; font-family: var(--font-code); font-weight: bold; border: 1.5px solid #000;">
        <input type="number" id="b21" value="7" style="padding: 2px; text-align: center; font-family: var(--font-code); font-weight: bold; border: 1.5px solid #000;">
        <input type="number" id="b22" value="8" style="padding: 2px; text-align: center; font-family: var(--font-code); font-weight: bold; border: 1.5px solid #000;">
      </div>
    </div>

    <button class="pixel-btn pixel-btn-secondary" id="strassen-btn-apply" style="padding: 6px 12px; font-size: 0.6rem;">UPDATE MATRICES</button>
  </div>

  <!-- Animated Arena Stage -->
  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 270px; overflow: hidden;">
    <!-- Black Panther Actor -->
    <div id="bp-actor" style="position: absolute; top: 15px; left: 30px; transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1); z-index: 20; display: flex; flex-direction: column; align-items: center;">
      <div style="font-family: var(--font-pixel); font-size: 0.5rem; background: #6b21a8; color: #fff; padding: 1px 4px; border-radius: 2px; margin-bottom: 2px;">◈ T'CHALLA</div>
      <img src="assets/blackpanther.png" style="width: 44px; height: 50px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 4px 8px rgba(107,33,168,0.7));">
    </div>

    <!-- 7 Products Display Rack -->
    <div style="margin-bottom: 16px;">
      <div style="font-family: var(--font-pixel); font-size: 0.6rem; color: #a855f7; margin-bottom: 8px;">STRASSEN'S 7 VIBRANIUM PRODUCTS (M1 - M7) [7 MULTIPLICATIONS INSTEAD OF 8]</div>
      <div id="strassen-prod-grid" style="display: grid; grid-template-columns: repeat(7, 1fr); gap: 6px;"></div>
    </div>

    <!-- Result Matrix C Assembly -->
    <div style="background: rgba(30, 41, 59, 0.7); border: 2px solid #a855f7; padding: 10px; border-radius: 4px; display: flex; justify-content: space-between; align-items: center;">
      <div>
        <span style="font-family: var(--font-pixel); font-size: 0.58rem; color: #22c55e;">OUTPUT MATRIX C = A * B</span>
        <div style="font-family: var(--font-code); font-size: 0.75rem; color: #94a3b8; margin-top: 2px;">C11 = M1+M4-M5+M7 | C12 = M3+M5 | C21 = M2+M4 | C22 = M1-M2+M3+M6</div>
      </div>
      <div id="strassen-res-matrix" style="display: grid; grid-template-columns: 50px 50px; gap: 6px; font-family: var(--font-code); font-weight: bold;"></div>
    </div>
  </div>

  <!-- Hero Telemetry & Formulas -->
  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 12px 16px; margin-bottom: 14px; min-height: 52px; display: flex; align-items: center; box-shadow: 0 2px 0 #0f172a;" id="strassen-dialogue">
    💬 <strong>Black Panther:</strong> "Standard matrix multiplication requires 8 recursive calls -> O(n^3). In Wakanda, we compute only 7 products -> O(n^2.807)!"
  </div>

  <!-- Interactive Controls -->
  <div class="viz-controls" style="display: flex; flex-wrap: wrap; gap: 10px;">
    <button class="pixel-btn pixel-btn-primary" id="strassen-btn-step">⚡ COMPUTE NEXT PRODUCT</button>
    <button class="pixel-btn pixel-btn-accent" id="strassen-btn-all">▶ COMPUTE ALL 7 PRODUCTS</button>
    <button class="pixel-btn pixel-btn-secondary" id="strassen-btn-reset">↺ RESET</button>
  </div>
</div>
""",
    "script": """
let strassenStep = 0;
let mVals = [0, 0, 0, 0, 0, 0, 0];
const strassenGrid = document.getElementById('strassen-prod-grid');
const strassenRes = document.getElementById('strassen-res-matrix');
const strassenDialogue = document.getElementById('strassen-dialogue');
const strassenCount = document.getElementById('strassen-prod-count');
const bpActor = document.getElementById('bp-actor');

const mFormulas = [
  "M1 = (A11 + A22) * (B11 + B22)",
  "M2 = (A21 + A22) * B11",
  "M3 = A11 * (B12 - B22)",
  "M4 = A22 * (B21 - B11)",
  "M5 = (A11 + A12) * B22",
  "M6 = (A21 - A11) * (B11 + B12)",
  "M7 = (A12 - A22) * (B21 + B22)"
];

function getInputs() {
  return {
    a11: parseInt(document.getElementById('a11').value) || 0,
    a12: parseInt(document.getElementById('a12').value) || 0,
    a21: parseInt(document.getElementById('a21').value) || 0,
    a22: parseInt(document.getElementById('a22').value) || 0,
    b11: parseInt(document.getElementById('b11').value) || 0,
    b12: parseInt(document.getElementById('b12').value) || 0,
    b21: parseInt(document.getElementById('b21').value) || 0,
    b22: parseInt(document.getElementById('b22').value) || 0
  };
}

function renderStrassen() {
  strassenGrid.innerHTML = '';
  for (let k = 0; k < 7; k++) {
    const el = document.createElement('div');
    el.style.cssText = `
      background: ${k < strassenStep ? '#6b21a8' : '#1e293b'};
      color: #fff; border: 2px solid ${k < strassenStep ? '#a855f7' : '#475569'};
      padding: 6px 4px; border-radius: 4px; text-align: center; font-family: var(--font-pixel); font-size: 0.55rem;
    `;
    el.innerHTML = `
      <div style="color:${k < strassenStep ? '#facc15' : '#94a3b8'};">M${k+1}</div>
      <div style="font-size:0.75rem; margin-top:2px;">${k < strassenStep ? mVals[k] : '?'}</div>
    `;
    strassenGrid.appendChild(el);
  }

  strassenCount.textContent = `${strassenStep} / 7`;

  // Render Result Matrix
  strassenRes.innerHTML = '';
  if (strassenStep >= 7) {
    const c11 = mVals[0] + mVals[3] - mVals[4] + mVals[6];
    const c12 = mVals[2] + mVals[4];
    const c21 = mVals[1] + mVals[3];
    const c22 = mVals[0] - mVals[1] + mVals[2] + mVals[5];
    [c11, c12, c21, c22].forEach(v => {
      const cell = document.createElement('div');
      cell.style.cssText = 'background: #22c55e; color: #000; padding: 6px; text-align: center; border: 1.5px solid #000; border-radius: 2px;';
      cell.textContent = v;
      strassenRes.appendChild(cell);
    });
  } else {
    for (let i = 0; i < 4; i++) {
      const cell = document.createElement('div');
      cell.style.cssText = 'background: #334155; color: #94a3b8; padding: 6px; text-align: center; border: 1.5px solid #000; border-radius: 2px;';
      cell.textContent = '-';
      strassenRes.appendChild(cell);
    }
  }
}

function stepStrassen() {
  if (strassenStep >= 7) return;
  const { a11, a12, a21, a22, b11, b12, b21, b22 } = getInputs();

  retroAudio.playClick();
  const k = strassenStep;
  let val = 0;
  if (k === 0) val = (a11 + a22) * (b11 + b22);
  else if (k === 1) val = (a21 + a22) * b11;
  else if (k === 2) val = a11 * (b12 - b22);
  else if (k === 3) val = a22 * (b21 - b11);
  else if (k === 4) val = (a11 + a12) * b22;
  else if (k === 5) val = (a21 - a11) * (b11 + b12);
  else if (k === 6) val = (a12 - a22) * (b21 + b22);

  mVals[k] = val;
  strassenStep++;

  bpActor.style.left = `${60 + k * 70}px`;

  strassenDialogue.innerHTML = `◈ <strong>Black Panther:</strong> "Calculated <strong>${mFormulas[k]}</strong> = ${val}."`;
  renderStrassen();

  if (strassenStep === 7) {
    retroAudio.playSuccess();
    strassenDialogue.innerHTML = `<strong>✨ VIBRANIUM MATRIX ASSEMBLED!</strong> Output Matrix C synthesized from 7 products! Sub-cubic speedup achieved!`;
  }
}

document.getElementById('strassen-btn-apply')?.addEventListener('click', () => {
  strassenStep = 0;
  renderStrassen();
  retroAudio.playClick();
});

document.getElementById('strassen-btn-step')?.addEventListener('click', () => {
  stepStrassen();
});

document.getElementById('strassen-btn-all')?.addEventListener('click', () => {
  while (strassenStep < 7) {
    stepStrassen();
  }
});

document.getElementById('strassen-btn-reset')?.addEventListener('click', () => {
  strassenStep = 0;
  mVals = [0, 0, 0, 0, 0, 0, 0];
  bpActor.style.left = '30px';
  renderStrassen();
  strassenDialogue.innerHTML = `💬 <strong>Black Panther:</strong> "Matrix calculation reset. Ready to compute 7 products."`;
});

renderStrassen();
"""
}

# -----------------------------------------------------------------------------
# 14. ROCKET RACCOON: Fractional Knapsack
# -----------------------------------------------------------------------------
PHYSICAL_SIMS_PART3["knapsack_fractional"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #d97706;">MISSION: KNOWHERE SCRAP SALVAGE HEIST</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Watch Rocket Raccoon sort salvage by credit ratio, pack whole parts, and laser-slice fractions.</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #f59e0b; padding: 6px 10px; border: 1px solid #475569;">
      HARNESS: <span id="rk-load-text" style="color: #22c55e;">0 / 20 KG</span> | PROFIT: <span id="rk-profit" style="color: #facc15;">0 CR</span>
    </div>
  </div>

  <!-- User Custom Knapsack Inputs -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; align-items: center; gap: 10px;">
      <label style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a;">HARNESS CAPACITY W (KG):</label>
      <input type="number" id="rk-input-cap" value="20" min="5" max="50" style="width: 65px; padding: 4px; font-family: var(--font-code); font-weight: bold; border: 2px solid #0f172a; text-align: center;">
      <button class="pixel-btn pixel-btn-secondary" id="rk-btn-apply" style="padding: 4px 10px; font-size: 0.58rem;">SET CAPACITY</button>
    </div>
    <div style="font-family: var(--font-code); font-size: 0.8rem; font-weight: bold; color: #d97706;">
      GREEDY CHOICE: HIGHEST RATIO (VALUE / WEIGHT)
    </div>
  </div>

  <!-- Animated Arena Stage -->
  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 270px; overflow: hidden;">
    <!-- Capacity Bar -->
    <div style="display: flex; justify-content: space-between; font-family: var(--font-pixel); font-size: 0.6rem; color: #94a3b8; margin-bottom: 6px;">
      <span>CARGO PACK FILL</span>
      <span id="rk-pct-text" style="color: #22c55e;">0% FILLED</span>
    </div>
    <div style="width: 100%; height: 16px; background: #1e293b; border: 2px solid #475569; margin-bottom: 16px; overflow: hidden;">
      <div id="rk-fill-bar" style="width: 0%; height: 100%; background: #22c55e; transition: width 0.3s ease;"></div>
    </div>

    <!-- Rocket Actor -->
    <div id="rk-actor" style="position: absolute; top: 75px; left: 30px; transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1); z-index: 20; display: flex; flex-direction: column; align-items: center;">
      <div style="font-family: var(--font-pixel); font-size: 0.5rem; background: #d97706; color: #fff; padding: 1px 4px; border-radius: 2px; margin-bottom: 2px;">⚙ ROCKET</div>
      <img src="assets/rocket.png" style="width: 44px; height: 50px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 4px 8px rgba(217,119,6,0.7));">
    </div>

    <!-- Available Scrap Items Rack -->
    <div style="margin-bottom: 16px;">
      <div style="font-family: var(--font-pixel); font-size: 0.58rem; color: #94a3b8; margin-bottom: 6px;">AVAILABLE SCRAP (SORTED BY GREEDY DENSITY v/w)</div>
      <div id="rk-items-grid" style="display: flex; gap: 10px; justify-content: center; align-items: center; min-height: 80px;"></div>
    </div>
  </div>

  <!-- Hero Telemetry & Invariant Box -->
  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 12px 16px; margin-bottom: 14px; min-height: 52px; display: flex; align-items: center; box-shadow: 0 2px 0 #0f172a;" id="rk-dialogue">
    💬 <strong>Rocket Raccoon:</strong> "Rule number one of looting: sort by credit density! Take whole parts first, then laser-slice the last chunk!"
  </div>

  <!-- Interactive Controls -->
  <div class="viz-controls" style="display: flex; flex-wrap: wrap; gap: 10px;">
    <button class="pixel-btn pixel-btn-primary" id="rk-btn-step">💰 GREEDY PACK NEXT ITEM</button>
    <button class="pixel-btn pixel-btn-accent" id="rk-btn-all">▶ AUTO-PACK HARNESS</button>
    <button class="pixel-btn pixel-btn-secondary" id="rk-btn-reset">↺ RESET HEIST</button>
  </div>
</div>
""",
    "script": """
let rkCap = 20;
let rkCurrentWeight = 0;
let rkTotalProfit = 0;
let rkItemIdx = 0;
let rkDone = false;

let rkItems = [
  { name: "Plasma Core", val: 120, wt: 6, ratio: 20, taken: 0 },
  { name: "Tesseract Shard", val: 100, wt: 10, ratio: 10, taken: 0 },
  { name: "Hadron Enclosure", val: 60, wt: 12, ratio: 5, taken: 0 },
  { name: "Cyber Limb", val: 30, wt: 10, ratio: 3, taken: 0 }
];

const rkGrid = document.getElementById('rk-items-grid');
const rkFillBar = document.getElementById('rk-fill-bar');
const rkLoadText = document.getElementById('rk-load-text');
const rkProfitText = document.getElementById('rk-profit');
const rkPctText = document.getElementById('rk-pct-text');
const rkDialogue = document.getElementById('rk-dialogue');
const rkActor = document.getElementById('rk-actor');

function renderRK() {
  rkGrid.innerHTML = '';
  rkItems.forEach((it, idx) => {
    const el = document.createElement('div');
    el.style.cssText = `
      background: ${it.taken > 0 ? (it.taken === 1 ? '#15803d' : '#ca8a04') : '#1e293b'};
      color: #fff; border: 2px solid ${idx === rkItemIdx && !rkDone ? '#f59e0b' : '#475569'};
      padding: 8px 10px; border-radius: 4px; text-align: center; font-family: var(--font-pixel); font-size: 0.6rem; min-width: 100px;
    `;
    el.innerHTML = `
      <div style="color:#facc15; font-size:0.55rem;">${it.name}</div>
      <div style="font-family:var(--font-code); margin:3px 0;">${it.val} CR / ${it.wt} KG</div>
      <div style="color:#38bdf8; font-size:0.5rem;">RATIO: ${it.ratio} CR/KG</div>
      <div style="margin-top:4px; font-size:0.5rem; background:rgba(0,0,0,0.5); padding:2px;">
        ${it.taken === 1 ? 'PACKED (100%)' : (it.taken > 0 ? `SLICED (${Math.round(it.taken*100)}%)` : 'IN VAULT')}
      </div>
    `;
    rkGrid.appendChild(el);
  });

  const pct = Math.min(100, Math.round((rkCurrentWeight / rkCap) * 100));
  rkFillBar.style.width = `${pct}%`;
  rkLoadText.textContent = `${rkCurrentWeight.toFixed(1)} / ${rkCap} KG`;
  rkProfitText.textContent = `${rkTotalProfit.toFixed(1)} CR`;
  rkPctText.textContent = `${pct}% FILLED`;
}

function stepRK() {
  if (rkDone || rkItemIdx >= rkItems.length || rkCurrentWeight >= rkCap) {
    rkDone = true;
    retroAudio.playSuccess();
    rkDialogue.innerHTML = `<strong>✨ HEIST COMPLETE!</strong> Harness filled to max capacity! Total profit: ${rkTotalProfit.toFixed(1)} Credits!`;
    return;
  }

  retroAudio.playClick();
  const item = rkItems[rkItemIdx];
  const remainCap = rkCap - rkCurrentWeight;

  rkActor.style.left = `${120 + rkItemIdx * 110}px`;

  if (item.wt <= remainCap) {
    // Take whole item
    item.taken = 1;
    rkCurrentWeight += item.wt;
    rkTotalProfit += item.val;
    rkDialogue.innerHTML = `⚙ <strong>Rocket:</strong> "Packed 100% of ${item.name} (${item.wt} kg for ${item.val} CR). Greedy profit: +${item.val} CR!"`;
    rkItemIdx++;
  } else {
    // Laser slice fraction
    const frac = remainCap / item.wt;
    item.taken = frac;
    const addedVal = item.val * frac;
    rkCurrentWeight += remainCap;
    rkTotalProfit += addedVal;
    rkDone = true;
    retroAudio.playHover();
    rkDialogue.innerHTML = `⚙ <strong>Rocket:</strong> "⚡ LASER-SLICED ${item.name}! Sliced ${remainCap.toFixed(1)} kg (${Math.round(frac*100)}%) for +${addedVal.toFixed(1)} CR! Harness 100% full!"`;
  }

  renderRK();
}

document.getElementById('rk-btn-apply')?.addEventListener('click', () => {
  rkCap = parseInt(document.getElementById('rk-input-cap').value) || 20;
  resetRK();
  retroAudio.playClick();
});

document.getElementById('rk-btn-step')?.addEventListener('click', () => {
  stepRK();
});

document.getElementById('rk-btn-all')?.addEventListener('click', () => {
  while (!rkDone && rkItemIdx < rkItems.length && rkCurrentWeight < rkCap) {
    stepRK();
  }
});

function resetRK() {
  rkCurrentWeight = 0;
  rkTotalProfit = 0;
  rkItemIdx = 0;
  rkDone = false;
  rkItems.forEach(it => it.taken = 0);
  rkActor.style.left = '30px';
  renderRK();
  rkDialogue.innerHTML = `💬 <strong>Rocket Raccoon:</strong> "Heist reset. Capacity set to ${rkCap} KG. Let's grab some loot!"`;
}

document.getElementById('rk-btn-reset')?.addEventListener('click', () => {
  resetRK();
});

renderRK();
"""
}

# -----------------------------------------------------------------------------
# 15. THOR: Minimum Cost Spanning Trees (MST)
# -----------------------------------------------------------------------------
PHYSICAL_SIMS_PART3["mst"] = {
    "html": """
<div class="sim-game-wrapper" style="width: 100%; text-align: left;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid #334155; padding-bottom: 8px;">
    <div>
      <span style="font-family: var(--font-pixel); font-size: 0.75rem; color: #b45309;">MISSION: RESTORING THE NINE REALMS BIFROST GRID</span>
      <p style="font-size: 0.82rem; color: #64748b; margin-top: 2px;">Watch Thor channel Mjolnir lightning along the lightest bridges, connecting all realms without cycles.</p>
    </div>
    <div style="font-family: var(--font-pixel); font-size: 0.65rem; background: #1e293b; color: #facc15; padding: 6px 10px; border: 1px solid #475569;">
      BRIDGES CONNECTED: <span id="thor-bridges-count" style="color: #22c55e;">0 / 4</span> | ENERGY: <span id="thor-energy" style="color: #38bdf8;">0 GW</span>
    </div>
  </div>

  <!-- Spanning Tree Invariant Bar -->
  <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 10px 14px; margin-bottom: 14px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="font-family: var(--font-pixel); font-size: 0.62rem; color: #0f172a;">
      REALMS: 5 (Asgard, Midgard, Vanaheim, Alfheim, Nidavellir)
    </div>
    <div style="font-family: var(--font-code); font-size: 0.8rem; font-weight: bold; color: #b45309;">
      MST THEOREM: EXACTLY |V| - 1 = 4 LIGHTEST ACYCLIC BRIDGES
    </div>
  </div>

  <!-- Animated Arena Stage -->
  <div style="background: #090d16; border: 3px solid #0f172a; padding: 18px; border-radius: 6px; box-shadow: inset 0 0 16px rgba(0,0,0,0.9); margin-bottom: 14px; position: relative; min-height: 290px; overflow: hidden;">
    <!-- Thor Actor -->
    <div id="thor-actor" style="position: absolute; top: 15px; left: 30px; transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1); z-index: 20; display: flex; flex-direction: column; align-items: center;">
      <div style="font-family: var(--font-pixel); font-size: 0.5rem; background: #b45309; color: #fff; padding: 1px 4px; border-radius: 2px; margin-bottom: 2px;">⚒ THOR</div>
      <img src="assets/thor.png" style="width: 44px; height: 50px; object-fit: contain; image-rendering: pixelated; filter: drop-shadow(0 4px 8px rgba(180,83,9,0.7));">
    </div>

    <!-- Realm Nodes and Bridges SVG -->
    <svg id="thor-bifrost-svg" style="width: 100%; height: 260px;">
      <!-- Planetary Bridges (Lines) -->
      <!-- A(100,60), M(260,40), V(420,70), L(160,200), N(380,200) -->
      <line id="edge-0" x1="100" y1="60" x2="260" y2="40" stroke="#475569" stroke-width="3"/>
      <line id="edge-1" x1="260" y1="40" x2="420" y2="70" stroke="#475569" stroke-width="3"/>
      <line id="edge-2" x1="100" y1="60" x2="160" y2="200" stroke="#475569" stroke-width="3"/>
      <line id="edge-3" x1="260" y1="40" x2="160" y2="200" stroke="#475569" stroke-width="3"/>
      <line id="edge-4" x1="260" y1="40" x2="380" y2="200" stroke="#475569" stroke-width="3"/>
      <line id="edge-5" x1="420" y1="70" x2="380" y2="200" stroke="#475569" stroke-width="3"/>
      <line id="edge-6" x1="160" y1="200" x2="380" y2="200" stroke="#475569" stroke-width="3"/>

      <!-- Edge Weight Labels -->
      <text x="175" y="40" fill="#38bdf8" font-family="'JetBrains Mono'" font-size="11" font-weight="bold">1 GW</text>
      <text x="345" y="45" fill="#38bdf8" font-family="'JetBrains Mono'" font-size="11" font-weight="bold">2 GW</text>
      <text x="110" y="140" fill="#38bdf8" font-family="'JetBrains Mono'" font-size="11" font-weight="bold">4 GW</text>
      <text x="220" y="130" fill="#38bdf8" font-family="'JetBrains Mono'" font-size="11" font-weight="bold">3 GW</text>
      <text x="310" y="130" fill="#38bdf8" font-family="'JetBrains Mono'" font-size="11" font-weight="bold">6 GW</text>
      <text x="415" y="140" fill="#38bdf8" font-family="'JetBrains Mono'" font-size="11" font-weight="bold">5 GW</text>
      <text x="265" y="220" fill="#38bdf8" font-family="'JetBrains Mono'" font-size="11" font-weight="bold">7 GW</text>

      <!-- Planetary Nodes -->
      <!-- Asgard -->
      <circle cx="100" cy="60" r="18" fill="#1e293b" stroke="#facc15" stroke-width="3"/>
      <text x="100" y="64" fill="#fff" font-family="'Press Start 2P'" font-size="8" text-anchor="middle">A</text>
      <!-- Midgard -->
      <circle cx="260" cy="40" r="18" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
      <text x="260" y="44" fill="#fff" font-family="'Press Start 2P'" font-size="8" text-anchor="middle">M</text>
      <!-- Vanaheim -->
      <circle cx="420" cy="70" r="18" fill="#1e293b" stroke="#22c55e" stroke-width="3"/>
      <text x="420" y="74" fill="#fff" font-family="'Press Start 2P'" font-size="8" text-anchor="middle">V</text>
      <!-- Alfheim -->
      <circle cx="160" cy="200" r="18" fill="#1e293b" stroke="#ec4899" stroke-width="3"/>
      <text x="160" y="204" fill="#fff" font-family="'Press Start 2P'" font-size="8" text-anchor="middle">L</text>
      <!-- Nidavellir -->
      <circle cx="380" cy="200" r="18" fill="#1e293b" stroke="#f97316" stroke-width="3"/>
      <text x="380" y="204" fill="#fff" font-family="'Press Start 2P'" font-size="8" text-anchor="middle">N</text>
    </svg>
  </div>

  <!-- Hero Telemetry Box -->
  <div style="background: #ffffff; border: 2px solid #0f172a; padding: 12px 16px; margin-bottom: 14px; min-height: 52px; display: flex; align-items: center; box-shadow: 0 2px 0 #0f172a;" id="thor-dialogue">
    💬 <strong>Thor:</strong> "The Nine Realms must be connected! Mjolnir will strike the lightest bridges without creating destructive energetic cycles!"
  </div>

  <!-- Interactive Controls -->
  <div class="viz-controls" style="display: flex; flex-wrap: wrap; gap: 10px;">
    <button class="pixel-btn pixel-btn-primary" id="thor-btn-step">⚡ CHANNEL MJOLNIR LIGHTNING</button>
    <button class="pixel-btn pixel-btn-accent" id="thor-btn-all">▶ FULL BIFROST RESTORATION</button>
    <button class="pixel-btn pixel-btn-secondary" id="thor-btn-reset">↺ RESET REALMS</button>
  </div>
</div>
""",
    "script": """
let thorEdgeStep = 0;
let thorConnected = 0;
let thorEnergyTotal = 0;
let thorDone = false;

// Sorted edges by weight
const thorEdges = [
  { id: 0, u: 'A', v: 'M', w: 1, cycle: false, x: 180, y: 50 },
  { id: 1, u: 'M', v: 'V', w: 2, cycle: false, x: 340, y: 55 },
  { id: 3, u: 'M', v: 'L', w: 3, cycle: false, x: 210, y: 120 },
  { id: 2, u: 'A', v: 'L', w: 4, cycle: true,  x: 130, y: 130 }, // Creates cycle with A-M-L
  { id: 5, u: 'V', v: 'N', w: 5, cycle: false, x: 400, y: 135 },
  { id: 4, u: 'M', v: 'N', w: 6, cycle: true,  x: 320, y: 120 },
  { id: 6, u: 'L', v: 'N', w: 7, cycle: true,  x: 270, y: 200 }
];

const thorActor = document.getElementById('thor-actor');
const thorDialogue = document.getElementById('thor-dialogue');
const thorBridgesLabel = document.getElementById('thor-bridges-count');
const thorEnergyLabel = document.getElementById('thor-energy');

function stepThor() {
  if (thorDone || thorEdgeStep >= thorEdges.length || thorConnected >= 4) {
    thorDone = true;
    retroAudio.playSuccess();
    thorDialogue.innerHTML = `<strong>✨ NINE REALMS RECONNECTED!</strong> Bifrost restored with exactly 4 bridges and minimal energy ${thorEnergyTotal} GW!`;
    return;
  }

  retroAudio.playClick();
  const e = thorEdges[thorEdgeStep];
  const lineEl = document.getElementById(`edge-${e.id}`);

  thorActor.style.left = `${e.x}px`;
  thorActor.style.top = `${e.y - 20}px`;

  setTimeout(() => {
    if (!e.cycle && thorConnected < 4) {
      retroAudio.playSuccess();
      lineEl.setAttribute('stroke', '#facc15');
      lineEl.setAttribute('stroke-width', '5');
      thorConnected++;
      thorEnergyTotal += e.w;
      thorDialogue.innerHTML = `⚒ <strong>Thor:</strong> "Mjolnir channels lightning along Bridge ${e.u}-${e.v} (weight ${e.w} GW)! Added to Spanning Tree!"`;
    } else {
      retroAudio.playError();
      lineEl.setAttribute('stroke', '#ef4444');
      lineEl.setAttribute('stroke-dasharray', '5,5');
      thorDialogue.innerHTML = `⚠️ <strong>Thor:</strong> "CYCLE DEFLECTED! Bridge ${e.u}-${e.v} (${e.w} GW) would form a closed loop. Rejected!"`;
    }

    thorBridgesLabel.textContent = `${thorConnected} / 4`;
    thorEnergyLabel.textContent = `${thorEnergyTotal} GW`;
    thorEdgeStep++;

    if (thorConnected >= 4) {
      thorDone = true;
      setTimeout(() => {
        retroAudio.playSuccess();
        thorDialogue.innerHTML = `<strong>✨ NINE REALMS RECONNECTED!</strong> Minimum Cost Spanning Tree complete (|V|-1 = 4 edges)!`;
      }, 300);
    }
  }, 350);
}

document.getElementById('thor-btn-step')?.addEventListener('click', () => {
  stepThor();
});

document.getElementById('thor-btn-all')?.addEventListener('click', () => {
  while (!thorDone && thorEdgeStep < thorEdges.length && thorConnected < 4) {
    stepThor();
  }
});

document.getElementById('thor-btn-reset')?.addEventListener('click', () => {
  thorEdgeStep = 0;
  thorConnected = 0;
  thorEnergyTotal = 0;
  thorDone = false;
  thorActor.style.left = '30px';
  thorActor.style.top = '15px';
  thorBridgesLabel.textContent = '0 / 4';
  thorEnergyLabel.textContent = '0 GW';
  thorEdges.forEach(e => {
    const lineEl = document.getElementById(`edge-${e.id}`);
    lineEl.setAttribute('stroke', '#475569');
    lineEl.setAttribute('stroke-width', '3');
    lineEl.removeAttribute('stroke-dasharray');
  });
  thorDialogue.innerHTML = `💬 <strong>Thor:</strong> "Bifrost grid reset. Lightest bridge is ready for Mjolnir!"`;
});
"""
}
