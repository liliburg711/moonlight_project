from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Contact
from django.contrib import messages


# Create your views here.
def contact(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        florist_email = request.POST['florist_email']
        product_id = request.POST['product_id']
        product = request.POST['product']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        # Check user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(product_id=product_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry 您已經詢問過關於此商品的問題')
                return redirect('/products/'+product_id)



        contact = Contact(user_id=user_id, product_id=product_id, product=product,
        name=name, email=email, phone=phone, message=message)

        contact.save()

        #Send mail
        send_mail(
            'Product Inquiry',
            'There has been an inquiry for '+ product +'. Sign into the admin panel for more info.',
            'liliburg711@gmail.com',
            [florist_email, 'liliburg711@gmail.com'], 
            fail_silently=False

        )
        
        print(florist_email)

        messages.success(request, 'Your request has been submitted, our florists will get back you soon 您的詢問已送出，我們的花藝師會盡快回覆您')
        

        return redirect('/products/'+product_id)