# Create ListA of 3 top career jobs you'd like
# create ListB of 3 top internship companies you'd like
# print a SINGLE sentence, print each ListA item, seperated by commas,
#   and ending the sentence with " are my top 3 career jobs I'd like."
# print a SINGLE line of all ListB items, with " are my top 3 favorite intership locations I'd like."

# set lists' values
ListA = ["Software Engineer", "Digital Design", "Data Scientist"]
ListB = ["Google","Microsoft","Amazon"]

# print strings by simple concatenation and index references
print(ListA[0],ListA[1],ListA[2]," are my top 3 career jobs I'd like.")
print(ListB[0],ListB[1],ListB[2]," are my top 3 favorite intership locations I'd like.")

print("====================")

# .join() method used to join all list elements with the specified delimeter (", ")
#   then concatenate ending sentence 
ListAString = ", ".join(ListA)
ListAString = ListAString + " are my top 3 career jobs I'd like."
print(ListAString)

ListBString = ", ".join(ListB) + " are my top 3 internship locations I'd like."
print(ListBString)