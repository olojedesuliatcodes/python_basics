string_list = ["apple","banana","cherry","date","fig"]
int_list = [5,3,8,1,9,2]

print(string_list)
print(int_list)

print(len(string_list))
print(len(int_list))

print(string_list[0])
print(string_list[-1])

print(int_list[1:5])
string_list.append("grape")
print(string_list)
string_list.insert(2,"orange")
print(string_list)

int_list.extend([10,11,12])
print(int_list)

string_list.remove("banana")
print(string_list)

int_list.pop()
print(int_list)

string_list.reverse()
print(string_list)
int_list.sort()
print(int_list)
int_list.sort(reverse=True)
print(int_list)

print(min(int_list))
print(max(int_list))
print(sum(int_list))

print(string_list.index("cherry"))
print("fig" in string_list)
int_list = [5, 3, 8, 1, 9, 2]
for number in int_list:
    print(number)
for index, item in enumerate(string_list):  
    print(f"Index {index}: {item}")

joined_string = "-".join(string_list)
print(joined_string)

string = "apple-banana-cherry-date"
split_list = string.split("-")
print(split_list)

fruit_tuple = ("mango", "pineapple", "papaya", "guava")

for fruit in fruit_tuple:
     print(fruit)
fruit_tuple = ("mango", "pineapple", "papaya", "guava")
print(fruit_tuple[0])
print(fruit_tuple[-1])

set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}

print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.union(set2))

