from mcstatus import JavaServer
print("Insert your IP\nip:port - hostname:25565")
ipserver = input()
server = JavaServer.lookup(ipserver)
status = server.status()
print(f"The server has {status.players.online} players and a latency of {status.latency} ms.")

