from channels.routing import route
from chat_app import consumers

channel_routing = [
	route('websocket.connect', 		consumers.ws_add,			path=r'^/chat/$'),#connect to websocket
	route('websocket.receive', 		consumers.ws_message,		path=r'^/chat/$'),#recieve message from websocket
	route('websocket.disconnect',	consumers.ws_disconnect, 	path=r'^/chat/$'),#disconnect from websocket
]