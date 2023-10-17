print("NAME  : Anilmon J")
print("Reg No: 22MCA006")
print("Batch : MCA 2022-24 ")
print("-------------------------------------------------------------------")
import matplotlib.pyplot as plt
heights=[61,63,64,66,68,69,71,71.5,72,72.5,73,73.5,74,74.5,76,76.2,76.5,77,77.5,78,78.5,79,79.2,80,81,82,83,84,85,87]
# Create a histogram with a bin size of 5
plt.hist(heights,bins=range(60,90,5),edgecolor='black',color='blue')
#Set labels and title
plt.xlabel('Height (in inches)')
plt.ylabel('Frequency')
plt.title('Cherry Tree Height Histogram')
plt.xticks(range(60,90,5))
# Show the histogram
plt.show()