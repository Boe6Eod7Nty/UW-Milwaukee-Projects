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
ListA = ["New York City","Tokyo","London","Los Angeles","Hong Kong"]
ListB = ["Milwaukee","New York City","Los Angeles","Grand Rapids","Las Vegas"]
ListC = ["Enchaladas","Eggs and waffles","Shwarma","Burgers","Chicago Deep Dish Pizza"]
ListD = ["English","Japanese","Swedish","Korean","Esperanto"]
ListE = ["December, 1963 (Oh, What a Night!)","Margaritaville","The Rubberband Man","Brandy (You\'re a Fine Girl)","Once in a Lifetime"]
ListF = ["La Masa","Shaker\'s","Ian\'s Pizza","AJ Bombers","Taco Bell"]
ListG = ["Liam","Caleb","Austin","Garrett","John"]
ListH = ["\'What's up?\'","\'Hey!\'","\'How\'ve you been?\'","\'Howdy\'","\'Hello\'"]
            # backslash is used to clarify it is not string syntax.

# loop 5 times, once for each entry in the lists
for i in range(0,5):
    # i is set as 0-4, each of the 5 indexex needed to print.
    sentance = ( # parenthesis allow for multi-line string concatenation
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
    print(sentance) # print each sentance as after it is 'assembled'
