from os import system
from re import match
from time import time, sleep 
from requests import get
from googlesearch import search
from bs4 import BeautifulSoup
import re
from flask import Blueprint, render_template, request, Flask
import json 

main = Blueprint(__name__, "views", static_folder="static", static_url_path="/static")

@main.route("/", methods=["GET"])
def home():
    print("SUCCESS")
    return render_template("index.html")


@main.route("/results", methods=["POST"])
def results():
    
    def brain(question, answer, sites, scanType):
        print("Starting.")
        timeBegin = time()
        
        answer = re.sub(r'\s+','',answer)
        global foundStat
        foundStat = False

        countDone = 0
        countSearch = 0
        recieved = 0
        global websites
        global plagSite
        websites = []
        searchSite = []
        plagSite = []

        print("Variables created.")

        # Creates a list with first n number of websites
        for site in search(question, num_results=int(sites+5), sleep_interval=0):
            websites.append(site)
        
        while len(websites) > sites:
            websites.pop()
            
        print("Websites grabbed.")

        # starts the loop

        print("Reading websites. ")
        for site in websites:
            searchSite.append(site)
            countSearch += 1
            url = site
            try:
                res = get(url)
                recieved += 1
            except:
                print()

            html_page = res.content
            soup = BeautifulSoup(html_page, 'html.parser')
            text = soup.find_all(text=True)
            output = ''
            blacklist = [
                '[document]',
                'noscript',
                'header',
                'html',
                'meta',
                'head',
                'input',
                'script',
                'style'
            ]

            for t in text:
                if t.parent.name not in blacklist:
                    output += '{} '.format(t)
            output = re.sub(r'\s+','',output)
            countDone += 1
            if answer in output:
                plagSite.append(site)
                foundStat = True

            else:
                if scanType == "checked":
                    brk_ans = list(answer)
                    lenans = len(answer)
                    s_ans = ''
                    for i in range(int(lenans / 2)):
                        s_ans += brk_ans[i]
                    if s_ans in output:
                        plagSite.append(site)
                    else:
                        continue
                else:
                    continue


        timeEnd = time()
        timeTaken = timeEnd - timeBegin

        print("\n---------- >>>> Sites Searched <<<< ----------\n")
        for webs in searchSite:
            print(webs)
        print("\n---------- >>>> Search Summary <<<< ----------\n")
        print("Query Sent:", countSearch)
        print("Response Recieved:", recieved)
        print("Success Rate:", int((recieved*100)/int(countSearch)), "%")
        print("Time Taken:", int(timeTaken),"s")
        if foundStat == True:
            print("Plagiarism Found:", foundStat)
        else:
            print("Plagiarism Found:", foundStat)
        if foundStat == True:
            print("\n---------- >>>> Plagiarism Table <<<< ----------\n")
            for s in plagSite:
                print(s)
            print("\n---------- >>>> - <<<< ----------\n")
        else:
            print("\n---------- >>>> - <<<< ----------")
            print("\nPLAGIARISM WAS NOT DETECTED. TRY INCREASING THE NUMBER OF SITES TO SEARCH.\n")
            print("---------- >>>> - <<<< ----------\n\n")
            
    def collect_data():
        quest = request.form.get("quest")
        ans = request.form.get("ans")
        google = request.form.get("google")
        bing = request.form.get("bing")
        advance = request.form.get("advance")
        nolink = request.form.get("nolink")
        # print(quest)
        # print(google)
        # print(bing)
        # print(advance)
        # print(nolink)
        option = request.form.get('engop')
        advance = request.form.get('advance')
        if advance:
            advance = True
        else:
            advance = False

        brain(quest, ans, int(nolink), advance)
     
    collect_data()
    return render_template("result.html", row=json.dumps(websites), stat=json.dumps(foundStat), plagSite=json.dumps(plagSite))

app = Flask(__name__)
app.register_blueprint(main, url_prefix="/")

if __name__ == '__main__':
    print("STARTING")
    app.run(debug=True, port=8080)
