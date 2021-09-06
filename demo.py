from bs4 import BeautifulSoup
import requests
import csv


def main(url):
    payload = {}
    headers = {'User-Agent': 'PostmanRuntime/7.28.3'}

    webpage = requests.request(
        "GET", url, headers=headers, data=payload, verify=False)

    soup = BeautifulSoup(webpage.content, "lxml")

    phone = soup.find(
        "span", attrs={"id": 'productTitle'}).string.strip().replace(',', '')
    price = soup.find(
        "span", attrs={"id": "priceblock_ourprice"}).string.strip().replace(',', '')
    stock = soup.find(
        'span', attrs={"class": "a-size-medium a-color-success"}).string.strip().replace(',', '')

    with open('amazonSmartPhone.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([phone, price, stock])


if __name__ == '__main__':
  # openning our url file to access URLs
    file = open("url.txt", "r")

    # iterating over the urls
    for links in file.readlines():
        main(links)
