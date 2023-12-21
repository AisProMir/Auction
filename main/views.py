from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Zayaka, InformationOfCargo, Transport


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

class GruzCreateView(TemplateView):
    template_name = "main/gruz_create.html"

    def post(self, request):
        name = request.POST["nazvanie"]
        temperatyra = request.POST["gradus"]
        ves = request.POST["nagruzka"]
        obiom = request.POST["mashtab"]
        kolvoMest = request.POST["skolko_mest"]
        stoimostGruza = request.POST["cena"]
        InformationOfCargo.objects.create(name=name, temperatyra=temperatyra, ves=ves,
                              obiom=obiom, kolvoMest=kolvoMest,
                              stoimostGruza=stoimostGruza)
        return redirect("reuisition-note-create")


class ReuisitionNoteCreateView(TemplateView):
    template_name = "main/reuisition_note_create.html"

    def get(self, request):
        items = InformationOfCargo.objects.all()
        options_transport = Transport.objects.all()
        params = {'items': items, 'options': options_transport}
        return render(request, self.template_name, params)

    def post(self, request):
        if request.method == 'POST':
            number = request.POST["nomer"]
            closing_time = request.POST["vrema"]
            gruz = request.POST["griz"]
            transport = request.POST["mashina"]
            kolishestvo = request.POST["skolko_mest"]
            pogruzka = request.POST["otcuda"]
            razgruzka = request.POST["cyda"]
            gabariti = request.POST["gabariti"]
            InformationOfCargo.objects.create(name=gruz)
            # name_of_transport = Transport.objects.get(name=transport)
            # gabariti_of_transport = Transport.objects.get(gabariti=gabariti)
            Transport.objects.create(name=gruz, gabariti=gabariti)
            Zayaka.objects.create(number=number, closing_time=closing_time, gruz=gruz,
                                  transport=transport, kolishestvo=kolishestvo,
                                  pogruzka=pogruzka, razgruzka=razgruzka)
        return redirect("index")

