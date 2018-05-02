from django.shortcuts import render
import pyrebase

config = {
    'apiKey': "AIzaSyC6C6gWxw8AwZaFZmrXZv6Ejy4sWu6dv4k",
    'authDomain': "stubu-2018.firebaseapp.com",
    'databaseURL': "https://stubu-2018.firebaseio.com",
    'projectId': "stubu-2018",
    'storageBucket': "stubu-2018.appspot.com",
    'messagingSenderId': "517232906173"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
# opening form
def singIn(request):

    return render(request, "signIn.html")
# get values from sign in and put it on welcome
def postsign(request):
    email = request.POST.get('email')
    passw = request.POST.get('pass')

    user = auth.sign_in_with_email_and_password(email,passw)

    return render(request, "welcome.html",{"e":email})