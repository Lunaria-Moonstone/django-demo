from django.shortcuts import render, HttpResponse

from simsys.forms import UserForm
from simsys.models import User


# Create your views here.

def login(request):
    userForm = UserForm(request.POST)
    if request.method == 'POST':
        if userForm.is_valid():
            try:
                User.objects.get(username=userForm.data.get('name'), password=userForm.data.get('password'))
                return HttpResponse('登录成功!')
            except User.DoesNotExist as e:
                print(e)
                return HttpResponse('登录失败，用户名不存在或密码错误!')
            except Exception as e:
                print(e)
                return HttpResponse('登录失败，未知错误!')
    return render(request, 'login.html', {'form': userForm})
