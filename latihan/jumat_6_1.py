def create_list(data):
    temp_i = []
    for i in range(data):
        temp_i.append(i)
    return temp_i
print (create_list(10))

def create_list(data):
    for i in range(data):
        yield i
print (list(create_list(10)))