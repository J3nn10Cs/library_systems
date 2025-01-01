from book import Book
class Library:
  def __init__(self,name):
    self._name = name
    self.list_book = []

  #metodo agregar un libro
  def add_book(self,title,author,gender):
    book = Book(title,author,gender)
    self.list_book.append(book)
  
  #metodo buscar libro por autor
  def search_book_author(self,author):
    book_found = []
    for book in self.list_book:
      if book._author == author:
        book_found.append(book)
    
    if book_found:
      print('Segun el autor : ')
      for book in book_found:
        print(f'''
          ID : {book.id}
          Titulo : {book.title}
          Autor : {book.author}
          Genero : {book.gender}
        ''')
    else:
      print(f'Autor {author} no encontrado')
    
  #buscar libro por genero
  def search_book_gender(self,gender):
    book_found = []
    for book in self.list_book:
      if book._gender == gender:
        book_found.append(book)
    
    if book_found:
      print('Segun el genero : ')
      for book in book_found:
        print(f'''
          ID : {book.id}
          Titulo : {book.title}
          Genero : {book.gender}
        ''')
    else:
      print(f'Genero {gender} no encontrado')
  
  #mostrar todos los libros
  def show_book(self):
    print(f'Todos los libros : ')
    for book in self.list_book:
      print(f'''
        Libro : {book.id}
        Titulo : {book.title}
        Autor : {book.author}
        Genero : {book.gender}
      ''')
  
  def show_book_id(self,id):
    book_found = None
    for book in self.list_book:
      if book.id == id:
        book_found = book
    
    if book_found is not None:
      print('Segun el ID : ')
      print(f'''
        ID : {book_found.id}
        Titulo : {book_found.title}
        Autor : {book_found.author}
        Genero : {book_found.gender}
      ''')