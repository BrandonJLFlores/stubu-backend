from django.shortcuts import render
import pyrebase
from django.contrib import auth

config = {
    'apiKey': "AIzaSyC6C6gWxw8AwZaFZmrXZv6Ejy4sWu6dv4k",
    'authDomain': "stubu-2018.firebaseapp.com",
    'databaseURL': "https://stubu-2018.firebaseio.com",
    'projectId': "stubu-2018",
    'storageBucket': "stubu-2018.appspot.com",
    'messagingSenderId': "517232906173"
}

firebase = pyrebase.initialize_app(config)

authe = firebase.auth()
database=firebase.database()
# opening form
def signIn(request):

    return render(request, "signIn.html")
# get values from sign in and put it on welcome
def postsign(request):
    email = request.POST.get('email') #from html
    passw = request.POST.get('pass') #from html
    try:
        user = authe.sign_in_with_email_and_password(email,passw)
    except:
        message="Invalid Credentials"
        return render(request,"signIn.html",{"messg":message}) #3rd param {name sa i send:content}
    print(user)
    print(user['idToken'])
    session_id=user['idToken']
    request.session['uid']=str(session_id) #requesting session, convert to str session id
    return render(request, "welcome.html",{"e":email})

def logout(request):
    auth.logout(request)
    return render(request,'signIn.html') #redirect

def signUp(request):

    return render(request,"signup.html")

def postsignup(request):
    name = request.POST.get('name')
    email = request.POST.get('email')  # from html
    passw = request.POST.get('pass')  # from html
    try:
        user = authe.create_user_with_email_and_password(email,passw)
        uid = user['localId']
        data = {"name": name, "status": "1"}
        database.child("users").child(uid).child("details").set(data)
    except:
        message="Error on creating account"
        return render(request,"signup.html",{"messg":message})



    return render(request,"signIn.html")