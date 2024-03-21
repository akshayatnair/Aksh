students={
          "anu":(200,300,400),
          "ammu":(300,280,110),
          "anju":(400,390,290),
          "arun":(500,470,380),
          "das":(390,400,300),
          "priya":(480,300,200),
          "sachu":(390,459,340)
          }
name = input("enter name of the student \n")
if name in students.keys():
 print(students[name])
else:
    print("no student with this name")





