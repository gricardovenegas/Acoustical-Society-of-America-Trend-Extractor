# By: Volker Strobel, improved by Patrick Hofmann, modified by Gabriel R. Venegas for ASA
from bs4 import BeautifulSoup
from urllib.request import Request, build_opener, HTTPCookieProcessor
from urllib.parse import urlencode
from http.cookiejar import MozillaCookieJar
import re, time, sys, urllib
import requests
from lxml import html

def get_num_results(search_term, start_date, end_date):
    """
    Helper method, sends HTTP request and returns response payload.
    """

    # Open website and read html
    query_params = { 'text1' : search_term, 'AfterYear' : start_date, 'BeforeYear' : end_date}
    url = "https://asa.scitation.org/action/doSearch?field1=AllField&" + urllib.parse.urlencode(query_params)
    pageContent = requests.get(url)
    tree = html.fromstring(pageContent.content)
    
    # extracts the number of search results using the xpath
    total_hits_xpath = '//*[@id="pb-page-content"]/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/span[3]/text()'
    total_hits_object = tree.xpath(total_hits_xpath)
   

    if total_hits_object != None:

        res = str(total_hits_object)
         
        if res == '[]':
            num_results = '0'
            success = True
        else:
            num_results = res.split("of ",1)[1][0:-2] # convert string to numbe
            success = True

    else:
        success = False
        num_results = 0

    return num_results, success

def get_range(search_term, start_date, end_date):

    fp = open("out.csv", 'w')
    fp.write("year,results\n")
    print("year,results")

    for date in range(start_date, end_date + 1):

        num_results, success = get_num_results(search_term, date, date)
        if not(success):
            print("It seems that you made to many requests to Google Scholar. Please wait a couple of hours and try again.")
            break
        year_results = "{0},{1}".format(date, num_results)
        print(year_results)
        fp.write(year_results + '\n')
        time.sleep(0.1)

    fp.close()

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("******")
        print("Academic word relevance")
        print("******")
        print("")
        print("Usage: python extract_occurences_JASA.py '<search term>' <start date> <end date>")
        print("")
        print('If you want to search for terms in quotations, connect terms with +')
        print('For example: "climate change" should be entered as climate+change')
        
    else:
        # if a '+' is found within search terms, encompass with ""
        if sys.argv[1].find('+') == -1:
            search_term = sys.argv[1]
        else:
            search_term = '"' + sys.argv[1] + '"'
            
        start_date = int(sys.argv[2])
        end_date = int(sys.argv[3])
        test = get_range(search_term, start_date, end_date)
