"""
Module 4 Assignment 2: String formatting

Begin by executing this script from the command line by typing
    `$ python assignment.py`


This script will print out all the questions and the returned value. This
script must execute without error.

Each question is a fill-in-the-blank and ends with a blank
`return` statement. Provide the answer to the question following
the return statement.

Sample question:

    def question():
        '''What is 2 + 2?'''
        return

    Answer:
        return 2 + 2

Note:  Use the system's current time wherever there is mention of
       today's date, or the current time (i.e. .today()). Do not hard
       code the date which you completed the assignment.


Some questions have variables in them, and will need manipulation. In that
case, perform whatever transformations to the variable, and make sure that
it is returned.

Example:
    def question():
        '''Do something to variable x and return.'''
        x = 'a variable'
        ... code that does stuff to x ...
        return x
"""


def question_1():
    """
    Return the following variables as part of my_str string
    using the "printf" inspired (old-style) formatting.
    The returned string should be
    "Capital city of Ottawa is in the province of Ontario."
    """
    cap_city = "ottawa"
    cap_prov = "ontario"

    my_str = 'Capital city of %s is in the provice of %s.'%(cap_city, cap_prov)
    
    return my_str


def question_2():
    """
    Return the following variables as part of my_str string
    using the ".format" (new-style) formatting. The returned string should be
    "Canada has 10 provinces and 3 territories."
    """
    num_prov = 10
    num_terr = 3

    my_str = 'Canada has {prov} and {terr} territories.'.format(prov=num_prov, terr=num_terr)
    
    return my_str


def question_3():
    """
    Return the following variables as part of my_str string
    using an f-string. The returned string should be
    "Canada has 10 provinces and 3 territories, capital city of Ottawa is in the province of Ontario."
    """
    num_prov = 10
    num_terr = 3
    cap_city = "ottawa"
    cap_prov = "ontario"

    my_str = f'Canada has {num_prov} provinces and {num_terr} territories, capital city of {cap_city} is in the province of {cap_prov}.'
    
    return my_str


def question_4():
    """
    Return the following variable 1234.9 as a dollar currency
    value. It should be prepended by the $ symbol and have 2
    decimal places.
    """
    amount = 1234.9
    return f"${amount:.2f}"


def question_5():
    """
    Return the following variable as a percentage value (i.e. 38%).
    """
    value = 0.38
    return f"{value:.0%}"


def question_6():
    """
    Return the following as a string including the positive sign.
    """
    value = 1234
    return f"+{value:}"


def question_7():
    """
    Return the following value as a dollar currency value including
    comma separators. (E.g. $123,567,90.00)
    """
    amount = 59430458187241.3283
    return f"${amount:,.2f}"


def question_8():
    """
    Return the following integer as a North American telephone
    number (e.g. (xxx) xxx-xxxx)
    """
    number = 4165551234
    num2=str(number)
    return '({}) {}-{}'.format(num2[:3], num2[3:6], num2[6:])


def question_9():
    """
    Return the following integer with trailing zeros so that
    it occupies 7 characters (e.g. 0000001)
    """
    number = 978
    return "%0*d" % (7, number)


def question_10():
    """
    Return a string which repeats the * character exactly 50 times.
    """
    fill=f'{"":*^50}'
    return fill


def question_11():
    """
    Return the phrase "Hello World" centered within a series of *
    characters. The total length of the string should be 79 characters.

    E.g. *** Hello World ***
    """
    
    fill="Hello World"
    
    return fill.center(79, "*")


def question_12():
    """
    Return today's date in the following format: Jan 1, 2019
    """
    from datetime import datetime
    today_date = datetime.now()
    
    return today_date.strftime("%b %d, %Y")


def question_13():
    """
    Return today's date in the following format: January 1, 2019
    """
    from datetime import datetime
    today_date = datetime.now()
    
    return today_date.strftime("%B %d, %Y")


def question_14():
    """
    Return today's date in YYYY-MM-DD format.
    """
    from datetime import datetime
    today_date = datetime.now()
    return today_date.date()


def question_15():
    """
    Return tomorrow's weekday name (i.e. if today is Friday,
    tomorrow is Saturday)
    """
    from datetime import datetime, timedelta
    today_date = datetime.now()
    td = timedelta(days=1)
    tomorrow = today_date + td
    return tomorrow.strftime("%A")


def question_16():
    """
    Return the current time in 24 hour format with seconds.
    (i.e. 23:21:03)
    """
    from datetime import datetime
    today_date = datetime.now()
    ntime = today_date.time()
    return ntime.strftime("%H:%M:%S")


def question_17():
    """
    Return the current date and time in ISO-8601 format.
    """
    from datetime import datetime
    today_date = datetime.now()
    return today_date.isoformat()


def question_18():
    """
    Return the current time using AM/PM time format. (e.g 1:34 PM)
    """
    from datetime import datetime
    today_date = datetime.now()
    ntime = today_date.time()
    return ntime.strftime("%I:%M %p")


def question_19():
    """
    Reformat the following string into 24-hour date format (HH:ss)
    """
    x = '5:49 PM'
    from datetime import datetime
    conv = datetime.strptime(x, "%I:%M %p")
    rettime = conv.strftime("%H:%M")
    return rettime


def question_20():
    """
    Using the strptime function, return the following string
    as a date object.
    """
    my_date = '2014-12-20'
    from datetime import datetime
    conv = datetime.strptime(my_date, "%Y-%m-%d")
    return conv


def question_21():
    """
    Using the strptime function, parse and return the following
    as a datetime object.
    """
    my_datetime = '2014-12-20 23:12'
    from datetime import datetime
    conv = datetime.strptime(my_datetime, "%Y-%m-%d %H:%M")
    return conv


def question_22():
    """
    Subtract 4 hours from the current datetime and return.
    """
    from datetime import datetime, timedelta
    tnow = datetime.now()
    tdelta = timedelta(hours=4)
    return tnow - tdelta


def question_23():
    """
    Add 7 days to the current datetime and return.
    """
    from datetime import datetime, timedelta
    tnow = datetime.now()
    tdelta = timedelta(days=7)
    return tnow + tdelta


def question_24():
    """
    Return the following string as a date object. Assume that
    a week begins on a Sunday.
    """
    my_date = 'Day 2 of week 23, 2020'
    from datetime import datetime
    conv = datetime.strptime(my_date, 'Day %w of week %U, %Y')
    return conv


def question_25():
    """
    If John was born on 4th of July 1982, How old is he today?
    (return just the number of years as integer)
    """
    from datetime import datetime
    tnow = datetime.now()
    TJohn = datetime.strptime('July 04, 1982', '%B %d, %Y')
    Tdel = tnow - TJohn
    Age = int((Tdel.days) / 365)
    return Age 


def question_26():
    """
    If baby "alex" was born on the first day of this year? What many days old is baby alex?
    (e.g. If today is Jan 25, alex is 24 days old). Return as an integer.
    """
    from datetime import datetime
    tnow = datetime.now()
    TAlex = datetime.strptime('January 1, 2020', '%B %d, %Y')
    Tdel = tnow - TAlex
    Age = int(Tdel.days) 
    return Age


def question_27():
    """
    How much time is left this year? Return a timedelta object.
    (Last day of the year at 23:59:59 marks end of the year)
    """
    from datetime import datetime, timedelta
    tnow = datetime.now()
    TEND = datetime.strptime('December 31, 2020 11:59PM', '%B %d, %Y %I:%M%p')
    Tdel = TEND-tnow 
    return Tdel


def question_28():
    """
    How many seconds are left this year? Return an integer.
    (Hint: look for a helper function on timedelta)
    """
    from datetime import datetime, timedelta
    tnow = datetime.now()
    TEND = datetime.strptime('December 31, 2020 11:59PM', '%B %d, %Y %I:%M%p')
    Tdel = TEND-tnow
    Tdelsec = Tdel.seconds
    Tdeldaysec = (Tdel.days *24*60*60)
    return Tdelsec+Tdeldaysec


if __name__ == '__main__':
    for num in range(1, 29):
        func = eval(f'question_{num}')
        question = ' '.join(func.__doc__.split())
        print(f'Question {num}: {question}')
        print(f'    {func()}\n\n')
