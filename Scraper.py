#################################
#
#  This is written to scrape a lot of NCAA basketball data off sports-reference.com
#
#  This code written by Chase Haymond on 3/16/2021
################################

from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime

today = datetime.datetime.now()
searchDate = datetime.datetime(2020, 11, 1)

while searchDate < today:
    month = searchDate.month
    day = searchDate.day
    year = searchDate.year

    url = "https://www.sports-reference.com/cbb/boxscores/index.cgi?month={month}&day={day}&year={year}".format(
        month=month,
        day=day,
        year=year)
    print("\n\n***** date: {month}/{day}/{year} *****".format(month=month, day=day, year=year))
    # print(url)

    page = urlopen(url)  # Opens the URL
    html = page.read().decode("utf-8")  # Reads the HTML from the page as a string
    soup = BeautifulSoup(html, "html.parser")  # Creates a BeautifulSoup object

    results = soup.find_all("div", {"class": "game_summary"})

    for result in results:
        allTeams = result.find_all_next("tr")
        homeTeam = allTeams[0].find("a").string
        homeTeamWinOrLose = allTeams[0].get("class")[0]
        if allTeams[0].find("span", {"class": "pollrank"}):
            homeTeamRank = allTeams[0].find("span", {"class": "pollrank"}).text
        else:
            homeTeamRank = ''

        awayTeam = allTeams[1].find("a").string
        awayTeamWinOrLose = allTeams[1].get("class")[0]
        if allTeams[1].find("span", {"class": "pollrank"}):
            awayTeamRank = allTeams[1].find("span", {"class": "pollrank"}).text
        else:
            awayTeamRank = ''

        print("\nhome: " + homeTeam + homeTeamRank + "(" + homeTeamWinOrLose.replace(" ", "") + ")" + "\nAway: " + awayTeam
              + awayTeamRank + " (" + awayTeamWinOrLose + ") ")

    searchDate = searchDate + datetime.timedelta(days=1)
