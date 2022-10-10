# File Write

textfile = open("D:\sample\TextFile.txt", "w")

line1 = "Hi Reshu how are you\n"

line2 = "How is your Automation scripts Practice"

textfile.write("Hey!!!\n")
textfile.writelines((line1, line2))

textfile.flush()

# # File Read

# textfile = open("D:\sample\TextFile.txt", "r")
#
# # print(textfile.read()) # It 'll read the entire file
# print(textfile.readline()) # It 'll read only line of the file

# File Append ---> It is used to write at the End of the File.
textfile = open("D:\sample\TextFile.txt", "a")

textfile.write("\nWhat's Up")
textfile = open("D:\sample\TextFile.txt", "r")
print(textfile.read())