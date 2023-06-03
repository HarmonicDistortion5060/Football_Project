import pytest
from django.test import Client
from django.db import IntegrityError
from .models import Player, Team

# Create your tests here.


def test_main():
    client = Client()
    response = client.get('/')
    assert response.status_code == 200


def test_notfound():
    client = Client()
    response = client.get('/matches')
    assert response.status_code == 404


def test_view_requires_login():
    client = Client()
    response = client.get('/players')  # jakiś widok wymagający zalogowania
    assert response.status_code == 301  # redirect
    assert response.url == '/players/'  # na jaki adres


@pytest.mark.django_db
def test_query_count(django_assert_num_queries):
    with django_assert_num_queries(2):
        Team.objects.create(name="test", country="test_last", logo="/path/to/logo")
        Player.objects.create(first_name="test", last_name="test_last", position="LP", age="25", team_id="1")


@pytest.mark.django_db
def test_query_create_team_player():
    team = Team.objects.create(name="test", country="test_last", logo="/path/to/logo")
    player = Player.objects.create(last_name="test_last", position="LP", age="25", team_id="2")
    assert player.team == team


@pytest.mark.django_db
def test_integrity_error():
    with pytest.raises(IntegrityError):
        Player.objects.create(first_name="test", last_name="test_last", position="LP", age="25")


def test_search_view():
    client = Client()
    resp = client.get('/search/')
    assert resp.status_code == 200
    assert 'search_matches.html' in resp.template_name
    assert b'Wyszukiwarka meczy' in resp.content
