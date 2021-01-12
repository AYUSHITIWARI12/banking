from django.shortcuts import render, HttpResponse
from home.models import Viewcustomer
from home.models import Userhistory
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login




from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home/home.html')

def about(request):
    return render(request,'home/about.html')


def viewcustomer(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        account = request.POST['account']
        cif = request.POST['cif']
        branchcode = request.POST['branchcode']
        state = request.POST['state']
        amount = request.POST['amount']
        content = request.POST['content']
        print(name, email, account, cif, branchcode, state, amount, content)
        if len(name)<2 or len(email)<3 or len(account)<12:
            messages.error(request, 'Please Fill the Details Correctly')
            # messages.success(request, 'Your Transaction Done Successfully!')
        else:
            viewcustomer = Viewcustomer(name=name, email=email, account=account,cif=cif, branchcode=branchcode, state=state,amount=amount,content=content)
            viewcustomer.save()
            messages.success(request, 'Your Transaction Done Successfully!')

    return render(request,'home/viewcustomer.html')
def history(request):
    return render(request,'home/history.html')
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        from django.contrib.auth import login
        login(request, user)
        return redirect('/')
    return render(request, 'home/login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        account = request.POST['account']
        aadhar = request.POST['aadhar']
        city = request.POST['city']
        state = request.POST['state']

        myuser = User.objects.create_user(username, email,password)
        myuser.name = username
        myuser.save()
        user = authenticate(username=username,password=password)
        from django.contrib.auth import login
        login(request, user)

        return redirect('/')
    return render(request, 'home/signup.html')
