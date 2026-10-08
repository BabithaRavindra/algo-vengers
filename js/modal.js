/**
 * ALGO-VENGERS — MISSION DOSSIER & TOPIC MODAL CONTROLLER
 * Handles interactive briefings for the 5 missions and 20 DAA topics
 */

class MissionModalController {
  constructor() {
    this.modal = document.getElementById('mission-dossier-modal');
    this.closeBtn = document.getElementById('modal-close-trigger');
    this.ackBtn = document.getElementById('modal-ack-trigger');
    this.badgeElem = document.getElementById('modal-badge-val');
    this.titleElem = document.getElementById('modal-title-val');
    this.descElem = document.getElementById('modal-desc-val');
    this.topicsContainer = document.getElementById('modal-topics-container');

    this.init();
  }

  init() {
    if (!this.modal) return;

    // Close listeners
    if (this.closeBtn) {
      this.closeBtn.addEventListener('click', () => this.close());
    }
    if (this.ackBtn) {
      this.ackBtn.addEventListener('click', () => this.close());
    }

    this.modal.addEventListener('click', (e) => {
      if (e.target === this.modal) {
        this.close();
      }
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && this.modal.classList.contains('active')) {
        this.close();
      }
    });

    // Attach click listeners to all mission access buttons and cards
    document.querySelectorAll('[data-access-mission]').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const missionId = btn.getAttribute('data-access-mission');
        this.openMission(missionId);
      });
    });

    // Attach click listeners to topic cards
    document.querySelectorAll('[data-inspect-topic]').forEach(card => {
      card.addEventListener('click', (e) => {
        const topicName = card.getAttribute('data-inspect-topic');
        this.openTopic(topicName);
      });
    });
  }

  openMission(missionId) {
    if (!window.MISSIONS_DATA) return;
    const mission = window.MISSIONS_DATA.find(m => m.id === missionId) || window.MISSIONS_DATA[0];

    if (this.badgeElem) this.badgeElem.textContent = `MISSION ${mission.num} // ${mission.codename}`;
    if (this.titleElem) this.titleElem.textContent = mission.title;
    if (this.descElem) this.descElem.textContent = mission.desc;

    if (this.topicsContainer) {
      this.topicsContainer.innerHTML = mission.topics.map(t => `
        <div class="modal-topic-item">
          <div>
            <div class="topic-item-title">${t.name}</div>
            <div style="font-size: 0.8rem; color: #94a3b8; margin-top: 2px;">${t.summary}</div>
          </div>
          <div class="topic-item-meta">${t.complexity}</div>
        </div>
      `).join('');
    }

    this.modal.classList.add('active');
    document.body.style.overflow = 'hidden';

    if (window.retroAudio) {
      window.retroAudio.playMissionOpen();
    }
  }

  openTopic(topicName) {
    if (!window.MISSIONS_DATA) return;
    let foundTopic = null;
    let parentMission = null;

    for (const m of window.MISSIONS_DATA) {
      const match = m.topics.find(t => t.name.toLowerCase() === topicName.toLowerCase());
      if (match) {
        foundTopic = match;
        parentMission = m;
        break;
      }
    }

    if (!foundTopic) return;

    if (this.badgeElem) this.badgeElem.textContent = `TOPIC DOSSIER // ${parentMission.title}`;
    if (this.titleElem) this.titleElem.textContent = foundTopic.name;
    if (this.descElem) this.descElem.textContent = foundTopic.summary;

    if (this.topicsContainer) {
      this.topicsContainer.innerHTML = `
        <div class="modal-topic-item">
          <div>
            <div class="topic-item-title">Algorithmic Paradigm</div>
            <div style="font-size: 0.8rem; color: #94a3b8;">Strategic Approach</div>
          </div>
          <div class="topic-item-meta">${foundTopic.paradigm}</div>
        </div>
        <div class="modal-topic-item">
          <div>
            <div class="topic-item-title">Theoretical Complexity</div>
            <div style="font-size: 0.8rem; color: #94a3b8;">Asymptotic Bound</div>
          </div>
          <div class="topic-item-meta">${foundTopic.complexity}</div>
        </div>
      `;
    }

    this.modal.classList.add('active');
    document.body.style.overflow = 'hidden';

    if (window.retroAudio) {
      window.retroAudio.playMissionOpen();
    }
  }

  close() {
    this.modal.classList.remove('active');
    document.body.style.overflow = '';
    if (window.retroAudio) {
      window.retroAudio.playClick();
    }
  }
}

document.addEventListener('DOMContentLoaded', () => {
  window.missionModalController = new MissionModalController();
});
