days_in_year = 365
hours_in_days = 24
min_per_hour = 60 
sec_per_min = 60

def main():

    total_seconds = days_in_year * hours_in_days * min_per_hour * sec_per_min

    print(f"There are {total_seconds} seconds in a year")

if __name__ == "__main__":
    main()