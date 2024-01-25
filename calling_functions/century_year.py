def is_century_year(year):
    given_year="True /Century Year" if year%100==0 else "False/ Not Century Year"
    return(given_year)
print(is_century_year(2340))