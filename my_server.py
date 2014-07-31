"""

Server:
	Loops looking for connections and maintaining current corrections (using socket ?select?).
	If it receives ?<send current state please>?, then the server returns it?s current state.
		?<current state X>?, where X is the amount of bytes that will be sent in total.
		?updateupdateupdateupdate? etc
	If it receives ?<new update X>?, where X is the amount of bytes that will be sent in total.
	
	The server needs to:
		negotiate connecting with a client
		wait for that client to request something
		two requests:
			"current_state": returns a string which represents the current state saved on the server
			"set_the_state": sets the current state to the string which follows
			
		when client wants to set the current state of the server:
		1. client sends:
		"<new update, size 4654645647>"
		2. server acknowledges
		3. client sends:
		"<message                    >dsfdsafasfasdfasdfasdfsadfasdfasfasfaf"
		"asdfdsfasdfdsfvdfvgdfvdfvdfvdfvdfvdfvdfvdfvdfvdfvdfvafdasfdsfasdfas"
		"dasddasdasfddssdcdscsdcsdcsdcsdcdsdcsfadsfdsfdsfsdfasdfdsfsdfdsfsfa"
		4. server acknowledges until projected size is met.
		5. if the projected size is not met within a reasonable time frame, 
		the server clears the message it has stored, and sends the message
		"<new update cancelled>"
		
	
	
"""

def decode_message(update_string):
	if update_string.startswith("new update, size ")
	
	return new_update, size, message

import select
import socket

BUFSIZ = 1024
QUEUE = 5
HOST = "0.0.0.0"
PORT = 5678

#create a socket object to represent our connection
#set some settings on that socket object - making this socket useful as a server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('', PORT))

#set server socket to start listening for connections
server_socket.listen(QUEUE)
print 'Listening to port',PORT,'...'

#a map of all the clients we have, name to socket:
client_sockets = {}

#sockets that must have data sent out
outputs = []
inputs = [server_socket]

while 1:

	inputready,outputready,exceptready = select.select(server_socket, outputs, [])