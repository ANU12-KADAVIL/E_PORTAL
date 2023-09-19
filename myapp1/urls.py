from django.urls import path
from myapp1 import views

urlpatterns = [
    path('function1/', views.function1),
    path('frontpage/',views.frontpage),
    path('about/',views.about),
    path('course/',views.course),
    path('login/',views.userlogin),
    path('forms/',views.forms),
    path('login1/',views.userlogin1),
    path('forms1/',views.forms1),
    path('table/',views.table),
    path('table1/',views.table1),
    path('signup/',views.signup),
    path('signup1/',views.signup1),
    path('attendance/',views.myattendance),
    path('check/',views.check),
    path('check/<id>',views.deletemyorder),
    path('leave/',views.myleave),
    path('sanction/',views.sanction),
    path('sanction/<id>',views.deleteleave),
    
]