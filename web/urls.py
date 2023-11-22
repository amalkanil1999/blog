from django.urls import path,include
from web.views import index,post


app_name="web"

urlpatterns = [
    path("",index,name='index'),
    path("<int:id>/",post,name='post')
]
