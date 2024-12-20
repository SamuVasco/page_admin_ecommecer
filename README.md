## atualmente em desenvolvimento ( iniciado dia 16/12/2024 )

# Painel de Administração de E-commerce com Django, Django REST Framework, Channels e Celery

Este projeto é um painel de administração para um sistema de e-commerce. Ele fornece uma API RESTful utilizando **Django REST Framework**, com funcionalidades em tempo real via **Django Channels** e execução assíncrona de tarefas com **Celery**.

### Tecnologias Utilizadas

- **Django**: Framework web principal para construção da aplicação.
- **Django REST Framework**: Para criação da API RESTful.
- **Django Channels**: Para funcionalidades em tempo real, como notificações e atualizações de status.
- **Celery**: Para gerenciamento de tarefas assíncronas, como envio de e-mails e processamento de pedidos.
- **PostgreSQL** (ou outro banco de dados) para armazenamento dos dados do sistema.

### 3. **Notificação em Tempo Real com Django Channels**

Utilizando o Django Channels, a aplicação oferece funcionalidades em tempo real, como:

- **Notificações de novos pedidos**: Sempre que um novo pedido for criado ou atualizado, uma notificação é enviada em tempo real para os administradores, informando sobre o status do pedido.
- **Atualizações em tempo real**: O painel de administração é atualizado em tempo real, permitindo que os administradores vejam as mudanças sem a necessidade de recarregar a página.
- **WebSockets**: A comunicação em tempo real é realizada via WebSockets, utilizando Channels para enviar notificações assíncronas.

### 4. **Processos Assíncronos com Celery**

O Celery é utilizado para processar tarefas de forma assíncrona e em segundo plano. Isso melhora o desempenho da aplicação e garante que tarefas demoradas não bloqueiem o fluxo de trabalho principal. Algumas das tarefas assíncronas implementadas incluem:

- **Envio de e-mails**: O envio de e-mails de confirmação de pedido, notificações de status de pedido, etc., é feito de maneira assíncrona, sem bloquear a aplicação.
- **Processamento de pedidos**: O processamento de pedidos, como verificar disponibilidade de estoque e processamento de pagamento, é realizado de forma assíncrona.
- **Tarefas de manutenção**: Outras tarefas como limpeza de dados antigos ou geração de relatórios também podem ser executadas em segundo plano usando o Celery.

---

Essas funcionalidades são essenciais para criar um painel de administração de e-commerce robusto, com a capacidade de consultar dados de produtos, gerar e controlar pedidos, e oferecer uma experiência em tempo real para os administradores.

## Contribuidores

Agradecemos a todos que contribuíram para o desenvolvimento deste projeto!

- **[Matheus-Matta](https://github.com/Matheus-Matta)**
- **[SamuVasco](https://github.com/SamuVasco)**