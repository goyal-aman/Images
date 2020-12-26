let url = 'http://127.0.0.1:8000/'
fetch(url)
    .then(function (response) {
        // The JSON data will arrive here
        return response.json();
    })
    .then(function (data) {
        appendData(data); 
    })
    .catch(function (err) {
        console.error("ERROR OCUURED MY AMAN:",  err);
        // If an error occured, you will catch it here
    });

function appendData(data){
    // TODO: improve this method 
    var mainContainer = document.getElementById("myData");
    for(var i=0; i<data.length; i++){
        var div = document.createElement("div");
        div.innerHTML =  '<li><div><time>' + data[i].date + '</time>' + data[i].text+'</div></li>';
        mainContainer.appendChild(div);
    }
}