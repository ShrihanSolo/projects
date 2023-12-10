import random
import matplotlib.pyplot as plt

colors = [[144,103,167], [225,151,76], [114,147,203], [144,103,167], [225,151,76], [114,147,203], [144,103,167], [225,151,76], [114,147,203], [144,103,167], [225,151,76], [114,147,203], [144,103,167], [225,151,76], [114,147,203]]
l = []
for i in colors:
    m = []
    for j in i:
        k = (j/255)*1
        m.append(k)
    l.append(m)

datastr = """O'rangers 	6 	25 	20 	25 	4 	10 	15 	15 	4 	6 	10 						140
Minty Maniacs 	25 	15 	25 	10 	8 	8 	2 	6 	15 	25 	0 						139
Midnight Wisps 	15 	12 	5 	11 	5 	20 	25 	10 	6 	5 	20 						134
Crazy Cat's Eyes 	11 	20 	10 	12 	25 	12 	9 	4 	9 	4 	15 						131
Savage Speeders 	2 	1 	15 	7 	12 	15 	12 	9 	12 	15 	25 						125
Raspberry Racers 	20 	7 	7 	15 	1 	25 	10 	5 	5 	12 	1 						108
Hazers 	9 	8 	6 	9 	6 	7 	0 	25 	20 	11 	3 						104
Team Galactic 	1 	11 	2 	20 	9 	11 	11 	11 	7 	9 	11 						103
Team Momo 	10 	10 	0 	5 	8 	4 	20 	20 	10 	2 	7 						96
Oceanics 	6 	0 	3 	4 	10 	3 	4 	7 	25 	20 	6 						88
Thunderbolts 	3 	2 	8 	2 	11 	5 	5 	9 	2 	8 	9 						64
Balls of Chaos 	12 	3 	11 	3 	20 	1 	3 	3 	1 	3 	2 						62
Green Ducks 	7 	4 	12 	6 	3 	0 	7 	1 	0 	10 	12 						62
Bumblebees 	8 	6 	9 	8 	2 	6 	1 	2 	8 	7 	4 						61
Hornets 	4 	9 	4 	1 	0 	9 	8 	12 	3 	0 	5 						55
Mellow Yellow 	0 	5 	1 	0 	15 	2 	6 	0 	11 	1 	8 						49"""

def dataCleaner(data):
    cln_data_lst = [] #[["Team", [12, 12,3, 23,4 ,3 ]]]
    data_lst = data.split()
    for i in data_lst:
        if not i.isdigit():
            if len(cln_data_lst) == 0 or len(cln_data_lst[-1][-1]) > 0:
                cln_data_lst.append([i, []])
            else:
                cln_data_lst[-1][0] = cln_data_lst[-1][0] + " " + i
        else:
            cln_data_lst[-1][-1].append(i)
    return cln_data_lst

cln_data = dataCleaner(datastr)

def totalData(data):
    tot_score_data = {}
    for i in data:
        tot_score_data[i[0]] = i[1][-1]
    return tot_score_data

tot_score_data = totalData(cln_data)

def randoEvent(data):
    initial_team_lst = list(data.keys())
    random_team_lst = []
    score_lst = [0,1,2,3,4,5,6,7,8,9,10,11,12,15,20,25]
    for i in score_lst:
        random_team_lst.append(initial_team_lst.pop(random.randrange(len(initial_team_lst))))
    return dict(zip(random_team_lst, score_lst))


def eventUpdate(data): #DATA IS DICT
    initial_dict = dict(data)
    for i in data:
        data[i] = int(data[i]) + randoEvent(data)[i]
    update_dict = data
    data = initial_dict
    return update_dict

def oneWin(data, num_rounds):
    win_data = dict(data)
    for i in range(num_rounds):
        win_data = eventUpdate(win_data)
    win_lst = [[i, win_data[i]] for i in list(win_data.keys())]
    return max(win_lst, key = lambda x: x[1])

def winCounter(data, trials, num_rounds):
    wincount_dict = {}
    for i in data:
        wincount_dict[i] = 0
    for i in range(trials):
        team, score = oneWin(data, num_rounds)
        wincount_dict[team] += 1
    for i in wincount_dict:
        wincount_dict[i] = (wincount_dict[i]/trials)*100
    return wincount_dict

def winPlotter(data, trials, num_rounds):
    data_dict = winCounter(data, trials, num_rounds)
    fig, ax = plt.subplots()
    for x, y, col in zip(list(data_dict.keys()), list(data_dict.values()), l):
        ax.bar(x, y, color = col)
    ax.set_xlabel("Team Name")
    ax.set_ylabel("Percentage Change of Winning Championship")
    plt.title("Probabilities of Winning the Championship ({} trials)".format(str(trials)))
    plt.show()
