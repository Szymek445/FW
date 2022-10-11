from datetime import datetime, timedelta, date
from workalendar.europe import Germany, France, UnitedKingdom
import calendar
import holidays


class T2_calculation():

    def __init__(self):
        self.today = datetime.today().strftime("%d/%m/20%y")
        self.year = datetime.today().strftime("20%y")

    def check_holiday(self, day):

        de = Germany()
        fr = France()
        uk = UnitedKingdom()

        de_holidays = holidays.Germany(years=[int(self.year), int(self.year)-1])
        fr_holidays = holidays.France(years=[int(self.year), int(self.year)-1])
        uk_holidays = holidays.UnitedKingdom(years=[int(self.year), int(self.year)-1])

        if day in de_holidays:
            raise Exception("Holiday_DE")
            print("ERRRRRR")
        
        if day in fr_holidays:
            raise Exception("Holiday_FR")

        if day in uk_holidays:
            raise Exception("Holiday_UK")

    def reporting_day(self):

        pass



x = T2_calculation()
# x.reporting_day()

x.check_holiday("2022-01-01")
