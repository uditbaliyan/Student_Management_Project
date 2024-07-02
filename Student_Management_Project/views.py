from django.shortcuts import render,redirect,HttpResponse
from app1.Email_Back_End import EmailBackEnd
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages 

def base(request):
    """
    Purpose: 
    """
    return render(request,'BASE.html')
    
# end def


def login(request):
    """
    Purpose: 
    """
    return render(request,'login.html')
    
# end def

def Do_login(request):
    """
    Purpose: 
    """
    if (request.method=="POST"):
        # comment:
        user=EmailBackEnd.authenticate(request,username=request.POST.get('email'),password=request.POST.get('password'))

        if (user!=None):
            # comment:
            login(request)
            user_type=user.user_type
            if (user_type=='1'):
                # comment: 
                return HttpResponse("this is hod")
            # end if
            elif (user_type=='2'):
                # comment: 
                return HttpResponse("this is staff")
            elif (user_type=='3'):
                # comment: 
                return HttpResponse("this is student")            
            else:
                # comment: 
                # message
                messages.error(request,'Email and Password invalid')
                return redirect ('login')
        else :
            # comment: 
            # message
            messages.error(request,'Email and Password invalid')
            return redirect ('login')
        # end if
    # end if
    
# end def