# Gerenciador de Tarefas

Bem-vindo ao Gerenciador de Tarefas, um aplicativo web para gerenciar suas tarefas diárias de forma eficiente. Este projeto foi desenvolvido utilizando Django e Bootstrap para fornecer uma interface amigável e responsiva.

## Funcionalidades

- **Autenticação de Usuário:** Registro, login e gerenciamento de perfil.
- **Gerenciamento de Tarefas:** Criação, visualização, edição e exclusão de tarefas.
- **Classificação de Tarefas:** Definição de prioridades (Baixa, Média, Alta) e categorização por projetos e tags.
- **Visualização de Tarefas:** Exibição de tarefas totais, pendentes, concluídas e tarefas específicas do dia.

## Tecnologias Utilizadas

- Django
- Bootstrap
- Crispy Forms
- SQLite (Banco de Dados padrão)

## Instalação

Siga as etapas abaixo para configurar e executar o projeto localmente.

### Pré-requisitos

- Python 3.6 ou superior
- Virtualenv

### Passos

1. **Clone o repositório:**
    ```bash
    git clone https://github.com/dnsouzadev/gerenciador-tarefas.git
    cd gerenciador-tarefas
    ```

2. **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Realize as migrações do banco de dados:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Crie um superusuário (opcional, para acesso ao admin):**
    ```bash
    python manage.py createsuperuser
    ```

6. **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

7. **Acesse o aplicativo:**
    Abra o navegador e vá para `http://127.0.0.1:8000/`

## Uso

Após instalar e executar o servidor de desenvolvimento, você pode acessar a aplicação para:

1. Registrar um novo usuário ou fazer login com um usuário existente.
2. Criar novos projetos e tags.
3. Adicionar, editar ou excluir tarefas associando-as a projetos e tags.
4. Visualizar o dashboard com estatísticas de tarefas.

## Estrutura do Projeto

- `autenticacao/` - Gerencia a autenticação e o perfil do usuário.
- `tasks/` - Gerencia as funcionalidades de tarefas, incluindo modelos, formulários e views.
- `templates/` - Contém os templates HTML para as views.
- `static/` - Arquivos estáticos (CSS, JS) usados no projeto.

## Contribuindo

Se você quiser contribuir com o projeto, siga os passos abaixo:

1. **Fork o repositório:**
    Clique no botão "Fork" no canto superior direito da página do repositório.

2. **Clone o seu fork localmente:**
    ```bash
    git clone https://github.com/seu-usuario/gerenciador-tarefas.git
    cd gerenciador-tarefas
    ```

3. **Crie uma branch para sua feature ou correção:**
    ```bash
    git checkout -b minha-feature
    ```

4. **Faça suas alterações e comite:**
    ```bash
    git commit -m "Adiciona minha nova feature"
    ```

5. **Envie suas alterações para o GitHub:**
    ```bash
    git push origin minha-feature
    ```

6. **Abra um Pull Request:**
    Vá até o repositório original e clique em "New Pull Request".

## Licença

Este projeto está licenciado sob os termos da [MIT License](LICENSE).

---

Se tiver qualquer dúvida ou problema, sinta-se à vontade para abrir uma issue no repositório.
