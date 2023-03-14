#GRIOT is a bot that adds names to a list of DB
known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]
print(len(known_users)," Names in DB") #tell me how many names exist
while True:
    print("Hi! My name is GRIOT")
    name = input("What is your name?: ").strip().capitalize()
    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system (y/n)?: ").lower()
        if remove == "y":
            known_users.remove(name)
            print("Okay, {}!".format(name),"that Name is deleted!!")
        elif remove == "n":
            print("Okay, Il keep that name")
    else:
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
