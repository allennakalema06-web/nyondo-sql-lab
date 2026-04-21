import sqlite3
conn = sqlite3.connect('nyondo_stock.db')
# Query A: Get every column of every product
conn.execute('''
SELECT *
FROM products;
''')
print("\nQuery A:")
rows = conn.execute("SELECT * FROM products;").fetchall()
for r in rows:
    print(r)

# Query B: Get only the name and price of all products
conn.execute('''
SELECT name, price
FROM products;  
                        
''')
print("\nQuery B:")
rows = conn.execute("SELECT name, price FROM products;").fetchall()
for r in rows:
    print(r)
#  Query C: Get full details of the product with id = 3
conn.execute('''
SELECT *
FROM products
WHERE id = 3;               
                        
''')
print("\nQuery C:")
rows = conn.execute("SELECT * FROM products WHERE id = 3;").fetchall()
for r in rows:
    print(r)

# Query D: Find all products whose name contains 'sheet' - use a partial match
conn.execute('''
SELECT *
FROM products  
WHERE name LIKE '%sheet%';             
                        
''')
print("\nQuery D:")
rows = conn.execute("SELECT * FROM products WHERE name LIKE '%sheet%';").fetchall()
for r in rows:
    print(r)

# Query E: Get all products sorted by price, highest first
conn.execute('''
SELECT *
FROM products  
ORDER BY price DESC;             
                        
''')
print("\nQuery E:")
rows = conn.execute("SELECT * FROM products ORDER BY price DESC;").fetchall()
for r in rows:
    print(r)
# Query F: Get only the 2 most expensive products
conn.execute('''
SELECT name, price
FROM products  
ORDER BY price DESC
LIMIT 2;                       
                        
''')
print("\nQuery F:")
rows = conn.execute("SELECT name, price FROM products ORDER BY price DESC LIMIT 2;").fetchall()
for r in rows:
    print(r)

# Query G: Update the price of Cement (id=1) to 38,000 then SELECT * to confirm
conn.execute('''
UPDATE products
SET price = 38000
WHERE id = 1;                                             
                        
''')
conn.commit()

print("\nQuery G:")
rows = conn.execute("SELECT * FROM products;").fetchall()
for r in rows:
    print(r)

