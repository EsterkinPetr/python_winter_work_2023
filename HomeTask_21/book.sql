CREATE TABLE book
(book_id int, book_title text, book_autor text, publisher_id int)
INSERT INTO book VALUES
(1, 'Посмотри на меня', 'Джим Арноски', 101),
(2, 'Мастер и Маргарита','Михаил Булгаков', 102),
(3, 'Три мушкетера', 'Александр Дюма', 103),
(4, 'Идиот','Федор Достоевский', 104),
(5, 'Муму', 'Иван Тургеньев', 105),
(6, 'Граф Монте Кристо', 'Александр Дюма', 106),
(7, 'Собачье сердце', 'Михаил Булгаков', 107)
SELECT * FROM book
SELECT book_title, publisher_id FROM book WHERE book_autor = 'Александр Дюма' 
SELECT * FROM book WHERE book_id >3
SELECT book_id, book_autor FROM book WHERE book_title = 'Идиот'
SELECT * FROM book WHERE book_autor != 'Федор Достаевский'