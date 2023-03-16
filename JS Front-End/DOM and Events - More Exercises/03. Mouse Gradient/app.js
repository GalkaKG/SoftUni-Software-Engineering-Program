function attachGradientEvents() {
    const divEl = document.getElementById('result');
    const gradientEl = document.getElementById('gradient');
    gradientEl.addEventListener('mousemove', calc);
    gradientEl.addEventListener('mouseleave', () => divEl.textContent = '');
    
    function calc(event) {
        let position = Math.floor((event.offsetX / (event.target.clientWidth - 1)) * 100);
        divEl.textContent = `${position}%`;    
    }
}
