shenggao = input('身高'+'(厘米|整数)')
tizhong = input('体重'+'(KG|整数)')
height = int(shenggao)
weight = int(tizhong)
bmi = weight/(height/100)**2
if bmi < 18.5:
    print('过轻')
elif 18.5 < bmi < 25:
    print('正常')
elif 25 < bmi < 28:
    print('过重')
elif 28 < bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')
print('bmi值',bmi)