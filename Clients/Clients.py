import socket
import threading

# Get user's name and ensure it's not empty
name = input("Choose your name: ").strip()

# Ensure a name is provided (if input is empty, prompt again)
while not name:
    name = input("You should provide name: ").strip()

# Create a socket object for communication
socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define server address and port
ADDRESS = "192.168.1.4"  # Server's IP address
PORT = 7000  # Port number for the server

# Connect the socket to the server using the address and port
socket_obj.connect((ADDRESS, PORT))

# Function to handle sending messages to the server
def sending_msg():
    while True:
        # Get message from user input
        sent_msg = input("Enter your message: ").strip()
        
        # Check if the user has entered a non-empty message
        if sent_msg:
            # Concatenate the user's name and message
            msg_name = name + " : " + sent_msg
            
            # Send the message to the server (encode it as bytes before sending)
            socket_obj.send(msg_name.encode())

# Function to handle receiving messages from the server
def recieve_msg():
    while True:
        # Receive a message from the server (up to 1024 bytes)
        recieved_msg = socket_obj.recv(1024).decode()
        
        # Print the received message
        print(recieved_msg)

# Create and start two threads: one for sending messages and another for receiving messages
thread_send = threading.Thread(target=sending_msg)  # Thread for sending messages
thread_receive = threading.Thread(target=recieve_msg)  # Thread for receiving messages

# Start the sending and receiving threads
thread_send.start()
thread_receive.start()
