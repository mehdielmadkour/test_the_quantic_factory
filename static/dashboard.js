const BASE_URL = 'http://127.0.0.1'
const PORT = ':8080'

const id_list = [
    'approval_time_by_district', 
    'approval_proportion_by_district', 
    'approval_time_by_type', 
    'approval_proportion_by_type', 
    'approval_time_by_constituency', 
    'approval_proportion_by_constituency'
]

function getData(id) {

    $.ajax({
        url: BASE_URL + PORT + '/api/' + id,
        success: function (response) {
            displayData(id, response, 'bar')
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus); alert("Error: " + errorThrown);
        }
    });

}

function displayData(id, response, type) {
    
    let data = {
        labels: response.labels,
        datasets: [{
            label: response.title,
            backgroundColor: 'rgb(10, 10, 200)',
            borderColor: 'rgb(255, 99, 132)',
            data: response.values
        }]
    }

    let config = {
        type: type,
        data: data,
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    }

    new Chart(
        document.getElementById(id),
        config
    )
}

id_list.forEach(id => {
    getData(id)
})