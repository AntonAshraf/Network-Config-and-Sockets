import socket
import threading

# Function to handle each client connection
def handle_client(client_socket):
    try:
        # Receive data from the client
        data = client_socket.recv(1024).decode("utf-8")
        # Reverse the received string
        reversed_string = data[::-1]
        # Send the reversed string back to the client
        client_socket.send(reversed_string.encode("utf-8"))
    except Exception as e:
        # Print any error that occurs during the client handling
        print(f"Error handling client: {e}")
    finally:
        # Close the client socket connection
        client_socket.close()

# Main function to set up the server
def main():
    host = "0.0.0.0"  # Listen on all available network interfaces
    port = 5000  # Choose a port number greater than 1023

    # Create a socket object using IPv4 and TCP protocols
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the specified host and port
    server_socket.bind((host, port))
    # Enable the server to accept connections, with a maximum backlog of 5
    server_socket.listen(5)

    print(f"Listening on {host}:{port}...")

    while True:
        # Accept a new client connection
        client, addr = server_socket.accept()
        print(f"Accepted connection from {addr[0]}:{addr[1]}")
        # Create a new thread to handle the client connection
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

# Run the main function when the script is executed
if __name__ == "__main__":
    main()