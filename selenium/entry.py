from selenium import webdriver
import time
import pandas as pd
import numpy as np

article_list = []
author_list = []
view_list = []
like_list = []
date_list = []

def article_scraping():
    driver = webdriver.Chrome('/Users/jypsnewmac/PycharmProjects/untitled8/chromedriver')
    for i in range(1, 50):
        driver.get("https://playentry.org/ds#!/free?sort=created&rows=1000&page=" + str(i))
        time.sleep(5)

        articles = driver.find_elements_by_xpath("/html/body/section/section/section/div[2]/div/table/tbody/tr/td[2]/div")
        for article in articles:
            article_list.append(article.text)

        authors = driver.find_elements_by_xpath("/html/body/section/section/section/div[2]/div/table/tbody/tr/td[3]")
        for author in authors:
            author_list.append(author.text)

        views = driver.find_elements_by_xpath("/html/body/section/section/section/div[2]/div/table/tbody/tr/td[5]")
        for view in views:
            view_list.append(view.text)

        likes = driver.find_elements_by_xpath("/html/body/section/section/section/div[2]/div/table/tbody/tr/td[5]")
        for like in likes:
            like_list.append(like.text)

        dates = driver.find_elements_by_xpath("/html/body/section/section/section/div[2]/div/table/tbody/tr/td[4]")
        for date in dates:
            date_list.append(date.text)

    driver.quit()


article_scraping()

data = {"title": article_list, "author": author_list, "dates": date_list, "views": view_list, "likes": like_list}
df = pd.DataFrame(data)
print(df)
df.to_excel('results.xlsx', sheet_name='results', encoding='euc-kr')
