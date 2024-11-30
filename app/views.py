from django.shortcuts import HttpResponse, render, redirect
from .models import Por, Tag, Test
from .form import form, Ts
from .filter import PostFilter
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request, 'home.html')

def post(request, pk):
    
    pos = Por.objects.get(id = pk)
    if request.method =='POST':
        if 'yes' in request.POST:
            pos.delete()
            return redirect('postss')
    return render(request, 'post.html', {'poss':pos, })

def posts(request):
    postss = Por.objects.all()
    po = Por.objects.filter(active = True)
    myfil = PostFilter(request.GET, queryset=po)
    po = myfil.qs
    return render(request, 'posts.html', {'data':po, 'fil':myfil})


def port(request):
    return render(request, 'port.html')



def create(request):
    froms = form()
    if request.method == 'POST':
        data = form(request.POST, request.FILES)
        if data.is_valid():
            data.save()
    return render(request, 'form.html', {'ff':froms})



def test(request):
    forms = Ts()
    if request.method == 'POST':
        data = Ts(request.POST, request.FILES)
        if data.is_valid():
            data.save()
            return redirect('postss')
    return render(request, 'test.html',{ 'form':forms})


def up(request, pk):
    postt = Por.objects.get(id=pk)
    fo = form(instance=postt)
    if request.method == 'POST':
        data = form(request.POST, request.FILES, instance=postt)
        if data.is_valid():
            data.save()
            return redirect('postss')
    return render(request, 'update.html', {'form':fo})


def dell(request, pk):
    postt = Por.objects.get(id=pk)
    fo = form(instance=postt)
    if request.method == 'POST':
        
            return redirect('postss')
    return render(request, 'delete.html', {'form':fo})



def send_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        subjec = request.POST.get('subject')
        try:
            print('111')
            send_mail(
                subject=subjec,
                message=message,
                from_email='khaledkgccc@gmail.com',  # بريدك الإلكتروني
                recipient_list=[email],
                fail_silently=False,
            )
            print('2222')
            return HttpResponse('تم إرسال البريد الإلكتروني بنجاح!')
        except Exception as e:
            return HttpResponse(f'حدث خطأ: {e}')

    return render(request, 'email.html')