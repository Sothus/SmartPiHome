$(function() {

    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var chatsock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + window.location.pathname);

    chatsock.onopen = function() {
           console.log("Connected!");
           console.log(document.URL)
    };

    chatsock.onmessage = function(message) {
        var message = jQuery.parseJSON(message.data)
        if(typeof message.sensor_id !='undefined')
        {
			console.log(message.value)
			$("#" + message.sensor_id).text(message.sensor_name + ": " + message.value);
		}
    };
   
});
