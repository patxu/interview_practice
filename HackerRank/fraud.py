# Complete the function below.
# store list of people with suspicious behavior
# if the transaction is more than $3000, add it to the list along with the time it occured
# if the person is added to the list, set their dictionary value to None (a flag)
# every time we see a person we update their entry in a dictionary
# the dictionary key is the person's name and value is the location and time
# if the person is already in the dictionary, check if the new entry is valid
# if it is, overwrite the value with the new info
# if not, add that person to the list, along with the time the fraud occured
# if the person is added to the list, set their dictionary value to None (a flag)
# sort the list ***** most runtime added here!


def  getSuspiciousList(transactions):
    amountFraud = 3000
    locationFraud = 60
    sList = [] # suspicious list; tuples (name, time)
    pDict = {} # dictionary of people; None means already in list!
    for t in transactions:
        name, amount, loc, time = t.split("|")
        amount = int(amount)
        time = int(time)
        if name in pDict and pDict[name] == None: #already in list
            continue
        if name in pDict:
            if loc != pDict[name][0] and time - pDict[name][1] < locationFraud:
                sList.append((name, time))
                pDict[name] = None
                continue
            else:
                pDict[name] = (loc,time)
        else:
            pDict[name] = (loc, time)
        if amount > amountFraud:
            sList.append((name, time))
            pDict[name] = None
    return [person[0] for person in sorted(sList, key=lambda person:person[1])]

print getSuspiciousList(["Shilpa|5000|CA|63"])
