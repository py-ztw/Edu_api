from rest_framework.generics import ListAPIView,RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from course.models import CourseCategory, Course
from course.pagination import CoursePageNumber
from course.serializer import CourseCategorySerializer, CourseModelSerializer


class CourseCategoryListAPIView(ListAPIView):
    """课程分类信息查询"""
    queryset = CourseCategory.objects.filter(is_show=True, is_delete=False).order_by("orders")
    serializer_class = CourseCategorySerializer


class CourseListAPIView(ListAPIView,RetrieveAPIView):
    """课程列表查询"""
    queryset = Course.objects.filter(is_show=True, is_delete=False).order_by("orders")
    serializer_class = CourseModelSerializer
    lookup_field = "id"
    # 通过继承ListModelMixin 提供self.list完成了查询所有
    # 通过继承RetrieveModelMixin 提供了self.retrieve 完成了查询单个
    def get(self, request, *args, **kwargs):
        book_id = kwargs.get("id")
        print(book_id)
        if "id" in kwargs:

            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)


class CourseFilterListAPIView(ListAPIView):
    """根据条件查询课程"""
    queryset = Course.objects.filter(is_show=True, is_delete=False).order_by("orders")
    serializer_class = CourseModelSerializer

    # 根据不同的分类id查询不同的课程
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ("course_category",)
    # 排序
    ordering_fields = ("id", "students", "price")
    # 分页   只能有一个
    pagination_class = CoursePageNumber
