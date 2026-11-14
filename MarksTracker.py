import matplotlib.pyplot as plt

subject   = ['English', 'Mathematics', 'Science', 'History', 'Language']
marks = [70, 85, 60, 90, 75]

plt.plot(subject, marks)
plt.show()

plt.bar(subject, marks, color='orange')
plt.title('My Subject Grade Bar Chart')
plt.xlabel('Subject')
plt.ylabel('Score')
plt.ylim(0, 100)
plt.show()