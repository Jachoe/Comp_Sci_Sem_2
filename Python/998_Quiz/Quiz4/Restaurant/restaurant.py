import random
restlist = ["Tickle tree","Burger king", "zen sushi"]
ticklelist = ["garlic fries","tuna melt","salad"]
kinglist = ["whooper","chessburger","Fries"]
sushilist = ["salmon","tuna","yellow tail"]
user = input("choose a restraunt to eat at:" + restlist)
if user == "Tickle tree":
    print(ticklelist)
    print(ticklelist[random.randrange(0,2)])
elif user == "Burger King":
    print(kinglist)
    print(kinglist[random.randrange(0,2)])
elif user == "zen sushi":
    print(sushilist)
    print(sushilist[random.randdrange(0,2)])