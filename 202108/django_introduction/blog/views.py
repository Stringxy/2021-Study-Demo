from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from blog.tasks import NormalTask
# Create your views here.

def hello(request):
    return HttpResponse("hello")

def do(request):
    # 执行异步任务
    #NormalTask.delay()
    NormalTask.apply_async(args=('hello','xy'),queue='normal_tasks')
    return JsonResponse({'result':'ok'})
