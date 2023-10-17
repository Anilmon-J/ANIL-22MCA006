print("NAME  : Anilmon J")
print("Reg No: 22MCA006")
print("Batch : MCA 2022-24 ")
print("-------------------------------------------------------------------")
import matplotlib.pyplot as plt

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
affordable_segment = [173, 153, 195, 147, 120, 144, 148, 109, 174, 130, 172, 131]
luxury_segment = [189, 189, 105, 112, 173, 109, 151, 194, 174, 145, 177, 161]
super_luxury_segment = [185, 185, 126, 134, 196, 153, 112, 133, 200, 145, 167, 110]
plt.figure(figsize=(12, 6))
plt.plot(months, affordable_segment, label='Affordable Segment', color='blue', linestyle='-', marker='o')
plt.plot(months, luxury_segment, label='Luxury Segment', color='red', linestyle='--', marker='s')
plt.plot(months, super_luxury_segment, label='Super Luxury Segment', color='green', linestyle='-.', marker='^')
plt.xlabel('Months of Year', fontsize=18)
plt.ylabel('Sales of Segments', fontsize=18)
plt.title('Sales Data', fontsize=18)
plt.legend(loc='upper right')
plt.show()