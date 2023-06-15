from django.shortcuts import render

# Create your views here.
def login(request):
    if request.method == 'get':
        print('ok')
        return render(request, 'login.html')
    return render(request, 'login.html')