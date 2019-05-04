from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Application


def index(request):
    return HttpResponse("申请记录")


def Application(request):
    # 去模型里取数据
    applicationList = Application.objects.all()
    # 将数据传递给模板,模板再渲染页面，将渲染好的页面返回给浏览器
    return render(request, 'myApp/application.html', {'application': applicationList})


def index(request):
    return HttpResponse("审核记录")


def checkRecord(request):
    # 获得对应的审核对象
    check = Application.objects.get(pk=num)
    # 获得审核对象下的所有状态对象列表
    checkList = check.state_set.all()
    return render(request, 'myApp/application.html', {"application": checkList})






