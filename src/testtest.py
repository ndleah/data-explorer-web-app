import pandas as pd
data = pd.read_csv("reddit_vm.csv", parse_dates = True)
data["timestamp"] = pd.to_datetime(data["timestamp"], errors = "ignore")
datetime_col = data.select_dtypes(include = ["datetime64"])
datetime_col.columns = datetime_col.columns.str.replace(' ','_') # replace the column has space with '_'

today_date = pd.Timestamp.today()
timedelta_dates = [today_date - dates for dates in datetime_col.stack()]
print(timedelta_dates.type)
futureday = pd.Series(timedelta_dates)
futuredate = len([day_num for day_num in futureday.dt.days if day_num > 0])