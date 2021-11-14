import item_db


class Item:
    def __init__(self, id, name, type, description):
        self.id = id
        self.name = name
        self.type = type
        self.description = description
        item_db.items.item_dict[id] = self


RedGemStoneItem = Item(5, "Red Gemstone", 'cute', 'This red glows with anger')
BlueGemStoneItem = Item(10, "Blue Gemstone", 'useless', 'this blue glows with calm')
GreenGemStoneItem = Item(15, "Green Gemstone", 'nice', 'this green glows with love')
