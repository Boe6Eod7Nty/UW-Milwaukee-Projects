# Lab goals;
# Create 8 lists:
# 5 favorite world cities
# 5 favorite US cities
# 5 favorite foods
# 5 languages you speak or would like to speak
# 5 favorite books, songs, or movies
# 5 favorite resturants, stores, or retail locations
# First names of 5 favorite friends, family, or special others
# 5 favorite expressions or greetings when seeing someone

# Create a print statement that performs the following story telling where 1 is index 1.
# Repeat for index 0-5 when you complete for index 1.
# In ListA(1) and ListB(1) I love to ear ListC(1) while speaking ListD(1) and enjoing ListE(1)
#       at ListF(1) with ListG(1) while saying ListH(1) to people walking by


# Create all list with data
ListA = ["Sydney","Tokyo","London","Moscow","Hong Kong"]
ListB = ["New York City","Milwaukee","Los Angeles","Grand Rapids","Las Vegas"]
ListC = ["Enchaladas","Eggs and waffles","Shwarma","Burgers","Chicago Deep Dish Pizza"]
ListD = ["English","Japanese","Swedish","Dutch","Esperanto"]
ListE = ["December, 1963 (Oh, What a Night!)","Margaritaville","The Rubberband Man","Brandy (You're a Fine Girl)","Once in a Lifetime"]
ListF = ["La Masa","Shaker's","Ian's Pizza","AJ Bombers","Taco Bell"]
ListG = ["Liam","Caleb","Austin","Garrett","John"]
ListH = ["'What's up?'","'Hey!'","'How've you been?'","'Howdy'","'Hello'"]
            # backslash is used to distinguish non-syntax string character.

# loop 5 times, once for each entry in the lists
for i in range(0,5):
    # i is set as 0-4, each of the 5 indexex needed to print.
    sentence = ( # parenthesis allow for multi-line string concatenation
                "In "
                + ListA[i] # world city
                + " and "
                + ListB[i] # US city
                + " I love to eat "
                + ListC[i] # food
                + " while speaking "
                + ListD[i] # language
                + " and enjoying "
                + ListE[i] # song
                + " at "
                + ListF[i] # resturant
                + " with "
                + ListG[i] # friend
                + " while saying "
                + ListH[i] # greeting
                + " to people walking by.\n"
                )
    print(sentence) # print each sentance as after it is 'assembled'


# course advisor for freshmen
# 8 total

list_tips = [
    "Attend Orientation",
    "Keep Organized",
    "Connect with your Instructors",
    "Ask for Help",
    "Keep Healthy",
    "Engage with your Interests",
    "Maintain Finances",
    "Embrace Mistakes"
]
list_tips_descriptions = [
    "This will help you familiarize yourself with campus, and you may find clubs or organizations with your interests!",
    "Once classes are in full swing, proper organization will help a lot!",
    "Your instructors want you to succeed! Always ask if you have questions of any kind.",
    "n/a",
    "n/a",
    "n/a",
    "n/a",
    "n/a"
]

print("There are many things you can do to help yourself succeed in your freshmen year of college. "
    + "Here are some great tips to keep in mind as you go through your first fall classes:")

for i in range(len(list_tips)):
    sentence = "  - " + list_tips[i]
    print(sentence)
    detail = "    - " + list_tips_descriptions[i]
    print(detail)

print("\nEnjoy your time!")

