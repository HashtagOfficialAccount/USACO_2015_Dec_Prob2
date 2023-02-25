exceed = 0
x = open("speeding.in")
segs = [int(i) for i in x.readline().split()]
speed_limit = []
bessie_speed = []
for i in range(segs[0]):
    speed_limit.append(x.readline().split())
for i in range(segs[1]):
    bessie_speed.append(x.readline().split())

lspeeds = []
bspeeds = []
for i in speed_limit:
    for j in range(int(i[0])):
        lspeeds.append(i[1])

for i in bessie_speed:
    for r in range(int(i[0])):
        bspeeds.append(i[1])

for i in range(100):
    if int(lspeeds[i]) < int(bspeeds[i]) and int(bspeeds[i]) - int(lspeeds[i]) > exceed:
        exceed = int(bspeeds[i]) - int(lspeeds[i])
        
y = open("speeding.out","w")
y.write(str(exceed))
print(exceed)
y.close()
x.close()
