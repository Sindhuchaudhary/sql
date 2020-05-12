Q1 = '''select player.* from player inner join matchcaptain on 
matchcaptain.team_id=player.team_id 
left join goaldetails on player.player_id=goaldetails.player_id  where  
player.player_id = matchcaptain.captain AND goaldetails.goal_id is null;'''


Q2 = '''select team_id,count(match_no) from matchteamdetails group by team_id;'''

Q3 = '''select goaldetails.team_id,count(goal_id)/23.0 from goaldetails
group by goaldetails.team_id;'''

Q4 = '''select captain , count(captain) from matchcaptain 
inner join match on match.match_no = matchcaptain.match_no group by captain;'''

Q5 = '''select count(distinct(player_id)) as no_players from player inner join matchcaptain on 
matchcaptain.captain=player.player_id inner join match on 
matchcaptain.match_no = match.match_no AND 
match.player_of_match=player.player_id AND matchcaptain.captain=player.player_id;'''


Q6 = '''select distinct(captain) from matchcaptain 
where not exists (select player_of_match from match 
inner join player on player.player_id=match.player_of_match 
where player.player_id=matchcaptain.captain);'''


Q7 = '''select strftime("%m",play_date) as month, count(match_no) as no_of_matches 
from match group by month order by no_of_matches DESC;'''

Q8 = '''select player.jersey_no,count(matchcaptain.captain) as
no_of_captains from player inner join matchcaptain on player.player_id=matchcaptain.captain  
group by player.jersey_no order by no_of_captains DESC,player.jersey_no DESC;'''

Q9 = '''select player.player_id ,avg(match.audience) as avg_audience from player 
inner join matchcaptain on player.team_id=matchcaptain.team_id inner join 
match on matchcaptain.match_no= match.match_no group by player.player_id
order by avg_audience DESC,player.player_id DESC;'''

Q10 = '''select player.team_id,avg(age) from player inner join team on team.team_id=player.team_id group by player.team_id;'''

Q11 = '''select avg(age) from player inner join matchcaptain on matchcaptain.captain = player.player_id;'''


Q12 = '''select strftime("%m",date_of_birth) as month ,count(player_id) as no_of_players
from player group by month order by no_of_players DESC,month DESC;'''

Q13 = '''select captain,count(win_lose) as no_of_wins from matchcaptain 
inner join player on matchcaptain.captain=player.player_id inner join 
matchteamdetails on matchteamdetails.team_id = player.team_id AND matchcaptain.match_no=matchteamdetails.match_no
where win_lose = "W" group by player.player_id order by no_of_wins DESC;'''




