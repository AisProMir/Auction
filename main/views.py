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


class ReuisitionNoteCreateView(TemplateView):
    template_name = "main/reuisition_note_create.html"


    def post(self, request):
        number = request.POST["nomer"]
        closing_time = request.POST["vrema"]
        gruz = request.POST["griz"]
        transport = request.POST["mashina"]
        kolishestvo = request.POST["skolko"]
        pogruzka = request.POST["otcuda"]
        razgruzka = request.POST["cyda"]
        Zayaka.objects.create(number=number, closing_time=closing_time,gruz=gruz,
                              transport=transport, kolishestvo=kolishestvo,
                              pogruzka=pogruzka,razgruzka=razgruzka)
        return redirect("index")

    def __init__(self, *args, **kwargs):
        super(InformationOfCargo, self).__init__(*args, **kwargs)
        self.id['gruz'].gueryset = Zayaka.objects.all()


class GruzCreateView(TemplateView):
    template_name = "main/gruz_create.html"

    def post(self, request):
        name = request.POST["nazvanie"]
        temperatyra = request.POST["gradus"]
        Ves = request.POST["nagruzka"]
        Obiom = request.POST["mashtab"]
        kolvoMest = request.POST["skolko mest"]
        stoimostGruza = request.POST["cena"]
        InformationOfCargo.objects.create(name=name,temperatyra=temperatyra,Ves=Ves,
                              Obiom=Obiom,kolvoMest=kolvoMest,
                              stoimostGruza=stoimostGruza)
        return redirect("reuisition-note-create")
