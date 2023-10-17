print("NAME  : Anilmon J")
print("Reg No: 22MCA006")
print("Batch : MCA 2022-24 ")
print("-------------------------------------------------------------------")
import matplotlib.pyplot as plt

modes=['Walking','Cycling','Car','Bus','Train']
frequency=[29,15,35,18,3]
plt.bar(modes,frequency,width=0.1,color='green')
plt.xlabel('Mode of Transport')
plt.ylabel('Frequency')
plt.title('Primary Mode of Transport to School')
plt.show()