import socket
import threading

# Function to initialize the server by creating a socket, binding to the address and port, and listening for connections
def initialize_server(address, port):
    # Create a socket object using IPv4 addressing (AF_INET) and TCP protocol (SOCK_STREAM)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the server socket to the specified address and port
    server_socket.bind((address, port))
    
    # Set the server socket to listen for incoming connections
    server_socket.listen()
    
    # Print the server address and port for confirmation
    print(f"Server listening on {address}:{port}")
    
    # List to keep track of all connected clients
    clients_list = []
    
    # Start accepting clients by calling accept_clients function
    accept_clients(server_socket, clients_list)

# Function to accept incoming client connections
def accept_clients(server_socket, clients_list):
    while True:
        # Accept a client connection. This blocks until a client connects
        client, client_address = server_socket.accept()
        
        # Append the new client to the clients list
        clients_list.append(client)
        
        # Start a new thread for the client to listen for messages
        client_thread(client, clients_list)

# Function to create and start a new thread that listens for a client's messages
def client_thread(client, clients_list):
    # Create a new thread and start it, passing the listening function with the client and the clients list as arguments
    client_threading = threading.Thread(target=thread_listening, args=(client, clients_list))
    client_threading.start()

# Function that listens for messages from the client in its own thread
def thread_listening(client, clients_list):
    while True:
        # Receive a message from the client (up to 1024 bytes) and decode it to string
        message = client.recv(1024).decode()
        
        # If a message was received, print it and broadcast it to all connected clients
        if message:
            print(f"Message from {client.getpeername()}: {message}")
            broadcast(message, clients_list)
        else:
            # If the client disconnects (no message), print the disconnection info
            print(f"Client {client.getpeername()} disconnected")
            
            # Remove the client from the clients list and close the connection
            clients_list.remove(client)
            client.close()

# Function to broadcast the received message to all connected clients
def broadcast(message, clients_list):
    for client in clients_list:
        try:
            # Send the message to the client (encode the message before sending)
            client.send(message.encode())
        except Exception as e:
            # If there is an error sending the message, print the error, remove the client, and close the connection
            print(f"Error broadcasting message to {client.getpeername()}: {e}")
            clients_list.remove(client)
            client.close()

# Main function that sets up the server by specifying the address and port
def main():
    my_port = 7000  # Port on which the server will listen for incoming connections
    my_address = "192.168.1.4"  # IP address where the server will run
    initialize_server(my_address, my_port)

# Entry point of the script. If the script is run directly, the main function will be executed
if __name__ == "__main__":
    main()
