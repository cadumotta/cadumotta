import json
import os

# Classe base: Pessoa (Usuário da biblioteca ou Autor)
class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    # Getters e Setters
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    def exibir_info(self):
        return f"Nome: {self.__nome}, Idade: {self.__idade}"


# Classe Usuário (Herda de Pessoa)
class Usuario(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.__matricula = matricula
        self.__livros_emprestados = []

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    def emprestar_livro(self, livro):
        if isinstance(livro, Livro):
            self.__livros_emprestados.append(livro)

    def devolver_livro(self, titulo):
        self.__livros_emprestados = [
            livro for livro in self.__livros_emprestados if livro.titulo != titulo
        ]

    def exibir_info(self):
        livros = ', '.join([livro.titulo for livro in self.__livros_emprestados]) or "Nenhum"
        return f"{super().exibir_info()}, Matrícula: {self.__matricula}, Livros Emprestados: {livros}"


# Classe Livro
class Livro:
    def __init__(self, titulo, autor, ano):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano

    # Getters e Setters
    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor):
        self.__autor = autor

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    def exibir_info(self):
        return f"Título: {self.__titulo}, Autor: {self.__autor}, Ano: {self.__ano}"


# Classe Biblioteca
class Biblioteca:
    def __init__(self, nome):
        self.__nome = nome
        self.__usuarios = []
        self.__livros = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def adicionar_livro(self, livro):
        if isinstance(livro, Livro):
            self.__livros.append(livro)

    def remover_livro(self, titulo):
        self.__livros = [livro for livro in self.__livros if livro.titulo != titulo]

    def cadastrar_usuario(self, usuario):
        if isinstance(usuario, Usuario):
            self.__usuarios.append(usuario)

    def exibir_info(self):
        info = f"Biblioteca: {self.__nome}\nLivros Disponíveis:\n"
        if self.__livros:
            info += '\n'.join([livro.exibir_info() for livro in self.__livros])
        else:
            info += "Nenhum livro cadastrado"

        info += "\n\nUsuários Cadastrados:\n"
        if self.__usuarios:
            info += '\n'.join([usuario.exibir_info() for usuario in self.__usuarios])
        else:
            info += "Nenhum usuário cadastrado"

        return info

    def salvar_em_arquivo(self, arquivo):
        dados = {
            "nome": self.__nome,
            "livros": [
                {"titulo": livro.titulo, "autor": livro.autor, "ano": livro.ano}
                for livro in self.__livros
            ],
            "usuarios": [
                {
                    "nome": usuario.nome,
                    "idade": usuario.idade,
                    "matricula": usuario.matricula,
                    "livros_emprestados": [livro.titulo for livro in usuario._Usuario__livros_emprestados]
                }
                for usuario in self.__usuarios
            ],
        }
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    @staticmethod
    def carregar_de_arquivo(arquivo):
        with open(arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)

        biblioteca = Biblioteca(dados["nome"])

        # Adicionar livros
        for livro_dados in dados["livros"]:
            biblioteca.adicionar_livro(
                Livro(livro_dados["titulo"], livro_dados["autor"], livro_dados["ano"])
            )

        # Adicionar usuários e restaurar livros emprestados
        for usuario_dados in dados["usuarios"]:
            usuario = Usuario(
                usuario_dados["nome"],
                usuario_dados["idade"],
                usuario_dados["matricula"]
            )
            # Emprestar livros novamente
            for titulo in usuario_dados["livros_emprestados"]:
                for livro in biblioteca.__livros:
                    if livro.titulo == titulo:
                        usuario.emprestar_livro(livro)
            biblioteca.cadastrar_usuario(usuario)

        return biblioteca

    # Métodos interativos
    def adicionar_usuario_interativo(self, arquivo_json):
        print("\n--- Adicionar Novo Usuário ---")
        nome = input("Nome do usuário: ")
        idade = int(input("Idade do usuário: "))
        matricula = input("Matrícula do usuário: ")
        usuario = Usuario(nome, idade, matricula)
        self.cadastrar_usuario(usuario)
        self.salvar_em_arquivo(arquivo_json)  # Salva após adicionar
        print(f"Usuário '{nome}' adicionado com sucesso!")

    def adicionar_livro_interativo(self, arquivo_json):
        print("\n--- Adicionar Novo Livro ---")
        titulo = input("Título do livro: ")
        autor = input("Autor do livro: ")
        ano = int(input("Ano de publicação: "))
        livro = Livro(titulo, autor, ano)
        self.adicionar_livro(livro)
        self.salvar_em_arquivo(arquivo_json)  # Salva após adicionar
        print(f"Livro '{titulo}' adicionado com sucesso!")


# Exemplo de uso
def main():
    NOME_ARQUIVO = "biblioteca.json"

    # Tenta carregar dados se o arquivo existir
    if os.path.exists(NOME_ARQUIVO):
        biblioteca = Biblioteca.carregar_de_arquivo(NOME_ARQUIVO)
    else:
        biblioteca = Biblioteca("Biblioteca Central")

    while True:
        print("\n--- Sistema de Gestão da Biblioteca ---")
        print("1. Adicionar Livro")
        print("2. Adicionar Usuário")
        print("3. Exibir Informações da Biblioteca")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            biblioteca.adicionar_livro_interativo(NOME_ARQUIVO)
        elif opcao == "2":
            biblioteca.adicionar_usuario_interativo(NOME_ARQUIVO)
        elif opcao == "3":
            print(biblioteca.exibir_info())
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
