import unittest

from phone_book_example.phonebook import Phonebook

class PhonebookTest(unittest.TestCase):
    def test_create_phonebook(self):
        phonebook = Phonebook()

    def test_lookup_entry_name(self):
        phonebook = Phonebook()
        phonebook.add("Bob","123457")
        self.assertEqual("123457",phonebook.lookup("Bob"))

    def test_missing_entry_raises_KeyError(self, keyError=None):
        phonebook = Phonebook()
        with self.assertRaises(keyError):
            phonebook.lookup("missing")
