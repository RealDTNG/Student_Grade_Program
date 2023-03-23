import os, time, msvcrt, sqlite3


temp_list = [["Dawson", "Hoyle"],["Dylan", "Baker"],["Ava", "Something"]]
temp_list.sort(key=lambda row: (row[0]),
               reverse=False)

print(temp_list)