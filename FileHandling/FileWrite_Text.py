# File Write

textfile = open("D:\sample\TextFile.txt", "w")  # If the file not exist then it 'll create the file

line1 = "Hi Reshu how are you\n"

line2 = "How is your Automation scripts Practice"

textfile.write("Hey!!!\n")
textfile.writelines((line1, line2))

textfile.flush()  # to clear the internal buffer

# File Read

textfile = open("D:\sample\TextFile.txt", "r")

print(textfile.read()) # It 'll read the entire file
print(textfile.readline()) # It 'll read only first line of the file
print(textfile.readlines()) # It 'll read lines in the list form

# File Append ---> It is used to write at the End of the File.
textfile = open("D:\sample\TextFile.txt", "a")

textfile.write("\nWhat's Up")
textfile = open("D:\sample\TextFile.txt", "r")
print(textfile.read())