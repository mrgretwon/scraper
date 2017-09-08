from django.test import TestCase

class TestClass(TestCase):

    def test_true_is_true(self):
        print("Testing CI")
        self.assertTrue(True)