import socket
import mysql.connector

# Conectar ao banco de dados MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root_password",
    database="quiz"
)

# Função para enviar questões ao cliente
def send_questions(client_socket):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM questions")
    questions = cursor.fetchall()
    for question in questions:
        # Envia a pergunta
        client_socket.sendall(question[1].encode() + b'\n')

        # Envia as opções de resposta
        options = ['a', 'b', 'c', 'd']
        for i in range(2, 6):
            client_socket.sendall(f"{options[i-2]}) {question[i]}\n".encode())

        # Recebe a resposta do cliente
        client_response = client_socket.recv(1024).decode().strip().lower()

        # Verifica se a resposta está correta
        if client_response == question[6].lower():
            client_socket.sendall(b"Correct!\n")
        else:
            client_socket.sendall(b"Wrong!\n")

# Configuração do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Server is listening...")

while True:
    client_socket, _ = server_socket.accept()
    print("Client connected.")
    send_questions(client_socket)