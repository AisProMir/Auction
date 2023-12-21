from django.db import models
from datetime import date


class Transport(models.Model):
    CHOICES = (
        ("Тент", "Tent"),
        ("Изотерма", 'Izoterma'),
        ("Рефрижератор", 'Refrezirator')
    )
    name = models.CharField(choices=CHOICES, max_length=50, default=0)
    gabariti = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.name}"


class InformationOfCargo(models.Model):
    name = models.CharField(max_length=100)
    temperatyra = models.IntegerField(default=0)
    ves = models.IntegerField(default=0)
    obiom = models.IntegerField(default=0)
    kolvoMest = models.IntegerField(default=0)
    stoimostGruza = models.DecimalField(decimal_places=2, max_digits=2, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class Zayaka(models.Model):
    number = models.IntegerField(unique=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    closing_time = models.DateTimeField()
    gruz = models.ForeignKey(InformationOfCargo, on_delete= models.CASCADE, related_name= 'gruz')
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE, related_name='transport')
    kolishestvo = models.IntegerField(default=1)
    pogruzka = models.TextField()  ### сделать фильтр
    razgruzka = models.TextField()
    "подумать над предложением спросить у Никиты" ### 23.08
    "подумать над статусом спросить у Никиты"
    "подумать над дейсвием спросить у Никиты"

    def __str__(self):
        return f"{self.number}-{self.gruz}"


