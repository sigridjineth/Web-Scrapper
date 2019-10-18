from selenium import webdriver
import time
import pandas as pd

title_list = []
author_list = []
view_list = []
like_list = []
comment_list = []


def article_scrapping():
    driver = webdriver.Chrome('/Users/jypsnewmac/PycharmProjects/untitled8/chromedriver')

    for i in range(1, 999):
        driver.get("about:blank")
        driver.get("https://playentry.org/all#!/?sort=updated&rows=12&page="+str(i))
        time.sleep(10)

        titles = driver.find_elements_by_xpath("/html/body/section/section/section/section/div[3]/div/div/div[2]/div[1]/div[1]")
        for title in titles:
            title_list.append(title.text)

        authors = driver.find_elements_by_xpath("/html/body/section/section/section/section/div[3]/div/div/div[2]/div[1]/div[2]/span/a")
        for author in authors:
            author_list.append(author.text)

        views = driver.find_elements_by_xpath("/html/body/section/section/section/section/div[3]/div/div/div[1]/div/div/span[1]")
        for view in views:
            view_list.append(view.text)

        likes = driver.find_elements_by_xpath("/html/body/section/section/section/section/div[3]/div/div/div[1]/div/div/span[2]")
        for like in likes:
            like_list.append(like.text)

        comments = driver.find_elements_by_xpath("/html/body/section/section/section/section/div[3]/div/div/div[1]/div/div/span[3]")
        for comment in comments:
            comment_list.append(comment.text)

    driver.quit()


if __name__ == "__main__":
    article_scrapping()

    data = {"title": title_list, "author": author_list, "views": view_list, "comment": comment_list, "likes": like_list}
    df = pd.DataFrame(data)
    df.to_excel('results_works.xlsx', sheet_name='results', encoding='euc-kr')