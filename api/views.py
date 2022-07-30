from rest_framework.response import Response
from rest_framework.decorators import api_view
from yaml import serialize
from base.models import Item
from .serializers import ItemSerializer



@api_view(['GET'])
def getData(request):
    #person = {'name':'Dennis','age':28}
    items = Item.objects.all()
    serializer = ItemSerializer(items,many=True)
    #return Response(person)  
    return Response(serializer.data)


@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)