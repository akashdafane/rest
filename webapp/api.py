from rest_framework import generics
from  rest_framework.response import Response
from .serializer import EmployeeSerializer
from .models import Employee
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import RegistraionSerializer


class EmployeeCreateApi(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeApi(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeUpdate(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDelete(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistraionSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'success'
            data['email'] = account.email
            data['username'] = account.username
        else:
            data = serializer.errors
        return Response(data)