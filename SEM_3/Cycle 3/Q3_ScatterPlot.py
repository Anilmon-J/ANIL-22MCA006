print("NAME  : Anilmon J")
print("Reg No: 22MCA006")
print("Batch : MCA 2022-24 ")
print("-------------------------------------------------------------------")
import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
affordable_segment = [173, 153, 195, 147, 120, 144, 148, 109, 174, 130, 172, 131]
luxury_segment = [189, 189, 105, 112, 173, 109, 151, 194, 174, 145, 177, 161]
super_luxury_segment = [185, 185, 126, 134, 196, 153, 112, 133, 200, 145, 167, 110]
plt.figure(figsize=(12, 6))
plt.scatter(months, affordable_segment, c='pink', label='Affordable Segment', s=100, marker='o')
plt.scatter(months, luxury_segment, c='yellow', label='Luxury Segment', s=100, marker='o')
plt.scatter(months, super_luxury_segment, c='blue', label='Super Luxury Segment', s=100, marker='o')
plt.xlabel('Months of Year', fontsize=18)
plt.ylabel('Sales of Segments', fontsize=18)
plt.title('Sales Data', fontsize=18)
plt.legend()
plt.show()