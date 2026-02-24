# with open("data.txt", "w") as file:
#         file.write("Jasur 22\n")
#         file.write("Alisher 26\n")
#         file.write("Ali 21\n")
#         file.write("Elbek 23\n")
#         file.write("Diyor 20\n")

# with open("data.txt", "r") as file:
#         for i in file:
#                 if  int(i.split(" ")[1]) > 21:
#                         print(i)

# sum = 0
# count = 0
# with open("data.txt", "r") as file:
#         for i in file:
#                 sum += int(i.split(" ")[1])
#                 count += 1
# mean = int(sum / count)
# print(mean)

# with open("data.txt", "a") as file:
#         file.write("GAni 27\n")
#         file.write("Eldor 30\n")
#         file.write("Samandar 12\n")

backup_file = ""
with open("data.txt", "r") as file:
        backup_file = file.read()

with open("backup.txt", "w") as file:
        file.write(backup_file)