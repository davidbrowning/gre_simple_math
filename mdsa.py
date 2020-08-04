import random
import time
from statistics import mean
total = 0
correct = 0
incorrect = 0
p_correct = 0
times = []

while (True):
    first = random.randint(2, 12)
    second = random.randint(2, 12)
    op = random.choice(["*","/","-","+"])
    if(op == "/"):
        first = first * random.randint(3,10)


    switcher = {
    "*": '{0:.3g}'.format(first * second),
    "/": '{0:.3g}'.format(first / second),
    "+": '{0:.3g}'.format(first + second),
    "-": '{0:.3g}'.format(first - second),
    }

    print(first,op,second,"=")
    value = float(switcher.get(op, "default"))
    start = time.time()
    ans = float('{0:.3g}'.format(float(input("Input your answer: "))))
    sec_elapsed = time.time() - start
    times.append(sec_elapsed)
    if(ans == value):
        correct = correct + 1
        total = total + 1
        print("correct!")
    elif (ans > (value - 0.5) and ans < (value + 0.5)):
        correct = correct + 1
        total = total + 1
        print("close enough! exact answer is: ", value)
    else:
        incorrect = incorrect + 1
        total = total + 1
        print("incorrect, correct answer: ", value)
    p_correct = correct / total
    print("-----------------------------------------\nPercent Correct: ", (100 * p_correct), "%\nAverage Time: ",mean(times), " seconds\nTotal Questions: ",total, "\n-----------------------------------------")
