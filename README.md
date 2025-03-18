# 📩 **CHATGRPC** 📤

##  **Membros do Grupo** 

| 👤 Nome                 | 🎫 Matrícula  |
|------------------------|--------------|
| Jairon Jose Tavares dos Santos   | 22112583    |
| Arnaldo Lucas Santos Duarte  | 22112370     |
| Jockson Mateus da Silva Duarte    | 22112374     |

Este é um exemplo de um sistema de chat simples usando gRPC, uma estrutura de chamada de procedimento remoto (RPC) moderna e eficiente. O projeto consiste em um servidor que gerencia as mensagens e clientes que podem enviar e receber mensagens em tempo real.

## Como funciona

O sistema é composto por três componentes principais:

1. **Servidor**: Gerencia as mensagens e as envia para todos os clientes conectados.
2. **Cliente**: Permite que o usuário envie e receba mensagens em tempo real.
3. **gRPC**: Facilita a comunicação entre cliente e servidor de forma eficiente.

### Arquitetura

- **`chat.proto`**: Define a interface do serviço de chat usando Protocol Buffers.
- **`chat_pb2.py` e `chat_pb2_grpc.py`**: Gerados automaticamente a partir do `chat.proto`, contêm as classes Python para as mensagens e serviços.
- **`servidor.py`**: Implementa o servidor gRPC que gerencia as mensagens.
- **`client.py`**: Implementa o cliente que permite ao usuário enviar e receber mensagens.
- **`requirements.txt`**: Lista as dependências do projeto.

## Como executar

### Pré-requisitos

- Python 3.7 ou superior
- `pip` para instalar as dependências

### Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/chat-grpc.git
   cd chat-grpc
