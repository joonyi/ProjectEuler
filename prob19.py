import calendar

# How many Sundays fell on the first of the month during the
# twentieth century (1 Jan 1901 to 31 Dec 2000)?
sunday = 0
lis = []
for i in range(1901,2001):
    for j in range(1,13):
        c = calendar.TextCalendar(calendar.SUNDAY)
        mycal = calendar.monthcalendar(i,j) #(year,month)
        if mycal[0][calendar.SUNDAY] == 1:
            sunday += 1
            lis.append((i,j))

print(sunday)
print(lis)
