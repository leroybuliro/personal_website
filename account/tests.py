import os
import pathlib
import unittest
# from selenium import webdriver
from django.test import TestCase
from .models import User

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

# driver = webdriver.Chrome()

# Create your tests here.
class AccountTestCase(TestCase):

    # def test_title(self):
    #     driver.get(file_uri("auth.html"))
    #     self.assertEqual(driver.title, "Enter your Email - Leroy Buliro")

    # def test_email(self):
    #     driver.get(file_uri("auth.html"))
    #     submission = driver.find_element_by_class_name("authform")
    
    # def setUp(self):
    #     a1 = User.objects.create(email="john@doe.co", alias="johndoe", password="aQ1!aQ1!")
    #     a2 = User.objects.create(email="john@doe.c", alias="johndoe2", password="aQ1!aQ1!")
    #     a3 = User.objects.create(email=".john@doe.c", alias="johndoe3", password="aQ1!aQ1!")
    #     a3 = User.objects.create(email="john@doe.co", alias="johndoe", password="aQ1!aQ1!")

    # def test_userCreation(self):
    #     self.assertIn()

    pass

if __name__ == "__main__":
    unittest.main()
