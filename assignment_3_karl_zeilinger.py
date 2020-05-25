"""
Assignment 3.
"""
from datetime import datetime, timedelta

gender = ['M', 'F', 'N']
genderdict = {"M": "male", "F": "female", "N": "non-binary"}

#calculates age of user - checks for future date error and invalid date
def getbirthdate():
    bdate = input("Please enter your date of birth in YYYY-mm-dd ")
    try:
        bdate = datetime.strptime(bdate, "%Y-%m-%d")
        tnow = datetime.now()
        Tdel = tnow - bdate
        Age = ((Tdel.days) / 365.25)
        if Age >= 0:
            return Age
        else:
            print("Invalid date value - please do not future date")
            return getbirthdate()
    except:
        print("Invalid date format please try again")
        return getbirthdate()

#checks if SIN is an integer value
def getSIN():
    SIN = input("Please enter your SIN # ")
    try:
        return int(SIN)
    except:
        print("Invalid SIN - please enter only a numeric value")
        return getSIN()

#checks if sex value exists in gender dict
def getSEX():
    ysex = input("Please enter your sex as M/F/N ")
    try:
        if ysex.upper() in gender:
            return ysex
        else:
            print("Invalid gender please try again.")
            return getSEX()
    except:
        pass

#if statement checks to ensure data entered in name / city before proceeding
def main():
    user = input("Please enter your name ")
    loc = input("Please enter your city of birth ")
    if user == "" or loc == "":
        print("Please ensure you enter a value for name and city of birth")
        main()
    else:
        age = int(getbirthdate())
        SIN = getSIN()
        sex = getSEX()
        print(f'{user} is a {age} year old {genderdict.get(sex.upper())}. They were born in {loc} and their SIN # is {SIN}.')
    
# Do not edit below
if __name__ == '__main__':
    main()
