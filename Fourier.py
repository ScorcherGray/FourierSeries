import numpy as np
import math
import matplotlib.pyplot as mpl

h = 0.1
x = np.arange(-0.1, 2*np.pi+0.1, h)
terms = [1, 2, 3, 5, 10, 15, 20, 25, 50]
series1 = np.empty(len(x))
series2 = np.empty(len(x))
series3 = np.empty(len(x))
series5 = np.empty(len(x))
series10 = np.empty(len(x))
series15 = np.empty(len(x))
series20 = np.empty(len(x))
series25 = np.empty(len(x))
series50 = np.empty(len(x))
diff1 = np.empty(len(x))
diff2 = np.empty(len(x))
diff3 = np.empty(len(x))
diff5 = np.empty(len(x))
diff10 = np.empty(len(x))
diff15 = np.empty(len(x))
diff20 = np.empty(len(x))
diff25 = np.empty(len(x))
diff50 = np.empty(len(x))
#terms = int(input('Enter number of terms: '))

f = np.empty(len(x))
mpl.figure(0)
for i in range(len(x)):
    f[i] = np.sin(2*x[i]) + np.cos(3*x[i])

mpl.plot(x,f, label = 'True Function')

for i in range(len(x)):
    sum = 0
    for n in range(1, 2):
        sinePart =  ((-1)** n) * 2 ** (2*n+1) * x[i]**(2*n+1) / math.factorial(2*n+1)
        cosinPart =  (-9) ** (n) * x[i]**(2*n) / math.factorial(2*n)
        sum = sum + sinePart + cosinPart

    series1[i] = sum
mpl.plot(x,series1, label = '1 term')

for i in range(len(x)):
    sum = 1
    for n in range(1, 2+1):
        sinePart =  ((-1)** n) * 2 ** (2*n+1) * x[i]**(2*n+1) / math.factorial(2*n+1)
        cosinPart =  (-9) ** (n) * x[i]**(2*n) / math.factorial(2*n)
        sum = sum + sinePart + cosinPart

    series2[i] = sum
mpl.plot(x,series2, label = '2 terms')

for i in range(len(x)):
    sum = 1
    for n in range(0, 3+1):
        sinePart =  ((-1)** n) * 2 ** (2*n+1) * x[i]**(2*n+1) / math.factorial(2*n+1)
        cosinPart =  (-9) ** (n) * x[i]**(2*n) / math.factorial(2*n)
        sum = sum + sinePart + cosinPart

    series3[i] = sum
mpl.plot(x,series3, label = '3 terms')
for i in range(len(x)):
    sum = 1
    for n in range(0, 5+1):
        sinePart =  ((-1)** n) * 2 ** (2*n+1) * x[i]**(2*n+1) / math.factorial(2*n+1)
        cosinPart =  (-9) ** (n) * x[i]**(2*n) / math.factorial(2*n)
        sum = sum + sinePart + cosinPart

    series5[i] = sum
mpl.plot(x,series5, label = '5 terms')
for i in range(len(x)):
    sum = 1
    for n in range(0, 10+1):
        sinePart =  ((-1)** n) * 2 ** (2*n+1) * x[i]**(2*n+1) / math.factorial(2*n+1)
        cosinPart =  (-9) ** (n) * x[i]**(2*n) / math.factorial(2*n)
        sum = sum + sinePart + cosinPart

    series10[i] = sum
mpl.plot(x,series10, label = '10 terms')
for i in range(len(x)):
    sum = 1
    for n in range(0, 15+1):
        sinePart =  ((-1)** n) * 2 ** (2*n+1) * x[i]**(2*n+1) / math.factorial(2*n+1)
        cosinPart =  (-9) ** (n) * x[i]**(2*n) / math.factorial(2*n)
        sum = sum + sinePart + cosinPart

    series15[i] = sum
mpl.plot(x,series15, label = '15 terms')
for i in range(len(x)):
    sum = 1
    for n in range(0, 20+1):
        sinePart =  ((-1)** n) * 2 ** (2*n+1) * x[i]**(2*n+1) / math.factorial(2*n+1)
        cosinPart =  (-9) ** (n) * x[i]**(2*n) / math.factorial(2*n)
        sum = sum + sinePart + cosinPart

    series20[i] = sum
mpl.plot(x,series20, label = '20 terms')
for i in range(len(x)):
    sum = 1
    for n in range(0, 25+1):
        sinePart =  ((-1)** n) * 2 ** (2*n+1) * x[i]**(2*n+1) / math.factorial(2*n+1)
        cosinPart =  (-9) ** (n) * x[i]**(2*n) / math.factorial(2*n)
        sum = sum + sinePart + cosinPart

    series25[i] = sum
mpl.plot(x,series25, label = '25 terms')
for i in range(len(x)):
    sum = 0
    for n in range(0, 50+1):
        sinePart =  (((-1)** n) * 2 ** (2*n+1) * x[i]**(2*n+1)) / math.factorial(2*n+1)
        cosinPart =  ((-9) ** (n) * x[i]**(2*n)) / math.factorial(2*n)
        sum = sum + sinePart + cosinPart

    series50[i] = sum
mpl.plot(x,series50, label = '50 terms')
mpl.ylim(-20, 20)
mpl.title('Series Approximation')
mpl.legend()
mpl.figure(1)
for i in range(len(x)):
    diff1[i] = f[i] - series1[i]
mpl.plot(x,diff1, label = 'diff1')

for i in range(len(x)):
    diff2[i] = f[i] - series2[i]
mpl.plot(x,diff2, label = 'diff2')

for i in range(len(x)):
    diff3[i] = f[i] - series3[i]
mpl.plot(x,diff3, label = 'diff3')

for i in range(len(x)):
    diff5[i] = f[i] - series5[i]
mpl.plot(x,diff5, label = 'diff5')

for i in range(len(x)):
    diff10[i] = f[i] - series10[i]
mpl.plot(x,diff10, label = 'diff10')

for i in range(len(x)):
    diff15[i] = f[i] - series15[i]
mpl.plot(x,diff15, label = 'diff15')

for i in range(len(x)):
    diff20[i] = f[i] - series20[i]
mpl.plot(x,diff20, label = 'diff20')

for i in range(len(x)):
    diff25[i] = f[i] - series25[i]
mpl.plot(x,diff25, label = 'diff25')

for i in range(len(x)):
    diff50[i] = f[i] - series50[i]
mpl.plot(x,diff50, label = 'diff50')
mpl.title('Error Plot')
mpl.ylim(-20, 20)
mpl.legend()
mpl.show()