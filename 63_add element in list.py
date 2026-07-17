fruit_list = ["Apple","Banana","Pineapple"]

# append
fruit_list.append("orange")  #elemenet added in the end 
# Output: fruit_list = ["Apple","Banana","Pineapple"]
print(fruit_list)

#insert
fruit_list.insert(3,"grapes")  #insert element on a specific index
# Output: ['Apple', 'Banana', 'Pineapple', 'grapes', 'orange']
print(fruit_list)

#extend
fruit_list.extend(["kiwi","pear"])  #add list
# Output: ['Apple', 'Banana', 'Pineapple', 'grapes', 'orange', 'kiwi', 'pear']
print(fruit_list)
