import matplotlib.pyplot as plt
import numpy as np

# Sample height data for 20 students (in centimeters)
student_heights = [150, 160, 165, 170, 155, 180, 175, 158, 162, 168,
                   172, 167, 160, 164, 158, 172, 169, 177, 165, 174]

# Names of the students (optional)
students = [
    "Ayesha","Ali","Fatima","Ahmed","Zara","Bilal","Sana","Usman","Hina","Sami","Maryam","Omar","Nida","Faizan","Saima","Hasan","Sara","Kamran","Rabia","Zain"]



# Bar Chart
plt.figure(figsize=(10, 5))

colors = plt.cm.viridis(np.linspace(0, 1, len(student_heights)))  
plt.bar(students, student_heights, color=colors)
plt.xlabel('Students')
plt.ylabel('Height (cm)')
plt.title('Bar Chart of Student Heights')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

