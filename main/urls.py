from django.urls import path
from .views import IndexView, ReuisitionNoteView, ReuisitionNoteCreateView,GruzCreateView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("reuisition_note/", ReuisitionNoteView.as_view(), name='reuisition-note'),
    path("reuisition_note/create/", ReuisitionNoteCreateView.as_view(), name='reuisition-note-create'),
    path("gruz/create/", GruzCreateView.as_view(), name='gruz-create')
    ]
