from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from .models import Group, Schedule, Teacher
from .serializers import GroupSerializer, ScheduleSerializer, TeacherSerializer

@extend_schema(tags=['Shedule'])
class GroupListByCourseView(APIView):
    def get(self, request, course_year):
        groups = Group.objects.filter(course_year=course_year)
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)

@extend_schema(tags=['Shedule'])
class ScheduleByGroupView(APIView):
    def get(self, request, group_id, weekday, week_type="Числитель"):
        schedule = Schedule.objects.filter(group_id=group_id, weekday=weekday, week_type=week_type).order_by('lesson_number')
        serializer = ScheduleSerializer(schedule, many=True)
        return Response(serializer.data)

@extend_schema(tags=['Shedule'])
class TeacherListView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

@extend_schema(tags=['Shedule'])
class ScheduleByTeacherView(APIView):
    def get(self, request, teacher_id, weekday, week_type="Числитель"):
        schedule = Schedule.objects.filter(teacher_id=teacher_id, weekday=weekday, week_type=week_type).order_by('lesson_number')
        serializer = ScheduleSerializer(schedule, many=True)
        return Response(serializer.data)
