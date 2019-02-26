-- 1. Вивести за допомогою команди SELECT своє прізвище, ім’я та по-батькові на екран.
SELECT 'Machekhin Mykyta Andriyovych' AS "full_name";

-- 2. Вибрати всі дані з таблиці Products.
SELECT * FROM products;

-- 3. Обрати всі назви продуктів з тієї ж таблиці, продаж яких припинено.
SELECT product_name FROM products
WHERE discontinued = 1;

-- 4. Вивести всі міста клієнтів уникаючи дублікатів.
SELECT DISTINCT city FROM customers;

-- 5. Вибрати всі назви компаній-постачальників в порядку зворотньому
-- алфавітному.
SELECT company_name FROM suppliers
ORDER BY company_name DESC;

-- 6. Отримати всі деталі замовлень, замінивши назви стовбчиків на їх
-- порядковий номер.
SELECT
  order_id AS "1",
  product_id AS "2",
  unit_price AS "3",
  quantity AS "4",
  discount AS "5"
FROM order_details;

-- 7. Вивести всі контактні імена клієнтів, що починаються з першої літери
-- вашого прізвища, імені, по-батькові.
SELECT contact_name FROM customers
WHERE 
  contact_name LIKE 'M%' OR
  contact_name LIKE 'm%' OR
  contact_name LIKE 'A%' OR
  contact_name LIKE 'a%';

-- 8. Показати усі замовлення, в адресах доставки яких є пробіл.
SELECT * FROM orders
WHERE ship_address LIKE '% %';

-- 9. Вивести назви тих продуктів, що починаються на знак % або _,
-- а закінчуються на останню літеру вашого імені.
SELECT product_name FROM products
WHERE
  product_name LIKE '\%%m' OR
  product_name LIKE '\%%M' OR
  product_name LIKE '\_%m' OR
  product_name LIKE '\_%M'