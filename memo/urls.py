from django.urls import path, include
from .views import createMemo,getMemo,createMemos,getMemos
urlpatterns = [
    path("createMemo/",createMemo),
    path("getMemo/",getMemo),
        path("createMemos/",createMemos)
,        path("getMemos/",getMemos)



]