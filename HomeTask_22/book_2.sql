CREATE TABLE book_2
(book_id int PRIMARY KEY,
title VARCHAR(50), 
AUTOR VARCHAR(50),
price int, 
amount int)
SELECT * FROM book_2
INSERT INTO book_2 VALUES
(1, 'Мастер и Маргарита', 'Булгаков', 670, 3),
(2, 'Белая гвардия', 'Булгаков', 540, 5),
(3, 'Идиот', 'Достаевский', 460, 10),
(4, 'Братья Карамазовы','Достаевский', 799, 2),
(5, 'Стихотворения', 'Есенин', 650, 15),
(6, 'Стихотворения и поэмы', 'Есенин',560, 10)
SELECT * FROM book_2 ORDER BY autor, price DESC