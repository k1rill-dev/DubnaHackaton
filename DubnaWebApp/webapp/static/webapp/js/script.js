let tg = window.Telegram.WebApp;

tg.expand();


var buttons = document.getElementsByClassName('butt'),
    forEach = Array.prototype.forEach;

forEach.call(buttons, function (b) {
    b.addEventListener('click', addElement);
});



function addElement(e) {
    var addDiv = document.createElement('div'),
        mValue = Math.max(this.clientWidth, this.clientHeight),
        rect = this.getBoundingClientRect();
        sDiv = addDiv.style,
        px = 'px';
        window.location.href = 'http://127.0.0.1:8000/menu';

        sDiv.width = sDiv.height = mValue + px;
        sDiv.left = e.clientX - rect.left - (mValue / 2) + px;
        sDiv.top = e.clientY - rect.top - (mValue / 2) + px;


    addDiv.classList.add('pulse');
    this.appendChild(addDiv);
}