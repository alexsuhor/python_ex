import time

t = int(time.time())

days = t // (24 * 60 * 60)
hours = t // (60 * 60) % 24 + 5
minutes = t // 60 % 60
seconds = t % 60

print(days, hours, minutes, seconds)
