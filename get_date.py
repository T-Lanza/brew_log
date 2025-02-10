import datetime

def get_month(month):
    if month == 1:
        return "January"
    elif month == 2:
        return "February"
    elif month == 3:
        return "March"
    elif month == 4:
        return "April"
    elif month == 5:
        return "May"
    elif month == 6:
        return "June"
    elif month == 7:
        return "July"
    elif month == 8: 
        return "August"
    elif month == 9:
        return "September"
    elif month == 10:
        return "October"
    elif month == 11:
        return "November"
    elif month == 12:
        return "December"
    else:
        return "No such Month"
    
def get_month_num(month):
    if month == 1:
        return "01"
    elif month == 2:
        return "02"
    elif month == 3:
        return "03"
    elif month == 4:
        return "04"
    elif month == 5:
        return "05"
    elif month == 6:
        return "06"
    elif month == 7:
        return "07"
    elif month == 8: 
        return "08"
    elif month == 9:
        return "09"
    elif month == 10:
        return "10"
    elif month == 11:
        return "11"
    elif month == 12:
        return "12"
    else:
        return "No such Month"
    
def get_date():
    now = datetime.datetime.now()
    
    month = str(get_month(now.month))
    day = str(now.day)
    year = str(now.year)

    return f"{month} {day}, {year}"

def get_date_num():
    now = datetime.datetime.now()
    
    month = str(get_month_num(now.month))
    day = str(now.day)
    year = str(now.year)

    return f"{month}/{day}/{year}"