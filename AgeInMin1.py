from tkinter import *
from tkinter import messagebox
import datetime
from datetime import *

def clearAll() :

    dayField.delete(0, END)
    monthField.delete(0, END)
    yearField.delete(0, END)
    rsltDayField.delete(0, END)
    rsltMonthField.delete(0, END)
    rsltYearField.delete(0, END)
    rsltMinuteField.delete(0, END)
 

def calculateAge() :

    today = date.today()
    Year = int(today.year)
    Month = int(today.month)
    Day = int(today.day)

    birth_day = int(dayField.get())
    birth_month = int(monthField.get())
    birth_year = int(yearField.get())

    given_year = Year
    given_month = Month
    given_day = Day

         
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
    rsltMinute = Label(gui, text = "Age In Minutes", bg = "gray")
    resultantAge = Button(gui, text = "Calculate!", fg = "Black", bg = "Red", command = calculateAge)
    clearAllEntry = Button(gui, text = "Clear All", fg = "Black", bg = "Red", command = clearAll)
    CopyRight = Label(gui, text = "©2022 www.bludenz.dev.\n All rights reserved", bg = "gray")

    dayField = Entry(gui)
    monthField = Entry(gui)
    yearField = Entry(gui)
     
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

    resultantAge.grid(row = 11, column = 3)
     
    rsltMinute.grid(row = 12, column = 3)
    rsltMinuteField.grid(row = 13, column = 3)
     
    clearAllEntry.grid(row = 14, column = 3)
    CopyRight.grid(row= 15, column= 3)     

    gui.mainloop()  