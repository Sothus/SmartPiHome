$(function() {

    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var chatsock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + window.location.pathname);

    chatsock.onopen = function() {
           console.log("Connected!");
           console.log(document.URL)
    };

    chatsock.onmessage = function(message) {
        console.log("Received Sock message!");
        console.log(message);
        console.log(jQuery.type(message));
        console.log(message.data)

    };
    
	$(".light-button").click(function(){
		console.log("click");
		var rasp = $(this).parent().parent().attr("id");
		var message = { "light": this.id, "raspberry": rasp};
		message = JSON.stringify(message);
		console.log(message);
		chatsock.send(message);
		console.log("PRZED: " + $(this).text());
		if($.trim($(this).text()) == "Wlacz")
			$(this).text("Wylacz");
		else
			$(this).text("Wlacz");
			
		console.log("PO: " + $(this).text());
	});
	
	$(".rgb-light-button").click(function(){
		console.log("rgb-click");
		chatosck.send(this.id);
		
	});

});
