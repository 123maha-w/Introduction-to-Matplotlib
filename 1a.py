import matplotlib.pyplot as plt

sudents_names=["sanjay","rahul","karan","wasim","ramesh","ajay","sartaj","priya"]
sudents_marks=[35,50,20,45,25,40,25,40]

marks_perc=[]
for x in sudents_marks:
    res = (x/50)*10
    marks_perc.append(res)

    print(marks_perc)

def marks_line_chart():
    plt.plot(sudents_names,sudents_marks)
    plt.title("sudents marks graph")
    plt.xlabel("sudents names")
    plt.ylabel("sudents marks")
    plt.show()

marks_line_chart()

def percentage_bar_chart():
    plt.bar(sudents_names,marks_perc)
    plt.title("sudents percentage graph")
    plt.xlabel("sudents names")
    plt.ylabel("sudents percentage")
    plt.show()

percentage_bar_chart()
