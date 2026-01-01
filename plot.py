import matplotlib.pylab as plt
a=[1,3,5,7,9,11,13,15,18]
b=[0,97,8,10,27,90,76,2,20]
plt.xlabel("Ratings")
plt.ylabel("UnderRatings")
plt.title("Data")
plt.plot(a,b,color="black",linewidth=2)
plt.show()