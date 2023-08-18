from django.shortcuts import render
from .models import Data
from .Serialisers import DataSerializers
from rest_framework .response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

class VisualizationView(APIView):

    def get(self,request):
        try:
            query=dict(request.query_params)
            queryDict={k: v[0] for k, v in query.items()}
            object = Data.objects.filter(**queryDict)
            serializer= DataSerializers(object,many=True)
            print(queryDict)
            
           
            return Response({
                'success':True,
                'data':serializer.data,
                'message':"data fetched successfully"
            },status=status.HTTP_200_OK)

        except NameError:
            return Response({
                "error":NameError

            },status=status.HTTP_400_BAD_REQUEST)