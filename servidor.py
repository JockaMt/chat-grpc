import grpc
from concurrent import futures
import chat_pb2
import chat_pb2_grpc
import threading
from queue import Queue
import signal  # Importando o módulo signal para tratar interrupções
import sys  # Importando o módulo sys para sair do programa

class ChatServicer(chat_pb2_grpc.ChatServiceServicer):
    def __init__(self):
        self.messages = []  # Lista para armazenar todas as mensagens
        self.clients = []  # Lista para armazenar os streams de clientes ativos
        self.lock = threading.Lock()  # Lock para garantir thread safety

    def SendMessage(self, request, context):
        """Recebe uma mensagem de um cliente e a envia para todos os clientes."""
        with self.lock:
            self.messages.append(request)  # Adiciona a mensagem à lista de mensagens
            # Envia a mensagem para todos os clientes conectados
            for client_stream in self.clients:
                try:
                    client_stream.put(request)
                except Exception as e:
                    print(f"Erro ao enviar mensagem para um cliente: {e}")
        return chat_pb2.MessageAck(success=True)

    def ReceiveMessages(self, request, context):
        """Streaming de mensagens para o cliente."""
        # Cria uma fila para o cliente atual
        client_queue = Queue()
        with self.lock:
            self.clients.append(client_queue)  # Adiciona o cliente à lista de clientes ativos

        try:
            # Envia todas as mensagens antigas para o novo cliente
            for message in self.messages:
                yield message

            # Envia novas mensagens para o cliente em tempo real
            while True:
                message = client_queue.get()  # Espera por novas mensagens
                yield message
        finally:
            # Remove o cliente da lista quando a conexão é encerrada
            with self.lock:
                self.clients.remove(client_queue)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServiceServicer_to_server(ChatServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("Servidor rodando na porta 50051...")
    server.start()

    # Função para encerrar o servidor de forma limpa
    def shutdown(signum, frame):
        print("\nEncerrando o servidor...")
        server.stop(0)  # Para o servidor de forma não bloqueante
        sys.exit(0)  # Sai do programa

    # Configura o tratamento para o sinal SIGINT (Ctrl+C)
    signal.signal(signal.SIGINT, shutdown)

    # Mantém o servidor em execução
    server.wait_for_termination()

if __name__ == '__main__':
    serve()