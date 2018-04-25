$(function(){
    
    loadbanner();
    initTopMenu();
    swiperMenu();
    initMenuSwiper();
    initCVS();
    mainInfo();
});

//       顶部轮播
function initTopSwiper(){

    var swiper = new Swiper("#topSwiper", {
        loop: true,
        pagination:".swiper-pagination",
        autoplay: 3000
    })
}


function loadbanner(){
    $.getJSON("/home/", function(data){
        // console.log(data);
        var banner_data = data["banner_data"];
        var banner_container = $("#topSwiperWrapper");
        for (var i=0;i<banner_data.length;i++){
            var swiper_silde = $("<div class='swiper-slide'></div>");
            var swiper_silde_a = $("<a href='#'></a>");
            var swiper_silde_a_img = $('<img>');
            swiper_silde_a_img.attr("src", banner_data[i]["img"]);
            swiper_silde_a_img.appendTo(swiper_silde_a);
            swiper_silde_a.appendTo(swiper_silde);
            swiper_silde.appendTo(banner_container);
        }
         initTopSwiper();
    })

}

//     导航
function initTopMenu() {
    $.getJSON('/home/', function (data) {
        // console.log(data);
        var menu_data = data['menu_data'];
        var menu_ul = $('#topMenu');
        
        for (var i = 0; i < menu_data.length; i++){
            var menu_ul_li = $('<li></li>');
            var menu_ul_li_img = $('<img>');
            var menu_ul_li_span = $('<span></span>');
            menu_ul_li_img.attr('src', menu_data[i]['img']);
            menu_ul_li_span.attr(menu_data[i]['name']);
            menu_ul_li_img.appendTo(menu_ul_li);
            menu_ul_li_span.appendTo(menu_ul_li);
            menu_ul_li.appendTo(menu_ul);
            
        }

    })

}

//      必购
function initMenuSwiper(){

    var swiper = new Swiper("#swiperMenu", {
        slidesPerView: 3
    })
}


function swiperMenu() {
    $.getJSON('/home/', function (data) {
        var swiper_menu_data = data['swiper_menu_data'];
        var swiper_menu_container = $('#swiperMenuWrapper');
        
        for (var i = 0; i < swiper_menu_data.length; i++){
            var swiper_slide = $('<li class="swiper-slide"></li>');
            var swiper_slide_img = $('<img>');
            swiper_slide_img.attr('src', swiper_menu_data[i]['img']);
            swiper_slide_img.appendTo(swiper_slide);
            swiper_slide.appendTo(swiper_menu_container);
        }
        
    })
    
}

//    商店
function initCVS() {
    $.getJSON('/home/', function (data) {
        var CVS_container = $('#CVS');
        
        // 第一部分
        var CVS_data0 = data['CVS_data0'];
        var CVS_h2 = $('<h2></h2>');
        var CVS_h2_img = $('<img>');
        CVS_h2_img.attr('src', CVS_data0.img);
        CVS_h2_img.appendTo(CVS_h2);
        CVS_h2.appendTo(CVS_container);

        // 第二部分
        var CVS_date1_3 = data['CVS_data1_3'];
        var CVS_fieldset = $('<fieldset></fieldset>');
        for (var i = 0; i < CVS_data1_3.length; i++){
            var CVS_a = $('<a href="#"></a>');
            var CVS_a_img = $('<img>');
            CVS_a_img.attr('src', CVS_date1_3[i][img]);
            CVS_a_img.appendTo(CVS_a);
            CVS_a.appendTo(CVS_fieldset);
        }
        CVS_fieldset.appendTo(CVS_container);

        // 第三部分
        var CVS_date3_7 = data['CVS_data3_7'];
        var CVS_ul = $('<ul></ul>');
        for (var j = 0; j < CVS_date3_7.length; j++){
            var ul_li = $('<li></li>');
            var ul_li_a = $('<a href="#"></a>');
            var ul_li_a_img = $('<img>');
            var ul_li_a_span = $('<span></span>');
            ul_li_a_img.attr('src', CVS_date3_7[j]['img']);
            ul_li_a_span.attr(CVS_date3_7[j]['name']);
            ul_li_a_img.appendTo(CVS_li_a);
            ul_li_a_span.appendTo(CVS_li_a);
            ul_li_a.appendTo(CVS_li);
            ul_li.appendTo(CVS_ul);
        }
        CVS_ul.appendTo(CVS_container);

        // 第四部分
        var CVS_date7_11 = data['CVS_data7_11'];
        var CVS_ol = $('<ol></ol>');
        for (var m = 0; m < CVS_date7_11.length; m++){
            var ol_li = $('<li></li>');
            var ol_li_a = $('<a href="#"></a>');
            var ol_li_a_img = $('<img>');
            ol_li_a_img.attr('src', CVS_date3_7[m]['img']);
            ol_li_a_img.appendTo(CVS_li_a);
            ol_li_a.appendTo(CVS_li);
            ol_li.appendTo(CVS_ul);
        }
        CVS_ol.appendTo(CVS_container);
    })

}

//   主要显示
function mainInfo() {
    $.getJSON('/home/', function (data) {
        var mainInfo_data = data['mainInfo_data'];
        var mainInfo_container = $('#mainInfo');

        for (var i = 0; i < mainInfo_data.length; i++){

            var main_section = $('<section></section>');

            // 第一部分
            var main_h3 = $('<h3></h3>');
            main_h3.attr(mainInfo_data[i]['name']);
            var h3_span = $('<span></span>');
            var h3_a = $('<a href="#">更多&gt;</a>');
            h3_span.appendTo(main_h3);
            h3_a.appendTo(main_h3);
            main_h3.appendTo(main_section);

            //  第二部分
            var main_div = $('<div></div>');
            var div_a = $('<a href="#"></a>');
            var div_a_img = $('<img>');
            div_a_img.attr('src', mainInfo_data[i]['img']);
            div_a_img.appendTo(div_a);
            div_a.appendTo(main_div);
            main_div.appendTo(main_section);

            //  第三部分
            var main_ul = $('<ul></ul>');

            //  列表1
            var ul_li1 = $('<li></li>');

            var li1_a = $('<a href="#"></a>');

            var li1_a_img = $('<img>');
            li1_a_img.attr('src', mainInfo_data[i]['img1']);
            li1_a_img.attr('alt', mainInfo_data[i]['longname1']);
            li1_a_img.appendTo(li1_a);

            var li1_a_p = $('<p class="description"></p>');
            li1_a_p.attr(mainInfo_data[i]['longname1']);
            li1_a_p.appendTo(li1_a);

            var li1_a_span = $('<span>￥</span>')
            var li1_a_s = $('<s>￥</s>');
            li1_a_span.attr(mainInfo_data[i]['price1']);
            li1_a_s.attr(mainInfo_data[i]['marketprice1']);
            li1_a_span.appendTo(li1_a);
            li1_a_s.appendTo(li1_a);

            var li1_button = $('<button></button>');
            var li1_button_span = $('<span>+</span>');
            li1_button_span.appendTo(li1_button);

            li1_a.appendTo(ul_li1);
            li1_button.appendTo(ul_li1);
            ul_li1.appendTo(main_ul);

            //  列表2
            var ul_li2 = $('<li></li>');

            var li2_a = $('<a href="#"></a>');

            var li2_a_img = $('<img>');
            li2_a_img.attr('src', mainInfo_data[i]['img2']);
            li2_a_img.attr('alt', mainInfo_data[i]['longname2']);
            li2_a_img.appendTo(li1_a);

            var li2_a_p = $('<p class="description"></p>');
            li2_a_p.attr(mainInfo_data[i]['longname2']);
            li2_a_p.appendTo(li2_a);

            var li2_a_span = $('<span>￥</span>')
            var li2_a_s = $('<s>￥</s>');
            li2_a_span.attr(mainInfo_data[i]['price2']);
            li2_a_s.attr(mainInfo_data[i]['marketprice2']);
            li2_a_span.appendTo(li2_a);
            li2_a_s.appendTo(li2_a);

            var li2_button = $('<button></button>');
            var li2_button_span = $('<span>+</span>');
            li2_button_span.appendTo(li2_button);

            li2_a.appendTo(ul_li2);
            li2_button.appendTo(ul_li2);
            ul_li2.appendTo(main_ul);

            //  列表3
            var ul_li3 = $('<li></li>');

            var li3_a = $('<a href="#"></a>');

            var li3_a_img = $('<img>');
            li3_a_img.attr('src', mainInfo_data[i]['img3']);
            li3_a_img.attr('alt', mainInfo_data[i]['longname3']);
            li3_a_img.appendTo(li3_a);

            var li3_a_p = $('<p class="description"></p>');
            li3_a_p.attr(mainInfo_data[i]['longname3']);
            li3_a_p.appendTo(li3_a);

            var li3_a_span = $('<span>￥</span>');
            var li3_a_s = $('<s>￥</s>');
            li3_a_span.attr(mainInfo_data[i]['price3']);
            li3_a_s.attr(mainInfo_data[i]['marketprice3']);
            li3_a_span.appendTo(li3_a);
            li3_a_s.appendTo(li3_a);

            var li3_button = $('<button></button>');
            var li3_button_span = $('<span>+</span>');
            li3_button_span.appendTo(li3_button);

            li3_a.appendTo(ul_li3);
            li3_button.appendTo(ul_li3);
            ul_li3.appendTo(main_ul);

            main_ul.appendTo(main_section);
            main_section.appendTo(mainInfo_container);
        }


    })

}









