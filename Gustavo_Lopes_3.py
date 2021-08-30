class Livro:
    def __init__ (self, titulo, autor, paginas, preço):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.preço = preço

    def get_autor(self):
        return self.autor

    def set_preço(self, novo_preço):
        self.preço = novo_preço

    

if __name__ == "__main__":

    livro1 = Livro('O Hobbit', 'J.R.R. Tolkien', 227, 50)
    print('Titulos: ', livro1.titulo)
    print('Autor: ', livro1.autor)
    print('Páginas: ', livro1.paginas)
    print('Preço: ', livro1.preço)

    livro1.set_preço(100)
    print('Novo Preço: ', livro1.preço)

