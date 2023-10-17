import matplotlib.pyplot as plt
print("NAME  : Anilmon J")
print("Reg No: 22MCA006")
print("Batch : MCA 2022-24 ")
print("-------------------------------------------------------------------")
years = [2001, 2002, 2003, 2004, 2005, 2006, 2007]
car_values = [24000, 22500, 19700, 17500, 14500, 10000, 5800]

plt.figure(figsize=(10, 5))
plt.subplot(1, 1, 1)

plt.plot(years, car_values, 'r-.', label='Car Value', linewidth=2)

plt.scatter(years, car_values, c='green', marker='*', s=70, label='Data Points')

plt.xlabel('Year')
plt.ylabel('Car Value')
plt.title('Value Depreciation', loc='left')

plt.legend()

plt.grid(True)
plt.show()