# LAN-Chat

## Overview
The LAN Chat Project is a Python-based implementation that allows users on the same Local Area Network (LAN) to communicate in real time. It includes a server-side script to manage connections and a client-side script to enable user interaction. The project uses the `socket` and `threading` modules to provide efficient communication.

## Features
- **Real-time communication**: Users can send and receive messages instantly.
- **Multi-client support**: The server handles multiple clients simultaneously.
- **Threading**: Concurrent threads enable seamless sending and receiving of messages without blocking.
- **Broadcasting**: Messages from any client are broadcast to all other connected clients.


## Project Structure
- **`Server.py`**: Handles incoming client connections, manages active clients, and broadcasts messages.
- **`Clients.py`**: Connects to the server, allows the user to send messages, and listens for incoming messages.
- **`Documentation.pdf`**: Contains a detailed explanation of the code, usage, and the LAN Chat testing phase.

## How It Works
### Server
1. Listens on a specified IP address and port for incoming connections.
2. Manages a list of active clients.
3. Forwards messages from one client to all other connected clients.

### Client
1. Connects to the server using its IP address and port.
2. Allows the user to send messages to the server.
3. Displays incoming messages from the server.

## Requirements
- Python 3.x
- Devices connected to the same Local Area Network (LAN)

## Setup and Usage
1. **Server Setup**:
   - Run `Server.py` on the machine that will act as the server.
   - Ensure the server's IP address and port are correctly configured in the script (adjust the `my_address` and `my_port` variables if needed).
   - Execute the following command in the terminal:
     ```bash
     python Server.py
     ```
   - The server will begin listening for incoming connections and display a message indicating its IP address and port.

2. **Client Setup**:
   - On each client device, open `Clients.py` and configure the `ADDRESS` and `PORT` variables to match the server's IP address and port.
   - Run the script using the following command:
     ```bash
     python Clients.py
     ```
   - Enter a unique name when prompted. This name will identify the client in the chat.
   - After connecting, you can start typing messages, which will be broadcast to all other connected clients.

3. **Chat Communication**:
   - Once the server is running and clients are connected:
     - Type messages in the client terminal to send them to all other connected clients.
     - Messages from other clients will appear in the terminal automatically.

4. **Stopping the Server or Clients**:
   - To stop the server or client scripts, press `Ctrl+C` in the terminal where the script is running. This will terminate the process.
