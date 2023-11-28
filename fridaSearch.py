import requests
from bs4 import BeautifulSoup
from colorama import Fore
import argparse

parser = argparse.ArgumentParser(description='Frida CodeShare Search')
parser.add_argument('-s', '--Search',type=str, help='Search word')
parser.add_argument('-a','-all', help='All frida codes')
args = parser.parse_args()


def logo():
    print(Fore.LIGHTRED_EX + """
                                                                  
█████████      ██████████     ███     ██████████         ████     
 █            ██      ██▓     ███     ██▒     ████      ███ ██    
 ██           ██      ██▓     ███     ███       ██     ▓██  ███   
 ████████      █████████▓     ███     ███       ██     ██    ██▒  
 █▒             ██▒   ██▓     ███     ██▒     ░███    ██████████  
███           ███░    ███     ███     ██████████     ██        ██ """ + Fore.WHITE + """ 

                   Frida CodeShare Search                         """ + Fore.LIGHTBLACK_EX + """ 
                                                      by phr4nt0m """ + Fore.RESET )

def all_articles():
    article_dic = list()
    for page in range(1,23): #23
        url = "https://codeshare.frida.re/browse?page=" + str(page)

        r = requests.get(url)   
        html = BeautifulSoup(r.text,'html.parser')
        articles_html = html.find_all('article')

        for article in articles_html:
            article_list = list()
            article_list.append(article.a.text.lower()) # Title
            article_list.append(article.h3.text.replace(" ","").replace("\n","")) # likes
            article_list.append(article.p.text.lower())   # Description
            article_list.append(article.a['href']) # Link
            article_dic.append(article_list) 
    return article_dic

def search_word(word_search):
    article_dic = all_articles()
    list_found= list()
    
    for item in article_dic:
        if word_search in item[0] or word_search in item[2]:
            list_found.append(item)

    return list_found


def print_dict(list_found):
    if (len(list_found)>0):
        for art in list_found:
            print(Fore.CYAN + "Name:      " + Fore.GREEN + art[0]+ Fore.RESET)
            print("Likes:       " + Fore.RED + art[1]+ Fore.RESET)
            print("Description: " + Fore.LIGHTBLACK_EX + art[2] + Fore.RESET)
            print("Url:         " + Fore.LIGHTBLUE_EX + art[3] + Fore.RESET )
            url = art[3]
            print("Code Run:    " + Fore.LIGHTMAGENTA_EX + "frida -U --codeshare " + url[url.rfind("@")+1:-1] +" -f YOUR_BINARY\n" + Fore.RESET)
    else:
        print(Fore.RED + " No Match Found !! ")


if (args.Search != "" ):
    logo()
    print_dict(search_word(args.Search))


