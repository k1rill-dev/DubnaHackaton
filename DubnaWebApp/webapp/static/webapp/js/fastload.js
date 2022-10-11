// здесь создаем объект-обертку, дабы не загрязнять глобальное пространство имен
var loader = loader || {}

// uri - полный адрес к удаленному JS файлу

loader.importJS = function( uri ) {
    let script = document.createElement('script');
    // получаем ссылку на тег head документа
    let head   = document.getElementsByTagName('head')[0];
    // устанавливаем тип и uri
    script.type = 'text/javascript';
    script.src  = uri;
    // загружаем скрипт в тег head
    head.appendChild(script);
}

//вызов 
loader.importJS('https://cdnjs.cloudflare.com/ajax/libs/timeago.js/3.0.2/timeago.js')
// timeago().format(new Date())


loader.importJS('https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.24.0/moment.min.js')
// moment().format('dddd')