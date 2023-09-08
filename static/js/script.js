$(document).ready(function () {
    const mapDiv = $('#map');
    if (mapDiv) {
        initMap();
    }
    $('.eventCard').click(function (e) {
        const id = $(this).attr('data-id');
        display_event(id);
    })
}
);

function display_event(id) {
    var result = {}
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
                result = event.fields
                console.log(event.fields)
            })

            $('#result').html(
                `
            <div class="eventDetailcard">
                <div class="eventImageContainer">
                    <img src="../static/images/Logo Party 4 The planet.png" alt="" />
                </div>
                <div class="eventDetailsContainer">
                    <div class="eventName">
                    <h2>${result.title}</h2>
                    </div>
                    <div class="eventInformations">
                        <p class="eventStartTime">
                            Start Date: ${result.start_datetime}
                        </p>
                        <p class="eventEndTime">
                            End Date: ${result.end_datetime}
                        </p>
                        <p class="eventParticipantsCounter">
                            203<i class="fa-solid fa-people-group"></i>
                        </p>
                        <p class="eventLocation">Location:${result.location}
                        <p class="eventOrganiser">
                            Organised by: ${result.organizer}
                        </p>
                        <p class="eventDescription">
                            Description: ${result.description}
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


var map;
async function initMap() {
    const { Map } = await google.maps.importLibrary("maps");
  
    map = new Map(document.getElementById("map"), {
      center: { lat: 53.44947, lng: -7.52297 },
      zoom: 8,
    });
  }


var map;
async function initMap() {
    const { Map } = await google.maps.importLibrary("maps");
  
    map = new Map(document.getElementById("map"), {
      center: { lat: 53.44947, lng: -7.52297 },
      zoom: 8,
    });
  }

// function to open Filter dropdown
function filterMenuOpen() {
    document.getElementById("filterDropdown").classList.toggle("show");
}