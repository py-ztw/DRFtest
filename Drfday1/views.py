from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views import View
from rest_framework.response import Response

# 免认证
from rest_framework.views import APIView

from Drfday1.models import User


@csrf_exempt
def user(request):
    if request.method == "GET":
        print("GET--查询")
        return HttpResponse("GET-SUCCESS")

    elif request.method == "POST":
        print("POST--添加")
        return HttpResponse("POST-SUCCESS")

    elif request.method == "PUT":
        print("PUT--修改")
        return HttpResponse("PUT-SUCCESS")

    elif request.method == "DELETE":
        print("DELETE--删除")
        return HttpResponse("DELETE-SUCCESS")

# 类视图免认证：@method_decorator(csrf_exempt, name="dispatch")
@method_decorator(csrf_exempt, name="dispatch")
class UserView(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get("id")
        print(user_id)
        if user_id:
            user = User.objects.filter(pk=user_id).values("username", "password", "gender").first()
            if user:
                return JsonResponse({
                    "status": 200,
                    "message": "查询单个用户成功",
                    "results": user
                })
        else:
            user_list = User.objects.all().values("username", "password", "gender")
            print(type(user_list))
            if user_list:
                return JsonResponse({
                    "status": 200,
                    "message": "查询所有用户成功",
                    "results": list(user_list),
                })

        return JsonResponse({
            "status": 500,
            "message": "查询失败",
        })

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        try:
            user_obj = User.objects.create(username=username, password=pwd)
            return JsonResponse({
                "status": 201,
                "message": "创建用户成功",
                "results": {"username": user_obj.username, "pwd":user_obj.password,"gender": user_obj.gender}
            })
        except:
            return JsonResponse({
                "status": 500,
                "message": "创建用户失败",
            })

class UserAPIView(APIView):

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get("id")
        print(user_id)
        if user_id:
            user = User.objects.filter(pk=user_id).values("username", "password", "gender").first()
            if user:
                return JsonResponse({
                    "status": 200,
                    "message": "查询单个用户成功",
                    "results": user
                })
        else:
            user_list = User.objects.all().values("username", "password", "gender")
            print(type(user_list))
            if user_list:
                return JsonResponse({
                    "status": 200,
                    "message": "查询所有用户成功",
                    "results": list(user_list),
                })

        return JsonResponse({
            "status": 500,
            "message": "查询失败",
        })


    def post(self, request, *args, **kwargs):
        request_data = request.data
        print(request_data['username'])
        if request_data == {}:
            return Response({
                "status": 500,
                "message": "数据有误"
            })
        user =User.objects.create(username=request_data['username'], password=request_data['password'])
        if user:
            return Response({
                "status": 200,
                "message": "用户创建成功",
                "results": dict(request_data)
            })
        else:
            return Response({
                "status": 500,
                "message": "用户创建失败"
            })