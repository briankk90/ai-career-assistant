from django.urls import path
from .views import HomeView, JobMatchView, ResumeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('api/match-jobs/', JobMatchView.as_view(), name='job-match'),
    path('api/generate-resume/', ResumeView.as_view(), name='resume'),
]
