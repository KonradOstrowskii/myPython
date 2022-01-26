

"""
Create a program whose task will be to count which user will do
the most planned things from the to-do list.
For the best user, as a reward program goona call him a winner.
The data will be provided in the form of JSON:
Task ID, i.e. a unique value (task 1,2,3,4 etc.)
user's ID
the content of the task
information whether the task has been completed
"""

import requests
import json

r = requests.get("https://jsonplaceholder.typicode.com/todos")


def count_task_frequency(tasks):
    completedTaskFrequencyByUser = dict()
    for value in tasks:
        if (value["completed"] == True):
            try:
                completedTaskFrequencyByUser[value["userId"]] += 1
            except KeyError:
                completedTaskFrequencyByUser[value["userId"]] = 1

    return completedTaskFrequencyByUser


def get_users_with_top_completed_tasks(completedTaskFrequencyByUser):
    usersIdWithMaxCompletedAmountOfTasks = []
    maxAmountOfCompletedTask = max(completedTaskFrequencyByUser.values())
    for userId, numberOfCompletedTask in completedTaskFrequencyByUser.items():
        if (numberOfCompletedTask == maxAmountOfCompletedTask):
            usersIdWithMaxCompletedAmountOfTasks.append(userId)

    return usersIdWithMaxCompletedAmountOfTasks


def change_list_into_conj_of_param(my_list, key="id"):
    conj_param = key + "="

    lastIteration = len(my_list)
    i = 0
    for item in my_list:
        i += 1
        if (i == lastIteration):
            conj_param += str(item)
        else:
            conj_param += str(item) + "&" + key + "="

    return conj_param


try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Invalid format")
else:
    completedTaskFrequencyByUser = count_task_frequency(tasks)
    usersWithTopCompletedTasks = get_users_with_top_completed_tasks(
        completedTaskFrequencyByUser)


conj_param = change_list_into_conj_of_param(usersWithTopCompletedTasks, "id")

r = requests.get("https://jsonplaceholder.typicode.com/users",
                 params=conj_param)

users = r.json()
for user in users:
    print("And the winner is : ", user["name"])
