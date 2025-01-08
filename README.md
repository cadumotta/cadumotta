# Sistema de Gestão de Biblioteca

## Descrição
Este projeto é um sistema de gestão de biblioteca que utiliza conceitos de Orientação a Objetos (OO) para gerenciar usuários e livros. Ele permite realizar operações como cadastro, listagem e serialização dos dados para arquivos JSON.

## Funcionalidades
- **Adicionar Usuários:** Cadastro de novos usuários, como estudantes ou professores.
- **Cadastrar Livros:** Inclusão de novos livros no sistema.
- **Listar Usuários e Livros:** Visualização detalhada das informações cadastradas.
- **Serialização e Desserialização:** Salvar e carregar dados do sistema utilizando arquivos JSON.

## Requisitos
- **Python:** Versão 3.7 ou superior.
- Biblioteca **json** (já incluída nas distribuições padrão do Python).

## Como Usar
### 1. Clonar o Repositório
```bash
# Clone este repositório
git clone https://github.com/seu-repo/sistema-biblioteca.git

# Navegue até o diretório do projeto
cd sistema-biblioteca
```

### 2. Executar o Sistema
```bash
# Execute o arquivo principal
python main.py
```

## Estrutura do Código
### Classes Principais
- **Pessoa:** Classe base que representa uma pessoa no sistema.
- **Usuario:** Subclasse que herda de `Pessoa`, com atributos adicionais para perfil de usuário.
- **Livro:** Representa os livros da biblioteca com atributos como título, autor e ano de publicação.
- **Biblioteca:** Gerencia listas de usuários e livros, com métodos para cadastro, listagem e serialização.

### Conceitos de Orientação a Objetos Implementados
- **Hierarquia:** `Pessoa` é a classe base de `Usuario`.
- **Herança:** `Usuario` herda atributos e métodos de `Pessoa`.
- **Polimorfismo:** Sobrescrita do método `exibir_info` nas subclasses.
- **Encapsulamento:** Atributos privados (âmbito controlado com prefixo `__`).
- **Getters e Setters:** Acessores e modificadores para todos os atributos.

### Estrutura de Arquivos
```plaintext
sistema-biblioteca/
├── main.py         # Arquivo principal do sistema.
├── README.md       # Documentação do projeto.
├── biblioteca.json # Arquivo gerado com dados serializados.
```

## Exemplos de Uso
### Adicionar Usuários
```python
# Criar um usuário
usuario = Usuario("Maria", 25, "Estudante")
biblioteca.adicionar_usuario(usuario)
```

### Adicionar Livros
```python
# Criar um livro
livro = Livro("Dom Quixote", "Miguel de Cervantes", 1605)
biblioteca.adicionar_livro(livro)
```

### Exibir Informações
```python
# Exibir dados da biblioteca
print(biblioteca.exibir_info())
```

### Salvar Dados em JSON
```python
# Salvar informações da biblioteca em um arquivo
biblioteca.salvar_em_arquivo("biblioteca.json")
```

### Carregar Dados de JSON
```python
# Carregar informações de um arquivo
biblioteca_carregada = Biblioteca.carregar_de_arquivo("biblioteca.json")
print(biblioteca_carregada.exibir_info())
```

## Conclusão
Este sistema atende aos seguintes requisitos de Orientação a Objetos:
- Hierarquia.
- Herança.
- Polimorfismo.
- Serialização (JSON).
- Encapsulamento total.
- Getters e Setters.

