from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
        "atlantic": League.objects.filter(name__iexact="Atlantic Soccer Conference")[0].teams.all(),
        "penguins": Team.objects.filter(team_name__iexact="Penguins").filter(location__iexact="Boston")[0].curr_players.all(),
        "icbc": Team.objects.filter(league__name__iexact="International Collegiate Baseball Conference"),
        "lopez": Player.objects.filter(last_name__iexact='lopez').filter(curr_team__league__name__iexact="American Conference of Amateur Football"),
        "football" : Player.objects.filter(curr_team__league__sport__iexact="Football"),
        "sophia" : Team.objects.filter(curr_players__first_name__iexact="sophia"),
        "sophialeague": League.objects.filter(teams__curr_players__first_name__iexact="sophia"),   
        "flores": Player.objects.filter(last_name__iexact="flores").exclude(curr_team__team_name__iexact="Roughriders").exclude(curr_team__location__iexact="washington"),
        "samevans": Team.objects.filter(all_players__first_name__iexact="samuel").filter(all_players__last_name__iexact="evans"),
        "tigercats": Team.objects.filter(team_name__iexact="Tiger-Cats").filter(location__iexact="Manitoba")[0].all_players.all(),
        "vikings": Player.objects.filter(all_teams__location__iexact="Wichita").filter(all_teams__team_name__iexact="vikings").exclude(curr_team__team_name__iexact="vikings").exclude(curr_team__location__iexact="Wichita"),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
