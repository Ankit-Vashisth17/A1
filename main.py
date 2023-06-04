import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
plt.title("Table of Two's")
plt.ylabel("Table of 2")
plt.xlabel("1 to 10")
plt.plot(x, y)
plt.show()
#Bar Plot
import matplotlib.pyplot as plt
x=[50,60,30,70,20]
y=["A","B","C","D","E"]
plt.bar (y,x,color="blue",width=0.1)
plt.title('TITLE OF THE BAR GRAPH')
plt.show()
#line plot
import matplotlib.pyplot as plt
x=[5,10,15,20,25]
y=[2,4,6,8,10]
plt.plot(x,y,color='orange')
plt.title ('title')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
#Pie plot
import matplotlib.pyplot as plt
x=[50,60,30,70,20]
y=["A","B","C","D","E"]
plt.pie (x,labels=y,)
plt.title('TITLE OF THE BAR GRAPH')
plt.show()

#Horizontal bar plot
import matplotlib.pyplot as plt
x=[50,60,30,70,20]
y=["A","B","C","D","E"]
plt.scatter (x,y,color='brown')
plt.title('TITLE OF  GRAPH')
plt.show()
#Horizontal bar plot
import matplotlib.pyplot as plt
x=[50,60,30,70,20]
y=["A","B","C","D","E"]
plt.bar(x,y,color='red',width=13)
plt.title('TITLE OF THE BAR GRAPH')
plt.show()









