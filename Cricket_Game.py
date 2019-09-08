"""
What factors could you control?
agression -> more boundaries  and outs
choose players or set behaviour or both?4
order? -> ball wear etc.
Partnerships
make changes between tests?
bat first or second
"""


from random import randint
from pandas import DataFrame


def runs_scored():
    out = False
    runs = 0
    while out is False:
        first_roll = randint(1, 6)
        second_roll = randint(1, 6)
        if first_roll == 5:
            if second_roll == 6:
                runs += 1
            elif second_roll == 5:
                runs += 0
            else:
                out = True
        elif first_roll % 2 == 0:
            runs += first_roll
        else:
            runs += first_roll
    return runs


england_scorecard = {"Batter": ["Jack Hobbs", "Alastair Cook", "Wally Hammond", "Ken Barrington", "Kevin Pietersen", "Ian Botham" , "Alan Knott", "Graeme Swann"],
        "Run Total":[runs_scored(),runs_scored(),runs_scored(),runs_scored(),runs_scored(),runs_scored(),runs_scored(),runs_scored()]}

australia_scorecard = {"Batter":["Matthew Hayden", "Victor Trumper", "Donald Bradman", "Ricky Ponting",
                  "Greg Chappell", "Keith Miller" , "Adam Gilchrist", "Shane Warne"],
        "Run Total":[runs_scored(),runs_scored(),runs_scored(),runs_scored(),runs_scored(),runs_scored(),runs_scored(),runs_scored()]}

england_total = sum(england_scorecard["Run Total"])
australia_total = sum(australia_scorecard["Run Total"])

print("England Scorecard:")
print(DataFrame(england_scorecard))
print("Total English runs: {}\n".format(england_total))
print("Australian Scorecard:")
print(DataFrame(australia_scorecard))
print("Total Australian runs: {}\n".format(australia_total))


if england_total == australia_total:
    print("The match is a tie!")
elif england_total > australia_total:
    print("England takes the game!")
else:
    print("Australia wins the match...")
