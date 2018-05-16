$(function() {

    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var chatsock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + window.location.pathname);

    chatsock.onopen = function() {
           console.log("Connected!");
           $('#test').text("Connected!");
           chatsock.send("Connected!");
           console.log(document.URL)
    };

    chatsock.onmessage = function(message) {
        console.log("Received Sock message!");
        console.log(message);
        console.log(jQuery.type(message));
        console.log(message.data)

    };

});
