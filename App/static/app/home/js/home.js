$(function(){

    initMenuSwiper();
    loadbanner();
});


function initTopSwiper(){

    var swiper = new Swiper("#topSwiper", {
        loop: true,
        pagination:".swiper-pagination",
        autoplay: 3000
    })
}

function initMenuSwiper(){

    var swiper = new Swiper("#swiperMenu", {
        slidesPerView: 3
    })
}
function loadbanner(){
    $.getJSON("/home/", function(data){
        console.log(data);
        var banner_data = data["banner_data"];
        var banner_container = $("#topSwiperWrapper");
        for (var i=0;i<banner_data.length;i++){
            var swiper_silde = $("<div class='swiper-slide'></div>");
            var swiper_silde_a = $("<a href=''#'></a>");
            var swiper_silde_a_img = $('<img>');
            swiper_silde_a_img.attr("src", banner_data[i]["img"]);
            swiper_silde_a_img.appendTo(swiper_silde_a);
            swiper_silde_a.appendTo(swiper_silde);
            swiper_silde.appendTo(banner_container)
        }
         initTopSwiper();
    })

}


