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

function add_to_cart(id){
    $.ajax({
        url: `/cart/add_to_cart/`+id+'/',
        type: 'GET',
        data: {'is_ajax':true},
        success: function (response) {
            if(response['success']){
                if(response['login_req']){
                    window.location='/user/sign_in_user'
                }
                else{
                    $('#cart_count').text(response['cart_count'])
                }
            }
        }
    })
}

function cart_to_wishlist(id, row_id){
    $.ajax({
        url: `/cart/cart_to_wish/`+id+'/',
        type: 'GET',
        data: {'is_ajax':true},
        success: function (response) {
            if(response['success']){
                if(response['login_req']){
                    window.location='/user/sign_in_user'
                }
                else{
                    if(response['wishlist_count']){
                        $('#wishlist_count').text(response['wishlist_count'])
                    }
                        $('#cart_count').text(response['cart_count'])
                        $("#cart_table_row_"+row_id).remove()
                }
                
            }
        }
    })
}

function remove_wish(id){
    $.ajax({
        url: `/wishlist/remove_wish/`+id+'/',
        type: 'GET',
        data: {'is_ajax':true},
        success: function (response) {
            if(response['success']){
                if(response['login_req']){
                    window.location='/user/sign_in_user'
                }
                else{
                    if(response['count']){
                        $('#wishlist_count').text(response['wishlist_count'])
                    }
                        $("#wishlist_table_row_"+id).remove()
                }  
            }
        }
    })
}

function remove_cart(id){
    $.ajax({
        url: `/cart/remove_cart/`+id+'/',
        type: 'GET',
        data: {'is_ajax':true},
        success: function (response) {
            if(response['success']){

                if(response['login_req']){
                    window.location='/user/sign_in_user'
                }
                else{
                    if(response['count']){
                        $('#cart_count').text(response['cart_count'])
                    }
                        $("#cart_table_row_"+id).remove()
                }
            }
        }
    })
}

function wishlist_to_cart(id){
    $.ajax({
        url: `/wishlist/wish_to_cart/`+id+'/',
        type: 'GET',
        data: {'is_ajax':true},
        success: function (response) {
            if(response['success']){
                if(response['login_req']){
                    window.location='/user/sign_in_user'
                }
                else{
                    if(response['cart_count']){
                        $('#cart_count').text(response['cart_count'])
                    }
                }  
            }
        }
    })
}

function helpfull(id){
    $.ajax({
        url: `/review/helpfull/`+id+'/',
        type: 'GET',
        data: {'is_ajax':true},
        success: function (response) {
            if(response['success']){
                $('.helpfull_count_'+id).text(response['helpfull_count']+ " people found this helpful")
            }
        }
    })
}

function add_one_cart(id){
    $.ajax({
        url: `/cart/add_one_cart/`+id+'/',
        type: 'GET',
        data: {'is_ajax':true},
        success: function (response) {
            if(response['success']){
                if(response['login_req']){
                    window.location='/user/sign_in_user'
                }
                else{
                    $('#cart_count_'+id).text(response['count'])
                }
               
            }
        }
    })
}

function remove_one_cart(id,item_id){
    $.ajax({
        url: `/cart/remove_one_cart/`+id+'/',
        type: 'GET',
        data: {'is_ajax':true},
        success: function (response) {
            if(response['success']){
                if(response['login_req']){
                    window.location='/user/sign_in_user'
                }
                else{
                    if(response["count"]){
                        $('#cart_count_'+id).text(response['count'])
                    }
                    if(response['count_zero']){
                        $("#cart_table_row_"+item_id).remove()
                    }
                }                
            }
        }
    })
}