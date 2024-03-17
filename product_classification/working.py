class Product:
    def __init__(self, name, vegan, locally_sourced, price):
        self.name = name
        self.vegan = vegan
        self.locally_sourced = locally_sourced
        self.price = price

    def display_info(self):
        print(f"Product: {self.name}")
        print(f"Vegan: {'Yes' if self.vegan else 'No'}")
        print(f"Locally Sourced: {'Yes' if self.locally_sourced else 'No'}")
        print(f"Price: ${self.price}")




def get_index_of_instance(variable, instance_list):
    for i, instance in enumerate(instance_list):
        if variable == instance.name:
            return i
    return -1  # Return -1 if the variable doesn't match any instance name

def item_score(product):
    score = 0
    if product.vegan:
        score += 20
    if product.locally_sourced:
        score += 10
    return score

def receipt_score(receipt_items):
    apple = Product("apple", True, True, 2.00)
    orange = Product("orange", True, False, 2.00)
    beef = Product("beef", False, False, 2.00)

    database = [apple, orange, beef]
    score = 0
    for item in receipt_items:
        product_index = get_index_of_instance(item, database)
        if product_index != -1:
            product = database[product_index]
            if product:
                score += item_score(product)
            else:
                print(f"Product '{item}' not found in the database.")
        else:
            print(f"Product '{item}' not found in the database.")
    return score
