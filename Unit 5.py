import math

filenametopdata= "13_43.5.csv"
filenamebottomdata= "13_159.5.csv"


all_data_top = [] # This makes a list

# with open(filenametopdata, "r", encoding="utf-8") as file:
#     location = range(1,604) 
#     all_data_top.add(location)

# all_data_bottom = [] # This makes a list

# with open(filenamebottomdata, "r", encoding="utf-8") as file:
#     location = range(1,606)  
#     all_data_bottom.add(location)

def get_data(filename: str) -> list:
    """Play around with this function to see what it does."""
    with open(filename, "r", encoding="utf-8") as file:
        all_data = []
        for line in file:
            line = line.strip()
            line = line.split(",")
            all_data.append(line)

    return all_data

# compute the mean and standard deviation of the data, to compare to each.
all_data_top = get_data(filenametopdata)
all_data_bottom = get_data(filenamebottomdata)

def calculate_standard_deviation(data: list) -> float:
    """Fix this so that it takes the right data"""
    n = len(data)
    
    # Calculate mean
    mean = sum(data) / n
    
    # Calculate variance
    variance = sum((x - mean) ** 2 for x in data) / n
    
    # Calculate standard deviation
    standard_deviation = math.sqrt(variance)
    
    return standard_deviation

# clean data
n = 604
for i in range(1, n):
    pass

# total = 0
# n = 604
# for i in location:
#     import math
#     Avg = {total/n}
#     Deviations = {x - Avg for x in all_data_top}
#     Squared_deviations = {x ** 2 for x in Deviations}
# print(f"Name: {all_data_top[0][2]}, {Avg}, {Deviations}, {Squared_deviations}")


