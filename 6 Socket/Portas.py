import socket

print(socket.getservbyname("domain"))
print("="*50)
print(socket.getservbyname("http"))
print("="*50)
print(socket.getservbyname("ftp"))
print("="*50)