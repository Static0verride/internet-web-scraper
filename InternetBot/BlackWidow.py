import requests
import os
import sys
import urllib
from urllib import request
from urllib import error
from bs4 import BeautifulSoup
from requests_ntlm import HttpNtlmAuth


class BlackWidow:

    def __init__(self, my_link, my_header=None, my_password=None, my_user=None,
                 my_domain=None, my_path=None):

        self.html_list = list()
        self.header = my_header
        self.link = my_link
        self.html_list.append(my_link)
        self.constraint = BlackWidow.__find_base(self)
        self.password = my_password     # Todo if domain is different imp changes
        self.username = my_user         # user name and password follow abv cmt
        self.domain = my_domain
        self.file_path = my_path

    def __find_base(self):
        """         Finds the base of a initial link
        Example. https://www.google.com/webhp? will return https://www.google.com
        """

        random_link = self.link
        base = ""

        for i in range(0, len(random_link)):
            base += random_link[i]
            if len(base) > 1:
                if random_link[i] == '/' and (random_link[i - 1] is not ':'
                                              and random_link[i - 1] is not '/'):
                    return base

    def __download(self, download_path, link):
        """ Grabs the link of the file of interest and downloads it
        to its appropriate file path
        """
        # doc_name = BlackWidow.reverse_special_char(os.path.basename(link))
        # print("\n[*] Downloading %s" % doc_name)

        # current = BlackWidow.__authentic_request(link)
        # doc_name = BlackWidow.reverse_special_char(os.path.basename(link))

        # f = open(download_path + doc_name, "wb")
        # f.write(current.content)
        # f.close()

    def __obtain_request(self, link):
        my_domain = self.domain
        usr = self.username
        pwd = self.password

        if self.username is not None or self.password is not None:   # will authenticate user
            try:
                result = requests.get(link, auth=HttpNtlmAuth(my_domain + "\\" + usr, pwd))
                return result
            except urllib.error.URLError:
                print("Website Does not exist or No connection to internet")
        try:
            if self.header is not None:
                req = urllib.request.Request(link, headers=self.header)
            else:
                req = urllib.request.Request(link)
            return req

        except urllib.error.URLError:
            print("Website Does not exist or No connection to internet")

    @staticmethod
    def reverse_special_char(link):
        """ Links sometimes contain special characters, here we replace
        there substituted value with the real thing and returns changes
        """
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

        my_link = self.html_list.pop()
        my_request = self.__obtain_request(my_link)
        html = urllib.request.urlopen(my_request)
        soup = BeautifulSoup(html, "html.parser")
        print(soup)
