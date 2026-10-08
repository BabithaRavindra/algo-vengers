/**
 * ALGO-VENGERS — MAIN APPLICATION LOGIC
 * Navigation, Toggles, DAA Process Steps, and Interactive Listeners
 */

document.addEventListener('DOMContentLoaded', () => {
  initNavbar();
  initToggles();
  initDaaFlowInteractive();
  initSectionScrollSpy();
  initHeroHudTicker();
});

/* Navigation & Mobile Drawer */
function initNavbar() {
  const navbar = document.querySelector('.pixel-navbar');
  const mobileToggle = document.getElementById('mobile-nav-toggle');
  const navMenu = document.getElementById('nav-menu');
  const navLinks = document.querySelectorAll('.nav-link');

  // Sticky navbar shadow on scroll
  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  }, { passive: true });

  // Mobile menu toggle
  if (mobileToggle && navMenu) {
    mobileToggle.addEventListener('click', () => {
      navMenu.classList.toggle('open');
      const isOpen = navMenu.classList.contains('open');
      mobileToggle.textContent = isOpen ? '[✕] MENU' : '[☰] MENU';
      if (window.retroAudio) {
        window.retroAudio.playClick();
      }
    });

    // Close mobile menu when link is clicked
    navLinks.forEach(link => {
      link.addEventListener('click', () => {
        navMenu.classList.remove('open');
        mobileToggle.textContent = '[☰] MENU';
      });
    });
  }
}

/* Audio & CRT Scanline Toggles */
function initToggles() {
  const sfxToggleBtn = document.getElementById('sfx-toggle-btn');
  const crtToggleBtn = document.getElementById('crt-toggle-btn');

  if (sfxToggleBtn) {
    sfxToggleBtn.addEventListener('click', () => {
      if (window.retroAudio) {
        const isEnabled = window.retroAudio.toggle();
        sfxToggleBtn.textContent = isEnabled ? '🔊 SFX: ON' : '🔇 SFX: OFF';
        sfxToggleBtn.classList.toggle('active', isEnabled);
      }
    });
  }

  if (crtToggleBtn) {
    crtToggleBtn.addEventListener('click', () => {
      document.body.classList.toggle('crt-disabled');
      const isDisabled = document.body.classList.contains('crt-disabled');
      crtToggleBtn.textContent = isDisabled ? '📺 CRT: OFF' : '📺 CRT: ON';
      crtToggleBtn.classList.toggle('active', !isDisabled);
      if (window.retroAudio) {
        window.retroAudio.playToggle(!isDisabled);
      }
    });
  }
}

/* Interactive DAA Flowchart (Section 02) */
function initDaaFlowInteractive() {
  const flowSteps = document.querySelectorAll('.daa-flow-step');
  const explainBox = document.getElementById('flow-explanation-box');

  const stepDetails = {
    problem: {
      title: "STAGE 1: PROBLEM SPECIFICATION",
      desc: "Precisely define computational inputs, required outputs, boundary preconditions, and invariant constraints before writing any code."
    },
    design: {
      title: "STAGE 2: STRATEGIC DESIGN",
      desc: "Select the appropriate algorithmic paradigm (Divide & Conquer, Greedy, Dynamic Programming, Backtracking) suited to the problem structure."
    },
    algorithm: {
      title: "STAGE 3: ALGORITHM FORMULATION",
      desc: "Develop unambiguous, finite, step-by-step instructions or pseudocode guaranteed to terminate on all valid inputs."
    },
    analyze: {
      title: "STAGE 4: ASYMPTOTIC ANALYSIS",
      desc: "Rigorously quantify worst, average, and best-case execution bounds using Big-O, Big-Omega, and Big-Theta metrics, analyzing space vs time trade-offs."
    },
    solution: {
      title: "STAGE 5: EFFICIENT SOLUTION",
      desc: "Produce verified, provably correct, scalable code optimized to run under real-world computational and hardware constraints."
    }
  };

  flowSteps.forEach(step => {
    step.addEventListener('click', () => {
      flowSteps.forEach(s => s.classList.remove('active'));
      step.classList.add('active');

      const stepKey = step.getAttribute('data-step');
      if (stepDetails[stepKey] && explainBox) {
        explainBox.innerHTML = `
          <strong style="color: var(--color-gold); font-family: var(--font-pixel); font-size: 0.72rem; display: block; margin-bottom: 6px;">
            ${stepDetails[stepKey].title}
          </strong>
          <span>${stepDetails[stepKey].desc}</span>
        `;
      }

      if (window.retroAudio) {
        window.retroAudio.playClick();
      }
    });
  });
}

/* ScrollSpy for Navigation Highlighting */
function initSectionScrollSpy() {
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');

  window.addEventListener('scroll', () => {
    const scrollPos = window.scrollY + 140;

    sections.forEach(sec => {
      const top = sec.offsetTop;
      const height = sec.offsetHeight;
      const id = sec.getAttribute('id');

      if (scrollPos >= top && scrollPos < top + height) {
        navLinks.forEach(link => {
          link.classList.remove('active');
          if (link.getAttribute('href') === `#${id}`) {
            link.classList.add('active');
          }
        });
      }
    });
  }, { passive: true });
}

/* Hero HUD Clock and Dynamic Status */
function initHeroHudTicker() {
  const timeElem = document.getElementById('hero-hud-time');
  if (!timeElem) return;

  function updateTime() {
    const now = new Date();
    const hrs = String(now.getHours()).padStart(2, '0');
    const mins = String(now.getMinutes()).padStart(2, '0');
    const secs = String(now.getSeconds()).padStart(2, '0');
    timeElem.textContent = `STARDATE ${hrs}:${mins}:${secs}`;
  }

  updateTime();
  setInterval(updateTime, 1000);
}
