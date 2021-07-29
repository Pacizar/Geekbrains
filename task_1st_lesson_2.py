time = int(input("Введите произвольное количество секунд: "))
t = time

minutes = (t // 60) % 60
m = minutes

hours = t // 3600
h = hours

seconds = (t % 3600) % 60
s = seconds

print("{:02}:{:02}:{:02}".format(h, m, s,))
