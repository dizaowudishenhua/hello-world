$(function () {
    var numberType = typeof 1
    
    if (typeof parseInt(localStorage.getItem('chapter'))!=numberType){
        localStorage.getItem('chapter','1')
    }
    
    var index = '1'


    function waitStar(){
        $('#waitting').css('display','block')
    }
    function waitEnd(){
        $('#waitting').css('display','none')
    }
    function getBook(query) {
        waitStar()
        $.ajax({
            type: 'get',
            url: "/book",
            data: query,
            success: function (result) {
                const str = JSON.parse(result)
                $('.bookname h1').text(str.title)
                $('#content p').remove()
                str.content.forEach((element) => {

                    $('#content .bottem1').before($('<p>&emsp;&emsp;' + element.content + '</p>'))

                });
                if (parseFloat(str.chapter) >= 1) {
                    localStorage.setItem('chapter', str.chapter)
                }
                $(".goTop-hook").click()
                waitEnd()
            },
            error:function(err){
                waitEnd()
                alert('发生错误')
            }
        })
    }

    window.onload=function () {
        if (localStorage.getItem('chapter')) {
            index = localStorage.getItem('chapter')
        }
        getBook({
            'chapter': index,
            'method': 'primary'
        })
    };
    $('.bottem1 a:nth-child(1)').on('click', function () {
        if (localStorage.getItem('chapter')) {
            index = localStorage.getItem('chapter')
        }
        getBook({
            'chapter': index,
            'method': 'back'
        })

    })
    $('.bottem1 a:nth-child(3)').on('click', function () {
        if (localStorage.getItem('chapter')) {
            index = localStorage.getItem('chapter')
        }
        getBook({
            'chapter': index,
            'method': 'forward'
        })

    })


    $('.search button').on('click',()=>{
      var searchBookName =  $('.search input').val()
        waitStar()
        $.ajax({
            method:'get',
            url:'/content?bookname='+searchBookName,
            success:(result)=>{
                localStorage.setItem('chapter','1')
                
                alert(JSON.parse(result))
                location.reload()
            },
            error:(err)=>{
                
                alert('发生错误')
                location.reload()
                
            }
        })
    })


    $('.skip button').on('click',()=>{
          var skipChapterIndex = $('.skip input').val()
          localStorage.setItem('chapter',skipChapterIndex)
          location.reload()

    })

})


// 返回顶部
// $(window).scroll(function () {
//     if ($(window).scrollTop() >= 100) {
//         $(".goTop-hook").fadeIn(300)
//     } else {
//         $(".goTop-hook").fadeOut(300)
//     }
// })

$(".goTop-hook").on("click", function () {
    $("html").animate({
        scrollTop: 0
    }, 300)
})



