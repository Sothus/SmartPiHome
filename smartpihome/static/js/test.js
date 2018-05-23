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
		var rasp = $(this).parent().parent().attr("id");
		var message = { "rgb_light": this.id, "raspberry": rasp};
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

	
	$(".rgb-light-set-button").click(function(){
		console.log("rgb-click");
		var rasp = $(this).parent().parent().attr("id");
		var redVal = $(this).parent().find(".red_input").val();
		var greenVal = $(this).parent().find(".green_input").val();
		var blueVal = $(this).parent().find(".blue_input").val();
		 
		console.log(redVal);
		var message = { "rgb_light_set": this.id, "red_val": redVal, "green_val": greenVal, "blue_val": blueVal, "raspberry": rasp};
		message = JSON.stringify(message);
		console.log(message);
		chatsock.send(message);
	
	});

});
