import pandas as pd
from datetime import datetime as dt
from modules.email import email_chuff

now = dt(day=dt.now().day, month=dt.now().month, year=dt.now().year)
future = dt(day=17, month=9, year=2024)
countdown = future - now
w = divmod(countdown.days, 7)[0]
d = divmod(countdown.days, 7)[1]

if w > 1:
    if d != 1:
        message = (f'Just {w} weeks and {d} days to your holiday!')
    else:
        message = (f'Just {w} weeks and {d} day to your holiday!')
elif w == 1:
    if d != 1:
        message = (f'Just {w} week and {d} days to your holiday!')
    else:
        message = (f'Just {w} week and {d} day to your holiday!')
else:
    if d != 1:
        message = (f'Just {d} days to your holiday!')
    else:
        message = (f'Just {d} day to your holiday!')

email_chuff(
    ["simon@muddypaws.net", "alison@muddypaws.net"],
    message
)