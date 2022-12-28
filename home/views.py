from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

# Create your views here.

class HandelFileUpload(APIView):
    def post(self, request):
     try:
          data= request.data
          serializer= FileListSerializer(data= data)

          if serializer.is_valid():
            serializer.save(),
            return Response({'status' : 200, 'message':'Files Uploaded Successfully' })
        

          return Response({
             'status': 400,
             'message': 'Something went wrong !',
             'data': serializer.errors,
              })              
     except Exception as e:
        print(e)