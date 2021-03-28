class Location:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def display_object(self):
        return self.name + ": " + self.address
