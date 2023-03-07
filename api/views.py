import math
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import generics, status
from .models import User, UserType, Materiel
from .serializers import UserSerializer, UsertypeSerializer, MaterielSerializer
# Create your views here.
#https://codevoweb.com/build-crud-api-with-django-rest-framework/
"""class UserList(generics.ListCreateAPIView):
    serializer_class=UserSerializer
    def get_queryset(self):
        queryset = User.objects.all()
        usertype = self.request.query_params.get('usertype')
        if usertype is not None:
            queryset=queryset.filter(userType=usertype)
        return queryset

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=UserSerializer
    queryset = User.objects.all()


#CRUD usertype
class UsertypeList(generics.ListCreateAPIView):
    serializer_class=UsertypeSerializer
    queryset = UserType.objects.all()
#Getall

    def get(self, request):
        page_num = int(request.GET.get('page',1))
        limit_num = int(request.GET.get('limit',10))
        start_num = ( page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        usertype=UserType.objects.all()
        total_usertype = usertype.count()
        if search_param:
            usertype = usertype.filter(title_icontains=search_param)
        serializerusertypeG = self.serializer_class(usertype[start_num:end_num], many = True)
        return Response({
            "status": "success",
            "total": total_usertype,
            "page": page_num,
            "last_page": math.ceil(total_usertype / limit_num),
            "usertype": serializerusertypeG.data
        })

#ADD
def post(self, request):
        serializerusertypeA = self.serializer_class(data=request.data)
        if serializerusertypeA.is_valid():
            serializerusertypeA.save()
            return Response({"status": "success", "note": serializerusertypeA.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializerusertypeA.errors}, status=status.HTTP_400_BAD_REQUEST)


class UsertypeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=UsertypeSerializer
    queryset = UserType.objects.all()



#Materiel
class MaterielList(generics.ListCreateAPIView):
    serializer_class=MaterielSerializer
    def get_queryset(self):
        queryset = Materiel.objects.all()
        materiel = self.request.query_params.get('materiel')
        if materiel is not None:
            queryset=queryset.filter(materiel=materiel)
        return queryset

class MaterielDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=MaterielSerializer
    queryset = Materiel.objects.all()

#CRUD USERTYPE
@api_view(['GET'])
def getAll(request):
    usertype = UserType.objects.all()
    allusertype=[]
    for typeuser in usertype:
        allusertype.append(UsertypeSerializer(typeuser).data)
    print(allusertype)
    return Response(allusertype, status=200),
"""
#CRUD USERTYPE
@api_view(['GET'])
def getAll(request):
    usertype=UserType.objects.all()
    serialiser_usertype=UsertypeSerializer(usertype, many=True)
    return Response(serialiser_usertype.data)

@api_view(['POST'])
def add(request):
    libelle= request.data['usertypeLib']
    description = request.data['usertypedesc']
    usertype = UserType.objects.create(
        usertypeLib = libelle,
        usertypedesc = description
    )
    serializer_usertype = UsertypeSerializer(usertype)
    return Response(serializer_usertype.data, status=200)
    
@api_view(['PUT'])
def update(request, pk):
    updateusertype = request.data
    usertype=UserType.objects.get(id=pk)
    serialiser_usertype = UsertypeSerializer(instance=usertype, data=updateusertype)
    if serialiser_usertype.is_valid():
        serialiser_usertype.save()
    return Response(serialiser_usertype.data)

@api_view(['DELETE'])
def delete(request, pk):
    usertype=UserType.objects.get(id=pk)
    usertype.delete()
    return Response('delete usertype')

#CRUD materiel

@api_view(['POST'])
def addmat(request):
    libelle= request.data['materiellib']
    description = request.data['materieldesc']
    arrivage=request.data['materieldatearrivee']
    materiel = Materiel.objects.create(
        materiellib = libelle,
        materieldesc = description,
        materieldatearrivee=arrivage
    )
    serializer_materiel = MaterielSerializer(materiel)
    return Response(serializer_materiel.data, status=200)