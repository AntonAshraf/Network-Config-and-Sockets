import socket

# Main function to set up the UDP server
def main():
    # Create a UDP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind the socket to an IP address and port
    server.bind(('0.0.0.0', 5002))
    print("UDP server started on port 5002")

    while True:
        # Receive data from a client
        data, addr = server.recvfrom(1024)
        # Decode the received data and reverse the string
        reversed_data = data.decode()[::-1]
        # Print the received data from the client
        print(f"Received from client: {data.decode()}")
        # Print the reversed string that will be sent to the client
        print(f"Sending to client: {reversed_data}")
        # Send the reversed string back to the client
        server.sendto(reversed_data.encode(), addr)

# Run the main function when the script is executed
if __name__ == "__main__":
    main()