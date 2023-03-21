#GRIOT v2 is a bot that adds names to a list of DB also cheks grades
known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "George", "Harry"]

students = {
    "al": {"id": "ID0001", "age":26, "grade":"A"},
    "Boby": {"id": "ID0002", "age":27, "grade":"B"},
    "Clara": {"id": "ID0003", "age": 17, "grade":"C"},
    "Dany": {"id": "ID0004", "age":21, "grade":"D"},
    "Emmas":{"id": "ID0005", "age":22, "grade":"E"}
}

print(len(known_users)," Names in DB") #tell me how many names exist

while True:
    print("Hi! My name is GRIOT")
    name = input("What is your name?: ").capitalize().strip()

    if name in known_users: #check name in list
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system (y/n)?: ").lower()

        if remove == "y":
            known_users.remove(name)
            print("Okay, {}!".format(name),"that Name is deleted!!")
        elif remove == "n":
            print("Okay, Il keep that name")

    #elif names in students['name']:
    elif name in students.keys(): #check name in dictionary
        print("Your ID is", students[name]["id"], "& your grade is:", students[name]["grade"])
        add = input("Do you agree with this Grade (y/n)?: ")
        
        if add == "y":
            del students[name]
            print("Great, Grade Submitted to Board")
            print("Okay, {}! See you soon!!".format(name))
            
        elif add == "n":
            age = int(input("From 1 - 10 | whats your grade? ").strip())
            print("tnks That grade is under review!!")

    else: # Out of equation
        print("Humm... I dont think we have met {}".format(name))
        add_me = input("Would you like to be added to the system (y/n)?: ").strip().lower()

        if add_me == "y":
            print(known_users)
            known_users.append(name) #retuns empty value & add value
            print(known_users)
            print("Sure, {}!".format(name),"that Name is added!!")
        elif add_me == "n":
            print("Okay, no name added")
#
#class MainUI: 
 #  def__int__(self):
  #     self.initUI()
#
 #  def initUI(self):
  #     Popup = Button(self, text="Enter Value", command=self.showPopup)

   #def showPopup(self):
       #create the popup with an Entry here
