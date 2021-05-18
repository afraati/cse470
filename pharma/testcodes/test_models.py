from django.test import TestCase
from unittest import TestCase
from pharma.models import Dealer, Customer, Medicine

class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)
class DealerModelTest(TestCase):
     @classmethod
     def setUpTestData(cls):
         Dealer.objects.create(dname='Soham Das', address='Bangalore', phn_no='9954783950', email='soham@gmail.com')
         Dealer.save()
     #def test_email(self):

    #     self.assertEqual('soham@gmail.com', email)
     def test_dname_max_length(self):
         #dealer = Dealer.objects.get(id=1)
         max_length= Dealer._meta.get_field('dname').max_length
         self.assertEqual(max_length, 30)

     def test_email_max_length(self):
         max_length= Dealer._meta.get_field('email').max_length
         self.assertEqual(max_length, 50)

class CustomerModelTest(TestCase):
     @classmethod
     def setUpTestData(cls):
         Customer.objects.create(fname='Soham', lname='Das', address='Bangalore', phn_no='9954783950', email='soham@gmail.com')
         Customer.save()

     def test_lname_max_length(self):
        #dealer = Dealer.objects.get(id=1)
        max_length= Customer._meta.get_field('lname').max_length
        self.assertEqual(max_length, 30)

    #def test_lname_label(self):
    #    field_label = Customer._meta.get_field('lname').verbose_name
    #    self.assertEqual(field_label, 'first name')
class MedicineModelTest(TestCase):
     @classmethod
     def setUpTestData(cls):
         Medicine.objects.create(m_id=1, mname='Soha', dname='Datt', desc='Bangalore', price='20', stock=100)
         Medicine.save()

     def test_dname_max_length(self):
        #dealer = Dealer.objects.get(id=1)
        max_length= Medicine._meta.get_field('dname').max_length
        self.assertEqual(max_length, 30)
