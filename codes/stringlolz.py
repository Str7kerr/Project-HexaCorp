def prepend(list, str):
    # Using format()
    str += '{0}'
    list = [str.format(i) for i in list]
    return(list)

urls = ["ShowTeam.aspx?tid=22","ShowTeam.aspx?tid=40"]
str = "http://millenniumcricketleague.com/Home/"

for i in urls:
    i = str+i
    print(i)