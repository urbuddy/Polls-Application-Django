from django.urls import path

from . import views
app_name = "demo"
urlpatterns = [
    path("", views.index, name="index"),
    path("/create", views.create, name="create"),
    path("<int:question_id>/", views.details, name="details"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/votes/", views.votes, name="votes")
]
