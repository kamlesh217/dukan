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
        success: function (response) {
            if(response['success']){
                $('#cart_count').text(response['cart_count'])
            }
        }
    })
}

function cart_to_wishlist(id, row_id){
    $.ajax({
        url: `/cart/cart_to_wish/`+id+'/',
        type: 'GET',
        success: function (response) {
            if(response['success']){
                if(response['wishlist_count']){
                $('#wishlist_count').text(response['wishlist_count'])
            }
                $('#cart_count').text(response['cart_count'])
                $("#cart_table_row_"+row_id).remove()
            }
        }
    })
}


function remove_wish(id){
    $.ajax({
        url: `/wishlist/remove_wish/`+id+'/',
        type: 'GET',
        success: function (response) {
            if(response['success']){
                if(response['count']){
                $('#wishlist_count').text(response['wishlist_count'])
            }
                $("#wishlist_table_row_"+id).remove()
            }
        }
    })
}


function remove_cart(id){
    $.ajax({
        url: `/cart/remove_cart/`+id+'/',
        type: 'GET',
        success: function (response) {
            if(response['success']){
                if(response['count']){
                $('#cart_count').text(response['cart_count'])
            }
                $("#cart_table_row_"+id).remove()
            }
        }
    })
}





function wishlist_to_cart(id){
    $.ajax({
        url: `/wishlist/wish_to_cart/`+id+'/',
        type: 'GET',
        success: function (response) {
            if(response['success']){
                if(response['cart_count']){
                $('#cart_count').text(response['cart_count'])
            }
            }
        }
    })
}
