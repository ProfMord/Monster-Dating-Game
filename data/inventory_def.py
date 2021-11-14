import item_db


class Inventory:
    def __init__(self):
        pass

    inventory_list = []

    def add_item(self, item):
        self.inventory_list.append(item_db.items.item_dict.get(item))

    def remove_item(self, item):
        self.inventory_list.remove(item_db.items.item_dict.get(item))

    def get_inventory_list(self):
        return self.inventory_list
