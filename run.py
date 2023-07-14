import socket
import os
def get_ip_address():
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Connect to a remote server (doesn't matter which one)
        sock.connect(("8.8.8.8", 80))

        # Get the socket's own IP address
        ip_address = sock.getsockname()[0]
        return ip_address
    except socket.error:
        return None
    finally:
        # Close the socket
        sock.close()

# Example usage
ip_address = get_ip_address()
if ip_address:
    
    os.system("python manage.py runserver {}:8000".format(ip_address))

else:
    print("Failed to retrieve IP address.")
