$(document).ready(function () {

    // Add event listener to the event cards
    $('.eventCard').click(function (e) {
        const id = $(this).attr('data-id');
        display_event(id);
    })

    // get locations for each event
    let locations = [];
    let titles = [];
    const events = JSON.parse($('#hidden').val());
    for (let event of events) {
        locations.push({ lat: event.coordinates[0], lng: event.coordinates[1] });
        titles.push(event.title)
    }

    // If the map exists we initialize the map
    const mapDiv = $('#map');
    if (mapDiv) {
        initMap(locations, titles);
    }
}
);


/**
 * This function is used to dynamically get the information of the event with the passed id
 * @param {event id} id 
 */
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
            })

            const organizer = (json.organizer)

            $('#result').html(
                `
            <div class="eventDetailcard">
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
                        <p class="eventLocation">Location:${result.location}
                        <p class="eventOrganiser">
                            Organised by: ${organizer}
                        </p>
                        <p class="eventDescription">
                            Description: ${result.description}
                        </p>
                    </div>
                </div>
            </div>
            `);
        },
        error: function (xhr, errmsg, err) {
            $('#result').html("Sorry, there was an error displaying this content.");
        }
    })
}

// Initialize the map
var map;
async function initMap(locations, titles) {


    const { Map, InfoWindow } = await google.maps.importLibrary("maps");
    const { AdvancedMarkerElement, PinElement } = await google.maps.importLibrary(
        "marker",
    );

    map = new Map(document.getElementById("map"), {
        center: { lat: 53.44947, lng: -7.52297 },
        zoom: 8,
        mapId: "Events",
    });

    const infoWindow = new google.maps.InfoWindow({
        content: "",
        disableAutoPan: true,
    });
    // Create an array of alphabetical characters used to label the markers.
    const labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    // Add some markers to the map.
    const markers = locations.map((position, i) => {
        const label = labels[i % labels.length];
        const pinGlyph = new google.maps.marker.PinElement({
            glyph: label,
            glyphColor: "white",
        });
        const marker = new google.maps.marker.AdvancedMarkerElement({
            position,
            content: pinGlyph.element,
            title: titles[i]
        });

        // open info window when marker is clicked
        marker.addListener("click", () => {
            infoWindow.setContent(titles[i]);
            infoWindow.open(map, marker);
        });
        return marker;
    });

    // Add a marker clusterer to manage the markers.
    new markerClusterer.MarkerClusterer({ markers, map });
}

// function to open Filter dropdown
function filterMenuOpen() {
    document.getElementById("filterDropdown").classList.toggle("show");
}