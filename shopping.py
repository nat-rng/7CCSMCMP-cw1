from curses.ascii import isdigit
import random
import json
from datetime import datetime

# Global variables
unique_ids = set()
item_types = {'clothing', 'food', 'mobile phone'}

## Superclass Product Object ##
class Product():
    def __init__(self, name, price, quantity, unique_id, brand):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__unique_id = unique_id
        self.__brand = brand
        
    def to_json(self):
        json_dict = {"name": self.__name, "price": self.__price, "quantity": self.__quantity, 
                     "unique_id": self.__unique_id, "brand": self.__brand}
        json_object = json.dumps(json_dict)
        return json_object
    
    #Setteer and Getter methods to access attributes of the Product class
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    def get_quantity(self):
        return self.__quantity
    
    def get_unique_id(self):
        return self.__unique_id

class Clothing(Product):
    def __init__(self, 
                name, price, quantity, unique_id, brand,
                size, material
                ):
        super().__init__(name, price, quantity, unique_id, brand)
        self.__size = size
        self.__material = material
        
    #Oterride the to_json method to include the size and material attributes
    def to_json(self):
        json_dict = {"name": self.__name, "price": self.__price, "quantity": self.__quantity, 
                     "unique_id": self.__unique_id, "brand": self.__brand, "size": self.__size,
                     "material": self.__material}
        json_object = json.dumps(json_dict)
        return json_object
        
class Food(Product):
    def __init__(self, 
                name, price, quantity, unique_id, brand,
                expiry_date, gluten_free, suitable_for_vegans
                ):
        super().__init__(name, price, quantity, unique_id, brand)
        self.__expiry_date = expiry_date
        self.__gluten_free = gluten_free 
        self.__suitable_for_vegans = suitable_for_vegans

    #Override the to_json method to include the expiry_date, gluten_free and suitable_for_vegans attributes
    def to_json(self):
        json_dict = {"name": self.__name, "price": self.__price, "quantity": self.__quantity, 
                     "unique_id": self.__unique_id, "brand": self.__brand, "expiry_date": self.__expiry_date,
                     "gluten_free": self.__gluten_free, "suitable_for_vegans": self.__suitable_for_vegans}
        json_object = json.dumps(json_dict)
        return json_object
    
class MobilePhone(Product):
    def __init__(self, 
            name, price, quantity, unique_id, brand,
            os, model_year, screen_size
            ):
        super().__init__(name, price, quantity, unique_id, brand)
        self.__os = os
        self.__model_year = model_year
        self.__screen_size = screen_size
    
    #Override the to_json method to include the os, model_year and screen_size attributes    
    def to_json(self):
        json_dict = {"name": self.__name, "price": self.__price, "quantity": self.__quantity, 
                     "unique_id": self.__unique_id, "brand": self.__brand, "os": self.__os, 
                     "model_year": self.__model_year, "screen_size": self.__screen_size}

# Initialise shopping cart as empty list only accessible by this module via private variable setters  nd getters
class ShoppingCart():
    def __init__(self):
        self.__my_cart = []
    
    def add_product(self, p):
        self.__my_cart.append(p)
        
    def remove_product(self, p):
        self.__my_cart = list(filter(lambda products: products != p, self.__my_cart))
        
    def get_contents(self):
        return sorted(self.__my_cart, key=lambda item: item.get_name())

    def change_product_quantity(self, p, q):
        p.set_quantity(q)

        p.quantity = q
#Function to allows user to enter a unique EAN ID. Input is verified against the set of unique IDs; strings, floats and negative numbers are not allowed.
#It has a built in recursion to allow the user to try again if they enter an invalid ID.
#If the ID is valid, it is added to the set of unique IDs.
#Provides an option to auto generate an ID with input 'gen id'
def enter_ean_id():
    try:
        input_unique_id = input("Enter 13 digit EAN code: ")
        if input_unique_id.lower() == 'gen id':
            input_unique_id = generate_id()
            return input_unique_id
        elif input_unique_id in unique_ids:
            print("Duplicate ID! A random one has been generated for you.")
            input_unique_id = generate_id()
            return input_unique_id
        elif len(str(input_unique_id)) != 13:
            print("EAN code must be 13 digits. Please try again (or enter 'gen id' to generate it).")
            return(enter_ean_id())
        elif input_unique_id.isdigit() == False or int(input_unique_id) < 0:
            print("EAN code must consist of digits between [0,9]. Please try again (or enter 'gen id' to generate it).")
            return(enter_ean_id())
        else:
            return str(input_unique_id)
    except TypeError:
        print("EAN code must consist of digits between [0,9]. Please try again (or enter 'gen id' to generate it).")
        return(enter_ean_id())

#function to auto generate a unique ID, generates a 13 digit number and checks if it is already in the set of unique IDs
def generate_id():
    unique_id = ''
    for _ in range(13):
        unique_id += str(random.randint(0,9))
    if unique_id in unique_ids:
        generate_id()
    unique_ids.add(unique_id)
    return unique_id
#Function to allow user to add a product to the shopping cart. User is prompted to enter the product type, name, brand, price, quantity and unique ID.    
def command_a(shopping_cart):
    print("\nAdding a new product to the shopping cart...")
    item_type = str(input("Enter item type: "))
    if item_type not in item_types:
        print("Product type not found. Try Again.")
        command_a(shopping_cart)
    else:
        enter_product_details(shopping_cart, item_type)
# Helper function for the above to allow for recursion if the user enters an invalid value and stay at the currrent input prompt
def enter_product_details(shopping_cart, item_type):
    name = enter_str_val("Name")
    price = enter_numerical_val("Price")
    quantity = enter_numerical_val("Quantity")
    unique_id = enter_ean_id()
    brand = enter_str_val("Brand")
    if item_type.lower() == 'clothing':
        size = enter_numerical_val("Size")
        material = enter_str_val("Material")
        product = Clothing(name, price, quantity, unique_id, brand, size, material)
        shopping_cart.add_product(product)
    elif item_type.lower() == 'food':
        expiry_date = enter_datetime_val("Expiry Date")
        gluten_free = enter_boolean_value("Check Gluten")
        suitable_for_vegans = enter_boolean_value("Check Vegan")
        product = Food(name, price, quantity, unique_id, brand,
                        expiry_date, gluten_free, suitable_for_vegans)
        shopping_cart.add_product(product)
    elif item_type.lower() == 'mobile phone':
        os = enter_str_val("OS")
        model_year = enter_datetime_val("Model Year")
        screen_size = enter_numerical_val("Screen Size")
        product = MobilePhone(name, price, quantity, unique_id, brand,
                                os, model_year, screen_size)
        shopping_cart.add_product(product)
    print("You added {} to the shopping cart".format(name))
    print("The cart contains {} products".format(len(shopping_cart.get_contents())))
#Helper function to allow user to enter a string value. Input is verified to be a string and not empty.
def enter_str_val(val_type):
    if val_type.lower() == 'name':
        val = str(input("Enter item name: "))
        if val == '':
            print("Name field cannot be empty")
            return(enter_str_val(val_type))
        return val
    elif val_type.lower() == 'brand':
        val = str(input("Enter item brand: "))
        if val == '':
            print("Brand field cannot be empty")
            return(enter_str_val(val_type))
        return val
    elif val_type.lower() == 'material':
        val = str(input("Enter item material: "))
        if val == '':
            print("Material field cannot be empty")
            return(enter_str_val(val_type))
        try:
            if isinstance(float(val),float) == True:
                print("Material must be a string value.")
                return(enter_str_val(val_type))
        except ValueError:
            return val
    elif val_type.lower() == 'os':
        val = str(input("Enter mobile phone operating system: "))
        if val == '':
            print("OS field cannot be empty.")
            return(enter_str_val(val_type))
        return val
#Helper function to allow user to enter a numerical value. Input is verified to be a float or string and not negative or empty.
def enter_numerical_val(val_type):
    if val_type.lower() == "price":
        try:
            price = float(input("Enter item price: "))
            if price < 0.00:
                print("Prices cannot be negative.")
                return(enter_numerical_val(val_type))
            return price
        except ValueError:
            print("Price must be a numerical value.")
            return(enter_numerical_val(val_type))
    elif val_type.lower() == "quantity":
        try:
            quantity = int(input("Enter item quantity: "))
            if quantity < 1:
                print("Quantity cannot be less than 1. Try again.")
                return(enter_numerical_val(val_type))
            return quantity
        except ValueError:
            print("Quantity must be an integer value. Try again.")
            return(enter_numerical_val(val_type))
    elif val_type.lower() == 'size':
        try:
            size = int(input("Enter item size as an integer: "))
            if size < 0:
                print("Size cannot be negative.")
                return(enter_numerical_val(val_type))
            return size
        except ValueError:
            print("Item size must be an integer value.")
            return(enter_numerical_val(val_type))
    elif val_type.lower() == "screen size":
        try:
            screen_size = float(input("Enter screen size in inches: "))
            if screen_size < 0:
                print("Screen size cannot be negative.")
                return(enter_numerical_val(val_type))
            return screen_size
        except ValueError:
            print("Screen size must be a floating point value.")
            return(enter_numerical_val(val_type))
#Helper function to allow user to enter a datetime value. Input is verified to be a datetime object of the right format and not empty.
def enter_datetime_val(val_type):
    if val_type.lower() == "expiry date":
        try:
            expiry_date = str(input("Enter item expiry date (dd/mm/yyyy): "))
            datetime.strptime(expiry_date, '%d/%m/%Y')
            return expiry_date
        except ValueError:
            print("Invalid date format, please try again")
            return(enter_datetime_val(val_type))
    elif val_type.lower() == "model year":
        try:
            model_year = str(input("Enter item model year (yyyy): "))
            datetime.strptime(model_year, '%Y')
            return model_year
        except ValueError:
            print("Invalid date format, please try again")
            return(enter_datetime_val(val_type))
#Helper function to verify a boolean value. Input is verified to be a boolean value and not empty.
def enter_boolean_value(val_type):
    if val_type.lower() == "check gluten":
        try:
            gluten_free_str = str(input("Is the item gluten free? (Y/N): "))
            gluten_free = bool_yes_no(gluten_free_str)
            return gluten_free
        except ValueError as e:
            print(e)
            return(enter_boolean_value(val_type))
    elif val_type.lower() == "check vegan":
        try:
            suitable_for_vegans_str = str(input("Is the item suitable for Vegans? (Y/N): "))
            suitable_for_vegans = bool_yes_no(suitable_for_vegans_str)
            return suitable_for_vegans
        except ValueError as e:
            print(e)
            return(enter_boolean_value(val_type))
#function to return boolean value from Y or N input
def bool_yes_no(yn):
    if yn.lower() == "y" or yn.lower() == "yes":
        return True
    elif yn.lower() == "n" or yn.lower() == "no":
        return False
    else:
        raise ValueError("Invalid input, must be Yes/Y or No/N.")
#Function to remove product from shopping cart by unieque ID, verifies that the ID is in the cart and not empty.
def command_r(shopping_cart):
    if bool(shopping_cart.get_contents()) == False:
        print("\nNo items in shopping cart.")
    else:
        del_id = str(input("\nInput product ID to delete: "))
        if del_id in unique_ids:
            for i in shopping_cart.get_contents():
                if i.get_unique_id() == del_id:
                    unique_ids.remove(del_id)
                    shopping_cart.remove_product(i)
                    print("Item {} removed".format(del_id))
        else:
            print("\nInvalid product ID, please try again.")
            command_r(shopping_cart)
#Command to display the contents of the shopping cart. Formatted to display items quantity, uniqueID, name, price and total price.
def command_s(shopping_cart):
    print("Cart Summary:")
    if bool(shopping_cart.get_contents()) == True:
        items = 0
        total_price = 0
        for i in shopping_cart.get_contents():
            items += 1
            if i.quantity > 1:
                print("\t" + str(items) + " - " + str(i.get_quantity()) + " x " + str(i.get_name()) + " = £" + str("{:.2f}".format(round(i.get_quantity()*i.get_price(),2))) + " - Item ID: " + i.unique_id())
            else:
                print("\t" + str(items) + " - " + str(i.get_name()) + " = £" + str("{:.2f}".format(round(i.get_quantity()*i.get_price(),2))) + " - Item ID: " + i.get_unique_id())
            total_price += round(i.get_quantity()*i.get_quantity(),2)
        print("\tTotal Price = £" + str("{:.2f}".format(total_price)))
    else:
        print("\nShopping Cart is Empty.")
#Function to changee the quantity of an item in the shopping cart. Changes don through unique ID and berifies that the ID is in the cart and not empty.
def command_q(shopping_cart):
    if bool(shopping_cart.get_contents()) == False:
        print("\nNo items in shopping cart.")
    else:
        change_id = str(input("Input product ID to change: "))
        if change_id in unique_ids:
            for i in shopping_cart.get_contents():
                if i.get_unique() == change_id:
                        change_item_quant(shopping_cart, i, change_id)
        else:
            print("\nInvalid product ID, please double check and try again.")
#Helper function to change the quantity of an item in the shopping cart. Verifies that the new quantity is an integer and not empty.
#If the new quantity is 0, the item can be removed from the cart if the user accepts the prompt.
#If the new quantity is the same as the current quantity, a message is shown to the user
def change_item_quant(shopping_cart, item, change_id):
    og_quantity = int(item.get_quantity())
    print("\nCurrent number of this item in cart: " + og_quantity)
    try:
        quantity = int(input("Please enter the desired quantity: "))
        if quantity == og_quantity:
            print("Quantity unchanged.")
        elif quantity == 0:
            print("\nYou are about to delete this item from the cart. Are you sure you want to continue?")
            decision = input("\nType 'Y' to Proceed or 'N' to Cancel: ")
            if decision.lower() == "y":
                unique_ids.remove(change_id)
                shopping_cart.remove_product(item)
                print("\nItem Deleted.")
            elif decision.lower() != "n":
                print("\nInvalid input, please try again.")
                change_item_quant(shopping_cart, item, change_id)
            else:
                print("\nDeletion aborted.")
        elif quantity < 0:
            print("Quantity cannot be negative, please try again.")
            change_item_quant(shopping_cart, item, change_id)
        else:
            shopping_cart.change_product_quantity(item, int(quantity))
            print("Quantity of {} changed from {} to {}".format(change_id, og_quantity, quantity))
    except ValueError:
        print("Invalid input, input must be an interger. Please try again.")
        change_item_quant(shopping_cart, item, change_id)    
#Function to display the contents of the shopping cart. Formatted to display items in json format in the console.   
def command_e(shopping_cart):
    if bool(shopping_cart.get_contents()) == False:
            print("\nNo items in shopping cart.")
    else:
        shopping_cart_dict = {"shopping_cart":[]}
        item_no = 0
        total_price = 0
        for i in shopping_cart.get_contents():
            item_no += 1
            key = "item" + str(item_no)
            item_dict = {key: json.loads(i.to_json())}
            shopping_cart_dict["shopping_cart"].append(item_dict)
            total_price += round(i.get_quantity()*i.price,2)
        shopping_cart_dict["total_price"]  = total_price
        shopping_cart_json = json.dumps(shopping_cart_dict, indent=1)
        print(shopping_cart_json)
#Command to show a list of possible commands the user can enter.       
def command_h():
    print("The following commands are supported:")
    print("\t[A] - Add a new product to the cart")
    print("\t[R] - Remove a product to the cart")
    print("\t[S] - Print a summary of the cart")
    print("\t[Q] - Change thee quantity of a product")
    print("\t[E] - Export a JSON version of the cart")
    print("\t[T] - Terminate the program")
    print("\t[H] - See the list of supported commands")
#Main function to run the program. Creates a shopping cart object and runs the command loop.
def main():
    print("\nStarted! Type your next command or type 'H' to get a list of Available Commands")
    terminate = False
    shopping_cart = ShoppingCart()
    while terminate == False:
        user_input = input("\nEnter command: ")
        user_input = user_input.upper()
        if user_input == 'T':
            print("Goodbye!") 
            terminate = True
        elif user_input == 'A':
            command_a(shopping_cart)
        elif user_input == 'R':
            command_r(shopping_cart)
        elif user_input == 'S':
            command_s(shopping_cart)
        elif user_input == 'Q':
            command_q(shopping_cart)
        elif user_input == 'E':
            command_e(shopping_cart)
        elif user_input == 'H':
            command_h()
        else:
            print("\nInvalid command, try again or use H to see a list of valid commands.")

if __name__ == "__main__":
    main()

                 
    