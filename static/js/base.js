console.log('hello kamlesh')
var user_status=false
var cart_list=[]
if(localStorage.getItem("cart_list")){
    cart_list=JSON.parse(localStorage.getItem("cart_list"))
}
else{
    localStorage.setItem("cart_list", JSON.stringify(cart_list));
    cart_list=JSON.parse(localStorage.getItem("cart_list"))
}

$(document).ready(function(){
    $.ajax({
        url: `/status/`,
        type: 'GET',
        success: function (response) {
            user_status=response['user_status']
            if(response['cart_count']){
                $('#cart_count').text(response['cart_count'])
            }
            else{
                $('#cart_count').text(cart_list.length)
            }
        }
    })
})

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}



function a(id){
    console.log(user_status)
    if(user_status){
        $.ajax({
            url: `/cart/add_to_cart/`+id+'/',
            type: 'GET',
            success: function (response) {
                if(response['success']){
                    $('#cart_count').text(response['cart_count'])
                }
            }
        })
    }
    else{
        if(! cart_list.includes(id)){
            cart_list.push(id)
        }
        localStorage.setItem("cart_list", JSON.stringify(cart_list));
        $('#cart_count').text(cart_list.length)
    }       
}
