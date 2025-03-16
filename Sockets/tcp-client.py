import socket

# Main function to handle client operations
def main():
    server_ip = "192.168.1.25"  # Ip of raspberry pi
    server_port = 5000  # Port number to connect to the server

    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server using the specified IP and port
    client_socket.connect((server_ip, server_port))

    while True:
        # Get input from the user
        user_input = input("Enter a string (or 'exit' to quit): ")
        
        # Check if the user wants to exit
        if user_input.lower() == 'exit':
            break
        
        # Send the user input to the server
        client_socket.send(user_input.encode("utf-8"))
        
        # Receive the reversed string from the server
        reversed_string = client_socket.recv(1024).decode("utf-8")
        
        # Print the reversed string
        print(f"Reversed string: {reversed_string}")

    # Close the socket connection
    client_socket.close()

# Run the main function when the script is executed
if __name__ == "__main__":
    main()