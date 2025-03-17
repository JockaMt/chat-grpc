import grpc
import chat_pb2
import chat_pb2_grpc
import threading

def receive_messages(stub):
    """Função para receber mensagens do servidor em segundo plano."""
    for message in stub.ReceiveMessages(chat_pb2.Empty()):
        print(f"{message.user}: {message.text}")

def run():
    # Solicitar o nome do usuário
    username = input("Digite seu nome de usuário: ")

    channel = grpc.insecure_channel('localhost:50051')
    stub = chat_pb2_grpc.ChatServiceStub(channel)

    # Enviar uma mensagem inicial informando que o usuário entrou
    response = stub.SendMessage(chat_pb2.Message(user=username, text="entrou!"))
    print("Resposta do servidor:", response.success)

    # Iniciar uma thread para receber mensagens
    threading.Thread(target=receive_messages, args=(stub,), daemon=True).start()

    # Loop para enviar mensagens
    while True:
        msg = input()
        if msg.lower() == "sair":
            break
        response = stub.SendMessage(chat_pb2.Message(user=username, text=msg))
    print("Resposta do servidor:", response.success) if response.success else ""

if __name__ == '__main__':
    run()