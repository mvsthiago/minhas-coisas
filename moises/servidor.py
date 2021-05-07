import socket
import requests
HOST = ''
PORT = 5000
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print('Conectado por', cliente)
    while True:
        msg = con.recv(1024)
        if not msg: break
        msg = msg.decode('utf-8')
        response = requests.get('http://gistapis.etufor.ce.gov.br:8081/api/linhas/' + msg)
        msg = str(response.json())
        msg = msg.encode('utf-8')
        con.send(msg)


    print('Finalizando conexao do cliente', cliente)
    con.close()