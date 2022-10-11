var one = $("#one");
    var two = $("#two");

    var span = $("span");


  $(window).on('resize', function () {
      
      if (window.matchMedia("screen and (min-width: 1px) and (max-width:392px)").matches) {
         two.css({
                "background": "blue"

            })
        }else {
            two.css({
                "background": "red"

            })
        }
 
    })