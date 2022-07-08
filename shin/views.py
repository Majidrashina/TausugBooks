from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import perinfo

installed_apps = ['shin']

def Homepage(request):
	return render(request,'Buybooks.html')



def Books(request):
	if request.method == 'POST':
		first_name= request.POST['First_Name']
		last_name = request.POST['Last_Name']
		num = request.POST['phone']
		add = request.POST['Adress']
		city = request.POST['City']
		prov = request.POST['Province']
		pos = request.POST['postal']
		data = Pinfo.objects.create(Fname = first_name,
		Lname = last_name,
		Pnumb = num,
		Shipad = add,
		Citi= city,
		Prov= prov,
		Postal = pos,)
		data.save()
	return render(request,'products.html')

def Checkout(request):
	report = Pinfo.objects.all()
	return render(request,'checkout.html', {'report':report})

def edit(request, id):
	info = Pinfo.objects.get(id=id)
	form = perinfo(instance=info)
	if request.method == 'POST':
		form = perinfo(request.POST, instance = info)
		if form.is_valid():
			form.save()
			return redirect('/order')

	return render(request, 'edit.html', {'form':form})
		
def cancel(request, id):
    a = Pinfo.objects.get(id=id)
    for x in Pinfo.objects.only('id'):

        print(x)
        if a == x:
            d = "a"
            print(d)
            x = Pinfo.objects.get(id=id).delete()
            break
    return redirect('/order')



#def MainPage(request):
#	if request.method == 'POST':
#		Registration.objects.create(newfirstname=request.POST['First_Name'], 
#			newlastname= request.POST['Last_Name'],
#			newphonenumber= request.POST['phone'],
#			newshipadd= request.POST['Street_Adress'],
#			newcity= request.POST['City'],
#			newprovince=request.POST['Province'],
#			newPostal=request.POST['postal'],
#			newamount=request.POST['AMOUNT'],
#			newpackaging=request.POST['packaging'],)
#		return redirect('/')
#	reglist = Registration.objects.all()
#	return render(request, 'mainpage.html',{'registered':reglist})
