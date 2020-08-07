class Phonebook:
    def __init__(self):
        self.entries = {}

    def add(self, name, number):
        self.entries[name] = number

    def lookup(self, name):
        return self.entries[name]

    def is_consistent(self):
        return True

    def get_names(self):
        names = []
        for values in self.entries.keys():
            names.append(values)
        return names

    def get_numbers(self):
        numbers = []
        for values in self.entries.values():
            numbers.append(values)
        return numbers
