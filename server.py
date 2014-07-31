import socket, select

HOST = socket.gethostname()
PORT = 50007
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(2)
print "server_socket is", server_socket

#count = 0

potential_readers = [server_socket]
potential_writers = []
potential_errs = []

class ServerException():
    pass

class Server():
    state = "***no state set***"

def handle_new_connection(socket, reader_list):
    conn, addr = socket.accept()
    print 'Connected by', addr, socket
    potential_readers.append(conn)
    print 'potential_readers', reader_list
    return reader_list

def handle_incoming_data(socket):
    data = socket.recv(1024)
    print "data received (", data, ")"
    return data

def form_response(data):
    response_data = "sorry - I didn't understand that"
    
    if data.startswith("read   |"):
        response_data = Server.state
    elif data.startswith("write  |") and len(data) > 8:
        Server.state = data[8:]
        response_data = "data written to state. thanks"
    return response_data

while 1:
    ready_to_read, ready_to_write, in_error = select.select(potential_readers, potential_writers, potential_errs, 1)

    potential_readers = [server_socket]
    potential_writers = []
    potential_errs = []

    #accept any incoming connections. this is our server socket
    for readable_socket in ready_to_read:
        #it's our server socket that has found a new connection
        if readable_socket is server_socket:
            potential_readers = handle_new_connection(readable_socket, potential_readers)
        #it's a client connection socket with data for us
        else:
            data = ""
            try:
                data = handle_incoming_data(readable_socket)
            except ServerException: readable_socket.close()
            else:
                #form a string in response to the data received
                #attach this string as a new attribute to the socket
                #when we are ready to write to the socket later,
                #we just look up .outgoing_data to see what we should
                #send.
                outgoing_data = form_response(data)
                #potential_writers.append(readable_socket)

    #if we have a socket ready to listen to us,
    #for writable_socket in ready_to_write:
        #write back an acknowledgement
                print "saying thanks and goodbye to ", readable_socket
                readable_socket.send(outgoing_data)
                #and we're done
                readable_socket.close()
    
    #count += 1
    #print "still looping, count is ", count
