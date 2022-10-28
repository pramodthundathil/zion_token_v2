from tokenize import Token
from django.shortcuts import render,redirect
from .models import TokenTable
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from datetime import datetime
import datetime

#Displaying token On screen

@login_required(login_url="SignIn")
def TokenDisplayer(request):
    call_token = TokenTable.objects.filter(CallStatus = False)
    try:
        first_token  = call_token[0]
        token_call = first_token.Tokens
    except:
        return render(request,'index1.html')
    
    return render(request,'index1.html',{"token_call":token_call,"call_token":call_token})

# Genarate the Token also render Token admin
@login_required(login_url="SignIn")
def TokenGenerator(request):
    all_Tokens = TokenTable.objects.all()
    last_token = TokenTable.objects.all().last()
    last_number = last_token.Tokens
    call_token = TokenTable.objects.filter(CallStatus = False)
    try:
        first_token  = call_token[0]
        token_call = first_token.Tokens
    except:
        splited_token = last_number.split("-")
        X = int(splited_token[-1])
        x = X+1
        token = "N-{}".format(x)
        name = "unknown"
        Token = TokenTable.objects.create(Tokens = token,CustomerName = name)
        Token.save()    
        messages.success(request,"Token Number {}".format(token))    
        return redirect("TokenGenerator")
    
    if request.method == "POST":
        splited_token = last_number.split("-")
        X = int(splited_token[-1])
        x = X+1
        token = "N-{}".format(x)
        name = request.POST["Pname"]
        Token = TokenTable.objects.create(Tokens = token,CustomerName = name)
        Token.save()    
        messages.success(request,"Token Number {}".format(token))    
        return redirect("TokenGenerator")
        
    return render(request,'index.html',{"token":last_number,"token_call":token_call,"all_Tokens":all_Tokens})      

# Token Calling 

@login_required(login_url="SignIn")
def CallToken(request):
    
    call_token = TokenTable.objects.filter(CallStatus = False)
    try:
        first_token  = call_token[0]
        first_token.CallStatus = True
        first_token.save()
    except:
        return redirect("TokenGenerator")
         
    return redirect("TokenGenerator")

# Recalling Token also render Token admin
@login_required(login_url="SignIn")
def ReCallToken(request):
    if request.method == "POST":
        Token_id = request.POST["tokenid"]
        token = TokenTable.objects.get(id = Token_id)
        token.CallStatus = False
        token.save()
        Token = token.Tokens
        all_Tokens = TokenTable.objects.all()
        last_token = TokenTable.objects.all().last()
        last_number = last_token.Tokens
        call_token = TokenTable.objects.filter(CallStatus = False)
        return render(request,'index.html',{"token":last_number,"token_call":Token,"all_Tokens":all_Tokens})      
        
    return redirect("TokenGenerator")

@login_required(login_url="SignIn")
def RestTokenNewDay(request):
    if request.method == "POST":
        d = datetime.datetime.now()
        y = str(d.year) + str(d.month) +str(d.day)
        file = open(y+".txt","w")
        file.close()
        file = open(y+".txt","a")
        qry_set = TokenTable.objects.all()
        for x in qry_set:
            val = str(x.Tokens)+ ":"+ str(x.CustomerName)+ " :-" +str(x.Token_date)+"\n"
            file.write(val)
        file.close()
        
        qry_set.delete()
        token = "N-1"
        name = "Unknown"
        Token = TokenTable.objects.create(Tokens = token,CustomerName = name)
        Token.save()
        return redirect("TokenGenerator")
        
    
# Token Admin Screen  
@login_required(login_url="SignIn")
def TokenAdmin(request):
    return render(request,"index.html")

# user Login
def SignIn(request):
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST["pswd"]
        user = authenticate(request,username = username, password=password)
        if user is not None:
            login(request,user)
            return redirect("TokenGenerator")
        else:
            messages.info(request,"Username or password Incorrect")
            return redirect("SignIn")
            
    return render(request,"login.html")

# user logout
def SignOut(request):
    logout(request)
    return redirect("SignIn")