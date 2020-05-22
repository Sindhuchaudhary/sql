Q1 = '''select avg(age) from player;'''

Q2 = '''select match_no,play_date from match  where audience > 50000 order by match_no ASC;'''

Q3 = '''select team_id ,count(win_lose) as win from matchteamdetails where win_lose ="W" group by team_id order by win DESC,team_id ASC;'''

Q4 = '''select match_no,play_date from match where stop1_sec>(select avg(stop1_sec) from match) order by match_no DESC;'''


Q5 = '''select m.match_no,t.name,p.name from matchcaptain m inner join team t on t.team_id = m.team_id inner join player p on p.player_id = m.captain order by m.match_no ,t.name ASC;''' 


Q6 = '''select m.match_no ,p.name,p.jersey_no from match m inner join player p on p.player_id = m.player_of_match order by m.match_no ASC;'''

Q10 = '''select avg(goal) from (select count(goal_id) as goal from goaldetails GROUP BY team_id);'''

Q7 = '''select t.name,avg(p.age) as av_age from team t inner join player p on p.team_id = t.team_id group by t.team_id HAVING av_age>26;'''


Q8 = '''select p.name,p.jersey_no,p.age,count(gt.goal_id) as no_of_goals from player p inner join goaldetails gt on p.player_id = gt.player_id group by p.player_id HAVING no_of_goals>=1 AND p.age<=27 order by no_of_goals DESC,p.name ASC;'''

Q9 = '''select team_id ,(count(goal_id)*100.0/(select count(goal_id) from goaldetails))  as percentage from goaldetails group by team_id  having percentage>0;'''


Q11 = '''select player_id,name,date_of_birth from player where player_id not in (select distinct player_id from goaldetails) order by player_id ASC;'''


Q12 ='''select t.name,m.match_no,m.audience,m.audience-(select avg(m1.audience) from match m1 inner join matchcaptain mc1 on m1.match_no=mc1.match_no
inner join team t1 on t1.team_id=mc1.team_id where t.team_id=t1.team_id)
from match m inner join matchcaptain mc on m.match_no=mc.match_no
inner join team t on t.team_id=mc.team_id  order by m.match_no ASC;'''

