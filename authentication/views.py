from django.shortcuts import render, redirect
from authentication.forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def index(request):
    return render(request, "index.html")


def login(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            # Check if the user exists
            user = authenticate(request, username=username, password=password)
            if user is None:
                form.add_error("password", "Username or password incorrect")
                return render(request, "login.html", {"form": form})

            # user has entered valid credentials, he can now be logged in
            auth_login(request, user)

            # set a flash message and redirect to the index page
            messages.success(request, "You have been logged in successfully!")

            return redirect("index")
        else:
            messages.error(request, "Invalid form data")
            return redirect("login")

    # if a GET we'll create a blank form
    else:
        form = LoginForm()

    context = {
        "form": form
    }
    return render(request, "login.html", context)


def register(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # Extract cleaned data from the form
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            password_confirm = form.cleaned_data.get("password_confirm")

            # Check if the passwords match
            if password != password_confirm:
                form.add_error("password_confirm", "Passwords do not match")
                return render(request, "register.html", {"form": form})

            # Perform any additional validations if necessary
            if User.objects.filter(email=email).exists():
                form.add_error("email", "Email already exists")
                return render(request, "register.html", {"form": form})
            elif User.objects.filter(username=username).exists():
                form.add_error("username", "Username already exists")
                return render(request, "register.html", {"form": form})

            # Create a new user instance
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            user.save()

            # set a flash message and redirect to the login page
            messages.success(request, "User created successfully! You can now login.")

            return redirect("login", permanent=True)
        else:
            messages.error(request, "Invalid form data")
            return redirect("register")

    # if a GET we'll create a blank form
    else:
        form = RegisterForm()

    context = {
        "form": form
    }
    return render(request, "register.html", context)
