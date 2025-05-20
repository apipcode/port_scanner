import socket
import threading

# Function to scan a port with threading
def scan_port_thread(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)  # Set timeout for socket communication
    result = s.connect_ex((ip, port))  # Try to connect to the given IP and port
    if result == 0:
        print(f"Port {port} is open on {ip}")  # If the port is open
    else:
        print(f"Port {port} is closed on {ip}")  # If the port is closed
    s.close()

# Main function that uses threading to scan multiple ports simultaneously
def main():
    ip = input("Enter the IP address to scan: ")  # Get the IP address input from the user
    start_port = int(input("Enter the starting port: "))  # Get the starting port from the user
    end_port = int(input("Enter the ending port: "))  # Get the ending port from the user
    
    print(f"Scanning ports on {ip} simultaneously...")

    threads = []  # List to store threads
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port_thread, args=(ip, port))  # Create a thread for each port
        threads.append(thread)  # Add thread to the list
        thread.start()  # Start the thread to scan the port

    for thread in threads:
        thread.join()  # Wait for all threads to finish

if __name__ == "__main__":
    main()
