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
