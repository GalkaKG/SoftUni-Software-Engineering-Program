const vRipple = {
  mounted: (el, binding) => {
    el.style.position = 'relative';
    el.style.overflow = 'hidden';
    el.addEventListener('click', (ev) => {
      const rippleTarget = el.getBoundingClientRect();
      const rippleEl = document.createElement('span');
      const rippleMax = +binding.value || 50;
      const offsetY = ev.clientY - rippleTarget.y;
      const offsetX = ev.clientX - rippleTarget.x;
      let handler = null;
      let diameter = 1;
      let opacity = 0.65;

      handler = setInterval(animate, 15);
      ev.target.appendChild(rippleEl);
      rippleEl.style.position = 'absolute';
      rippleEl.style.height = '10px';
      rippleEl.style.width = '10px';
      rippleEl.style.borderRadius = '100%';
      rippleEl.style.backgroundColor = '#f2f2f2';
      rippleEl.style.left = `${offsetX}px`;
      rippleEl.style.top = `${offsetY}px`;

      function animate() {
        if (diameter < rippleMax) {
          diameter++;
          opacity -= 0.65 / rippleMax;
          rippleEl.style.transform = `scale(${diameter})`;
          rippleEl.style.opacity = `${opacity}`;
        } else {
          rippleEl.remove();
          clearInterval(handler);
        }
      }
    });
  },
};

export default vRipple;