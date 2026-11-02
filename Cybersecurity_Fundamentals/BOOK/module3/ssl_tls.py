
import ssl
import socket

hostname = "www.bhu.ac.in"
port = 443

context = ssl.create_default_context()

with socket.create_connection((hostname, port)) as sock:
    with context.wrap_socket(
        sock, server_hostname=hostname
    ) as secure_socket:

        certificate = secure_socket.getpeercert()

        print("Connection Successful!")
        print("TLS Version:",
              secure_socket.version())

        print("Certificate Details:")
        print("Subject:",
              certificate.get("subject"))

        print("Issuer:",
              certificate.get("issuer"))

        print("Valid From:",
              certificate.get("notBefore"))

        print("Valid Until:",
              certificate.get("notAfter"))
