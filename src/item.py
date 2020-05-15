class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'Item name: {self.name}\nItem Description: {self.description}'

    def get_name(self):
        return self.name
    
    def se_name(self, new_name):
        self.name = new_name

