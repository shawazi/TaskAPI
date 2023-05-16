from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

# Create your views here.

def home(request):
    return HttpResponse("<h2>Task Tracker API</h2>")

@api_view(["GET", "POST"])

def task_view(request):
    
    if request.method == "POST":
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    # Below is implemented automatically when method=="GET".
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)
    
@api_view(["GET", "PUT", "PATCH", "DELETE"])

def task_detail(request, id):
    if request.method == "GET":
        # data = Task.objects.get(id=id)
        task = get_object_or_404(Task, id=id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    elif request.method == "PUT":
        task = get_object_or_404(Task, id=id)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == "Patch":
        task = get_object_or_404(Task, id=id)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == "DELETE":
        task = get_object_or_404(Task, id=id)
        task.delete()
        return Response({"message" : "Deleteted successfully"})
    
class TaskView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        param = self.request.query_params.get("completed")
        if param == "true":
            return Task.objects.filter(done=True)
        if param == "true":
            return Task.objects.filter(done=False)
        return super().get_queryset()
    
    def get_serializer(self, *args, **kwargs):
        # code here
        return super().get_serializer(*args, **kwargs)

    def perform_create(self, serializer):
        # code here
        serializer.save(priority='L', task=serializer.validated_data.get("task").upper())
        return super().perform_create(serializer)

class TaskDetail(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = "id"

class TaskCRUD(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer