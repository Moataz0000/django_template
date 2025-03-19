from django.db import models



class StudentClassChoices(models.IntegerChoices):
    CLASS_A = 1
    CLASS_B = 2
    CLASS_C = 3