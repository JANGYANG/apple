from django.shortcuts import render
from manitto.models import Apple
from manitto.smsSender import Sms

# Create your views here.
def index(request):
    return render(request, 'manitto/index.html')


def result(request):

    a = Apple.objects.filter(name=request.POST.get('name')).first()
    print(a)
    if a:
        sms = Sms()
        # def send(self, name, phoneNum, manitto):
        sms.send(a.name, a.phone, a.manittoId.name)


        
        return render(request, 'manitto/okgo.html')
    else:
        return render(request, 'manitto/fail.html')

def reset(request):

    return render(request,'manitto/reset.html')

def reset_result(request):
    print(request.POST.get('password'))
    if request.POST.get('password') == "qowjddbs":
        print('success')

        from manitto.shuffle import shuffle
        shuffle()

        return render(request, 'manitto/reset_result.html')
    else:
        print('fail')
        return render(request, 'manitto/fail.html')

    