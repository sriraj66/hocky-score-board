from django.urls import path
from .views import *

urlpatterns = [
    path("",index,name="index"),
    path("create/match/",create_match,name='create_match'),
    path("control/view/<int:id>/admin",control,name='control'),

    path('update/match/<int:id>/edit',update_details,name='update_details'),
    path('update/color/<int:id>/edit',update_color,name='update_color'),

    path("dash/<int:id>",dash,name="dash"),
    path("update/score/borard/<int:id>",update_panel,name='update_panel'),

    path('timer/start/<int:id>', start_timer, name='start_timer'),
    path('timer/update/<int:id>', update_timer, name='update_timer'),
    path('timer/stop/<int:id>', stop_timer, name='stop_timer'),
    path('timer/pause/<int:id>', pause_timer, name='pause_timer'),
    path('timer/resume/<int:id>', resume_timer, name='resume_timer'),
    path('timer/reset/<int:id>', reset_timer, name='reset_timer'),

]