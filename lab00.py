# Lab00, CS 9, Aliaksei Lenski

def areElementsInList(list1, list2):
    ''' This function takes two lists as its parameters (list1 and
        list2). Return True if each element in list1 exists in list2.
        Return False otherwise. If list1 contains no elements, True is
        returned.
    '''
    
    for i in list1:
        if i not in list2:
            return False

    return True
    # COMPLETE FUNCTION DEFINITION HERE
"""
assert areElementsInList(["one",2], [0,"one",2,"three"]) == True
assert areElementsInList([],[1,2,3,4]) == True
assert areElementsInList([1,2,3],[1,2]) == False
assert areElementsInList([1,2,3],[3,2,1]) == True
"""
def alternateCase(s):
    ''' This function takes a string parameter (s) and returns a new
        string that flips the case of each alpha character in s.
    '''

    temp = ""
    for i in s :
        if i.isupper() == True:
            temp += i.lower()
        elif i.isdigit():
            temp +=i
        elif i.islower()== True:
            temp += i.upper()
        elif i==" ":
            temp += " "
        elif i==".":
            temp+=i
    return temp

    
    # COMPLETE FUNCTION DEFINITION HERE
'''
assert alternateCase("") == ""
assert alternateCase("This is a Sentence") == "tHIS IS A sENTENCE"
asassert alternateCase("CS9") == "cs9"
assert alternateCase("9.95") == "9.95"
'''

def getCharacterCount(s):

    ''' This function takes a string parameter (s) and returns a dictionary
        type where each key in the dictionary is a unique upper-case character
        in s and its associated value is the number of occurences the unique
        character exists in s. Note that the unique characters should be case
        insensitive ("a" and "A" are considered the same and should be stored as
        "A" in the dictionary). Non alpha characters (including whitespaces)
        and their occurences should also be stored in the dictionary.
    '''

    # COMPLETE FUNCTION DEFINITION HERE
    '''
    for i in range(len(s)):
        k=s[i]
        for k in s:
            print("1")
            newdict = {i:k}
            print("2")
            if k.islower() == True:
                print("3")
                newdict = {i:k.isupper()}
                print("4")
            elif k.isupper() == True:
                newdict = {i:k}
            elif k.isdigit():
                newdict = {i:k}
            elif k==" ":
                newdict = {i:k}
            elif k==".":
                newdict = {i:k}
        return newdict
   '''
    newdict = {}
    for key in s:
        if key.upper() in newdict:
            newdict[key.upper()] = newdict[key.upper()]+1
        else:
            newdict[key.upper()]=1
    return newdict
'''        
x = getCharacterCount("This is a Sentence")
assert x.get("S") == 3
assert x.get("P") == None
assert x.get("I") == 2
assert x.get(" ") == 3

y = getCharacterCount("Pi is Approximately 3.14159")
assert y.get("1") == 2
assert y.get("A") == 2
assert y.get("P") == 3
assert y.get(".") == 1
assert y.get(4) == None
'''

