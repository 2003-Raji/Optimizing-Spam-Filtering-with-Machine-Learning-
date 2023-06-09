from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from email_admin.models import SpamModel
from user.models import RegisterModel, SendmailModel, FeedbackModel


def login(request):
    if request.method == "POST":
        if request.method == "POST":
            usid = request.POST.get('username')
            pswd = request.POST.get('password')
            if usid == 'admin' and pswd == 'admin':
                return redirect('admin_page')
    return render(request,'email_admin/login_page.html')

def admin_page(request):
    obj=RegisterModel.objects.all()
    return render(request,'email_admin/admin_page.html',{'objects':obj})

def analysis_page(request):
    obj=SendmailModel.objects.all()

    return render(request,'email_admin/analysis_page.html',{'obj':obj})

def analysisdelete(request,pk):

    obj = get_object_or_404(SendmailModel, pk=pk)
    obj.delete()
    return redirect('analysis_page')
def categoryanalysis_chart(request,chart_type):
    chart = SendmailModel.objects.values('category').annotate(dcount=Count('category'))
    return render(request,'email_admin/chart.html',{'objects':chart,'chart_type':chart_type})

def viewfeedback(request):
    obj = FeedbackModel.objects.all()
    return render(request,'email_admin/viewfeedback.html',{'object':obj})