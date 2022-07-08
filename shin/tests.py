from django.test import TestCase
from shin.views import MainPage
from shin.models import Registration
#from django.http import HttpRequest
#from django.template.loader import render_to_string
#from django.urls import resolve


class HomePageTest(TestCase):
	def test_mainpage_as_seen_client(self):
		resp =self.client.post('/', data= {
		'First_Name': 'Rashina',
		'Last_Name' : 'Majid',
		'phone' :'09123456789',
		'Street_Adress' : 'BLK4',
		'City' : 'Dasmarinas',
		'Province' : 'Cavite',
		'postal' : '4114',
		'AMOUNT' : '299',
		'packaging' : 'Brown Box',
		})
		self.assertEqual(Registration.objects.count(), 1)
		newEntry = Registration.objects.first()
		self.assertEqual(newEntry.newfirstname , 'Rashina')
		self.assertEqual(newEntry.newlastname , 'Majid')
		self.assertEqual(newEntry.newphonenumber , '09123456789')
		self.assertEqual(newEntry.newshipadd , 'BLK4')
		self.assertEqual(newEntry.newcity , 'Dasmarinas')
		self.assertEqual(newEntry.newprovince , 'Cavite')
		self.assertEqual(newEntry.newPostal , '4114')
		self.assertEqual(newEntry.newamount , '299')
		self.assertEqual(newEntry.newpackaging , 'Brown Box')

	def test_redirect_POST(self):
		response = self.client.post('/', data={ 
		'First_Name': 'Rashina', #ito din n
		'Last_Name' : 'Majid',
		'phone' :'09123456789',
		'Street_Adress' : 'BLK4',
		'City' : 'Dasmarinas',
		'Province' : 'Cavite',
        'postal' : '4114',
        'AMOUNT' : '299',
        'packaging' : 'Brown Box',
        })
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')

	def test_only_saves_items_if_necessary(self):
		self.client.get('/')
		self.assertEqual(Registration.objects.count(), 0)

class ORMTest(TestCase):
 	def test_saving_retrieving_list(self):
 		entry1 = Registration()
 		entry1.newfirstname = 'Rashina'
 		entry1.newlastname  = 'Majid'
 		entry1.newphonenumber = '09123456789'
 		entry1.newshipadd ='BLK4'
 		entry1.newcity ='Dasmarinas'
 		entry1.newprovince ='Cavite'
 		entry1.newPostal ='4114'
 		entry1.newamount ='299'
 		entry1.newpackaging ='Brown Box'
 		entry1.save()

 		entry2 = Registration()
 		entry2.newfirstname = 'Zero'
 		entry2.newlastname  = 'Shi'
 		entry2.newphonenumber = '09123456666'
 		entry2.newshipadd ='BLK10'
 		entry2.newcity ='Imus'
 		entry2.newprovince ='Cavite'
 		entry2.newPostal ='4114'
 		entry2.newamount ='299'
 		entry2.newpackaging ='Plain Box'
 		entry2.save()

 		items = Registration.objects.all()
 		self.assertEqual(items.count(), 2)
 		items1 = items[0]
 		items2 = items[1]

 		

 		self.assertEqual(items2.newfirstname, 'Zero')
 		self.assertEqual(items2.newlastname, 'Shi')
 		self.assertEqual(items2.newphonenumber, '09123456666')
 		self.assertEqual(items2.newshipadd, 'BLK10')
 		self.assertEqual(items2.newcity, 'Imus')
 		self.assertEqual(items2.newprovince, 'Cavite')
 		self.assertEqual(items2.newPostal, '4114')
 		self.assertEqual(items2.newamount, '299')
 		self.assertEqual(items2.newpackaging, 'Plain Box')

 		self.assertEqual(items1.newfirstname, 'Rashina')
 		self.assertEqual(items1.newlastname, 'Majid')
 		self.assertEqual(items1.newphonenumber, '09123456789')
 		self.assertEqual(items1.newshipadd, 'BLK4')
 		self.assertEqual(items1.newcity, 'Dasmarinas')
 		self.assertEqual(items1.newprovince, 'Cavite')
 		self.assertEqual(items1.newPostal, '4114')
 		self.assertEqual(items1.newamount, '299')
 		self.assertEqual(items1.newpackaging, 'Brown Box')

 	def test_template_displays_list(self):
 		Registration.objects.create(newfirstname='Rashina',
 			newlastname='Majid',
 			newphonenumber='09123456789', 
 			newshipadd='BLK4',
 			newcity='Dasmarinas', 
 			newprovince='Cavite', 
 			newPostal='4114',
 			newamount='299',
 			newpackaging='Brown Box',)

 		Registration.objects.create(newfirstname='Zero', 
 			newlastname='Shi',
 			newphonenumber='09123456666',
 			newshipadd='BLK10',
 			newcity='Imus',
 			newprovince='Cavite', 
 			newPostal='4114',
 			newamount='299',
 			newpackaging='Plain Box',)
 		response = self.client.get('/')
 		self.assertIn('1: Rashina Majid 09123456789 BLK4 Dasmarinas Cavite 4114 299 Brown Box', response.content.decode())
 		self.assertIn('2: Zero Shi 09123456666 BLK10 Imus Cavite 4114 299 Plain Box', response.content.decode())