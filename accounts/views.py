from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from orders.models import Order, OrderItem

# Create your views here.
def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #Check if passwords match
        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)

                    # Directly Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'You are logged in')
                    # return redirect('index')

                    # Next step Login after register
                    user.save()
                    messages.success(request, 'You are now registered and can login in')
                    return redirect('login')
                    

        else: 
            messages.error(request, 'Password is not match')
            return redirect('register')
    else: 
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        # Login User
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')

def dashboard(request):
    
    order = Order.objects.order_by('-updated').filter(username=request.user.username, email=request.user.email)
    print(order)

    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    print(user_contacts)
  

    return render(request, 'accounts/dashboard.html', {'order': order, 'contacts': user_contacts})