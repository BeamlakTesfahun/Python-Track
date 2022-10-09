import math
AB = int(input())
BC = int(input())
teta = (math.atan(AB/BC))
teta_d = round(math.degrees(teta))
print(teta_d,chr(176),sep='')
