# Purely-functional control flow.
# Rewrite the following code block without using if/elif/else:


def result_old(score):
    if score == 1:
        return "Winner"
    elif score == -1:
        return "Loser"
    else:
        return "Tied"


def result(score):
    return (score == 1 and "winner") or (score == -1 and "loser") or "tied"


print(result(1))
print(result(-1))
print(result(0))
print(result_old(1))
print(result_old(-1))
print(result_old(0))
