/**
 * ALGO-VENGERS — AMBIENT PIXEL PARTICLES CANVAS
 * High performance floating square pixel dust & energy sparks
 */

class PixelParticleCanvas {
  constructor(canvasId = 'fx-canvas') {
    this.canvas = document.getElementById(canvasId);
    if (!this.canvas) return;
    this.ctx = this.canvas.getContext('2d');
    this.particles = [];
    this.count = 42;
    this.colors = ['#00f0ff', '#f5b722', '#ff3838', '#10ac84', '#8854d0'];
    this.width = window.innerWidth;
    this.height = window.innerHeight;
    this.init();
  }

  init() {
    this.resize();
    window.addEventListener('resize', () => this.resize(), { passive: true });

    // Spawn initial pixel motes
    for (let i = 0; i < this.count; i++) {
      this.particles.push(this.createParticle());
    }

    this.render();
  }

  createParticle(randomY = true) {
    const size = Math.random() > 0.6 ? 4 : 2;
    return {
      x: Math.random() * this.width,
      y: randomY ? Math.random() * this.height : this.height + 10,
      size: size,
      speedY: -(0.3 + Math.random() * 0.7),
      speedX: (Math.random() - 0.5) * 0.4,
      color: this.colors[Math.floor(Math.random() * this.colors.length)],
      alpha: 0.15 + Math.random() * 0.55,
      pulseSpeed: 0.01 + Math.random() * 0.02,
      pulseOffset: Math.random() * Math.PI
    };
  }

  resize() {
    this.width = window.innerWidth;
    this.height = window.innerHeight;
    this.canvas.width = this.width;
    this.canvas.height = this.height;
  }

  render() {
    this.ctx.clearRect(0, 0, this.width, this.height);

    for (let i = 0; i < this.particles.length; i++) {
      const p = this.particles[i];
      p.y += p.speedY;
      p.x += p.speedX;
      p.pulseOffset += p.pulseSpeed;

      const currentAlpha = Math.max(0.1, p.alpha + Math.sin(p.pulseOffset) * 0.2);

      // Wrap-around
      if (p.y < -10 || p.x < -10 || p.x > this.width + 10) {
        this.particles[i] = this.createParticle(false);
      }

      this.ctx.fillStyle = p.color;
      this.ctx.globalAlpha = currentAlpha;
      // Draw pixel square (crisp)
      this.ctx.fillRect(Math.floor(p.x), Math.floor(p.y), p.size, p.size);
    }

    this.ctx.globalAlpha = 1.0;
    requestAnimationFrame(() => this.render());
  }
}

document.addEventListener('DOMContentLoaded', () => {
  window.pixelParticles = new PixelParticleCanvas();
});
