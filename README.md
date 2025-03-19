# 🏥 Sistema Hospitalar

[![Django](https://img.shields.io/badge/Django-4.x-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Contributors](https://img.shields.io/github/contributors/yTheu/Hospital)](https://github.com/yTheu/Hospital/graphs/contributors)
[![Stars](https://img.shields.io/github/stars/yTheu/Hospital?style=social)](https://github.com/yTheu/Hospital/stargazers)

Este é um sistema hospitalar desenvolvido com **Django**, criado para facilitar o gerenciamento de **pacientes**, **médicos**, **enfermeiros**, **consultas** e **medicamentos**.  
O sistema permite que diferentes tipos de usuários (administradores, médicos e pacientes) acessem e gerenciem informações conforme suas permissões.

---

## ⚙️ Funcionalidades

### 👩‍💼 Administrador
- Gerenciamento de **pacientes**, **médicos**, **enfermeiros**
- Gerenciamento de **consultas** e **medicamentos**

### 🩺 Médico
- Visualização e edição de **consultas**
- Acesso à lista de **pacientes** e **medicamentos**

### 👤 Paciente
- Login com **CPF**
- Visualização de **consultas agendadas e anteriores**

---

## 🚀 Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/yTheu/Hospital.git
cd Hospital

# 2. Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Instale o Django
pip install django

# 4. Aplique as migrações
python manage.py migrate

# 5. Crie o superusuário
python manage.py createsuperuser

# 6. Inicie o servidor
python manage.py runserver

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

## 🤝 Contribuindo

Contribuições são muito bem-vindas!  
Você pode abrir uma **issue** para sugerir melhorias ou enviar um **Pull Request (PR)** com novas funcionalidades ou correções.

### Como contribuir:

```bash
# 1. Faça um fork do projeto
# 2. Crie uma branch com a sua feature
git checkout -b minha-feature

# 3. Commit suas alterações
git commit -m "feat: adiciona nova feature"

# 4. Envie para o repositório remoto
git push origin minha-feature

# 5. Abra um Pull Request

## Colaboradores

[@Lipe099](https://github.com/Lipe099) 
[@yTheu]{hhtps://github.com/yTheu) 
