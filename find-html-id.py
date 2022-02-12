
import argparse
from ast import parse
import requests
from html.parser import HTMLParser
from bs4 import BeautifulSoup


def GetResponseCode(target):
    return str(requests.get(target)).split('[')[1].replace(']>', '')


def GetWebsiteSource(url):
    return requests.get(url).text


def ParseWebsite(target, id):
    return BeautifulSoup(target, 'html.parser').find(id=id)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-u', '--url', help="Enter the URL in a complete format, for example 'https://contoso.com' ")
    parser.add_argument(
        '-i', '--id', help="Enter the HTML ID that you want to search. I recommend passing in quotes to prevent the need to esapce characters.")
    # parser.add_argument(
    #     '-v', '--verbose', help="Use this option to get results for both success and failure.")

args = parser.parse_args()


if (ParseWebsite(GetWebsiteSource(args.url), args.id)) != None:
    print("The HTML Id " + args.id + " was found at " + args.url)
