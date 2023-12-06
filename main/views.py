from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Zayaka, InformationOfCargo, Transport
from .forms import Zayaka_form

class IndexView(TemplateView):
    template_name = "main/index.html"
    def get(self, request, *args, **kwargs):
        pass
        return render(request, self.template_name)


class ReuisitionNoteView(TemplateView):
    template_name = "main/reuisition_note.html"
    def get(self, request, *args, **kwargs):
        zayakas = Zayaka.objects.all()
        params = {
            "zayakas": zayakas
        }
        return render(request, self.template_name, params)


class ReuisitionNoteCreateView(TemplateView):
    template_name = "main/reuisition_note_create.html"

    def create(self, request):
        error = ''
        if request.method == 'POST':
            form = Zayaka_form(request.POST)
            if form.is_valid():
                form.save()
                return request('reuisition_note.html')
            else:
                error = 'Заполните все поля'
        form = Zayaka_form

        data = {
            'form': form,
            'error': error
        }

        return render(request,self.template_name, data)