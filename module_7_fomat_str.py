team1 = "Мастера кода"
team2 = "Волшебники данных"

team1_num = 5
team2_num = 6

score_1 = 40
score_2 = 42

team1_time = 1552.512
team2_time = 2153.31451

tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / len([team1, team2])

print("В команде %s участников: %d!" % (team1, team1_num))

print("Итого сегодня в командах участников: %d челоаек и %d человек!" % (team1_num, team2_num))

print("Команда {1} решила задач: {0}!".format(score_2, team2))

print("{0} решили задачи за {1} с !".format(team2, team2_time))

print(f"Команды решили {score_1} и {score_2} задач.")

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = f"Победа команды {team1}"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = f"Победа команды {team2}!"
else:
    result = "Ничья!"

print(result)

print(f"Сегодня было решено {tasks_total} задач, в среднем по {round(time_avg, 2)} екунды на задачу!.")
