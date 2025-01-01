class Book:
  count = 0
  #atributos
  def __init__(self,title,author,gender):
    Book.count += 1
    self.id = Book.count
    self._title = title
    self._author = author
    self._gender = gender
  
  #metodo get
  @property
  def title(self):
    return self._title
  @property
  def author(self):
    return self._author
  @property
  def gender(self):
    return self._gender
  
  #metodo set
  @title.setter
  def title(self, title):
    self._title = title
  #metodo set
  @title.setter
  def title(self, author):
    self._author = author
  #metodo set
  @title.setter
  def title(self, gender):
    self._gender = gender