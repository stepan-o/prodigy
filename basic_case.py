import random


num_users = 100
num_tasks = 100
for _ in range(num_users):
    scores = [random.randint(0, 1) for _ in range(1, num_tasks)]
    print(sum(scores) / num_tasks)
