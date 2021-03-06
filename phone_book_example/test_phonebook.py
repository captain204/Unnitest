import unittest

from phone_book_example.phonebook import Phonebook

class PhonebookTest(unittest.TestCase):

    def setUp(self):
        self.phonebook = Phonebook()

    def test_lookup_entry_name(self):
        self.phonebook.add("Bob","123457")
        self.assertEqual("123457",self.phonebook.lookup("Bob"))

    @unittest.skip("WIP")
    def test_missing_entry_raises_KeyError(self, keyError=None):
        with self.assertRaises(keyError):
            self.phonebook.lookup("missing")

    @unittest.skip("WIP")
    def test_empty_phone_book_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())

    @unittest.skip("WIP")
    def test_phonebook_with_normal_entries_is_consistent(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Mary","012345")
        self.assertTrue(self.phonebook.is_consistent())


    def test_phonebook_with_duplicate_entries_is_consistent(self):
        self.phonebook.add("Bob","12345")
        self.phonebook.add("Mary","12345")
        self.assertFalse(self.phonebook.is_consistent())

    @unittest.skip("WIP")
    def test_phonebook_with_numbers_that_prefix_one_another_is_inconsistent(self):
        self.phonebook.add("Bob","12345")
        self.phonebook.add("Mary","123")
        self.assertFalse(self.phonebook.is_consistent())


    def test_phonebook_adds_names_and_numbers(self):
        self.phonebook.add("Sue","12345")
        self.assertIn("Sue",self.phonebook.get_names())
        self.assertIn("12345",self.phonebook.get_numbers())

