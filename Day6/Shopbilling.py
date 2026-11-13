# Develop a Python program for a small shop to process customer purchases. Store product 
#names and prices in a dictionary, items added to the cart in a list, product categories in a set, 
#and product details using tuples. Create functions to display products, add items to the cart, and 
#calculate the total bill. Use a recursive function to compute the total price of all items in the cart. 

# Product names and prices using Dictionary
products = {
    "Pen": 10,
    "Notebook": 50,
    "Pencil": 5
}
# Product categories using Set
categories = {"Stationery", "Education", "Office"}
# Product details using Tuples
product_details = (
    ("Pen", 10),
    ("Notebook", 50),
    ("Pencil", 5)
)
# Cart using List
cart = []

# Function to display products
def display_products():
    print("\nAvailable Products:")
    for name, price in products.items():
        print(name, ":", price)
# Function to add items to cart
def add_to_cart():
    try:
        name = input("Enter product name: ").strip().capitalize()

        if name not in products:
            raise NameError

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            raise ValueError

        cart.append((name, quantity))

        print("Item added to cart successfully.")

    except ValueError:
        print("Invalid quantity! Please enter a number.")

    except NameError:
        print("Product not found in store.")

    except TypeError:
        print("Cart data type error.")

# Recursive function to calculate total
def calculate_total(items):
    if len(items) == 0:
        return 0

    name, quantity = items[0]

    if not isinstance(name, str) or not isinstance(quantity, int):
        raise TypeError

    price = products[name]

    return (price * quantity) + calculate_total(items[1:])

# Function to display cart and total bill
def total_bill():
    print("\nItems in Cart:")

    try:
        for name, quantity in cart:
            print(name, "x", quantity)

        # Calculate total using recursion
        total = calculate_total(cart)

        # Division check
        if len(cart) == 0:
            raise ZeroDivisionError

        print("Total Bill:", total)

    except TypeError:
        print("Cart data type error.")

    except ZeroDivisionError:
        print("Calculation error: division by zero.")

# Main menu
while True:
    print("\n1. Display Products")
    print("2. Add Item to Cart")
    print("3. View Total Bill")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            display_products()

        elif choice == 2:
            add_to_cart()

        elif choice == 3:
            total_bill()

        elif choice == 4:
            print("Thank you for shopping!")
            break

        else:
            print("Invalid choice. Try again.")

    except ValueError:
        print("Please enter a valid menu number.")
