import re
import sqlite3
conn = sqlite3.connect('nyondo_stock.db')

# TODO: rewrite using ? placeholder - never use f-strings in SQL
def search_product_safe(name):
    # your code here
    if not name.strip():
        return "Rejected: empty search"
    
    if "<" in name or ">" in name:
        return "Rejected: invalid characters"
    query = "SELECT * FROM products WHERE name LIKE ?"
    rows = conn.execute(query, (f"%{name}%",)).fetchall()
    return rows


def login_safe(username, password):
    # your code here
    if not username or not password:
        return "Rejected: empty fields"
    
    if " " in username:
        return "Rejected: username contains spaces"
    
    if len(password) < 4:
        return "Rejected: password too short"
    
    if not re.match("^[a-zA-Z0-9]+$", username):
        return "Rejected: invalid username format"
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    print(f'Query (safe): {query}')
    print(f'Parameters: ({username}, {password})')
    row = conn.execute(query, (username, password)).fetchone()
    print(f'Result: {row}\n')
    return row

# These must ALL return [] or None when you run them
print('Test 1:', search_product_safe("' OR 1=1--"))
print('Test 2:', search_product_safe("' UNION SELECT id,username,password,role FROM users--"))
print('Test 3:', login_safe("admin'--", 'anything'))
print('Test 4:', login_safe("' OR '1'='1", "' OR '1'='1"))


print('Test 5:', search_product_safe('cement')) #-> works normally
print('Test 6:', search_product_safe('')) #-> rejected
print('Test 7:', search_product_safe('<script>')) #-> rejected 
print('Test 8:', login_safe('admin', 'admin123')) #-> works 
print('Test 9:', login_safe('admin','ab')) #-> rejected (too short)
print('Test 10:', login_safe('ad min', 'pass123')) #-> rejected (space in username)