import psycopg2
from BusinessObject import Customer as CustomerEntity
class Customer:
    def __init__(self,ConnectionData):
        self.ConnectionData = ConnectionData
    def insert(self,customer):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "INSERT INTO TblCustomers(CustomerName,ContactName,Address,City,PostalCode,Country) VALUES (%s,%s,%s,%s,%s,%s)"
            record_to_insert = (customer.CustomerName,customer.ContactName,customer.Address,customer.City,customer.PostalCode,customer.Country)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert TblCustomers successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_all(self):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM TblCustomers"
            cur.execute(sql)
            con.commit()           
            rows = cur.fetchall()
            result = []
            for row in rows:
                c = CustomerEntity()
                c.fetch_data(row)
                result.append(c.to_json())
            con.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_by_id(self,customer: CustomerEntity):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM TblCustomers WHERE customerid=%s"

            cur.execute(sql,(customer.CustomerID, ))
            con.commit()           
            row = cur.fetchone()
            if row:
                c = CustomerEntity()
                c.fetch_data(row)
                return c, 200
            con.close()
            return "Customer ID not found", 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def update(self, customer: CustomerEntity):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "UPDATE TblCustomers SET customername=%s,contactname=%s, address=%s,city=%s, postalcode=%s, country=%s WHERE customerid=%s"
            cur.execute(sql,(customer.CustomerName, customer.ContactName, customer.Address, customer.City, customer.PostalCode, customer.Country, customer.CustomerID))
            con.commit()           
            row = cur.rowcount
            if row>0:
                return "Updated Customer", 200
            con.close()
            return "Customer ID not found", 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def delete(self, customer: CustomerEntity):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "DELETE FROM TblCustomers WHERE customerid=%s"
            cur.execute(sql,(customer.CustomerID,))
            con.commit()           
            row = cur.rowcount
            if row>0:
                return "Delete Customer", 200
            con.close()
            return "Customer ID not found", 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()
#Categorie
class Categorie:
 def __init__(self,ConnectionData):
        self.ConnectionData = ConnectionData
    def insert(self,Categories):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "INSERT INTO TblCategories(CategoryName,Description) VALUES (%s,%s)"
            record_to_insert = (Categories.CategoryName,Categories.Description)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert TblCategories successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_all(self):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM TblCategories"
            cur.execute(sql)
            con.commit()           
            rows = cur.fetchall()
            result = []
            for row in rows:
                c = CategoryEntity()
                c.fetch_data(row)
                result.append(c.to_json())
            con.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_by_id(self,Categorie: CategoryEntity):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM TblCategories WHERE Categorieid=%s"
            cur.execute(sql,(Categorie.CategoryID, ))
            con.commit()           
            row = cur.fetchone()
            if row:
                c = CategoryEntity()
                c.fetch_data(row)
                return c, 200
            con.close()
            return "Categorie ID not found", 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def update(self, Categorie: CategoryEntity):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "UPDATE TblCategories SET CategoryName=%s,Description=%s"
            cur.execute(sql,(Categorie.CategoryName, Categorie.Description, Categorie.CategoryID))
            con.commit()           
            row = cur.rowcount
            if row>0:
                return "Updated Categorie", 200
            con.close()
            return "Categorie ID not found", 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def delete(self, Categorie: CategoryEntity):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "DELETE FROM TblCategories WHERE Categorieid=%s"
            cur.execute(sql,(Categorie.CustomerID,))
            con.commit()           
            row = cur.rowcount
            if row>0:
                return "Delete Categorie", 200
            con.close()
            return "Categorie ID not found", 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()
#Employee
class Employee:
    def __init__(self, ConnectionData):
        self.ConnectionData = ConnectionData

    def insert(self, employee: EmployeeEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "INSERT INTO tblemployees(lastname, firstname, birthdate, photo, notes) VALUES (%s, %s, %s, %s, %s)"
            record_to_insert = (employee.LastName, employee.FirstName, employee.Birthdate, employee.Photo, employee.Notes)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert tblemployees successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_all(self):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM tblemployees"
            cur.execute(sql)
            con.commit()
            rows = cur.fetchall()
            result = []
            for row in rows:
                c = EmployeeEntity()
                c.fetch_data(row)            
                result.append(c.to_json())
            con.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_by_id(self, employee: EmployeeEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM tblemployees WHERE employeeid=%s"
            cur.execute(sql, (employee.EmployeeID, ))
            con.commit()
            row = cur.fetchone()
            if row:
                c = EmployeeEntity()
                c.fetch_data(row)
                return c, 200
            con.close()
            return 'Employee ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def update(self, employee: EmployeeEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "UPDATE tblemployees SET lastname=%s, firstname=%s, birthdate=%s, photo=%s, notes=%s WHERE employeeid=%s"
            cur.execute(sql, (employee.LastName, employee.FirstName, employee.Birthdate, employee.Photo, employee.Notes, employee.EmployeeID))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Updated employee', 200
            con.close()
            return 'Employee ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def delete(self, employee: EmployeeEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "DELETE FROM tblemployees WHERE employeeid=%s"
            cur.execute(sql, (employee.EmployeeID, ))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Deleted employee', 200
            con.close()
            return 'Employee ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

#Order
class Order:
    def __init__(self, ConnectionData):
        self.ConnectionData = ConnectionData

    def insert(self, order: OrderEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "INSERT INTO tblorders(customerid, employeeid, orderdate, shipperid) VALUES (%s, %s, %s, %s)"
            record_to_insert = (order.CustomerID, order.EmployeeID, order.OrderDate, order.ShipperID)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert tblorders successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_all(self):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM tblorders"
            cur.execute(sql)
            con.commit()
            rows = cur.fetchall()
            result = []
            for row in rows:
                c = OrderEntity()
                c.fetch_data(row)            
                result.append(c.to_json())
            con.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_by_id(self, order: OrderEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM tblorders WHERE orderid=%s"
            cur.execute(sql, (order.OrderID, ))
            con.commit()
            row = cur.fetchone()
            if row:
                c = OrderEntity()
                c.fetch_data(row)
                return c, 200
            con.close()
            return 'order ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def update(self, order: OrderEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "UPDATE tblorders SET customerid=%s, employeeid=%s, orderdate=%s, shipperid=%s WHERE orderid=%s"
            cur.execute(sql, (order.CustomerID, order.EmployeeID, order.OrderDate, order.ShipperID, order.OrderID))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Updated order', 200
            con.close()
            return 'order ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def delete(self, order: OrderEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "DELETE FROM tblorders WHERE orderid=%s"
            cur.execute(sql, (order.OrderID, ))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Deleted order', 200
            con.close()
            return 'order ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()
#OrderDetail
class OrderDetail:
    def __init__(self, ConnectionData):
        self.ConnectionData = ConnectionData

    def insert(self, orderr: OrderDetailEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "INSERT INTO tblorderdetails(orderid, productid, quantity) VALUES (%s, %s, %s)"
            record_to_insert = (orderr.OrderID, orderr.ProductID, orderr.Quantity)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert tblorderdetails successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_all(self):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM tblorderdetails"
            cur.execute(sql)
            con.commit()
            rows = cur.fetchall()
            result = []
            for row in rows:
                c = OrderDetailEntity()
                c.fetch_data(row)            
                result.append(c.to_json())
            con.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_by_id(self, orderr: OrderDetailEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM tblorderdetails WHERE orderdetailid=%s"
            cur.execute(sql, (orderr.OrderDetailID, ))
            con.commit()
            row = cur.fetchone()
            if row:
                c = OrderDetailEntity()
                c.fetch_data(row)
                return c, 200
            con.close()
            return 'order detail ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def update(self, orderr: OrderDetailEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "UPDATE tblorderdetails SET orderid=%s, productid=%s, quantity=%s WHERE orderdetailid=%s"
            cur.execute(sql, (orderr.OrderID, orderr.ProductID, orderr.Quantity, orderr.OrderDetailID))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Updated order', 200
            con.close()
            return 'order detail ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def delete(self, orderr: OrderDetailEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "DELETE FROM tblorderdetails WHERE orderdetailid=%s"
            cur.execute(sql, (orderr.OrderDetailID, ))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Deleted order detail', 200
            con.close()
            return 'order detail ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

#Product
class Product:
    def __init__(self, ConnectionData):
        self.ConnectionData = ConnectionData
    def insert(self, product):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "INSERT INTO tblproducts(ProductName, SupplierID, CategoryID, Unit, Price) VALUES (%s, %s, %s, %s, %s)"
            record_to_insert = (product.ProductName, product.SupplierID, product.CategoryID, product.Unit, product.Price)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert TblProducts successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_all(self):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM tblproducts"
            cur.execute(sql)
            con.commit()           
            rows = cur.fetchall()
            result = []
            for row in rows:
                c = ProductEntity()
                c.fetch_data(row)
                result.append(c.to_json())
            con.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_by_id(self, product: ProductEntity):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM tblproducts WHERE productid=%s"
            cur.execute(sql, (product.ProductID,))
            con.commit()           
            row = cur.fetchone()
            if row:
                c = ProductEntity()
                c.fetch_data(row)
                return c, 200
            con.close()
            return 'Product ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def update(self, product: ProductEntity):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "UPDATE tblproducts SET productname=%s, supplierid=%s, categoryid=%s, unit=%s, price=%s WHERE productid=%s "
            cur.execute(sql,(product.ProductName, product.SupplierID, product.CategoryID, product.Unit, product.Price, product.ProductID))
            con.commit()           
            row = cur.rowcount
            if row > 0:
                return 'Updated product', 200
            con.close()
            return 'Product ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def delete(self, product: ProductEntity):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "DELETE FROM tblproducts WHERE productid=%s"
            cur.execute(sql,(product.ProductID,))
            con.commit()           
            row = cur.rowcount
            if row>0:
                return "Delete Product", 200
            con.close()
            return "Product ID not found", 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()


if __name__ == "__main__":
    print('this is data object package')