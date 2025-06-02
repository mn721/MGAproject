from rest_framework import viewsets, filters, generics
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter
from .models import Task, TaskHistory
from .serializers import TaskSerializer, TaskHistorySerializer, UserRegisterSerializer
from django.contrib.auth.models import User

class TaskFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    description = CharFilter(field_name='description', lookup_expr='icontains')
    status = CharFilter(field_name='status', lookup_expr='iexact')
    assigned_user = CharFilter(field_name='assigned_user__username', lookup_expr='iexact')

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'status', 'assigned_user']

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = TaskFilter
    search_fields = ['name', 'description']

    @action(detail=True, methods=['get'], url_path='history')
    def history(self, request, pk=None):
        task = self.get_object()
        history = task.history.all().order_by('-changed_at')
        page = self.paginate_queryset(history)
        serializer = TaskHistorySerializer(page, many=True)
        return self.get_paginated_response(serializer.data)

class TaskHistoryFilter(FilterSet):
    task = CharFilter(field_name='task__id', lookup_expr='exact')

    class Meta:
        model = TaskHistory
        fields = ['task']

class TaskHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TaskHistory.objects.all().order_by('-changed_at')
    serializer_class = TaskHistorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskHistoryFilter

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer