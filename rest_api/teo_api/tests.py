from django.test import TestCase

class YourTestClass(TestCase):

    def test_false_is_true(self):
        print("Nie dzialaja testy i nie wiem dlaczego.")
        self.assertTrue(True)