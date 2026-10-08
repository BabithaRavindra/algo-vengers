/**
 * ALGO-VENGERS — CUSTOM PIXEL CURSOR ENGINE
 * Renders individual Avenger pixel-art cursors on interactive element hover
 */

class HeroCursorManager {
  constructor() {
    this.follower = null;
    this.wrapper = null;
    this.currentHero = null;
    this.isActive = false;
    this.mouseX = -100;
    this.mouseY = -100;
    this.targetX = -100;
    this.targetY = -100;
    this.rafId = null;

    // SVG Pixel Art Templates for the 7 Avengers
    this.cursorTemplates = {
      ironman: `
        <svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" shape-rendering="crispEdges">
          <!-- Circular Frame -->
          <circle cx="16" cy="16" r="14" fill="#800c0c" stroke="#f5b722" stroke-width="2"/>
          <!-- Faceplate -->
          <rect x="9" y="8" width="14" height="15" fill="#e74c3c"/>
          <rect x="11" y="9" width="10" height="12" fill="#f5b722"/>
          <rect x="11" y="19" width="10" height="3" fill="#e74c3c"/>
          <!-- Glowing Cyan Slit Eyes -->
          <rect x="12" y="14" width="3" height="2" fill="#00f0ff"/>
          <rect x="17" y="14" width="3" height="2" fill="#00f0ff"/>
          <!-- Mouth Slit -->
          <rect x="14" y="19" width="4" height="1" fill="#000000"/>
        </svg>
      `,
      captain: `
        <svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" shape-rendering="crispEdges">
          <!-- Outer Red Ring -->
          <circle cx="16" cy="16" r="14" fill="#c0392b" stroke="#000000" stroke-width="1.5"/>
          <!-- White Ring -->
          <circle cx="16" cy="16" r="11" fill="#ecf0f1"/>
          <!-- Inner Red Ring -->
          <circle cx="16" cy="16" r="8" fill="#c0392b"/>
          <!-- Blue Center -->
          <circle cx="16" cy="16" r="5" fill="#2980b9"/>
          <!-- Pixel Star -->
          <polygon points="16,12 17.5,15.5 21,15.5 18,17.5 19.5,21 16,18.8 12.5,21 14,17.5 11,15.5 14.5,15.5" fill="#ffffff"/>
        </svg>
      `,
      thor: `
        <svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" shape-rendering="crispEdges">
          <!-- Mjolnir Hammer Head -->
          <rect x="7" y="6" width="18" height="12" fill="#7f8c8d" stroke="#1e272e" stroke-width="1.5"/>
          <rect x="9" y="8" width="14" height="2" fill="#bdc3c7"/>
          <rect x="7" y="14" width="18" height="2" fill="#576574"/>
          <!-- Lightning Inscription -->
          <path d="M16 8 L14 12 L17 12 L15 16" stroke="#00f0ff" stroke-width="1.5" fill="none"/>
          <!-- Leather Handle -->
          <rect x="14" y="18" width="4" height="11" fill="#6d4c41"/>
          <rect x="14" y="20" width="4" height="2" fill="#4e342e"/>
          <rect x="14" y="24" width="4" height="2" fill="#4e342e"/>
          <!-- Wrist Strap Pommel -->
          <rect x="13" y="29" width="6" height="2" fill="#95a5a6"/>
        </svg>
      `,
      hulk: `
        <svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" shape-rendering="crispEdges">
          <!-- Heavy Hulk Fist -->
          <rect x="8" y="10" width="16" height="16" rx="2" fill="#27ae60" stroke="#145a32" stroke-width="1.5"/>
          <!-- Knuckles -->
          <rect x="8" y="7" width="4" height="5" fill="#2ecc71" stroke="#145a32" stroke-width="1"/>
          <rect x="12" y="6" width="4" height="6" fill="#2ecc71" stroke="#145a32" stroke-width="1"/>
          <rect x="16" y="6" width="4" height="6" fill="#2ecc71" stroke="#145a32" stroke-width="1"/>
          <rect x="20" y="8" width="4" height="5" fill="#2ecc71" stroke="#145a32" stroke-width="1"/>
          <!-- Purple Wristband / Wrap -->
          <rect x="9" y="23" width="14" height="4" fill="#8e44ad"/>
          <rect x="11" y="24" width="10" height="2" fill="#9b59b6"/>
        </svg>
      `,
      widow: `
        <svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" shape-rendering="crispEdges">
          <!-- Tactical Emblem Frame -->
          <circle cx="16" cy="16" r="14" fill="#181e28" stroke="#ff3838" stroke-width="1.5"/>
          <!-- Hourglass Symbol -->
          <polygon points="10,9 22,9 16,16" fill="#ff3838"/>
          <polygon points="16,16 22,23 10,23" fill="#ff3838"/>
          <!-- Center Core Glow -->
          <circle cx="16" cy="16" r="1.5" fill="#ffffff"/>
        </svg>
      `,
      hawkeye: `
        <svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" shape-rendering="crispEdges">
          <!-- Precision Arrow Shaft -->
          <line x1="6" y1="26" x2="24" y2="8" stroke="#8854d0" stroke-width="3"/>
          <!-- Arrow Head / Tip -->
          <polygon points="26,6 18,8 24,14" fill="#ff9f43" stroke="#000" stroke-width="1"/>
          <polygon points="27,5 21,7 25,11" fill="#f5cd79"/>
          <!-- Arrow Fletching (Purple Feathers) -->
          <polygon points="5,27 10,25 7,22" fill="#5f27cd"/>
          <polygon points="4,28 9,26 6,23" fill="#8854d0"/>
        </svg>
      `,
      spiderman: `
        <svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" shape-rendering="crispEdges">
          <!-- Spidey Head Silhouette -->
          <path d="M9 8 C9 3, 23 3, 23 8 C25 15, 24 23, 16 29 C8 23, 7 15, 9 8 Z" fill="#eb4d4b" stroke="#130f40" stroke-width="1.5"/>
          <!-- Web Lines on Mask -->
          <line x1="16" y1="4" x2="16" y2="28" stroke="#130f40" stroke-width="1"/>
          <line x1="9" y1="14" x2="23" y2="14" stroke="#130f40" stroke-width="1"/>
          <!-- Iconic White Lenses with Black Borders -->
          <polygon points="11,12 14,12 15,18 11,16" fill="#ffffff" stroke="#130f40" stroke-width="1.5"/>
          <polygon points="21,12 18,12 17,18 21,16" fill="#ffffff" stroke="#130f40" stroke-width="1.5"/>
        </svg>
      `
    };

    this.init();
  }

  init() {
    // Check for touch / pointer coarse devices
    if (window.matchMedia && window.matchMedia('(pointer: coarse)').matches) {
      return; // Fallback to touch controls
    }

    // Create custom cursor follower
    this.follower = document.createElement('div');
    this.follower.id = 'custom-cursor-follower';
    this.wrapper = document.createElement('div');
    this.wrapper.className = 'cursor-icon-wrapper';
    this.follower.appendChild(this.wrapper);
    document.body.appendChild(this.follower);

    // Event listeners for smooth tracking
    window.addEventListener('mousemove', (e) => this.onMouseMove(e), { passive: true });
    window.addEventListener('mousedown', () => this.onMouseDown());
    window.addEventListener('mouseup', () => this.onMouseUp());
    document.addEventListener('mouseleave', () => this.hide());

    this.attachElementListeners();
    this.startLoop();
  }

  onMouseMove(e) {
    this.mouseX = e.clientX;
    this.mouseY = e.clientY;
  }

  onMouseDown() {
    if (this.follower) {
      this.follower.classList.add('clicking');
    }
    if (window.retroAudio) {
      window.retroAudio.playClick();
    }
  }

  onMouseUp() {
    if (this.follower) {
      this.follower.classList.remove('clicking');
    }
  }

  startLoop() {
    const loop = () => {
      // Smooth interpolation for silky motion
      this.targetX += (this.mouseX - this.targetX) * 0.45;
      this.targetY += (this.mouseY - this.targetY) * 0.45;

      if (this.follower) {
        this.follower.style.transform = `translate3d(${this.targetX}px, ${this.targetY}px, 0) translate(-50%, -50%)`;
      }
      this.rafId = requestAnimationFrame(loop);
    };
    loop();
  }

  attachElementListeners() {
    // Delegate hover detection
    document.addEventListener('mouseover', (e) => {
      const target = e.target.closest('button, .pixel-btn, a, .mission-card, .arsenal-card, .algo-hero-card, .daa-flow-step, .interactive-target, .learning-step-card');
      if (target) {
        const heroSection = target.closest('[data-hero-cursor]');
        if (heroSection) {
          const heroKey = heroSection.getAttribute('data-hero-cursor');
          this.showHeroCursor(heroKey);
          if (window.retroAudio) {
            window.retroAudio.playHover();
          }
        }
      }
    });

    document.addEventListener('mouseout', (e) => {
      const target = e.target.closest('button, .pixel-btn, a, .mission-card, .arsenal-card, .algo-hero-card, .daa-flow-step, .interactive-target, .learning-step-card');
      if (target) {
        const related = e.relatedTarget ? e.relatedTarget.closest('button, .pixel-btn, a, .mission-card, .arsenal-card, .algo-hero-card, .daa-flow-step, .interactive-target, .learning-step-card') : null;
        if (!related) {
          this.hide();
        }
      }
    });
  }

  showHeroCursor(heroKey) {
    if (!this.cursorTemplates[heroKey]) return;
    this.wrapper.innerHTML = this.cursorTemplates[heroKey];
    this.follower.classList.add('visible');
    this.currentHero = heroKey;
    this.isActive = true;
  }

  hide() {
    if (this.follower) {
      this.follower.classList.remove('visible');
    }
    this.isActive = false;
  }
}

document.addEventListener('DOMContentLoaded', () => {
  window.heroCursorManager = new HeroCursorManager();
});
