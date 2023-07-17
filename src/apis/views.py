#from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .scheduler.cat_swarm import main


# SRS_CMP2 page 18
@api_view(['POST'])
def generate(request):
    try:
        algs1_request = request.data
        users = algs1_request["users"]
        courses = algs1_request["courses"]
        classrooms = algs1_request["classrooms"]

        scheduled_courses = main(users, courses, classrooms)
        return Response(scheduled_courses, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)