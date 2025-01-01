from library import Library
from book import Book
print('Sistema de biblioteca')

libreary1 = Library('Chileno Santisteban')

libreary1.add_book('Los perros','Mario Vargar Llosa','Romantico')
libreary1.add_book('100 años de soledad','Gabriel Garcia Marquez','Novela')
libreary1.add_book('El diario de Nicolas','Mario Vargar Llosa','Juego')
libreary1.add_book('Hola','Mario Vargar Llosa','Romantico')

libreary1.search_book_author('Mario Vargar Llosa')

#buscar por id
libreary1.show_book_id(2)

#motrar todos los libros
libreary1.show_book()

#MOSTRAR SEGUN GENEO
libreary1.search_book_gender('Novela')