from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def resturant(request):
    if request.method == 'POST':
        Name = request.POST['restuarant_name']
        street = request.POST['street_name']
        number = request.POST['number']
        city = request.POST['city']
        zipcode = request.POST['Zipcode']
        state_or_province = request.POST['state']
        county = request.POST['country']
        telephone = request.POST['telephone_no']
        r = Restaurant(name=Name,street=street,number=number,city=city,zipcode=zipcode,state_or_province=state_or_province,
                       county=county,telephone=telephone)
        r.save()
        return render(request,'restaurant_app/restaurant.html')
    return render(request,'restaurant_app/restaurant.html')


def dish(request,id):
    d=Dish.objects.filter(restaurant=id)
    if request.method == 'POST':
        Name = request.POST['dishName']
        description = request.POST['description']
        price = request.POST['price']
        image = request.FILES['image']
        d = Dish(name=Name,description=description,price=price,image=image,restaurant=Restaurant.objects.get(id=id))
        d.save()
        return redirect('/dish/'+str(id))
    return render(request,'restaurant_app/dish.html',{'dishes':d,'res_id':id})

def review(request,id):
    r = Review.objects.filter(dish=id)
    if request.method =='POST':
        choices = request.POST['choices']
        comment = request.POST['comment']
        r = Review(rating=choices,comment=comment,dish=Dish.objects.get(id=id))
        r.save()
        return redirect('/review/'+str(id))
    return render(request,'restaurant_app/review.html',{'reviews':r,'dish_id':id})

def home(request):
    resturants = Restaurant.objects.all()

    if request.method == 'POST':
        Name = request.POST['restuarant_name']
        street = request.POST['street_name']
        number = request.POST['number']
        city = request.POST['city']
        zipcode = request.POST['Zipcode']
        state_or_province = request.POST['state']
        county = request.POST['country']
        telephone = request.POST['telephone_no']
        r = Restaurant(name=Name, street=street, number=number, city=city, zipcode=zipcode,
                       state_or_province=state_or_province,
                       county=county, telephone=telephone)
        r.save()
        return redirect('/all')
    return render(request, 'restaurant_app/home.html',{'resturants':resturants})



def delete(request,id):
    d = Review.objects.get(id=id)
    d.delete()
    return redirect('/all')

def update(request,id):
    r = Review.objects.get(id=id)
    if request.method =='POST':
        choices = request.POST['choices']
        comment = request.POST['comment']
        Review.objects.filter(id=id).update(rating=choices, comment=comment)
        return redirect('/all')
    return render(request,'restaurant_app/review.html',{'review':r})

def delete_resturant(request,id):
    r = Restaurant.objects.get(id=id)
    r.delete()
    messages.warning(request,'The resturant {} has been deleted'.format(id))
    return redirect('/all')

def update_resturant(request,id):
    r = Restaurant.objects.get(id=id)
    if request.method == 'POST':
        Name = request.POST['restuarant_name']
        street = request.POST['street_name']
        number = request.POST['number']
        city = request.POST['city']
        zipcode = request.POST['Zipcode']
        state_or_province = request.POST['state']
        county = request.POST['country']
        telephone = request.POST['telephone_no']
        Restaurant.objects.filter(id=id).update(name=Name, street=street, number=number, city=city, zipcode=zipcode,
                       state_or_province=state_or_province,
                       county=county, telephone=telephone)
        return redirect('/all')
    return render(request, 'restaurant_app/update_resturant.html', {'resturant': r})

def delete_dish(request,pk,id):
    d = Dish.objects.get(id=id)
    d.delete()
    return redirect('/dish/'+str(pk))

def update_dish(request,id):
    dish = Dish.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST['dishName']
        description = request.POST['description']
        price = request.POST['price']
        image = request.FILES['image']
        Dish.objects.filter(id=id).update(name=name, description=description, price=price, image=image )
        return redirect('/all')
    return render(request, 'restaurant_app/update_dish.html', {'dish': dish})


def update_review(request,pk,id):
    review = Review.objects.get(id=id)
    if request.method =='POST':
        choices = request.POST['choices']
        comment = request.POST['comment']
        Review.objects.filter(id=id).update(rating=choices,comment=comment)
        return redirect('/review/' + str(pk))
    return render(request, 'restaurant_app/update_review.html', {'review': review})


def delete_review(request,pk,id):
    Review.objects.get(id=id).delete()
    return redirect('/review/'+str(pk))


def fo(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            print(form)
        else:
            print('sorry')
    else:
        form =NameForm()
    return render(request,'restaurant_app/forms.html',{'form':form})

def search(request):
    search_box = request.POST['Search']
    data = Restaurant.objects.filter(name__icontains=search_box)
    return render(request,'restaurant_app/home.html',{'resturants':data})