from django.db import models

class Pinfo(models.Model):
	Fname = models.CharField(max_length = 200)
	Lname = models.CharField(max_length = 200)
	Pnumb = models.CharField(max_length = 200)
	Shipad = models.CharField(max_length = 200)
	Citi = models.CharField(max_length = 200)
	Prov = models.CharField(max_length = 200)
	Postal = models.CharField(max_length = 200)
	 
class Order(models.Model):
	user_Info = models.ForeignKey("Pinfo", on_delete = models.CASCADE)
	bquant = models.IntegerField()
	Pack = models.CharField(max_length = 200)
	Bookm = models.CharField(max_length = 200)
	highl = models.CharField(max_length = 200)
	Stick = models.CharField(max_length = 200)
	
class Binfo(models.Model):
	user_Info = models.ForeignKey("Order", on_delete = models.CASCADE)
	Mod = models.CharField(max_length = 200)
