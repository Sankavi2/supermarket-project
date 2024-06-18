def get_items():
    menu = {
        1: {"category": "Men", "items": [
            {"name": "Shirt", "price": 200},
            {"name": "Trousers", "price": 25},
            {"name": "Tie", "price": 30},
            {"name": "Shoes", "price": 150},
            {"name": "Belt", "price": 50}
        ]},
        2: {"category": "Women", "items": [
            {"name": "Dress", "price": 130},
            {"name": "Skirt", "price": 200},
            {"name": "Blouse", "price": 180},
            {"name": "Heels", "price": 455},
            {"name": "Purse", "price": 25}
        ]},
        3: {"category": "Kids", "items": [
            {"name": "T-Shirt", "price": 150},
            {"name": "Shorts", "price": 120},
            {"name": "Cap", "price": 80},
            {"name": "Sneakers", "price": 30},
            {"name": "Toy Car", "price": 50}
        ]},
        4: {"category": "Grocery", "items": [
            {"name": "Rice", "price": 25},
            {"name": "Sugar", "price": 10},
            {"name": "Salt", "price": 5},
            {"name": "Oil", "price": 30},
            {"name": "Milk", "price": 20},
            {"name": "Bread", "price": 12}
        ]}
    }
    items = []
    print("Menu:")
    for key, value in menu.items():
        print(f"\n{key}. {value['category']}:")
        for index, item in enumerate(value['items'], start=1):
            print(f"  {index}. {item['name']}: ${item['price']}")
    while True:
        category_selection = input("Enter the number for the category (1: Men, 2: Women, 3: Kids, 4: Grocery) or 0 to finish: ")
        if category_selection == '0':
            break
        try:
            category_index = int(category_selection)
            if category_index in menu:
                while True:
                    item_selection = input(f"Enter the item number from {menu[category_index]['category']} (0 to finish): ")
                    if item_selection == '0':
                        break
                    try:
                        item_index = int(item_selection) - 1
                        if 0 <= item_index < len(menu[category_index]['items']):
                            quantity = int(input("Enter quantity: "))
                            if quantity > 0:
                                selected_item = menu[category_index]['items'][item_index].copy()
                                selected_item["quantity"] = quantity
                                items.append(selected_item)
                            else:
                                print("Quantity must be greater than 0.")
                        else:
                            print("Invalid selection.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
            else:
                print("Invalid category selection.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    return items
