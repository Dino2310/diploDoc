$('#rec749301459').css({ 'padding-bottom': '0' })

$('.t754__col').children().css({'width': '20vh'})



$('#rec749319188').css({'position':'static'})
$('.t754__parent').css(
    {
        'display': 'flex',
        'width': '80%',
        'overflow-x': 'auto',

    }
)



setInterval(()=>{  // проверяет формированность страницы категории,  чтобы запустить формирование полей зарпосов
    if($('.js-store-parts-switcher').length){
        init}
},100)



function init() { // инициализирует при запуске создание и наопленение страницы категории в питоне приложения shop запускает пориложение ajax_ansvwer
    let list = $('.t951__sidebar-wrapper').children()
    $.ajax({
        url: '/a',
        type: "GET",
        data: {},

        success: function (data) {
            list.eq(0).html(data['content']['res'])
            $('#cat_prod').html(data['content']['prod'])
            $('.t-store__filter__search-and-sort').html(data['content']['search'])
<<<<<<< HEAD
            list.eq(1).html("")
            if (!$('.js-store-parts-switcher')){
                s()}
                
                else{
                    list.eq(0).html(data['content']['res'])
                    $('#cat_prod').html(data['content']['prod'])
                    $('.t-store__filter__search-and-sort').html(data['content']['search'])
                    list.eq(1).html("")
                }
                
=======
            list.eq(1).html("")           
>>>>>>> edd4b94a37b2f4b995f59607b7c8e39cf043fcdf
        },
        error: function (s) {
            console.log('err');
        }
    })
    
 
    $('.js-store-filters-prodsnumber').html("")

}



function prod(id_prod){ // формирует модальнео окно товара в питоне приложения shop вызывает ф-ию prod
    $.ajax({
        url:'/prod',
        type: 'GET',
        data : {'id': id_prod},

        success: function(data){
            close_display()
            $('#product_card').html(data['content']['res'])
            $('.t-popup__close-wrapper').click(close_display)
            $('.btn_bsk').click(select)
            $('.t706__carticon-counter').html(data['content']['prod'])
        },
    error: function (s) {
        console.log('err');
    }
    })

}




function reloadcat(search, interface, sort, price_max, price_min, type_dev) {// обработка и применения фильтров на старнице категории в питоне вызывает ф-ию ajax_ansvwer приложения shop
    let cat = $('.t951__sidebar-wrapper').children()
    $.ajax({
        url: '/a',
        type: "GET",
        data: { "min": price_min,
             'max': price_max,
             'type_dev' : type_dev,
             'sort' : sort ,
             'interface' : interface,
             'search' : search },

        success: function (data) {
            $('#cat_prod').html(data['content']['prod'])
            cat.eq(1).html("")
            
        },
        error: function (s) {
            console.log('err');
        }
    })
}

function close_display() { // работа с модлальным окном товара на страницах индекс и категории
    $('.t456__positionfixed').toggleClass('btn_bsk')
    $('.t951__sidebar').toggleClass('btn_bsk')
    $('#product_card').toggleClass('btn_bsk')
    $('#product_card').toggleClass('dpl')
    $('#product_card').html("")
}



function select(){  //считывает все фильтры страницы категории и отправляет в аякс для применения данных
    let interface = []
    let price_max = $(`input[name= "max"]`).val()
    let price_min = $(`input[name= 'min']`).val()
    let sort = $('#sort').val()
    let type_dev = $('.active').attr('name')
    for (let i of document.querySelectorAll('.t-checkbox')){
        if (i.checked){interface.push(i.getAttribute('name'))}
    }
    let search = $('input[name="query"]').val()
    interface = interface? interface.join(','):[]
    reloadcat(search, interface, sort, price_max, price_min, type_dev)

} 

function filter_price(val, type = 0) { // менят значение дипазона цены в фильтре старинцы катеогрии в зависимости от положения ползунка
    if (type){
        $(`input[name="price:${val}"]`).val($(`input[name=${val}]`).val())}
    else{
        $(`input[name=${val}]`).val($(`input[name="price:${val}"]`).val())
    }
}







init()

function cat(f) { //Это функция прилетет из браузера  страница category при выборе все, кнопка, контроллер, реле
    $('.t951__sidebar-wrapper').children().children().removeClass('active')
    $('.' + f).addClass('active')
    $('.js-store-filters-prodsnumber').html(f)
    $('.js-store-filters-prodsnumber').html("столько-то")
    select()
}



function cart(prod, name ){// функция обработки корзины ( кнопки в корзину на страницах категоии и старотовой) ф-ия в питоне count_prod
    $.ajax({
        url: '/count',
        type: "GET",
        data: { "fn": "fn",
             'id': prod,
             'user' : name,
            'score':$(`.count${prod}`).val() },

        success: function (data) {
            $(`#btn${prod}`).children().each(
                function(){
                    $(this).toggleClass('btn_bsk')
                }
            )
            $(`.counts${prod}:not(.btn_bsk)`).html(1)
            let score = data['content']['sum']
            if (!score){
                $('.t706__carticon-imgwrap').toggleClass('btn_bsk')
            }
            else{
                $('.t706__carticon-imgwrap').removeClass('btn_bsk')
                $('.t706__carticon-counter').html(score)
            }
            
        },
        error: function (s) {
            console.log('err');
        }
    })
}


function bascet(fn, prod, user){/* функция обработки корзины ( кнопки в корзину на страницах категоии и старотовой) ф-ия 
    в питоне count_prod в отличае от предыдущей ф-ункции работает уже с кнопками сложить  и вычесть*/
    $.ajax({                    
        url: '/count',
        type: "GET",
        data: { "fn": fn,
             'id': prod,
             'user' : user,
            'score':$(`#count${prod}`).val() },

        success: function (data) {
            let score = data['content']['sum']
            if (!score){
                $('.t706__carticon-imgwrap').toggleClass('btn_bsk')
            }
            else{
                $('.t706__carticon-imgwrap').removeClass('btn_bsk')
                $('.t706__carticon-counter').html(score)
            }
            let count = data['content']['count'] 

            if(count){
                $(`.counts${prod}:not(.btn_bsk)`).html(count)
            }
            else{                
                $(`#btn${prod}`).children().each(
                    function(){
                        $(this).toggleClass('btn_bsk')
                }
            )

            }
            
        },
        error: function (s) {
            console.log('err');
        }
    })
}



setTimeout(()=>{ // инициализация фистров на старице категории
        $('#sort').on('change', select)
        $('input[name= "min"]').on('change', select)
        $('input[name= "max"]').on('change', select)
        $('input[name= "price:min"]').on('change', select)
        $('input[name= "price:max"]').on('change', select)
        $('#interface').on('change', select)
        $('input[name="query"]').on('change',select)
    }, 1000)















    // ---------------------------------------------------------------------------------------------------//
window.isMobile = !1;
if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
    window.isMobile = !0
}
window.browserLang = (window.navigator.userLanguage || window.navigator.language).toUpperCase().slice(0, 2);
window.tildaBrowserLang = window.browserLang;
function t_throttle(fn, threshhold, scope) {
    var last;
    var deferTimer;
    threshhold || (threshhold = 250);
    return function() {
        var context = scope || this;
        var now = +new Date();
        var args = arguments;
        if (last && now < last + threshhold) {
            clearTimeout(deferTimer);
            deferTimer = setTimeout(function() {
                last = now;
                fn.apply(context, args)
            }, threshhold)
        } else {
            last = now;
            fn.apply(context, args)
        }
    }
}
function t456_setListMagin(recid, imglogo) {
    var rec = document.getElementById('rec' + recid);
    if (!rec || window.innerWidth <= 980)
        return;
    var menu = rec.querySelector('.t456');
    var leftSide = menu ? menu.querySelector('.t456__leftwrapper') : null;
    var list = menu ? menu.querySelector('.t456__list') : null;
    var leftSideWidth = leftSide ? leftSide.offsetWidth : 0;
    if (list)
        list.style.marginRight = (imglogo ? leftSideWidth : leftSideWidth + 30) + 'px'
}
function t706_onSuccessCallback() {
    var products = document.querySelector('.t706__cartwin-products');
    var cartBottom = document.querySelector('.t706__cartwin-bottom');
    var cartForm = document.querySelector('.t706 .t-form__inputsbox');
    if (products)
        t706_slideUp(products, 10);
    if (cartBottom)
        t706_slideUp(cartBottom, 10);
    if (cartForm)
        t706_slideUp(cartForm, 700);
    try {
        tcart__unlockScroll()
    } catch (error) {}
}
function t706_slideUp(target, duration) {
    if (!target)
        return;
    if (!duration && duration !== 0)
        duration = 500;
    target.style.transitionProperty = 'height, margin, padding';
    target.style.transitionDuration = duration + 'ms';
    target.style.boxSizing = 'border-box';
    target.style.height = target.offsetHeight + 'px';
    target.style.overflow = 'hidden';
    target.style.height = '0';
    target.style.paddingTop = '0';
    target.style.paddingBottom = '0';
    target.style.marginTop = '0';
    target.style.marginBottom = '0';
    setTimeout(function() {
        target.style.display = 'none';
        target.style.height = '';
        target.style.paddingTop = '';
        target.style.paddingBottom = '';
        target.style.marginTop = '';
        target.style.marginBottom = '';
        target.style.overflow = '';
        target.style.transitionDuration = '';
        target.style.transitionProperty = ''
    }, duration)
}
function t670_init(recid) {
    t670_imageHeight(recid);
    t670_show(recid);
    t670_hide(recid)
}
function t670_show(recid) {
    var rec = document.getElementById('rec' + recid);
    if (!rec)
        return;
    var playBtns = rec.querySelectorAll('.t670__play');
    Array.prototype.forEach.call(playBtns, function(play) {
        play.addEventListener('click', function() {
            var videoType = play.getAttribute('data-slider-video-type');
            var url;
            var nextEl;
            var prevEl;
            var iframe;
            var video;
            var source;
            switch (videoType) {
            case 'youtube':
                url = play.getAttribute('data-slider-video-url');
                nextEl = play.nextElementSibling;
                prevEl = play.previousElementSibling.previousElementSibling;
                if (nextEl) {
                    iframe = document.createElement('iframe');
                    iframe.classList.add('t670__iframe');
                    iframe.width = '100%';
                    iframe.height = '100%';
                    iframe.src = 'https://www.youtube.com/embed/' + url + '?autoplay=1&enablejsapi=1';
                    iframe.frameBorder = '0';
                    iframe.setAttribute('webkitallowfullscreen', '');
                    iframe.setAttribute('mozallowfullscreen', '');
                    iframe.setAttribute('allowfullscreen', '');
                    iframe.setAttribute('allow', 'autoplay');
                    nextEl.innerHTML = '';
                    nextEl.insertAdjacentElement('beforeend', iframe)
                }
                if (prevEl && prevEl.classList.contains('t-bgimg'))
                    prevEl.style.opacity = '0';
                break;
            case 'vimeo':
                url = play.getAttribute('data-slider-video-url');
                nextEl = play.nextElementSibling;
                prevEl = play.previousElementSibling.previousElementSibling;
                var idMatch = /vimeo[^/]*\/(\d+)\/?(\w*)\/?/i.exec(url);
                var id = idMatch ? idMatch[1] : null;
                var hash = idMatch ? '?h=' + idMatch[2] : null;
                if (nextEl) {
                    iframe = document.createElement('iframe');
                    iframe.classList.add('t670__iframe');
                    iframe.width = '100%';
                    iframe.height = '100%';
                    iframe.src = 'https://player.vimeo.com/video/' + id + hash + '&amp;api=1';
                    iframe.frameBorder = '0';
                    iframe.setAttribute('allowfullscreen', '');
                    iframe.setAttribute('allow', 'autoplay; fullscreen');
                    nextEl.innerHTML = '';
                    nextEl.insertAdjacentElement('beforeend', iframe)
                }
                if (prevEl && prevEl.classList.contains('t-bgimg'))
                    prevEl.style.opacity = '0';
                break;
            case 'mp4':
                url = play.getAttribute('data-slider-video-url');
                nextEl = play.nextElementSibling;
                prevEl = play.previousElementSibling.previousElementSibling;
                if (nextEl) {
                    video = document.createElement('video');
                    source = document.createElement('source');
                    video.insertAdjacentElement('beforeend', source);
                    video.classList.add('t670__video');
                    video.controls = !0;
                    source.src = url;
                    nextEl.innerHTML = '';
                    nextEl.insertAdjacentElement('beforeend', video);
                    video = nextEl.querySelector('video');
                    if (video)
                        video.play()
                }
                if (prevEl && prevEl.classList.contains('t-bgimg'))
                    prevEl.style.opacity = '0';
                break
            }
            if (nextEl)
                nextEl.style.zIndex = '3'
        })
    })
}
function t670_hide(recid) {
    var rec = document.getElementById('rec' + recid);
    if (!rec)
        return;
    var elBody = rec.querySelector('.t670__frame');
    rec.addEventListener('updateSlider', function() {
        if (elBody)
            elBody.innerHTML = '';
        if (elBody)
            elBody.style.zIndex = ''
    })
}
function t670_imageHeight(recid) {
    var rec = document.getElementById('rec' + recid);
    if (!rec)
        return;
    var images = rec.querySelectorAll('.t670__separator');
    Array.prototype.forEach.call(images, function(img) {
        var width = img.getAttribute('data-slider-image-width') || 0;
        var height = img.getAttribute('data-slider-image-height') || 0;
        var ratio = height / width;
        var padding = ratio * 100;
        img.style.paddingBottom = padding + '%'
    })
}
var t754_POPUP_SHOWED_EVENT_NAME = 'catalog:popupShowed';
var t754_POPUP_CLOSED_EVENT_NAME = 'catalog:popupClosed';
function t754__init(recid) {
    setTimeout(function() {
        t_onFuncLoad('t_prod__init', function() {
            t_prod__init(recid)
        });
        t754__hoverZoom_init(recid);
        t754_initPopup(recid);
        t754__updateLazyLoad(recid);
        t754__alignButtons_init(recid);
        t_onFuncLoad('t_store_addProductQuantityEvents', function() {
            t754_initProductQuantity(recid)
        });
        var event = document.createEvent('HTMLEvents');
        event.initEvent('twishlist_addbtn', !0, !1);
        document.body.dispatchEvent(event)
    }, 500)
}
function t754_initProductQuantity(recid) {
    var rec = document.getElementById('rec' + recid);
    if (!rec)
        return;
    var productList = rec.querySelectorAll('.t754__col, .t754__product-full');
    Array.prototype.forEach.call(productList, function(product) {
        t_store_addProductQuantityEvents(product)
    })
}
function t754__showMore(recid) {
    var rec = document.getElementById('rec' + recid);
    if (!rec)
        return;
    var wrapperBlock = rec.querySelector('.t754');
    if (!wrapperBlock)
        return;
    var productColumns = wrapperBlock.querySelectorAll('.t754__col');
    var cardsSize = productColumns.length;
    var cardsCount = parseInt(wrapperBlock.getAttribute('data-show-count'), 10);
    if (isNaN(cardsCount) || cardsCount < 1)
        return;
    Array.prototype.forEach.call(productColumns, function(column) {
        column.style.display = 'none'
    });
    for (var i = 0; i < cardsCount; i++) {
        if (productColumns[i]) {
            productColumns[i].style.display = 'inline-block'
        }
    }
    var showMoreButton = wrapperBlock.querySelector('.t754__showmore');
    if (!showMoreButton)
        return;
    if (showMoreButton.querySelector('td').textContent === '') {
        showMoreButton.querySelector('td').textContent = t754__dict()
    }
    if (cardsCount < productColumns.length) {
        showMoreButton.style.display = 'inline-block'
    }
    t754__showSeparator(wrapperBlock, cardsCount);
    showMoreButton.addEventListener('click', function() {
        var currentColumns = wrapperBlock.querySelectorAll('.t754__col');
        var currentColumnsShowed = 0;
        Array.prototype.forEach.call(currentColumns, function(column) {
            if (column.style.display === 'inline-block') {
                ++currentColumnsShowed
            }
        });
        for (var i = 0; i < cardsCount + currentColumnsShowed; i++) {
            if (currentColumns[i]) {
                currentColumns[i].style.display = 'inline-block'
            }
        }
        if (cardsCount + currentColumnsShowed >= cardsSize) {
            showMoreButton.style.display = 'none'
        }
        if (!document.querySelector('.t-records').getAttribute('data-tilda-mode')) {
            if (window.lazy === 'y' || document.getElementById('allrecords').getAttribute('data-tilda-lazy') === 'yes') {
                t_onFuncLoad('t_lazyload_update', function() {
                    t_lazyload_update()
                })
            }
        }
        t754__showSeparator(wrapperBlock, cardsCount + currentColumnsShowed);
        if (wrapperBlock.querySelector('[data-buttons-v-align]')) {
            t754__alignButtons(recid)
        }
    })
}
function t754__showSeparator(rec, cardsCount) {
    if (window.jQuery && rec instanceof jQuery) {
        rec = rec.get(0)
    }
    var allSeparators = rec.querySelectorAll('.t754__separator_number');
    Array.prototype.forEach.call(allSeparators, function(separator) {
        separator.classList.add('t754__separator_hide');
        if (separator.getAttribute('data-product-separator-number') <= cardsCount) {
            separator.classList.remove('t754__separator_hide')
        }
    })
}
function t754__dict() {
    var dictionary = {
        EN: 'Load more',
        RU: 'Загрузить ещё',
        FR: 'Charger plus',
        DE: 'Mehr laden',
        ES: 'Carga más',
        PT: 'Carregue mais',
        UK: 'Завантажити ще',
        JA: 'もっと読み込む',
        ZH: '裝載更多',
    };
    var language = window.browserLang;
    return dictionary[language] ? dictionary[language] : dictionary.EN
}
function t754__alignButtons_init(recid) {
    var rec = document.getElementById('rec' + recid);
    if (!rec)
        return;
    if (!rec.querySelector('[data-buttons-v-align]')) {
        return
    }
    try {
        t754__alignButtons(recid);
        if (document.querySelector('.t-records').getAttribute('data-tilda-mode') === 'edit') {
            setInterval(function() {
                t754__alignButtons(recid)
            }, 200)
        }
        window.addEventListener('resize', t_throttle(function() {
            if (window.noAdaptive && window.isMobile) {
                return
            }
            t754__alignButtons(recid)
        }, 200));
        var wrapperBlock = rec.querySelector('.t754');
        if (wrapperBlock) {
            wrapperBlock.addEventListener('displayChanged', function() {
                t754__alignButtons(recid)
            })
        }
        if (window.isMobile) {
            window.addEventListener('orientationchange', function() {
                t754__alignButtons(recid)
            })
        }
    } catch (error) {
        console.log('buttons-v-align error: ' + error.message)
    }
}
function t754__alignButtons(recid) {
    var rec = document.getElementById('rec' + recid);
    if (!rec)
        return;
    var wrappers = rec.querySelectorAll('.t754__textwrapper');
    var maxHeight = 0;
    var container = rec.querySelector('.t754__parent');
    if (!container)
        return;
    var itemsInRow = parseInt(container.getAttribute('data-blocks-per-row'), 10);
    if (!itemsInRow) {
        itemsInRow = 3
    }
    var mobileView = window.innerWidth <= 480;
    var tableView = window.innerWidth <= 960 && window.innerWidth > 480;
    var mobileOneRow = window.innerWidth <= 960 && rec.querySelector('.t754__container_mobile-flex');
    var mobileTwoItemsInRow = window.innerWidth <= 480 && rec.querySelector('.t754 .mobile-two-columns');
    if (mobileView) {
        itemsInRow = 1
    }
    if (tableView) {
        itemsInRow = 2
    }
    if (mobileTwoItemsInRow) {
        itemsInRow = 2
    }
    if (mobileOneRow) {
        itemsInRow = 999999
    }
    var count = 1;
    var wrappersInRow = [];
    Array.prototype.forEach.call(wrappers, function(element) {
        element.style.height = 'auto';
        if (itemsInRow === 1) {
            element.style.height = 'auto'
        } else {
            wrappersInRow.push(element);
            if (element.offsetHeight > maxHeight) {
                maxHeight = element.offsetHeight
            }
            Array.prototype.forEach.call(wrappersInRow, function(wrapper) {
                wrapper.style.height = maxHeight + 'px'
            });
            if (count === itemsInRow) {
                count = 0;
                maxHeight = 0;
                wrappersInRow = []
            }
            count++
        }
    })
}
function t754__hoverZoom_init(recid) {
    if (window.isMobile)
        return;
    var rec = document.getElementById('rec' + recid);
    if (!rec)
        return;
    try {
        if (!rec.querySelector('[data-hover-zoom]')) {
            return
        }
        var hoverScript = 'https://static.tildacdn.com/js/tilda-hover-zoom-1.0.min.js';
        if (document.querySelector("script[src^='" + hoverScript + "']")) {
            t_onFuncLoad('t_hoverZoom_init', function() {
                t_hoverZoom_init(recid)
            })
        } else {
            var script = document.createElement('script');
            script.type = 'text/javascript';
            script.src = hoverScript;
            script.onload = function() {
                setTimeout(function() {
                    t_hoverZoom_init(recid)
                }, 500)
            }
            ;
            script.onerror = function(error) {
                console.log('Upload script error: ', error)
            }
            ;
            document.head.appendChild(script)
        }
    } catch (error) {
        console.log('Zoom image init error: ' + error.message)
    }
}
function t754__updateLazyLoad(recid) {
    var scrollContainer = document.querySelector('#rec' + recid + ' .t754__container_mobile-flex');
    var tRecords = document.querySelector('.t-records');
    if (!tRecords)
        return;
    var currentMode = tRecords.getAttribute('data-tilda-mode');
    if (scrollContainer && currentMode !== 'edit' && currentMode !== 'preview') {
        scrollContainer.addEventListener('scroll', t_throttle(function() {
            if (window.lazy === 'y' || document.getElementById('allrecords').getAttribute('data-tilda-lazy') === 'yes') {
                t_onFuncLoad('t_lazyload_update', function() {
                    t_lazyload_update()
                })
            }
        }))
    }
}
function t754_initPopup(recid) {
    var rec = document.getElementById('rec' + recid);
    if (!rec)
        return;
    var popup = rec.querySelector('.t-popup');
    var body = document.body;
    var linksProd = rec.querySelectorAll('[href^="#prodpopup"]');
    Array.prototype.forEach.call(linksProd, function(popupLink) {
        var product = popupLink.closest('.js-product');
        var productLid = product.getAttribute('data-product-lid');
        var productLinks = document.querySelectorAll('.r a[href$="#!/tproduct/' + recid + '-' + productLid + '"]');
        Array.prototype.forEach.call(productLinks, function(productLink) {
            productLink.addEventListener('click', function() {
                if (rec.querySelector('[data-product-lid="' + productLid + '"]')) {
                    var linkToPopup = product.querySelector('[href^="#prodpopup"]');
                    if (linkToPopup) {
                        var event = document.createEvent('HTMLEvents');
                        event.initEvent('click', !0, !1);
                        linkToPopup.dispatchEvent(event)
                    }
                }
            })
        });
        popupLink.addEventListener('click', clickOnceHandler, !1);
        function clickOnceHandler(event) {
            event.preventDefault();
            var product = popupLink.closest('.js-product');
            var productLid = product.getAttribute('data-product-lid');
            t_onFuncLoad('t_sldsInit', function() {
                t_sldsInit(recid + ' #t754__product-' + productLid)
            });
            popupLink.removeEventListener('click', clickOnceHandler, !1)
        }
        popupLink.addEventListener('click', showPopupHandler, !1);
        function showPopupHandler(event) {
            event.preventDefault();
            var isT1002Button = event.target.classList.contains('t1002__addBtn') || event.target.parentNode.classList.contains('t1002__addBtn');
            if (isT1002Button)
                return;
            t754_showPopup(recid);
            var product = popupLink.closest('.js-product');
            var productLid = product.getAttribute('data-product-lid');
            var productFull = popup.querySelector('.js-product[data-product-lid="' + productLid + '"]');
            productFull.style.display = 'block';
            var analitics = popupLink.getAttribute('data-track-popup');
            if (analitics && productFull && window.Tilda) {
                var productName = productFull.querySelector('.js-product-name');
                if (productName) {
                    var virtTitle = productName.textContent;
                    if (!virtTitle) {
                        virtTitle = 'prod' + productLid
                    }
                    Tilda.sendEventToStatistics(analitics, virtTitle)
                }
            }
            var currentUrl = window.location.href;
            if (currentUrl.indexOf('#!/tproduct/') < 0 && currentUrl.indexOf('%23!/tproduct/') < 0 && currentUrl.indexOf('#%21%2Ftproduct%2F') < 0) {
                if (history.replaceState) {
                    window.history.replaceState('', '', window.location.href + '#!/tproduct/' + recid + '-' + productLid)
                }
            }
            t754_updateSlider(recid + ' #t754__product-' + productLid);
            if (window.lazy === 'y' || document.getElementById('allrecords').getAttribute('data-tilda-lazy') === 'yes') {
                t_onFuncLoad('t_lazyload_update', function() {
                    t_lazyload_update()
                })
            }
        }
    });
    if (popup) {
        popup.addEventListener('mousedown', function(event) {
            var windowWidth = window.innerWidth;
            var maxScrollBarWidth = 17;
            var windowWithoutScrollBar = windowWidth - maxScrollBarWidth;
            if (event.clientX > windowWithoutScrollBar) {
                return
            }
            if (event.target === this) {
                t754_closePopup(body, popup)
            }
        });
        var allRecords = document.getElementById('allrecords');
        var currentMode = allRecords.getAttribute('data-tilda-mode');
        var isPublishedPage = currentMode !== 'edit' && currentMode !== 'preview';
        if (isPublishedPage && (window.lazy === 'y' || allRecords.getAttribute('data-tilda-lazy') === 'yes')) {
            popup.addEventListener('scroll', function(event) {
                t_onFuncLoad('t_lazyload_update', function() {
                    t_lazyload_update()
                })
            })
        }
    }
    var closeButtons = rec.querySelectorAll('.t-popup__close, .t754__close-text');
    Array.prototype.forEach.call(closeButtons, function(button) {
        button.addEventListener('click', function() {
            t754_closePopup(body, popup)
        })
    });
    document.addEventListener('keydown', function(event) {
        var isGalleryShowedOldLib = document.body.classList.contains('t-zoomer__show');
        if (isGalleryShowedOldLib)
            return;
        var isGalleryShowedNewLib = document.body.classList.contains('t-zoomer__active');
        if (isGalleryShowedNewLib)
            return;
        var isPopupShowed = document.body.classList.contains('t-body_popupshowed');
        if (!isPopupShowed)
            return;
        if (popup && popup.classList.contains('t-popup_show')) {
            if (event.keyCode === 27) {
                t754_closePopup(body, popup)
            }
        }
    });
    if (!document.getElementById('record' + recid)) {
        t754_checkUrl(recid)
    }
    if (popup && popup.hasAttribute('data-fixed-button')) {
        t754_fixedPopupButton(recid)
    }
}
function t754_showPopup(recid) {
    var rec = document.getElementById('rec' + recid);
    if (!rec)
        return;
    if (rec.classList.contains('r_hidden')) {
        rec.classList.remove('r_hidden')
        if (rec.classList.contains('r_anim')) {
            rec.classList.remove('r_anim')
        }
    }
    var popup = rec.querySelector('.t-popup');
    var fullProducts = popup.querySelectorAll('.t754__product-full');
    Array.prototype.forEach.call(fullProducts, function(product) {
        product.style.display = 'none'
    });
    popup.style.display = 'block';
    setTimeout(function() {
        popup.querySelector('.t-popup__container').classList.add('t-popup__container-animated');
        popup.classList.add('t-popup_show');
        t_triggerEvent(popup, t754_POPUP_SHOWED_EVENT_NAME)
    }, 50);
    setTimeout(function() {
        if (window.lazy === 'y' || document.getElementById('allrecords').getAttribute('data-tilda-lazy') === 'yes') {
            t_onFuncLoad('t_lazyload_update', function() {
                t_lazyload_update()
            })
        }
    }, 300);
    var body = document.body;
    if (typeof t_triggerEvent === 'function')
        t_triggerEvent(document.body, 'popupShowed');
    body.classList.add('t-body_popupshowed');
    var event = document.createEvent('HTMLEvents');
    event.initEvent('twishlist_addbtn', !0, !1);
    body.dispatchEvent(event)
}
function t754_closePopup(body, popup) {
    var fullProducts = popup.querySelectorAll('.t754__product-full');
    if (typeof t_triggerEvent === 'function')
        t_triggerEvent(document.body, 'popupHidden');
    body.classList.remove('t-body_popupshowed');
    popup.classList.remove('t-popup_show');
    var currentUrl = window.location.href;
    var indexToRemove = currentUrl.indexOf('#!/tproduct/');
    var event = document.createEvent('HTMLEvents');
    event.initEvent('twishlist_addbtn', !0, !1);
    body.dispatchEvent(event);
    if (/iPhone|iPad|iPod/i.test(navigator.userAgent) && indexToRemove < 0) {
        indexToRemove = currentUrl.indexOf('%23!/tproduct/');
        if (indexToRemove < 0) {
            indexToRemove = currentUrl.indexOf('#%21%2Ftproduct%2F')
        }
    }
    currentUrl = currentUrl.substring(0, indexToRemove);
    setTimeout(function() {
        popup.scrollTop = 0;
        popup.style.display = 'none';
        Array.prototype.forEach.call(fullProducts, function(product) {
            product.style.display = 'none'
        });
        if (history.replaceState) {
            window.history.replaceState('', '', currentUrl)
        }
    }, 300);
    t_triggerEvent(popup, t754_POPUP_CLOSED_EVENT_NAME)
}
function t754_updateSlider(recid) {
    var rec = document.querySelector('#rec' + recid);
    if (!rec)
        return;
    t_onFuncLoad('t_slds_SliderWidth', function() {
        t_slds_SliderWidth(recid)
    });
    var slider = rec.querySelector('.t-slds__container');
    var paddingLeft = parseInt(slider.style.paddingLeft) || 0;
    var paddingRight = parseInt(slider.style.paddingRight) || 0;
    var sliderWrapper = rec.querySelector('.t-slds__items-wrapper');
    var sliderWidth = slider.clientWidth - (paddingLeft + paddingRight);
    var pos = parseFloat(sliderWrapper.getAttribute('data-slider-pos'));
    sliderWrapper.style.transform = 'translate3d(-' + sliderWidth * pos + 'px, 0, 0)';
    t_onFuncLoad('t_slds_UpdateSliderHeight', function() {
        t_slds_UpdateSliderHeight(recid)
    });
    t_onFuncLoad('t_slds_UpdateSliderArrowsHeight', function() {
        t_slds_UpdateSliderArrowsHeight(recid)
    })
}
function t754_checkUrl(recid) {
    var currentUrl = window.location.href;
    var tprodIndex = (currentUrl.indexOf('#!/tproduct/') + 1 || currentUrl.indexOf('%23!/tproduct/') + 1 || currentUrl.indexOf('#%21%2Ftproduct%2F') + 1 || currentUrl.indexOf('#!%2Ftproduct%2F') + 1 || currentUrl.indexOf('%23%21%2Ftproduct%2F') + 1) - 1;
    if (tprodIndex !== -1) {
        var currentUrl = currentUrl.substring(tprodIndex, currentUrl.length);
        var curProdLid = currentUrl.substring(currentUrl.indexOf('-') + 1, currentUrl.length);
        if (curProdLid) {
            var curProdLidMatch = curProdLid.match(/([0-9]+)/g);
            if (curProdLidMatch) {
                curProdLid = curProdLidMatch[0]
            }
        }
        if (currentUrl.indexOf(recid) === -1)
            return;
        var rec = document.getElementById('rec' + recid);
        if (!rec)
            return;
        if (currentUrl.indexOf(recid) !== 0 && rec.querySelector('[data-product-lid="' + curProdLid + '"]')) {
            var currentLink = rec.querySelector('[data-product-lid="' + curProdLid + '"] [href^="#prodpopup"]');
            var event = document.createEvent('HTMLEvents');
            event.initEvent('click', !0, !1);
            if (currentLink) {
                currentLink.dispatchEvent(event)
            }
        }
    }
}
function t754_fixedPopupButton(recId) {
    var rec = document.getElementById('rec' + recId);
    if (!rec)
        return;
    var MOBILE_MAX_WIDTH = 560;
    var popup = rec.querySelector('.t-popup');
    var popupContainer = popup.querySelector('.t-popup__container');
    var btnWrappers = rec.querySelectorAll('.t754__btn-wrapper');
    Array.prototype.forEach.call(btnWrappers, function(el) {
        el.classList.add('t754__btn-wrapper-fixed')
    });
    function addStyle() {
        popupContainer.style.paddingBottom = '90px';
        popupContainer.style.cssText += ';transform:none !important;'
    }
    function resetStyle() {
        popupContainer.style.paddingBottom = '';
        popupContainer.style.transform = ''
    }
    function handleResize() {
        if (window.innerWidth > MOBILE_MAX_WIDTH) {
            resetStyle();
            return
        }
        addStyle()
    }
    if (window.isMobile) {
        window.addEventListener("orientationchange", handleResize)
    }
    popup.addEventListener(t754_POPUP_SHOWED_EVENT_NAME, function() {
        setTimeout(function() {
            handleResize()
        }, 0)
    });
    popup.addEventListener(t754_POPUP_CLOSED_EVENT_NAME, function() {
        resetStyle()
    });
    window.addEventListener('resize', handleResize)
}
if (!Element.prototype.matches) {
    Element.prototype.matches = Element.prototype.matchesSelector || Element.prototype.msMatchesSelector || Element.prototype.mozMatchesSelector || Element.prototype.webkitMatchesSelector || Element.prototype.oMatchesSelector
}
if (!Element.prototype.closest) {
    Element.prototype.closest = function(s) {
        var el = this;
        while (el && el.nodeType === 1) {
            if (Element.prototype.matches.call(el, s)) {
                return el
            }
            el = el.parentElement || el.parentNode
        }
        return null
    }
}


window.isMobile = !1;
if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
    window.isMobile = !0
}
function t_throttle(fn, threshhold, scope) {
    var last;
    var deferTimer;
    threshhold || (threshhold = 250);
    return function() {
        var context = scope || this;
        var now = +new Date();
        var args = arguments;
        if (last && now < last + threshhold) {
            clearTimeout(deferTimer);
            deferTimer = setTimeout(function() {
                last = now;
                fn.apply(context, args)
            }, threshhold)
        } else {
            last = now;
            fn.apply(context, args)
        }
    }
}
function t228__init(recid) {
    var rec = document.getElementById('rec' + recid);
    if (!rec)
        return;
    var menuBlock = rec.querySelector('.t228');
    var mobileMenu = rec.querySelector('.t228__mobile');
    var menuSubLinkItems = rec.querySelectorAll('.t-menusub__link-item');
    var rightBtn = rec.querySelector('.t228__right_buttons_but .t-btn');
    var mobileMenuPosition = mobileMenu ? mobileMenu.style.position || window.getComputedStyle(mobileMenu).position : '';
    var mobileMenuDisplay = mobileMenu ? mobileMenu.style.display || window.getComputedStyle(mobileMenu).display : '';
    var isFixedMobileMenu = mobileMenuPosition === 'fixed' && mobileMenuDisplay === 'block';
    var overflowEvent = document.createEvent('Event');
    var noOverflowEvent = document.createEvent('Event');
    overflowEvent.initEvent('t228_overflow', !0, !0);
    noOverflowEvent.initEvent('t228_nooverflow', !0, !0);
    if (menuBlock) {
        menuBlock.addEventListener('t228_overflow', function() {
            t228_checkOverflow(recid)
        });
        menuBlock.addEventListener('t228_nooverflow', function() {
            t228_checkNoOverflow(recid)
        })
    }
    rec.addEventListener('click', function(e) {
        var targetLink = e.target.closest('.t-menusub__target-link');
        if (targetLink && window.isMobile && window.innerWidth <= 980) {
            if (targetLink.classList.contains('t-menusub__target-link_active')) {
                if (menuBlock)
                    menuBlock.dispatchEvent(overflowEvent)
            } else {
                if (menuBlock)
                    menuBlock.dispatchEvent(noOverflowEvent)
            }
        }
        var currentLink = e.target.closest('.t-menu__link-item:not(.tooltipstered):not(.t-menusub__target-link):not(.t794__tm-link):not(.t966__tm-link):not(.t978__tm-link):not(.t978__menu-link)');
        if (currentLink && mobileMenu && isFixedMobileMenu)
            mobileMenu.click()
    });
    Array.prototype.forEach.call(menuSubLinkItems, function(linkItem) {
        linkItem.addEventListener('click', function() {
            if (mobileMenu && isFixedMobileMenu)
                mobileMenu.click()
        })
    });
    if (rightBtn) {
        rightBtn.addEventListener('click', function() {
            if (mobileMenu && isFixedMobileMenu)
                mobileMenu.click()
        })
    }
    if (menuBlock) {
        menuBlock.addEventListener('showME601a', function() {
            var menuLinks = rec.querySelectorAll('.t966__menu-link');
            Array.prototype.forEach.call(menuLinks, function(menuLink) {
                menuLink.addEventListener('click', function() {
                    if (mobileMenu && isFixedMobileMenu)
                        mobileMenu.click()
                })
            })
        })
    }
}
function t228_checkOverflow(recid) {
    var rec = document.getElementById('rec' + recid);
    var menu = rec ? rec.querySelector('.t228') : null;
    if (!menu)
        return;
    var mobileContainer = document.querySelector('.t228__mobile_container');
    var mobileContainerHeight = t228_getFullHeight(mobileContainer);
    var windowHeight = document.documentElement.clientHeight;
    var menuPosition = menu.style.position || window.getComputedStyle(menu).position;
    if (menuPosition === 'fixed') {
        menu.classList.add('t228__overflow');
        menu.style.setProperty('height', (windowHeight - mobileContainerHeight) + 'px', 'important')
    }
}
function t228_checkNoOverflow(recid) {
    var rec = document.getElementById('rec' + recid);
    if (!rec)
        return !1;
    var menu = rec.querySelector('.t228');
    var menuPosition = menu ? menu.style.position || window.getComputedStyle(menu).position : '';
    if (menuPosition === 'fixed') {
        if (menu)
            menu.classList.remove('t228__overflow');
        if (menu)
            menu.style.height = 'auto'
    }
}
function t228_setWidth(recid) {
    var rec = document.getElementById('rec' + recid);
    if (!rec)
        return;
    var menuCenterSideList = rec.querySelectorAll('.t228__centerside');
    Array.prototype.forEach.call(menuCenterSideList, function(menuCenterSide) {
        menuCenterSide.classList.remove('t228__centerside_hidden')
    });
    if (window.innerWidth <= 980)
        return;
    var menuBlocks = rec.querySelectorAll('.t228');
    Array.prototype.forEach.call(menuBlocks, function(menu) {
        var maxWidth;
        var centerWidth = 0;
        var paddingWidth = 40;
        var leftSide = menu.querySelector('.t228__leftside');
        var rightSide = menu.querySelector('.t228__rightside');
        var menuList = menu.querySelector('.t228__list');
        var mainContainer = menu.querySelector('.t228__maincontainer');
        var leftContainer = menu.querySelector('.t228__leftcontainer');
        var rightContainer = menu.querySelector('.t228__rightcontainer');
        var centerContainer = menu.querySelector('.t228__centercontainer');
        var centerContainerLi = centerContainer ? centerContainer.querySelectorAll('li') : [];
        var leftContainerWidth = t228_getFullWidth(leftContainer);
        var rightContainerWidth = t228_getFullWidth(rightContainer);
        var mainContainerWidth = mainContainer ? mainContainer.offsetWidth : 0;
        var dataAlign = menu.getAttribute('data-menu-items-align');
        var isDataAlignCenter = dataAlign === 'center' || dataAlign === null;
        maxWidth = leftContainerWidth >= rightContainerWidth ? leftContainerWidth : rightContainerWidth;
        maxWidth = Math.ceil(maxWidth);
        Array.prototype.forEach.call(centerContainerLi, function(li) {
            centerWidth += t228_getFullWidth(li)
        });
        if (mainContainerWidth - (maxWidth * 2 + paddingWidth * 2) > centerWidth + 20) {
            if (isDataAlignCenter) {
                if (leftSide)
                    leftSide.style.minWidth = maxWidth + 'px';
                if (rightSide)
                    rightSide.style.minWidth = maxWidth + 'px'
            }
        } else {
            if (leftSide)
                leftSide.style.minWidth = maxWidth + '';
            if (rightSide)
                rightSide.style.minWidth = maxWidth + ''
        }
        if (menuList && menuList.classList.contains('t228__list_hidden'))
            menuList.classList.remove('t228__list_hidden')
    })
}
function t228_getFullWidth(el) {
    if (!el)
        return 0;
    var marginLeft = el.style.marginLeft || window.getComputedStyle(el).marginLeft;
    var marginRight = el.style.marginRight || window.getComputedStyle(el).marginRight;
    marginLeft = parseInt(marginLeft, 10) || 0;
    marginRight = parseInt(marginRight, 10) || 0;
    return el.offsetWidth + marginLeft + marginRight
}
function t228_getFullHeight(el) {
    if (!el)
        return 0;
    var marginTop = el.style.marginTop || window.getComputedStyle(el).marginTop;
    var marginBottom = el.style.marginBottom || window.getComputedStyle(el).marginBottom;
    marginTop = parseInt(marginTop, 10) || 0;
    marginBottom = parseInt(marginBottom, 10) || 0;
    return el.offsetHeight + marginTop + marginBottom
}



//--------------------------------//