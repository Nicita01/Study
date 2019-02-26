--  1. Необхідно знайти кількість рядків в таблиці, що містить більше ніж
--     2147483647 записів. Напишіть код для MS SQL Server та ще однієї
--     СУБД (на власний вибір).

-- для MS SQL Server. Для відношень з кількістю кортежів > 2^31-1, існує
-- функція COUNT_BIG, що не викидає помилку.
SELECT COUNT_BIG(*) FROM tableName;
-- для PostgreSQL. Функція count повертає значення типу bigint (до 8 байт)
SELECT count(*) FROM tableName;

--  2. Підрахувати довжину свого прізвища за допомогою SQL.
SELECT char_length('Machekhin');

--  3. У рядку з своїм прізвищем, іменем, та по-батькові замінити
--     пробіли на знак ‘_’ (нижнє підкреслення).
SELECT replace('Machekhin Mykyta Andriyovych', ' ', '_');

--  4. Створити генератор імені електронної поштової скриньки,
--     що шляхом конкатенації об’єднував би дві перші літери з колонки
--     імені, та чотири перші літери з колонки прізвища користувача, що
--     зберігаються в базі даних, а також домену з вашим прізвищем.

-- створимо відношення з іменами та прізвищами людей
CREATE TABLE IF NOT EXISTS full_name (
  first_name varchar(80),
  last_name varchar(80)
);
-- заповнимо деякими даними для тестів
INSERT INTO full_name VALUES
  ('Nikita', 'Machekhin'),
  ('Ivan', 'Ivanov');
-- зробимо запит для генерації скриньок
SELECT concat(
  substring(first_name from 1 for 2),
  substring(last_name from 1 for 4),
  '@machekhin')
FROM full_name;
-- видалимо тимчасову таблицю
DROP TABLE full_name;

--  5. За допомогою SQL визначити, в який день тиждня ви народилися.
SELECT EXTRACT(ISODOW FROM TIMESTAMP '2000-05-29');

-- Northwind:

-- 1. Вивести усі данні по продуктам, їх категоріям, та постачальникам,
--    навіть якщо останні з певних причин відсутні.
SELECT *
FROM products
  INNER JOIN categories ON products.category_id = categories.category_id
  LEFT JOIN suppliers ON products.supplier_id = suppliers.supplier_id;

-- 2.	Показати усі замовлення, що були зроблені в квітні 1988 року та не були відправлені.
SELECT * FROM orders
WHERE EXTRACT(MONTH FROM order_date) = 4 AND
EXTRACT(YEAR FROM order_date) = 1988 AND
shipped_date IS NULL;
-- 3. Відібрати усіх працівників, що відповідають за північний регіон.

SELECT DISTINCT employees.*
FROM employees
  INNER JOIN employee_territories ON
    employees.employee_id = employee_territories.employee_id
  INNER JOIN territories ON
    employee_territories.territory_id = territories.territory_id
  INNER JOIN region ON territories.region_id = region.region_id
WHERE region.region_description = 'Northern';

-- 4. Вирахувати загальну вартість з урахуванням знижки усіх замовлень,
--    що були здійснені на непарну дату.

  SELECT sum(unit_price * quantity - unit_price * quantity * discount)
  FROM order_details RIGHT JOIN orders
    ON orders.order_id = order_details.order_id
  WHERE EXTRACT(DAY FROM order_date)::int % 2 = 1;

-- 5.Знайти адресу відправлення замовлення з найбільшою ціною
--   (враховуючи усі позиції замовлення, їх вартість, кількість,
--   та наявність знижки).

-- створимо представлення, що для кожного замовлення створить кортеж
-- з адресою та сумою замовлення
CREATE OR REPLACE VIEW sums AS
  SELECT 
    orders.ship_address,
    sum(unit_price * quantity - unit_price * quantity * discount) AS sum
  FROM orders LEFT JOIN order_details
    ON orders.order_id = order_details.order_id
  GROUP BY orders.order_id;
-- знайдемо адресу, що відповідає найбільшій вартості
SELECT ship_address
FROM sums
WHERE sum = (SELECT max(sum) FROM sums);
