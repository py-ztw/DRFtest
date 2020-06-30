from rest_framework import serializers, exceptions

from Drf_day03.models import Book, Press


class PressModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Press
        fields = ("press_name", "address", "pic")


class BookModelSerializer(serializers.ModelSerializer):
    publish = PressModelSerializer()
    class Meta:
        model = Book
        fields = ("book_name", "price", "pic", "publish")

        # 可以直接查询所有字段
        # fields = "__all__"
        # 可以指定不展示哪些字段
        # exclude = ("is_delete", "create_time", "status")
        # 指定查询深度  关联对象的查询  可以查询出有外键关系的信息
        # depth = 1


class BookDeModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ("book_name", "price", "publish", "authors")
        extra_kwargs = {
            "book_name": {
                "required": True,  # 设置为必填字段
                "min_length": 3,
                "error_messages": {
                    "required": "图书名必填",
                    "min_length": "长度太短"
                }
            },
            "price": {
                "max_digits": 5,
                "decimal_places": 4,
            }
        }

    def validate_book_name(self, value):
        if "1" in value:
            raise exceptions.ValidationError("图书名含有1")
        return value

    def validate(self, attrs):
        pwd = attrs.get("password")
        re_pwd = attrs.pop("re_pwd")
        if pwd != re_pwd:
            raise exceptions.ValidationError("两次密码不一致")

        return attrs


class BookModelSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("book_name", "price", "publish", "authors", "pic")

        extra_kwargs = {
            "book_name": {
                "required": True,
                "min_length": 3,
                "error_messages": {
                    "required": "图书名必填",
                    "min_length": "长度太短"
                }
            },
            "publish": {
                "write_only": True
            },
            "authors": {
                "write_only": True
            },
            "pic": {
                "read_only": True
            }
        }

    def validate_book_name(self, value):
        if "1" in value:
            raise exceptions.ValidationError("图书名含有1")
        return value

    def validate(self, attrs):

        price = attrs.get("price", 0)
        if price > 90:
            raise exceptions.ValidationError("超过设定金额~")

        return attrs
