from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class internalLoginView(APIView):
  def post(self,request):
    response = Response()
    response.set_cookie('jwt','oeu',httponly=True,max_age=36000)
    return response