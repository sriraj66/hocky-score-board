from django.db import models

from django.db import models
from django.utils import timezone

class Timer(models.Model):

    min = models.PositiveIntegerField(default=0)
    sec = models.PositiveIntegerField(default=0)

    total_sec = models.PositiveIntegerField(default=0)

    is_running = models.BooleanField(default=False)
    is_pause = models.BooleanField(default=False)

    remaining_time = models.PositiveIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']


class Match(models.Model):
    t_1 = models.CharField(max_length=255,blank=True,verbose_name="Team 1",null=True)
    t_2 = models.CharField(max_length=255,verbose_name="Team 2",blank=True,null=True)

    t_s_1 = models.PositiveIntegerField(verbose_name="Team 1 Score",blank=True,null=True)
    t_s_2 = models.PositiveIntegerField(verbose_name="Team 2 Score",blank=True,null=True)

    min = models.PositiveIntegerField(verbose_name='Minutes',blank=True,null=True,default=0)
    sec = models.PositiveIntegerField(verbose_name='Seconds',blank=True,null=True,default=0)

    timer = models.ForeignKey(Timer,null=True,on_delete=models.CASCADE,blank=True)

    quater = models.CharField(max_length=10,blank=True,null=True,default="Q1")


    t_1_c = models.CharField(max_length=20,verbose_name="Team 1 Color",blank=True,null=True)
    t_2_c = models.CharField(max_length=20,verbose_name="Team 2 Color",blank=True,null=True)
    b_g = models.CharField(max_length=20,default='#33cc33',verbose_name="Background Color")
    s_c = models.CharField(max_length=20,verbose_name="Score Color",blank=True,null=True)

    t_c = models.CharField(max_length=20,verbose_name="Timer Color",blank=True,null=True)
    q_c = models.CharField(max_length=20,verbose_name="Quater Color",blank=True,null=True)

    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self) -> str:
        return f"{self.t_1} VS {self.t_2}"

    class Meta:
        ordering = ['-id']