from django.db import models


# Create your models here.
class Client(models.Model):
    session_id = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id} - {self.session_id}"


class Window(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    x = models.FloatField()
    y = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()


class System(models.Model):
    window = models.ForeignKey(Window, on_delete=models.CASCADE)


class Solar(models.Model):
    system = models.OneToOneField(System, on_delete=models.CASCADE)
    color = models.CharField('Цвет солнца', max_length=10)
    x = models.FloatField('X в рамках окна')
    y = models.FloatField('Y в рамках окна')
    radius = models.FloatField('Радиус в рамках окна')
