from django.test import TestCase

class YourTestClass(TestCase):

    def test_false_is_true(self):
        print("Method: test_true_is_true.")
        self.assertTrue(True)