import sqlite3


db_path = 'C:\\Users\\temma\\Documents\\01 Learning\\Python_QA_Auto\\QA_Auto_Python'
db_name = '\\become_qa_auto.db'


class Database():

    def __init__(self):
        self.connection = sqlite3.connect(db_path + db_name)
        self.cursor = self.connection.cursor()

#Induvidual part

    def get_max_qnt_product(self):
        query = "SELECT name, description, quantity \
            FROM products \
            WHERE quantity = (SELECT MAX(quantity) FROM products)"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    

    def get_qnt_orders_by_products(self):
        query = "SELECT products.id, products.name, COUNT(orders.id) \
        FROM products JOIN orders ON products.id = orders.product_id  \
            GROUP BY products.name"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record


    def get_top_3_customers_by_orders(self):
        query = "SELECT customers.id, COUNT(orders.id) as qnt_orders \
            FROM customers JOIN orders ON customers.id = orders.customer_id  \
            GROUP BY customers.id ORDER BY qnt_orders DESC LIMIT 3"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record


    def avoid_russian_letters(self):
        query = "SELECT * FROM Customers \
            WHERE name||address||city LIKE '%ы%' \
            OR name||address||city LIKE '%э%' \
            OR name||address||city LIKE '%ъ%' \
            OR name||address||city LIKE '%ё%'"
            
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record


#methods for insertion and deletion test data

    def insert_order(self, order_id, customer_id, product_id, order_date):
        query = f"INSERT OR REPLACE INTO orders \
            VALUES ({order_id}, {customer_id}, {product_id}, '{order_date}')"
        self.cursor.execute(query)
        self.connection.commit()    

    
    def add_сustomer(self, customer_id, name, address, city):
        query = f"INSERT OR REPLACE INTO customers (id, name, address, city) \
            VALUES ({customer_id}, '{name}', '{address}', '{city}')"
        self.cursor.execute(query)
        self.connection.commit()    


    def delete_order_by_id(self, order_id):
        query = f"DELETE FROM orders WHERE id = {order_id}"
        self.cursor.execute(query)
        self.connection.commit()


    def delete_customer_by_id(self, customer_id):
        query = f"DELETE FROM customers WHERE id = {customer_id}"
        self.cursor.execute(query)
        self.connection.commit()


#Main part

    def test_connection(self):
        sqlite_version_query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_version_query)
        record = self.cursor.fetchall()
        print(f"SQLite version is: {record}")


    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    

    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    

    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()


    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    

    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()


    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()


    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = f"SELECT orders.id, customers.name, products.name, \
            products.description, orders.order_date \
            FROM orders JOIN customers ON orders.customer_id = customers.id \
            JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record