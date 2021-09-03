from prototype.Backend.python_files import scrapeCode
# nltk.download('stopwords')
import string
from nltk.corpus import stopwords


def text_process(mess):
    nopunc = [char for char in mess if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    clear_txt = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
    return ' '.join(clear_txt)


inp = input()
res = text_process(inp)
scrapeCode.generate_code(inp)
# print(res)
