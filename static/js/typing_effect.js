function runTypingEffect() {
  const t1 = 'Have you checked out our';
  const t2 = 'Leaderboard?';
  const t3 = 'Check Now';

  const firstTypingEl = document.getElementById('typing-text-1');
  const secondTypingEl = document.getElementById('typing-text-2');
  const thirdTypingEl = document.getElementById('typing-text-3');
  const typingDelay = 100;

  typeText(t1, firstTypingEl, typingDelay);
  setTimeout(() => {
    typeText(t2, secondTypingEl, typingDelay);
  }, 2150);
  setTimeout(() => {
    typeText(t3, thirdTypingEl, typingDelay);
  }, 3150);
}

function typeText(text, typingElement, delay) {
  for (let i = 0; i < text.length; i++) {
    setTimeout(() => {
      typingElement.textContent += text.charAt(i);
    }, delay * i);
  }
}

document.addEventListener('DOMContentLoaded', runTypingEffect);
