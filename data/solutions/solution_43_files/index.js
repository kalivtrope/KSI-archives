var logged=!1;$(window).load(function(){function e(){i.width()/i.height()<a?d.removeClass().addClass("bgheight"):d.removeClass().addClass("bgwidth")}var i=$(window),d=$("#background-image"),a=d.width()/d.height();i.resize(e).trigger("resize")});