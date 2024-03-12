from django.shortcuts import render
from emp_register.forms import info_forms



def index(request):
    return render(request,"index.html")
    

def Login(request):
    
    
   
    return render(request,"login.html")
def Homepage(request):
    name=request.POST["name"]
    email=request.POST["mail"]
    print(email)
    pwd=request.POST["pwd"]
    re_pwd=request.POST["re_pwd"]
    
    if pwd!=re_pwd or len(email) ==0 or len(name)==0 :
        
        message="Enter Correct Details!!"
        return render(request,"login.html",{"message":message})
    else:
        request.session["name"]=name
        return render(request,"sign.html",{"name":name})


    
    
    
    
    


