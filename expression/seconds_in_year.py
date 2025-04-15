    
#Constants
days_in_year: int = 365
hours_in_day: int = 24
mins_in_hour: int = 60
secs_in_min: int = 60

def main():
# The code calculates the number of seconds in a year by multiplying the number of days in a year (365) by the number of hours in a day (24),
    print("There are" + str(days_in_year * hours_in_day * mins_in_hour * secs_in_min) + " seconds in a year.")

if __name__ == "__main__":
    main()