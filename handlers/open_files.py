"""
    Получение всех ID из сохранённых файлов
"""

# Получаем все Chat ID -> group_id <=> type list -> list_group_id

with open('handlers/GROUP_ID.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()

split_content = []
for line in content:
    split_content.extend(line.split())

group_id = {} # Все Chat ID
list_group_id = [] # Все Chat ID в list
count_group = 1
for i in range(len(split_content)):
    if "GROUP_ID:" == split_content[i]:
        name = split_content[i].replace(":", "")
        group_id[f"{count_group}_{name}"] = int(split_content[i + 1])
        list_group_id.append(int(split_content[i + 1]))
        count_group += 1


# Получаем все User ID Admin -> admin_id <=> type list -> list_admin_id

with open('handlers/user_admin_start.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()

split_content = []
for line in content:
    split_content.extend(line.split())

admin_id = {} # Все User ID - Admin
list_admin_id = [] # Все User-Admin ID в list
count_group = 1
for i in range(len(split_content)):
    if "User_ID:" == split_content[i]:
        name = split_content[i].replace(":", "")
        admin_id[f"{count_group}_{name}"] = int(split_content[i + 1])
        list_admin_id.append(int(split_content[i + 1]))
        count_group += 1
