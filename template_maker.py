import os
day = input("Enter Day: ")
os.mkdir("day" + day)
open("day" + day + "/input.txt", "w+")
python_file = open("day" + day + "/day" + day + ".py", "w+")
python_file.write("file = open('../day" + day + "/input.txt', 'r').read()\nthings = file.split(\"\\n\")\n")
