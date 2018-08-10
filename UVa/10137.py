import math


def trip_expenses(numOfStudent):
    money_spent = [float(input()) for _ in range(numOfStudent)]
    avg_money = sum(money_spent) / numOfStudent

    below_average = math.floor(avg_money * 100) / 100
    above_average = math.ceil(avg_money * 100) / 100

    positive_diff = sum(elm - above_average for elm in money_spent if elm > avg_money)
    negative_diff = sum(below_average - elm for elm in money_spent if elm < avg_money)

    return max(positive_diff, negative_diff)


if __name__ == '__main__':

    while True:
        numOfStudent = int(input())
        if not numOfStudent:
            break
        amount_exchanged = trip_expenses(numOfStudent)
        print('${:.2f}'.format(amount_exchanged))
