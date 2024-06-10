import pytest
from modules.common.database import Database

#Induvidual part

@pytest.mark.database
def test_max_qnt_product():
    db = Database()
    db.insert_product(99, 'test', 'data', 999)
    max_qnt = db.get_max_qnt_product()

    assert max_qnt[0][0] == 'test'
    assert max_qnt[0][1] == 'data'
    assert max_qnt[0][2] == 999

    db.delete_product_by_id(99)

@pytest.mark.database
def test_qnt_orders_by_products():
    db = Database()

    #insert test data
    db.insert_product(99, 'test', 'data', 999)
    db.insert_order(10001, 100, 99, '')
    db.insert_order(10002, 101, 99, '')

    qnt_orders_by_prod = db.get_qnt_orders_by_products()

    #move result data to dictionary 
    qnt_orders_by_prod_dict = {}
    for i in range(len(qnt_orders_by_prod)):
        qnt_orders_by_prod_dict[qnt_orders_by_prod[i][0]] = qnt_orders_by_prod[i][2]

    assert qnt_orders_by_prod_dict[99] == 2
    
    #remove test data
    db.delete_order_by_id(10001)
    db.delete_order_by_id(10002)
    db.delete_product_by_id(99)


@pytest.mark.database
def test_top_3_customers():
     db = Database()

     #insert test data
     db.insert_order(10001, 100, 99, '')
     db.insert_order(10002, 100, 99, '')
     db.insert_order(10005, 100, 99, '')
     db.insert_order(10003, 101, 99, '')
     db.insert_order(10004, 101, 99, '')
     db.add_сustomer(100, 'Boris', 'Mist Patona', 'Kyiv')
     db.add_сustomer(101, 'Ivan', 'Ratusha', 'Ivano-Frankivsk')

     top3 = db.get_top_3_customers_by_orders()

     #move result data to dictionary
     top3_dict = {}
     for i in range(len(top3)):
         top3_dict[top3[i][0]] = top3[i][1]
    
     assert top3_dict[100] == 3
     assert top3_dict[1] == 1

     #remove test data
     db.delete_customer_by_id(100)
     db.delete_customer_by_id(101)
     db.delete_order_by_id(10001)
     db.delete_order_by_id(10002)
     db.delete_order_by_id(10003)
     db.delete_order_by_id(10004)
     db.delete_order_by_id(10005)


@pytest.mark.database
def test_no_russian_letters():
     db = Database()

    #insert test data
     db.add_сustomer(100, 'Борыс', 'Mist Patona', 'Kyiv')
     db.add_сustomer(101, 'Ivan', 'Ratusha', 'Ivano-Frankivsk')

     string = db.avoid_russian_letters()

     assert len(string) == 1

     db.delete_customer_by_id(100)
     db.delete_customer_by_id(101)


#Main part

@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()

@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)

@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    quantity = db.select_product_qnt_by_id(1)

    assert quantity[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    quantity = db.select_product_qnt_by_id(4)

    assert quantity[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)

    rows = db.select_product_qnt_by_id(99)

    assert len(rows) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)

    assert len(orders) == 1
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'
