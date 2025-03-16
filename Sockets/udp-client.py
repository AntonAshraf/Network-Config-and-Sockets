import socket

# Main function to handle client operations
def main():
    # Create a UDP socket
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        # Prompt the user to enter a string to reverse
        data = input("Enter string to reverse: ")
        # Check if the user wants to exit
        if data.lower() == 'exit':
            break
        # Send the user's input to the server
        client.sendto(data.encode(), ('127.0.0.1', 5002))  # Send data to the server
        # Receive the response from the server
        response, _ = client.recvfrom(1024)  # Receive response from the server
        # Print the reversed string received from the server
        print(f"Received from server: {response.decode()}")

    # Close the socket
    client.close()  # Close the socket

# Run the main function when the script is executed
if __name__ == "__main__":
    main()