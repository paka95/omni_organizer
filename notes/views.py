from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, DestroyAPIView
from .apps import NotesConfig
from .models import Note
from .serializers import NoteSerializer

# Create your views here.

app_name = NotesConfig.name


class Index(View):
    template_name = 'notes/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

class GetNotes(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class DeleteNote(DestroyAPIView):
    serializer_class = NoteSerializer    
    queryset = Note.objects.all()