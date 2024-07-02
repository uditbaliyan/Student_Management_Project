from django.shortcuts import render,redirect,HttpResponse




def home(request):
    """
    Purpose: 
    """
    return render(request,'HOD/home.html')
    
# end def