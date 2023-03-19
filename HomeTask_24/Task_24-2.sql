CREATE VIEW amount_by_autor AS
SELECT autor_id, SUM(amount) AS SA
from  book1
GROUP BY autor_id;

CREATE VIEW min_s_amount AS
SELECT MIN(SA) AS MSA
FROM (SELECT *FROM amount_by_autor) que_1;

SELECT name_autor, SUM(amount) AS KOL
FROM autor INNER JOIN book1
ON autor.autor_id = book1.autor_id
GROUP BY name_autor
HAVING SUM(amount)=(SELECT * FROM min_s_amount )