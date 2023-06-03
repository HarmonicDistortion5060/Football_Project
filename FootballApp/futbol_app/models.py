from django.db import models

# Create your models here.


class Team(models.Model):
    """
    Represents a Team in the database
    Attributes:
        name (CharField): The name of given team
        country (CharField): The country of given team
        logo (ImageField): The logo of given team
    """
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='team_logos/')


class Player(models.Model):
    """
    Represents a Player in the database
    Attributes:
        first_name (CharField): The first name of given player
        last_name (CharField): The last name of given player
        position (CharField): The position of given player
        age (IntegerField): The age of given player
        team: Defines a one-to-many relationship with the Team model
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    age = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')


class Match(models.Model):
    """
    Represents a Match in the database
    Attributes:
       home_team: Defines a one-to-many relationship with the Team model (with related_name attribute)
       away_team: Defines a one-to-many relationship with the Team model (with related_name attribute)
       date (DateTimeField): Date of the match
       venue (CharField): The stadium where the match took place
       spectators (IntegerField): Number of spectators in a given match
       home_team_score (IntegerField): Home team score
       away_team_score (IntegerField): Away team score
    """
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='games_home')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='games_away')
    date = models.DateTimeField()
    venue = models.CharField(max_length=100)
    spectators = models.IntegerField()
    home_team_score = models.IntegerField()
    away_team_score = models.IntegerField()


class Goal(models.Model):
    """
    Represents a Goal in the database
    Attributes:
       match: Defines a one-to-many relationship with the Match model
       player: Defines a one-to-many relationship with the Player model
       minute (IntegerField): Time the goal was scored
    """
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    minute = models.IntegerField()


class League(models.Model):
    """
    Represents a League in the database
    Attributes:
        name (CharField): The name of given league
        country (CharField): The country of given league
        teams: Defines a many-to-many relationship with the Team model
        start_date (DateField): Start date of the league
        end_date (DateField): End date of the league
        season (IntegerField): The season of given league
    """
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    teams = models.ManyToManyField(Team)
    start_date = models.DateField()
    end_date = models.DateField()
    season = models.IntegerField()
