# Implement a class to hold room information. This should have name and
# description attributes.
class Room:    

    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items
        # self.n_to = None
        # self.s_to = None
        # self.e_to = None
        # self.w_to = None
    
    def __str__(self):
        output = f'{self.name} contains items: '
        for i in self.items:
            output += f"\n {i}"
        output += f'\nCurrent location description: {self.description}'
        return output

        # return self.name, self.description
    
    