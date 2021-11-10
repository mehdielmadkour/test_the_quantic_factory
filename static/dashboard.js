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
    
    let data = {
        labels: response.district,
        datasets: [{
            label: 'approval time',
            backgroundColor: 'rgb(10, 10, 200)',
            borderColor: 'rgb(255, 99, 132)',
            data: response.approval_time
        }]
    }

    let config = {
        type: 'bar',
        data: data,
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    }

    let approval_time_by_district = new Chart(
        document.getElementById('approval_time_by_district'),
        config
    )
}