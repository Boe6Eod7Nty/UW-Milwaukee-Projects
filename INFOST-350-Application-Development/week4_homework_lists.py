# GOALS:
# Create ListA of 3 top career jobs you'd like
# create ListB of 3 top internship companies you'd like
# print a SINGLE sentence, print each ListA item, seperated by commas,
#   and ending the sentence with " are my top 3 career jobs I'd like."
# print a SINGLE line of all ListB items, with " are my top 3 favorite intership locations I'd like."

print("====================")
# set lists' values
ListA = ["Software Engineer", "Digital Design", "Data Scientist"]           #top career jobs I'd like
ListB = ["Valve","Baird","CD Project Red","North Western Mutual",'Google']  #top internship locations I'd like

# pop() method seperates the final element from the list
#        this is due to X, Y, & Z lists needing the ", & " at the end
ListAEnd = ListA.pop(-1)
ListBEnd = ListB.pop(-1)

# .join() method is used to join all list elements with the specified delimeter (", "),
#    then concatenate list ending grammer and the ending sentence.
ListAString = ", ".join(ListA) # joins all list elements into a string seperated by commas (", ")
ListAString = ListAString + ", & " + ListAEnd # adds ending list element w/ corrected grammer
ListAString = ListAString + " are my top 3 career jobs I'd like." # adds ending sentence.
print(ListAString)  # print result string

ListBString = ", ".join(ListB)
ListBString = ListBString + ", & " + ListBEnd
ListBString = ListBString + " are my top 5 internship locations I'd like."
ListBString = ListBString + "\n" # \n to add line break before Extended Excercise below
print(ListBString)

# Extended Excercise:
ListC = [   #what I need in a portofolio to acheive this.
            "Self-starter Projects",
            "Open-Source Contributions",
            "Full-Stack Examples"
        ]
ListCString = "Here are some things I need in a portofolio to acheive this: \n - " #Introduce tips list
ListCString = ListCString + "\n - ".join(ListC) # join list elements into string, seperated by line breaks and indentation.
print(ListCString)

print("====================\n")