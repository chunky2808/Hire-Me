$(document).ready(function(){

	var socket = new WebSocket('ws://127.0.0.1:8000/chat/');
	socket.onopen = websocket_connection_ok;
	socket.onmessage = websocket_msj_received;

	$('#form').submit(function(e){
		e.preventDefault();
		data = {
			'name' : $('input[name="name"]').val(),
			'message': $('input[name="text"]').val()
		}
		socket.send(JSON.stringify(data));
		$('#form')[0].reset();
	});

});

function websocket_connection_ok(){
	alert('The connection has been established');
}

function websocket_msj_received(e){
	data = JSON.parse(e.data);
	code = '<div class="col s12">'				+
				'<div class="name">'				+
					'<h4>'+ data.name +'</h4>'	+
				'</div>'							+
				'<div class="content">'			+
					'<p>'+ data.message +'</p>'	+
				'</div>'							+
			'</div>';
	$('#conversation').append(code);
}