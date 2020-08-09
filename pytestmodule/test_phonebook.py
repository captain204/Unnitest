import pytest

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

@pytest.fixture
def phonebook():
    return Phonebook()



def test_phonebook_lookup(phonebook):
    phonebook.add("Lola",123)
    assert 123 == phonebook.lookup("Lola")

def test_phone_book_gives_acces_to_name_numbers(phonebook):
    phonebook.add("Amaka","123456")
    assert "Amaka" in phonebook.get_names()
    assert "123456" in phonebook.get_numbers()

def test_missing_entry_raises_keyError():
    pytest.skip("WIP")
    phonebook = Phonebook()
    with pytest.raises("keyError"):
        phonebook.lookup("missing")