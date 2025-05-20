Code Explanation

1. **`scan_port_thread`**:

   * This function is responsible for scanning a single port. It uses the `socket` module to attempt a connection to the provided IP address and port.
   * If the connection is successful (`result == 0`), it means the port is open. If not, the port is closed.

2. **`main`**:

   * This function collects user input for the IP address and the port range (start and end port).
   * It then starts scanning each port within the provided range using threading to scan multiple ports simultaneously.

3. **Threading**:

   * Threading allows the program to scan multiple ports at the same time, significantly speeding up the process compared to scanning one port at a time.

4. **Running the Program**:

   * The program will ask for the IP address and the port range you want to scan.
   * It then scans the ports in parallel using threads and outputs whether each port is open or closed.

For IP Address: When the program asks for the IP address (prompt: "Enter the IP address to scan"), only enter the IP address, not the port. For example:
192.168.1.10

For Ports: When the program asks for the starting port (prompt: "Enter the starting port"), only enter numeric values (e.g., 80, 22, 443).
For example, if you want to scan from port 1 to port 100:
Enter the starting port: 1
Enter the ending port: 100
