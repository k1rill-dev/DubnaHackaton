let tg = window.Telegram.WebApp;
Telegram.WebApp.ready();
tg.expand();
tg.MainButton.textColor = '#FFFFFF';
tg.MainButton.color = '#2cab37';

let id = tg.initDataUnsafe.user.id
//alert(tg.initDataUnsafe.user.id)
//tg.initData
