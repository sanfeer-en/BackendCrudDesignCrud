from django.urls import path
from .views import index , form , table , delete , update , Edit

urlpatterns = [
    path("home", index),
    path("form" , form , name="form"),
    path("table" , table , name="table"),
    path("delete/<int:id>", delete , name="delete"),
    path("update/<int:id>", update , name="update"),
    path("edit/<int:id>", Edit , name="edit"),
    
]