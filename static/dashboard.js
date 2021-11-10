const BASE_URL = 'http://127.0.0.1'
const PORT = ':8080'

$.ajax({
    url: BASE_URL + PORT + '/api/approval_time_by_district',
    success: function (response) {
        display_approval_time_by_district(response)
    },
    error: function (XMLHttpRequest, textStatus, errorThrown) {
        alert("Status: " + textStatus); alert("Error: " + errorThrown);
    }
});

function display_approval_time_by_district(response) {
    console.log(response)
}