import requests
import os
import urllib
from urllib import request
from urllib import error
from bs4 import BeautifulSoup
from requests_ntlm import HttpNtlmAuth


class BlackWidow:

    def __init__(self, my_link, my_password=None, my_user=None,
                 my_domain=None, my_path=None):

        self.link = my_link
        self.constraint = BlackWidow.find_base(my_link)
        self.password = my_password
        self.username = my_user
        self.domain = my_domain
        self.file_path = my_path

    def find_base(self):
        """ Finds the base of a link
        Example. https://www.google.com/webhp?
        will return https://www.google.com
        """

        random_link = self.link
        base = ""
        for i in range(0, len(random_link)):
            base += random_link[i]
            if len(base) > 1:
                if random_link[i] == '/' and (random_link[i - 1] is not ':'
                                              and random_link[i - 1] is not '/'):
                    return base

    def download(self, download_path, link):
        doc_name = BlackWidow.reverse_special_char(os.path.basename(link))
        print("\n[*] Downloading %s" % doc_name)

        current = BlackWidow.authentic_request(link)
        doc_name = BlackWidow.reverse_special_char(os.path.basename(link))

        f = open(download_path + doc_name, "wb")
        f.write(current.content)
        f.close()

    def authentic_user(self, link):
        my_domain = self.domain
        usr = self.username
        pwd = self.password

        try:
            result = requests.get(link, auth=HttpNtlmAuth(my_domain + "\\" + usr, pwd))
            soup = BeautifulSoup(result.content, "html.parser")
            return soup
        except:
            pass

        try:
            req = urllib.request.Request(link)
            html = urllib.request.urlopen(req)
            soup = BeautifulSoup(html, "html.parser")
            return soup

        except urllib.error.URLError:
            print("Website Does not exist or No connection to internet")
        except:
            print("Found my error")
            return None

    @staticmethod
    def reverse_special_char(link):
        temp = link

        if temp.__contains__('%20'):
            temp = temp.replace("%20", ' ')
        if temp.__contains__('%28'):
            temp = temp.replace('%28', '(')
        if temp.__contains__('%29'):
            temp = temp.replace('%29', ')')
        if temp.__contains__('%7B'):
            temp = temp.replace('%7B', '{')
        if temp.__contains__('%7D'):
            temp = temp.replace('%7D', '}')

        return temp

    def go_spider_go(self):
        print(self.link)
