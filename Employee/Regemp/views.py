from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from Regemp.forms import ProfileFm, RegistrationForm
from Regemp.models import ProfileMod


# Create your views here.
def check(request):
    form = ProfileFm()
    context = {'form': form}
    qs = ProfileMod.objects.all()
    context['reg'] = qs
    if request.method == "POST":
        form = ProfileFm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("check")
    return render(request, "Regemp/check.html", context)


def Register(request):
    form = RegistrationForm()
    context = {'form': form}
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("SignUp")
        else:
            context = {}
            context['form'] = form
            return render(request, "Regemp/Registeration.html", context)
            print("valid")
    return render(request, "Regemp/Registeration.html", context)


def SignUp(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("pwd")
        print(username, ",", password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return redirect("Signin")
    return render(request, "Regemp/Signin.html")


def index(request):
    emp = ProfileMod.objects.all()
    context = {'check': emp}

    return render(request, "Regemp/index.html", context)


def EmpView(request, pk):
    form = ProfileMod.objects.get(id=pk)
    context = {'view': form}
    return render(request, "Regemp/Empview.html", context)


def EmpEdit(request, pk):
    obj = ProfileMod.objects.get(id=pk)
    form = ProfileFm(instance=obj)
    context = {'edit': form}
    if request.method == "POST":
        print("inside post")
        obj = ProfileMod.objects.get(id=pk)
        form = ProfileFm(instance=obj, data=request.POST, files=request.FILES)
        if form.is_valid():
            print("inside edit")
            form.save()
            return redirect("index")
        else:
            form = ProfileFm(request.POST)
            context = {}
            context['edit'] = form
            return render(request, "Regemp/EmpEdit.html", context)
    return render(request, "Regemp/EmpEdit.html", context)


def DeletePro(request, pk):
    dele = ProfileMod.objects.get(id=pk)
    dele.delete()
    form = ProfileFm()
    context = {'del': form}
    qs = ProfileMod.objects.all()
    context['Prodel'] = qs
    return redirect("index")
