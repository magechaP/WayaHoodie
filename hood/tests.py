from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Neighborhood,Profile,Business
from django.contrib.auth.models import User


class Neighborhood_TestCases(TestCase):
   def setUp(self):
       self.user1= User(id=1,username='muk',email='muk@gmail.com',password='1234')
       self.user1.save()
       self.profile = Profile(user_id=1,bio='eat alot',profile_pic='images/default.jpg')
       self.profile.save_profile()
       self.neighborhood =Neighborhood(id=1,name='mukonesi', health_department_address='99300', health='mUK', count='4')
       self.neighborhood.create_neighborhood()
       self.business = Business(id=1, business_name = 'makaa', business_email='m@gmail.com')


   def tearDown(self):
       Profile.objects.all().delete()
       User.objects.all().delete()
       Neighborhood.objects.all().delete()

   def test_is_instance(self):
       self.assertTrue(isinstance(self.user1,User))
       self.assertTrue(isinstance(self.profile,Profile))
       self.assertTrue(isinstance(self.neighborhood,Neighborhood))

   def test_save_method(self):
       self.neighborhood.create_neighborhood()
       all_objects = Neighborhood.objects.all()
       self.assertTrue(len(all_objects)>0)

   def test_delete_method(self):
       self.neighborhood.create_neighborhood()
       filtered_object = Neighborhood.objects.filter(name='mukonesi')
       filtered_object.delete()
       all_objects = Neighborhood.objects.all()
       self.assertTrue(len(all_objects) == 0)

   def test_display_all_objects_method(self):
       self.neighborhood.create_neighborhood()
       all_objects = Neighborhood.retrieve_all()
       self.assertEqual(all_objects.name,'mukonesi')

   def test_update_single_object_property(self):
       self.neighborhood.create_neighborhood()
       filtered_object =Neighborhood.update_occupants('4','5')
       fetched = Neighborhood.objects.get(count='5')
       self.assertEqual(fetched.count,'5')

   def test_find_neighborhood_by_id(self):
       self.neighborhood.create_neighborhood()
       fetched_neighborhood = Neighborhood.find_neighborhood_by_id(1)
       self.assertEqual(fetched_neighborhood.id,1)

  

