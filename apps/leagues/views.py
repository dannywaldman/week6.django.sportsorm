from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"basketball": League.objects.filter(sport__iexact='basketball'),
        "womens": League.objects.filter(name__icontains='women'),
        "hockey": League.objects.filter(name__icontains='hockey'),
        "nofootball": League.objects.exclude(name__icontains="football"),
        "conference": League.objects.filter(name__icontains="onference"),
        "atlantic": League.objects.filter(name__istartswith="atlantic"),
        "dallas": Team.objects.filter(location__iexact="dallas"),
        "raptors": Team.objects.filter(team_name__iexact="raptors"),   
        "city": Team.objects.filter(location__icontains="city"),
        "t": Team.objects.filter(team_name__istartswith="t"), 
        "allteams": Team.objects.all().order_by('location'),
        "teamsreverse": Team.objects.all().order_by('-team_name'),
        "cooper": Player.objects.filter(last_name__iexact='cooper'),
        "joshua": Player.objects.filter(first_name__iexact='joshua'), 
        "coopjosh": Player.objects.filter(last_name__iexact='cooper').exclude(first_name__iexact='joshua'),
        "alex": Player.objects.filter(first_name__iexact='alexander') | Player.objects.filter(first_name__iexact='wyatt'), 
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
