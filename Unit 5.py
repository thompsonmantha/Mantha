filenametopdata= "13_43.5.csv"
filenamebottomdata= "13_159.5.csv"

#all_data_top= []
#with open(filenametopdata, "r", encoding="utf-8") as file:
#    for line in file:
#        all_data_top.append(line.split(","))

#all_data_bottom= []
#with open(filenamebottomdata, "r", encoding="utf-8") as file:
#    all_data_bottom.append(line.split(","))

all_data_top= set()
with open(filenametopdata, "r", encoding="utf-8") as file:
    location = range(1,604) 
    all_data_top.add(location)

all_data_bottom= set()
with open(filenamebottomdata, "r", encoding="utf-8") as file:
    location = range(1,606)  
    all_data_bottom.add(location)

total = 0
n = 604
for i in location:
    import math
    Avg = {total/n}
    Deviations = {x - Avg for x in all_data_top}
    Squared_deviations = {x ** 2 for x in Deviations}
print(f"Name: {all_data_top[0][2]}, {Avg}, {Deviations}, {Squared_deviations}")


#total = 0
#n=604
#for i in range(1, n):
#    total += float(all_data_top[i][2])
#    #print(all_data_top[i][2])
#    import math
#    Avg = {total/n}
#    Deviations = {x - Avg for x in all_data_top}
#    Squared_deviations = {x ** 2 for x in Deviations}
#print(f"Name: {all_data_top[0][2]}, {Avg}, {Deviations}, {Squared_deviations}")

#total = 0
#n=606
#for i in range(1, n):
#    total += float(all_data_top[i][2])
#    #print(all_data_top[i][2])
#    Avg = {total/n}
#print(f"Name: {all_data_top[0][2]}, {Avg}")
