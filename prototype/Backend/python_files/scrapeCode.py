import requests
from bs4 import BeautifulSoup
import re
from requests_html import HTMLSession
import urllib
# nltk.download('stopwords')
import string
from nltk.corpus import stopwords


def get_source(url):
    session = HTMLSession()
    response = session.get(url)
    return response


def scrape_google(query):
    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.co.uk/search?q=" + query)

    links = list(response.html.absolute_links)
    google_domains = ('https://www.google.',
                      'https://google.',
                      'https://webcache.googleusercontent.',
                      'http://webcache.googleusercontent.',
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.')

    for url in links[:]:
        if url.startswith(google_domains):
            links.remove(url)

    return links


def comment_remover(text):
    def replacer(match):
        s = match.group(0)
        if s.startswith("/") or s.startswith("#"):
            return " "
        else:
            return s

    pattern = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE,
    )
    return re.sub(pattern, replacer, text)


def scrape_code(url, language='Java'):
    flag = False
    for i in url:
        if language in i and "geeksforgeeks" in i:
            flag = True
            break
    if not flag:
        return "please try again"
    print(i)
    r = requests.get(i)
    soup = BeautifulSoup(r.content, "html.parser")

    table = soup.find("div", attrs={"class": "code-container"})
    sp = re.compile("[@$///*\;}{]")
    print("--------------------------------")
    output = ""
    if table is None:
        return "please try again"

    for row in table.findAll("code"):
        if sp.search(row.text) is None:
            output += row.text + " "
        else:
            output += row.text + "\n"

    return comment_remover(output)


def generate_code(query, language='Java'):
    url = scrape_google(query + ' program geeksforgeeks')
    print(scrape_code(url, language))


def text_process(mess):
    nopunc = [char for char in mess if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    clear_txt = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
    language = clear_txt[len(clear_txt) - 1]
    response = [language, ' '.join(clear_txt)]
    return response


inp = input()
res = text_process(inp)
generate_code(res[1], res[0])
