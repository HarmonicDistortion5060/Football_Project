from django.contrib.auth import login
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Team, Player, Goal, Match
from django.db.models import Q
from futbol_app.forms import RegisterForm


class RegisterView(FormView):
    """
    Represents a form view for user registration.
    Inherits Django's Form view and uses Register form and
    'register.html template by default
    Attributes: form_class, template_name, success_url
    Methods: form_valid
    """
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('teams')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        password_repeated = form.cleaned_data['password2']

        if User.objects.filter(email=email).exists():
            form.add_error(None, 'Ten mail jest zajęty!')
            return super().form_invalid(form)
        if password != password_repeated:
            form.add_error(None, 'Hasło nie pasuje')
            return super().form_invalid(form)
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )
        login(self.request, user)
        return super().form_valid(form)


class TeamList(ListView):
    """
    Represents a list view for all team's.
    Inherits Django's List view and uses Team model and
    'team_list.html template by default
    Attributes: model, context_object_name
    """
    model = Team
    context_object_name = 'teams'


class PlayerListView(ListView):
    """
    Represents a list view for all player's.
    Inherits Django's List view and uses Player model and
    'player_list.html template by default
    Attributes: model, context_object_name, paginate_by
    """
    model = Player
    context_object_name = "players"

    paginate_by = 50


class PlayerGoalsView(DetailView):
    """
    Represents a detail view for searching player's goals
    Inherits Django's detail view and uses Player model and
    'player_goals.html template by default
    Attributes: model, template_name, context_object_name
    Methods: get_context_data
    """
    model = Player
    template_name = "player_goals.html"
    context_object_name = 'player'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['goals'] = Goal.objects.filter(player=self.object)
        return context


class MatchSearchView(ListView):
    """
    Represents a list view for searching matches
    Inherits Django's List view and uses Match model and
    'search_matches.html template by default
    Attributes: model, template_name
    Methods: get_queryset
    """
    model = Match
    template_name = 'search_matches.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(
                Q(home_team__name__icontains=query) |
                Q(away_team__name__icontains=query)
            )
        else:
            object_list = self.model.objects.none()
        return object_list
