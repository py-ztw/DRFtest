from Drf_day2.models import Employee
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EmployeeSerializer, EmployeeDeSerializer


class EmployeeAPIView(APIView):

    def get(self, request, *args, **kwargs):

        user_id = kwargs.get("pk")

        if user_id:
            emp_obj = Employee.objects.get(pk=user_id)
            emp_ser = EmployeeSerializer(emp_obj)
            data = emp_ser.data
            return Response({
                "status": 200,
                "msg": "查询成功",
                "results": data,
            })
        else:
            emp_list = Employee.objects.all()
            emp_list_ser = EmployeeSerializer(emp_list, many=True).data

            return Response({
                "status": 200,
                "msg": "查询成功",
                "results": emp_list_ser,
            })

    def post(self, request, *args, **kwargs):
        user_data = request.data
        if not isinstance(user_data, dict) or user_data == {}:
            return Response({
                "status": 501,
                "msg": "数据有误",
            })
        serializer = EmployeeDeSerializer(data=user_data)
        print(serializer.is_valid())
        if serializer.is_valid():
            emp_obj = serializer.save()
            return Response({
                "status": 201,
                "msg": "创建成功",
                "results": EmployeeSerializer(emp_obj).data
            })
        else:
            return Response({
                "status": 501,
                "msg": "创建失败",
                "results": serializer.errors# errors中有验证失败后错误信息
            })
