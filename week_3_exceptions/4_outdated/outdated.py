def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    while True:
        user_date = input("Date: ")
        try:
            m, d, y = user_date.replace(" ","").split("/")
            if 1 <= int(m) <= 12 and 1 <= int(d) <= 31:
                break
        except:
            try:
                if "," in user_date:
                    m, d, y = user_date.replace(",","").split()
                else:
                    continue
                for month in months:
                    if m == month:
                        m = months.index(month) + 1
                if 1 <= int(m) <= 12 and 1 <= int(d) <= 31:
                    break
             except:
                pass
    m, d = int(m), int(d)        
    print(f"{y}-{m:02}-{d:02}")

main()
