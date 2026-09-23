import http.server
import ssl

server = http.server.HTTPServer(
    ("localhost", 4443),
    http.server.SimpleHTTPRequestHandler
)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain("server.crt", "server.key")

server.socket = context.wrap_socket(
    server.socket,
    server_side=True
)

print("HTTPS server listening on https://localhost:4443")

server.serve_forever()
