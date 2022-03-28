$(function(){
    $.ajax({
        url:'/contentName',
        methed:'get',
        success:(data)=>{
         var  contentName =  data.split('---')
        
         var dl = $('.list dl')
         contentName.forEach((element,index) => {
             if(index===0){
                 console.log(element);
                $('h1').text(element)
             }else{
                var dt = $('<dt index='+index+'>'+element+'</dt>')
                dt.on('click',()=>{
                    localStorage.setItem('chapter',''+index)
                    location.href = '.././index.html'
                })
                dl.append(dt)
             }

         });
        },
        error:(err)=>{
            alert(err)
        }
    })
})