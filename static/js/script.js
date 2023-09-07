$(document).ready(function () {
    $('.eventCard').click(function (e) {
        const id = $(this).attr('data-id');
        display_event(id);
    })
}
);

function display_event(id) {
    var results = []
    var token = $("input[name=csrfmiddlewaretoken]").val();

    $.ajax({
        type: "POST",
        url: "",
        data: {
            id: id,
            csrfmiddlewaretoken: token,
        },
        success: function (json) {
            $('#placeholder-image').hide();
            $.each(JSON.parse(json.selected_event), function (index, event) {
                results.push(event.fields)
            })

            $('#result').html(
                `
            <div class="eventDetailcard">
                <div class="eventImageContainer">
                    <img src="../static/images/Logo Party 4 The planet.png" alt="" />
                </div>
                <div class="eventDetailsContainer">
                    <div class="eventName">
                    <h2>${results[0].title}</h2>
                    </div>
                    <div class="eventInformations">
                        <p class="eventStartTime">
                            Start Date: ${results[0].start_datetime}
                        </p>
                        <p class="eventEndTime">
                            End Date: ${results[0].end_datetime}
                        </p>
                        <p class="eventParticipantsCounter">
                            203<i class="fa-solid fa-people-group"></i>
                        </p>
                        <p class="eventLocation">Location:${results[0].location}
                        <p class="eventOrganiser">
                            Organised by: ${results[0].organizer}
                        </p>
                        <p class="eventDescription">
                            Description: ${results[0].description}
                        </p>
                    </div>
                </div>
                <div class="eventButtonsContainer">
                    <button class="joinButton">
                    <p>Join</p>
                    </button>
                    <button class="shareButton">
                    <p>Share</p>
                    </button>
                </div>
            </div>
            `);
        },
        error: function (xhr, errmsg, err) {
            $('#result').html(err);
            $('#spinner').hide();
        }
    })
}

// function to open Filter dropdown
function filterMenuOpen() {
    document.getElementById("filterDropdown").classList.toggle("show");
}