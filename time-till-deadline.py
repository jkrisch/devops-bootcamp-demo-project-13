import datetime

user_input = input("Enter your goal with a deadline (format: dd.MM.yyyy) separated by a colon (':')\n")

args = user_input.split(":")

goal = args[0]
#use strip to make sure white spaces are ignored
deadline = args[1].strip()

try:
    deadline_date = datetime.datetime.strptime(deadline, '%d.%m.%Y')
    today = datetime.datetime.today()
    time_till_deadline = deadline_date - today
    hours_till_deadline = int(time_till_deadline.total_seconds()/3600)
    print(f"Dear User. You've got {time_till_deadline.days} days left to {goal}. This means {hours_till_deadline} hours. Keep on going!")
except ValueError as error:
    print("Wrong date format. Please use dd.MM.yyyy (e.g. 31.12.2024)")
