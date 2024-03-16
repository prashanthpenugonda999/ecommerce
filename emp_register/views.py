from django.shortcuts import render
from emp_register.forms import info_forms


def index(request):
    return render(request,"index.html")
    

def Register(request):
    message="Create account"
    login="Sign up"
    
    return render(request,"register.html",{"message":message,"login":login})
    

   
def Login(request):
    try:
        request.session["register"]
        register=request.session["register"]
    except:

        register="none"
    
    if register == "true":
        message="Log in into account"
        login="Login"
        return render(request,"login.html",{"message":message,"login":login})
    else:
        login="Sign up"  
        
        message="Create Account First"
        return render(request,"register.html",{"message":message,"login":login})

    
def Homepage(request):
    
    name=request.POST["name"]
    email=request.POST["mail"]
    
    pwd=request.POST["pwd"]
    re_pwd=request.POST["re_pwd"]
    request.session["mail"]=email
    request.session["pwd"]=pwd
    request.session.set_expiry(0)
    
    if pwd!=re_pwd or len(email) ==0 or len(name)==0 :
        
        
        login="Sign up"  
        
        message="Enter Correct Details!!"
        return render(request,"register.html",{"message":message,"login":login})
    else:
        message1="Successfully"
        message2="Created"
        message3="Account"
        request.session["register"]="true"
        request.session["name"]=name
        return render(request,"sign.html",{"name":name,"message1":message1,"message2":message2,"message3":message3})

    
  
  
def Loginpage(request):
    input_pwd=request.POST["pwd"]
    print(input_pwd)
    input_mail=request.POST["mail"]
    login="Login"
    email=request.session["mail"]
    name=request.session["name"]
    pwd=request.session["pwd"]
    print(pwd)
    print(email)
    if input_pwd==pwd and email==input_mail:
        return render(request,"sign.html",{"name":name})
        
    else:
        message="Enter Correct Details!!"
        return render(request,"login.html",{"message":message,"login":login})


    
    
    
    
    


