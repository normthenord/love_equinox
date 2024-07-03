import datetime
from love_equinox import love_equinox

first_date = datetime.datetime(2006, 5, 26)

S_birthday = datetime.datetime(1988, 6, 12)
M_birthday = datetime.datetime(1988, 8, 18)
S_Equinox = love_equinox(first_date, S_birthday)
M_Equinox = love_equinox(first_date, M_birthday)

print(S_Equinox)
print(M_Equinox)

