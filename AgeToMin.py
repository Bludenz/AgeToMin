from tkinter import *
from tkinter import messagebox
import datetime
from datetime import *

def clearAll() :

    dayField.delete(0, END)
    monthField.delete(0, END)
    yearField.delete(0, END)
    givenDayField.delete(0, END)
    givenMonthField.delete(0, END)
    givenYearField.delete(0, END)
    rsltDayField.delete(0, END)
    rsltMonthField.delete(0, END)
    rsltYearField.delete(0, END)
    rsltMinuteField.delete(0, END)
 
def checkError() :

    if (dayField.get() == "" or monthField.get() == ""
        or yearField.get() == "" or givenDayField.get() == ""
        or givenMonthField.get() == "" or givenYearField.get() == "") :

        messagebox.showerror("Input Error")

        clearAll()
         
        return -1

def Today():
    today = date.today()
    year = today.year
    month = today.month
    day = today.day
    givenDayField.insert(10,str(day))
    givenMonthField.insert(10,str(month))
    givenYearField.insert(10,str(year))

def calculateAge() :

    value = checkError()

    if value ==  -1 :
        return
     
    else :
        today = date.today()
        Year1 = int(today.year)
        Month1 = int(today.month)
        Day1 = int(today.day)

        birth_day = int(dayField.get())
        birth_month = int(monthField.get())
        birth_year = int(yearField.get())

        given_year = Year1
        given_month = Month1
        given_day = Day1

         
        month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
         
        if (birth_day > given_day):
            given_month = given_month - 1
            given_day = given_day + month[birth_month-1]
                     
        if (birth_month > given_month):
            given_year = given_year - 1
            given_month = given_month + 12
                     
        calculated_day = given_day - birth_day;
        calculated_month = given_month - birth_month;
        calculated_year = given_year - birth_year;

        MinYear = calculated_year * 525600
        MinMonth = calculated_month * 43800
        MinDay = calculated_day * 1440

        Min = MinDay + MinMonth + MinYear
        Minutes = round(Min,1)
         
        rsltDayField.insert(10, str(MinDay))
        rsltMonthField.insert(10, str(MinMonth))
        rsltYearField.insert(10, str(MinYear))
        rsltMinuteField.insert(10,str(Minutes))

        

if __name__ == "__main__" :
 
    gui = Tk() 
    gui.configure(background = "gray")
    gui.iconbitmap(r"G:\Age\icon.ico")
    gui.title("Age In Minutes")
    gui.geometry("280x350")

    dob = Label(gui, text = "Date Of Birth", bg = "gray")
    givenDate = Label(gui, text = "Given Date", bg = "gray")
    day = Label(gui, text = "Day", bg = "gray")
    month = Label(gui, text = "Month", bg = "gray") 
    year = Label(gui, text = "Year", bg = "gray")
    givenDay = Label(gui, text = "Given Day", bg = "gray")
    givenMonth = Label(gui, text = "Given Month", bg = "gray")
    givenYear = Label(gui, text = "Given Year", bg = "gray")
    rsltYear = Label(gui, text = "Years", bg = "gray")
    rsltMonth = Label(gui, text = "Months", bg = "gray")
    rsltDay = Label(gui, text = "Days", bg = "gray")
    rsltMinute = Label(gui, text = "Age In Minutes", bg = "gray")
    resultantAge = Button(gui, text = "Calculate!", fg = "Black", bg = "Red", command = calculateAge)
    clearAllEntry = Button(gui, text = "Clear All", fg = "Black", bg = "Red", command = clearAll)
    TodayEntry = Button(gui, text = "Today's Date", fg = "Black", bg = "Red", command = Today)
    CopyRight = Label(gui, text = "©2022 www.bludenz.dev.\n All rights reserved", bg = "gray")

    dayField = Entry(gui)
    monthField = Entry(gui)
    yearField = Entry(gui)
     
    givenDayField = Entry(gui)
    givenMonthField = Entry(gui)
    givenYearField = Entry(gui)
     
    rsltYearField = Entry(gui)
    rsltMonthField = Entry(gui)
    rsltDayField = Entry(gui)
    rsltMinuteField = Entry(gui)
 

    dob.grid(row = 0, column = 3)
     
    day.grid(row = 1, column = 2)
    dayField.grid(row = 1, column = 3)
     
    month.grid(row = 2, column = 2)
    monthField.grid(row = 2, column = 3)
     
    year.grid(row = 3, column = 2)
    yearField.grid(row = 3, column = 3)
     
    givenDate.grid(row = 5, column = 3)
     
    givenDay.grid(row = 7, column = 2)
    givenDayField.grid(row = 7, column = 3)
     
    givenMonth.grid(row = 8, column = 2)
    givenMonthField.grid(row = 8, column = 3)
     
    givenYear.grid(row = 9, column = 2)
    givenYearField.grid(row = 9, column = 3)

    resultantAge.grid(row = 11, column = 3)
     
    rsltMinute.grid(row = 12, column = 3)
    rsltMinuteField.grid(row = 13, column = 3)
     
    clearAllEntry.grid(row = 14, column = 3)
    TodayEntry.grid(row = 6, column = 3)
    CopyRight.grid(row= 15, column= 3)
     

    gui.mainloop()  