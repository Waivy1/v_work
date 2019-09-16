from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
from django.views import View
from core import models

class IndexPage(View):
    def get(self, request):
        return render(request, 'index_page.html')

class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        input_login = request.POST['login']
        input_password = request.POST['password']

        try:
            new_user = models.User.objects.get(login=input_login, password=input_password)

        except models.User.DoesNotExist as e:
            return HttpResponse(f'user {input_login} doesnt exist')

        request.session['user_id'] = new_user.id

        return redirect('/')
