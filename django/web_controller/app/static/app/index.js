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

const csrftoken = getCookie('csrftoken');

$('button').click(function () {
    console.log(this.id + ' ' + 'clicked!');

    $.ajax({
        type: 'POST',
        url: '/app/toggle/' + this.value + '/',
        data: {
            'pin_number': this.value,
        },
        headers: {
            'X-CSRFToken': csrftoken
        },
        success: function() {
            console.log('Success');
        },
        dataType: 'text'
    })

    location.reload();
});