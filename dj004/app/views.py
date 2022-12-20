from django.shortcuts import render

# Create your views here.
from rest_framework import serializers, viewsets, routers
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin
from app.models import Student
from rest_framework.response import Response


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name']
        # field = '__all__'



# class StudentView(GenericAPIView):
#     queryset = Student.objects
#     serializer_class = StudentModelSerializer
#
#     def get(self, request):
#         # 原始1类
#         # ids = serializers.IntegerField(source='id')
#         # name = serializers.CharField(max_length=5)
#         # student = Student.objects.all()
#         # serializer = StudentSerializer(instance=student, many=True)
#         # print(serializer.data)
#
#         # 原始2类
#         # instance = Student.objects.all()
#         # s = StudentModelSerializer(instance=instance, many=True)
#         #
#         # s = self.serializer_class(instance=StudentView.queryset, many=True)
#         # s = self.get_serializer_class()(instance=StudentView.queryset, many=True)
#         #
#         s = self.get_serializer(instance=self.get_queryset(), many=True)
#         return Response(s.data)
#
#     def post(self, request):
#         s = self.get_serializer(data=request.data)
#         if s.valid():
#             s.save()
#             return Response(s.data)
#         return Response(s.errors)


# class StudentView(GenericAPIView, CreateModelMixin, ListModelMixin):
#     queryset = Student.objects
#     serializer_class = StudentModelSerializer
#
#     def get(self, request):
#         # 原始1类
#         # ids = serializers.IntegerField(source='id')
#         # name = serializers.CharField(max_length=5)
#         # student = Student.objects.all()
#         # serializer = StudentSerializer(instance=student, many=True)
#         # print(serializer.data)
#
#         # 原始2类
#         # instance = Student.objects.all()
#         # s = StudentModelSerializer(instance=instance, many=True)
#         #
#         # s = self.serializer_class(instance=StudentView.queryset, many=True)
#         # s = self.get_serializer_class()(instance=StudentView.queryset, many=True)
#         #3
#         # s = self.get_serializer(instance=self.get_queryset(), many=True)
#         # return Response(s.data)
#
#         #4
#         # ListModelMixin类对上面的方法做了封装
#         return self.list(request)
#
#     def post(self, request):
#         # s = self.get_serializer(data=request.data)
#         # if s.valid():
#         #     s.save()
#         #     return Response(s.data)
#         # return Response(s.errors)
#         return self.create(request)
#
#
# class StudentDetailView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = Student.objects
#     serializer_class = StudentModelSerializer
#
#     def get(self, request, pk):
#         # s = self.get_serializer(instance=self.get_object(), many=False)
#         # return Response(s.data)
#         return self.retrieve(request, pk)
#
#     def delete(self, request, pk):
#         # self.get_object().delete()
#         # return Response()
#         return self.destroy(request)
#
#     def put(self, request, pk):
#         # s = self.get_serializer(instance=self.get_object(), data=request.data)
#         # if s.is_valid():
#         #     s.save()
#         #     return Response(s.data)
#         # return Response(s.errors)
#         return self.update(request)


# 如果多个数据表，A， B, C 可以把上面的再做一层封装
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
#
#
# class StudentView(ListCreateAPIView):
#     queryset = Student.objects
#     serializer_class = StudentModelSerializer
#
#
# class StudentDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects
#     serializer_class = StudentModelSerializer


# 上面的两个类变量一样，还可以进一步封装
# url不同所以方法不一样，写了两个类，只要把路由统一，就能统一
from rest_framework.views import APIView
from rest_framework import viewsets


# class StudentView(APIView):
#     queryset = Student.objects
#     serializer_class = StudentModelSerializer
#
#
# class StudentDetailView(APIView):
#     queryset = Student.objects
#     serializer_class = StudentModelSerializer
#


# class StudentView(viewsets.ViewSetMixin, APIView):
#     def list(self, request):
#         return Response('list')
#
#     def create(self, request):
#         return Response('create')
#
#     def listget(self, request):
#         return Response('listget')
#
#     def listupdate(self, request):
#         return Response('listupdate')
#
#     def listdelete(self, request):
#         return Response('listdelete')

#
# from rest_framework.mixins import RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin, CreateModelMixin, ListModelMixin
#
#
# class StudentView(viewsets.ViewSetMixin, GenericAPIView, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin, CreateModelMixin, ListModelMixin):
#     queryset = Student.objects
#     serializer_class = StudentModelSerializer
#     # 这种方法，url传参不能随便定义，即入参get list 必须he继承类里的方法明一样


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name']
        # field = '__all__'

    def validated_name(self, value):
        if value.endswith('aaaa'):
            return value
        else:
            raise serializers.ValidationError("name必须以aaaa结尾")

class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects
    serializer_class = StudentModelSerializer
