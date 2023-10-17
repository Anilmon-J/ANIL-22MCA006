print("NAME  : Anilmon J")
print("Reg No: 22MCA006")
print("Batch : MCA 2022-24 ")
print("-------------------------------------------------------------------")
import matplotlib.pyplot as plt
days=['Mon', 'Tues', 'Wed', 'Thurs', 'Fri']
drinks_sales=[300,450,150,400,650]
food_sales=[400,500,350,300,500]
fig, (ax1, ax2)=plt.subplots(2,1,figsize=(8,6))
ax1.plot(days, drinks_sales,linestyle=":", color='cyan', marker='H',markersize=8,markerfacecolor='magenta',markeredgecolor='black')
ax1.set_xlabel('Days of week')
ax1.set_ylabel('Sale of Drinks')
ax1.set_title('Sales Data1', loc='right')
ax2.plot(days, food_sales, linestyle='--', color='yellow', marker='D', markersize=8, markerfacecolor='green', markeredgecolor='red')
ax2.set_xlabel('Days of Week')
ax2.set_ylabel('Sale of Food')
ax2.set_title('Sales Data2', loc='center')
ax1.grid(color='blue')
ax2.grid(color='blue')
plt.tight_layout()
plt.show()