import csv
import matplotlib.pyplot as plt

n = 14
fields = []
rows = []
no_files = [[0 for i in range(n)] for j in range(len(rows))]
potential_values = []
overall_values = []
count_90 = []
count_91 = []
count_92 = []
count_93 = []
count_94 = []
count_95 = []

def input_file_name():
    file_name = raw_input("Enter file name: ")
    input_file_name.file_name_appended = "D:\\Projects\\Tracking Player Potentials\\" + file_name + ".csv"
    print("\nFile to be imported is {0}".format(input_file_name.file_name_appended))

def file_opener():
    try:
        with open(input_file_name.file_name_appended, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            fields = csv_reader.next()
            for row in csv_reader:
                rows.append(row)
            print("\nTotal number of rows: {0}".format(csv_reader.line_num))
        print("\nFields are: " + ", ".join(field for field in fields))
        print("\nRows are:\n")
        #print(rows)
        for row in rows[:5]:
            for col in row:
                print("%25s"%col),
            print('\n')
    except:
        print("\nFile not found!\n")  

#def 

def main():
    input_file_name()
    file_opener()
    no_files.append(rows)
    for num_1 in no_files:
        for num_2 in num_1:
            #print("%25s"%num_2)
            potential_values.append(num_2[3])
            overall_values.append(num_2[2])
    potential_values.sort()
    overall_values.sort()
    #print(potential_values)
    #print(overall_values) 
    #print(len(potential_values))
    #print(potential_values)
    for i in potential_values:
        if i == '90':
            count_90.append(i)
        elif i == '91':
            count_91.append(i)
        elif i == '92':
            count_92.append(i)
        elif i == '93':
            count_93.append(i)
        elif i == '94':
            count_94.append(i)
        elif i >= '95':
            count_95.append(i)
    percentage_90 = len(count_90)*100.0 / len(potential_values)
    percentage_91 = len(count_91)*100.0 / len(potential_values)
    percentage_92 = len(count_92)*100.0 / len(potential_values)
    percentage_93 = len(count_93)*100.0 / len(potential_values)
    percentage_94 = len(count_94)*100.0 / len(potential_values)
    percentage_95 = len(count_95)*100.0 / len(potential_values)

    pie_labels = '90', '91', '92', '93', '94', '95 and above'
    pie_sizes = [percentage_90, percentage_91, percentage_92, percentage_93, percentage_94, percentage_95]
    pie_fig, pie_axis = plt.subplots()
    plt.title("Percentage Division of Potentials")
    pie_axis.pie(pie_sizes, labels=pie_labels, autopct='%2.2f%%')
    pie_axis.axis('equal')
    plt.subplots()
    plt.bar(pie_labels, [len(count_90), len(count_91), len(count_92), len(count_93), len(count_94), len(count_95)])
    plt.title("Bar Graph of Potentials")
    plt.ylabel('Number of Players')
    plt.xlabel('Potential Values')
    plt.show()

if __name__ == "__main__":
    main()