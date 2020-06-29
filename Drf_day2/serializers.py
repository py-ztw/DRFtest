from rest_framework import serializers
from Drf_day2.models import Employee
from DRF import settings


# 序列化器
class EmployeeSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()


    salt = serializers.SerializerMethodField()
    def get_salt(self, obj):
        return "23333"

    gender = serializers.SerializerMethodField()
    def get_gender(self, obj):
        return obj.get_gender_display() #choices类型 可以用get_字段名_display()直接访问值

    pic = serializers.SerializerMethodField()
    def get_pic(self, obj):
        return "%s%s%s" % ("http://127.0.0.1:8000", settings.MEDIA_URL, str(obj.pic))#推荐使用


# 反序列化器
class EmployeeDeSerializer(serializers.Serializer):

    username = serializers.CharField(
        max_length=10,
        min_length=2,
        error_messages={
            "max_length": "用户名过长",
            "min_length": "用户名太短",
        }
    )
    password = serializers.CharField(required=False)
    phone = serializers.CharField()

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)
