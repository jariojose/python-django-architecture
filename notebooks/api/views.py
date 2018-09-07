from rest_framework import generics
from notebooks.models import Notebook
from .serializers import NotebookSerializer


class NotebookPostRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = NotebookSerializer

    # queryset = Notebook.objects.all()
    # OR
    def get_queryset(self):
        return Notebook.objects.all()

    # def get_object(self):
    #     pk = self.kwargs.get('pk')
    #     return Notebook.objects.get(pk=pk)


class NotebookGetAllView(generics.ListAPIView):
    serializer_class = NotebookSerializer

    def get_queryset(self):
        return Notebook.objects.all()
