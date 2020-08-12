import unittest
import doctest
from yatzytest import yatzy

def load_test(loader,tests,ignore):
    tests.addTests(doctest.DocTestSuite(yatzy))
    return tests
