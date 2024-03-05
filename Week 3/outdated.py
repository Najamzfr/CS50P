months = [
    "January","February","March","April","May","June","July",
    "August","September","October","November","December"
]

while True:
    date = input('Date: ')
    try:
        month,day,year = date.split('/')
        year = year.strip()
        if (int(day)>=1 and int(day)<=31) and (int(month)>=1 and int(month)<=12):
            break

    except:
        try:
            old_month_day,year = date.split(',')
            old_month,old_day = old_month_day.split(' ')
            for i in range(len(months)):
                if old_month == months[i]:
                    month = i +1

            day = old_day.replace(",","")
            year = year.strip()

            if (int(day)>=1 and int(day)<=31) and (int(month)>=1 and int(month)<=12):
                break

        except:
            print()
            pass

print(f"{year}-{int(month):02}-{int(day):02}")

