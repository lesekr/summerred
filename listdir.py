import os

lists = []

#working directory
attempt_dir = os.getcwd() #pathname #variable

#working directory
for lists in os.listdir(attempt_dir):
    lists_path = os.path.realpath(lists)
    lists_size = os.path.getsize(lists)
    lists.append({'path': list_path, 'size': list_size})
   
print(*lists, sep='\n')
