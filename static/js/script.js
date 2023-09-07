$(document).ready(function () {
    $('#rightSide').append("<p>Loaded</p>")
    $('.eventCard').click(function (e) {
        const id = $(this).attr('data-id');
        display_event(id);
    })
}
);

function display_event(id) {
    console.log("hi", id)
    //$('#rightSide').append(`<p>${id}</p>`)
}


