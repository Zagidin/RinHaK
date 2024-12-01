"""
    Очищение файла GROUP_ID.txt -> находятся ID всех чатов куда добавили бота
    Очищение файла user_admin_start.txt -> находятся ID всех Admin кто добавил бота
"""

with open("GROUP_ID.txt", 'w') as file:
    file.write('')
with open("user_admin_start.txt", "w") as file:
    file.write('')

print("Файлы с Chat ID и Admin ID очищены ✅")
