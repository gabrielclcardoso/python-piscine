import datetime

today = datetime.datetime.now()
seconds = datetime.datetime.timestamp(today) * 1000

print(
    f'''Seconds since January 1, 1970: {seconds:,.4f} or {seconds:.2e} in \
scientific notation'''
)
print(today.strftime("%b %d %Y"))
