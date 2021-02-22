import ast

with open ("dictionary.txt", "r") as d:
    dict_data = d.read()
# reconstructing the data as a dictionary
dictionary = ast.literal_eval(dict_data)
# find depth
def dict_depth(dict_data, lenel = 1):
    str_dict_data = str(dict_data)
    count = 0
    for i in str_dict_data:
        if i == "{":
            count += 1 
    return(count)
# show the user the greater depth of dictionary 
print("greater depth of dictionary :",dict_depth(dict_data))
d.close()