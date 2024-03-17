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
    dataset = [['MONSTER PIPELINE', True, True, 1.85], ['BRIE, BACON & CHILLI', True, False, 3.0], ['PIZZA SWIRL', True, False, 1.1], ['IRN BRU 1L', False, True, 1.1], ['LINDT INTENSE ORANG', True, False, 1.6], ['LINDT INTENSE ORANG', True, False, 1.6], ['CARROTS LOOSE', False, False, 0.07], ['HERBAL ESSENCES', True, False, 2.0], ['JS 8 BRIOCHE ROLLS', False, False, 1.5], ['SSTC HW ANTIBC SILK', True, True, 0.6], ['EMMI MR.BIG 370ML', True, False, 2.65], ['NAKD BB MUFF B/BAR', True, False, 1.35], ['ALL DAY BREAKFAST SW', True, False, 2.75], ['STARBUCKS G CAFFE LA', True, True, 2.8], ['ALL DAY BREAKFAST SW', True, True, 2.75], ['JS 2X MIN CURED PIES', False, False, 1.3], ['ALL DAY BREAKFAST SW', True, True, 2.75], ['JS SCOTCH EGG', True, False, 1.3], ['COSTA REG VNL LATTE', True, True, 3.5], ['JS STONEBAKED BBQ CH', True, True, 3.5], ['JS SB MEAT FEAST', True, True, 3.5]]
    database = []
    for i in dataset:
        j = Product(i[0],i[1],i[2],i[3])
        database.append(j)

    
    score = 0
    for item in receipt_items:
        product_index = get_index_of_instance(item[0], database)
        if product_index != -1:
            product = database[product_index]
            if product:
                score += item_score(product)
            else:
                print(f"Product '{item}' not found in the database.")
        else:
            print(f"Product '{item}' not found in the database.")
    return score

