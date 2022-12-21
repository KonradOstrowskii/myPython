data = [410,20,106,102,4,89,56,202,203,420,345
        ,108.125,168,333]

min_value = 100
max_value = 200

for index in range(len(data)-1,-1,-1):
    if data[index] < min_value  or data[index] > max_value :
        print(index,data)
        del data[index]
        
print(f"Final data is {data}")

data_2 = [410,20,106,102,4,89,56,202,203,420,345
        ,108.125,168,333]

print("#"*20)

top_index = len(data_2) - 1
for index , value in enumerate(reversed(data_2))  :
    if value < min_value or value > max_value :
        print(top_index - index,value)
        del data_2[top_index - index]
print(f"Final data is {data_2}")
