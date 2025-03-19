# Sistema Hospitalar

Este é um sistema hospitalar desenvolvido em Django para gerenciar pacientes, médicos, enfermeiros, consultas e medicamentos. O sistema permite que diferentes tipos de usuários (administradores, médicos e pacientes) acessem e gerenciem informações relevantes de acordo com suas permissões.


## Funcionalidades

### Administrador
- Gerenciamento de pacientes
- Gerenciamento de médicos
- Gerenciamento de enfermeiros
- Gerenciamento de consultas
- Gerenciamento de medicamentos

### Médico
- Visualização de consultas agendadas e passadas
- Edição de consultas (diagnóstico, observações, medicação)
- Visualização de lista de pacientes
- Visualização de lista de medicamentos

### Paciente
- Login utilizando CPF
- Visualização de consultas agendadas e passadas

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/yTheu/Hospital.git
    cd Hospital
    ```

2. Crie um ambiente virtual e ative-o:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Execute as migrações do banco de dados:
    ```sh
    python manage.py migrate
    ```

5. Crie um superusuário para acessar a área administrativa:
    ```sh
    python manage.py createsuperuser
    ```

6. Inicie o servidor de desenvolvimento:
    ```sh
    python manage.py runserver
    ```

7. Acesse o sistema no navegador:
    ```
    http://127.0.0.1:8000/
    ```

## Estrutura de Diretórios

- `app1/`: Contém a aplicação principal com modelos, formulários, visualizações e templates.
- `hospital_system/`: Contém as configurações do projeto Django.
- `templates/`: Contém os templates HTML organizados por diretórios para cada tipo de usuário (adm, medico, paciente).

## Modelos

### Paciente
- `nome`
- `sintoma`
- `situacao`
- `estado_consulta`
- `cpf`
- `data_nascimento`
- `endereco`
- `telefone`
- `telefone_familiar`
- `user` (relacionamento com o modelo User do Django)

### Médico
- `nome`
- `cpf`
- `especializacao`
- `disponibilidade`
- `contratada`
- `data_nascimento`
- `endereco`
- `telefone`
- `email`
- `genero`
- `salario`
- `turno`
- `data_contratacao`

### Enfermeiro
- `nome`
- `cpf`
- `disponibilidade`
- `contratada`
- `endereco`
- `telefone`
- `data_nascimento`
- `data_contratacao`
- `email`
- `genero`
- `salario`
- `turno`

### Remédio
- `nome`
- `laboratorio`
- `bula`
- `tipo`
- `quantidade_estoque`
- `data_validade`

### Consulta
- `id_paciente` (relacionamento com Paciente)
- `id_enfermeiro` (relacionamento com Enfermeiro)
- `id_medico` (relacionamento com Médico)
- `id_medicação` (relacionamento com Remédio)
- `sintoma`
- `data_consulta`
- `observacao`
- `diagnostico`

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Colaboradores

@lipe
