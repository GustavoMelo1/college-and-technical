--technical-test 2

SELECT DISTINCT c.name
FROM clients c
INNER JOIN pedidos p ON c.id = p.cliente_id
WHERE c.ativo = TRUE 
  AND p.status = 'pago';

SELECT c.city, SUM(p.value) AS total_spent
FROM clients c
INNER JOIN orders p ON c.id = p.client_id
WHERE p.status = 'paid'
GROUP BY c.city
ORDER BY total_spent DESC;

SELECT c.name 
FROM clients c
LEFT JOIN orders p ON c.id = p.client_id
WHERE p.id IS NULL;