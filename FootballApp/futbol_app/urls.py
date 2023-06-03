from django.urls import path, include
from futbol_app.views import TeamList, PlayerListView, PlayerGoalsView, MatchSearchView, RegisterView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", RegisterView.as_view(), name="register"),
    path('teams/', TeamList.as_view(), name='teams'),
    path('players/', login_required(PlayerListView.as_view()), name='players'),
    path('player/<int:pk>/goals/', PlayerGoalsView.as_view(), name='player_goals'),
    path('search/', MatchSearchView.as_view(), name='search'),
    path('', MatchSearchView.as_view(), name='search'),
]
