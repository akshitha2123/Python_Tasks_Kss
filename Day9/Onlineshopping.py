# Online Shopping System (Multilevel Inheritance)


class Product:
    def product_details(self):
        print("Product: Electronics")

class ElectronicProduct(Product):
    def electronic_details(self):
        print("Category: Electronic Product")

class MobilePhone(ElectronicProduct):
    def mobile_details(self):
        print("Brand: Samsung")
        print("Model: Galaxy S24")

m = MobilePhone()

m.product_details()
m.electronic_details()
m.mobile_details()
