import matplotlib.pyplot as plt

x = []
y = []

num = int(input('데이터 수: '))
for i in range(num):
  x.append(int(input('배기량: ')))
  y.append(int(input('CO2 배출량: ')))

sum_x = 0
sum_y = 0

for i in range(len(x)):
  sum_x = sum_x + x[i]
  sum_y = sum_y + y[i]
mean_x, mean_y = sum_x/len(x), sum_y/len(y)

xy = 0
xx = 0
for i in range(len(x)):
  xy = xy + (x[i]-mean_x)*(y[i]-mean_y)
  xx = xx + (x[i]-mean_x)**2

a = xy/xx
b = mean_y - a * mean_x

while True:
  select = int(input('1.회귀식 출력, 2.CO2 배출량 예측, 3.시각화, 4.종료 '))
  if select == 1:
    print('회귀식:', 'CO2 배출량 =', a, '* 배기량 +', b)
  elif select == 2:
    displacement = int(input('배기량: '))
    print('예측 CO2 배출량:', a*displacement+b)
  elif select == 3:
    y_pred = []
    for i in range(len(x)):
      y_pred.append(a*x[i] + b)
    plt.figure(figsize=(5,3))
    plt.scatter(x, y, s=10, label='real')
    plt.plot(x, y_pred, 'r', label='prediction')
    plt.xlabel('displacement')
    plt.ylabel('CO2 emissions')
    plt.legend()
    plt.show()
  elif select == 4:
    print("종료하겠습니다")
    break
  else:
    print("잘못 입력하였습니다.")
