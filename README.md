# 📩 CHATGRPC

Sistema de chat simples usando gRPC, uma estrutura de chamada de procedimento remoto (RPC) moderna e eficiente.

---

## 🧠 Funcionalidades

* ✔️ Servidor: Gerencia as mensagens e as envia para todos os clientes conectados.
* ✔️ Cliente: Permite que o usuário envie e receba mensagens em tempo real.
* ✔️ gRPC: Comunicação facilitada entre cliente e servidor de forma eficiente.

---

## 🛠️ Tecnologias

* Python 3.7+
* gRPC
* Protocol Buffers

---

## ⚙️ Como usar

```bash id="cmd1"
# Clonar repositório
git clone https://github.com/seu-usuario/chat-grpc.git
cd chat-grpc

# Instalar dependências
pip install -r requirements.txt

# Iniciar o servidor
python servidor.py

# Em outro terminal, iniciar o cliente (para cada pessoa que deseja entrar)
python client.py
```

---

## 📸 Demonstração

(prints do chat funcionando no terminal)

---

## 🎯 Objetivo

Projeto desenvolvido para demonstrar o uso de gRPC na criação de um sistema de chat cliente-servidor moderno e eficiente em tempo real.

### Arquitetura do Projeto
* **`chat.proto`**: Define a interface do serviço de chat usando Protocol Buffers.
* **`chat_pb2.py` e `chat_pb2_grpc.py`**: Gerados automaticamente a partir do `chat.proto`, contêm as classes Python para as mensagens e serviços.
* **`servidor.py`**: Implementa o servidor gRPC que gerencia as mensagens.
* **`client.py`**: Implementa o cliente que permite ao usuário enviar e receber mensagens.
* **`requirements.txt`**: Lista as dependências do projeto.

### Membros do Grupo
| 👤 Nome | 🎫 Matrícula |
|---|---|
| Jairon Jose Tavares dos Santos | 22112583 |
| Arnaldo Lucas Santos Duarte | 22112370 |
| Jockson Mateus da Silva Duarte | 22112374 |

---

## 📄 Licença

MIT
