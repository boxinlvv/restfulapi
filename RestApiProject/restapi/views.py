from rest_framework import viewsets, filters, pagination
from .models import Student
from .serializers import StudentSerializers

# 分页
class PageSet(pagination.PageNumberPagination):
    #每页显示多少个
    page_size = 3
    #默认每页显示3个
    page_size_query_param = "size"
    #最大页数
    max_page_size = 10
    #获取页码数
    page_query_param = "page"


class StudentViewSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
    queryset = Student.objects.all().order_by('-pk')
    # 指定序列化的类
    serializer_class = StudentSerializers
    # 分页、搜索、排序
    # 指定分页配置
    pagination_class = PageSet
    # 配置搜索功能,filter_backends元组下要添加filters.OrderingFilter才能实现排序功能
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,) 
    # 设置搜索的关键字
    search_fields = ('=name','sid')
    # 设置需要被排序的字段
    ordering_fields = ('name', 'sid')