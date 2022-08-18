from django.urls import path, include
from .views import createMemo,getMemo
urlpatterns = [
    path("createMemo/",createMemo),
    path("getMemo/",getMemo)


]