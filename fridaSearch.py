
import requests
from bs4 import BeautifulSoup
from colorama import Fore
import argparse
import json

parser = argparse.ArgumentParser(description='Frida CodeShare Search')
parser.add_argument('-s', '--search', type=str, help='Search word')
parser.add_argument('-a', '--all', action='store_true', help='All frida codes')
parser.add_argument('-o', '--output', type=str, help='Output file in JSON format')
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
    article_list = []

    for page in range(1, 23):  # 23
        url = f"https://codeshare.frida.re/browse?page={page}"
        r = requests.get(url)
        html = BeautifulSoup(r.text, 'html.parser')
        articles_html = html.find_all('article')

        for article in articles_html:
            title = article.a.text.lower()
            likes = article.h3.text.replace(" ", "").replace("\n", "")
            description = article.p.text.lower()
            link = article.a['href']
            article_list.append({"Name": title, "Likes": likes, "Description": description, "Url": link})

    return article_list


def search_word(word_search):
    article_list = all_articles()
    list_found = [item for item in article_list if word_search in item["Name"] or word_search in item["Description"]]
    return list_found


def print_dict(list_found):
    if list_found:
        for art in list_found:
            print(Fore.CYAN + f"Name:      {Fore.GREEN}{art['Name']}{Fore.RESET}")
            print(f"Likes:       {Fore.RED}{art['Likes']}{Fore.RESET}")
            print(f"Description: {Fore.LIGHTBLACK_EX}{art['Description']}{Fore.RESET}")
            print(f"Url:         {Fore.LIGHTBLUE_EX}{art['Url']}{Fore.RESET}")
            url = art['Url']
            print(f"Code Run:    {Fore.LIGHTMAGENTA_EX}frida -U --codeshare {url[url.rfind('@')+1:-1]} -f YOUR_BINARY{Fore.RESET}\n")
    else:
        print(Fore.RED + " No Match Found !! ")


def save_to_json(data, output_file):
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=2)


if args.search:
    logo()
    result = search_word(args.search)
    print_dict(result)
    if args.output:
        save_to_json(result, args.output)
elif args.all:
    logo()
    result = all_articles()
    print_dict(result)
    if args.output:
        save_to_json(result, args.output)
else:
    logo()
    parser.print_help()

