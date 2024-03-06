import socket

def receive_and_send():
    # Conecta ao servidor
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    while True:
        # Recebe a pergunta
        question = client_socket.recv(1024).decode()
        if question == "No more questions":
            print("No more questions. Quiz complete.")
            break

        print(question)

        # Recebe e mostra as opções de resposta
        options = client_socket.recv(1024).decode().split("\n")
        for option in options:
            if option.strip():  # Ignora linhas em branco
                print(option)

        # Solicita a resposta do usuário
        response = input("Responda com a letra correspondente à sua escolha: ").strip().lower()
        client_socket.sendall(response.encode())

        # Recebe e mostra o resultado da resposta
        result = client_socket.recv(1024).decode().strip()
        print(result)

    client_socket.close()

# Chamada da função
receive_and_send()
