from django.urls import path

from . import views
app_name = "demo"
urlpatterns = [
    # path("", views.index, name="index"),
    # path("<int:question_id>/", views.details, name="details"),
    # path("<int:question_id>/results/", views.results, name="results"),

    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="details"),
    path("<int:pk>/results/", views.ResultView.as_view(), name="results"),

    path("/create", views.create, name="create"),
    path("<int:question_id>/votes/", views.votes, name="votes"),

]
