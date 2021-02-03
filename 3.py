import json
import urllib.request
import datetime

start = str(datetime.datetime.now()).split("-")[0:2]
start = "-".join(start)  # create string of current month and year
days = [start + "-0" + str(i) for i in range(1, 10)]  # get the appropriate from of days from 1 to 9
days = days + [start + "-" + str(i) for i in range(10, 32)]  # from days of 10 to 31

print("Wait while we are processing the data...")
winning_numbers = []

for day in days:
    try:
        url = f"https://api.opap.gr/draws/v3.0/1100/draw-date/{day}/{day}/draw-id"  # get the id draws

        opap_draws = urllib.request.urlopen(url)  # open the draws url
        html = opap_draws.read()
        html = html.decode()
        first_draw = json.loads(html, strict=False)[0]  # from the list of draws get the first one
        # print(first_draw)

        url2 = f"https://api.opap.gr/draws/v3.0/1100/{first_draw}"  # get the results of the first draw

        r = urllib.request.urlopen(url2)
        html = r.read()
        html = html.decode()
        data = json.loads(html, strict=False)
        print(sorted(data["winningNumbers"]["list"]), day)
        winning_numbers += sorted(data["winningNumbers"]["list"])
    except:
        break

print(winning_numbers)

for i in range(1, 81):
    count = winning_numbers.count(i)
    print(f"The number {i} appears {count} times")




