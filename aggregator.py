from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

def scrape_the_verge_titles():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    url = 'https://www.theverge.com'
    driver.get(url)

    articles = driver.find_elements(By.CSS_SELECTOR, 'div.c-entry-box--compact__body')

    titles = []
    for article in articles:
        title_element = article.find_element(By.CSS_SELECTOR, 'h2.c-entry-box--compact__title')
        date_element = article.find_element(By.CSS_SELECTOR, 'time.c-byline__item')
        link_element = title_element.find_element(By.TAG_NAME, 'a')
        
        title = title_element.text
        date = datetime.strptime(date_element.get_attribute('datetime').split('T')[0], '%Y-%m-%d')
        link = link_element.get_attribute('href')
        
        if date >= datetime(2022, 1, 1):
            titles.append((title, link, date))
    
    driver.quit()

    # Sort titles anti-chronologically (latest first)
    titles.sort(key=lambda x: x[2], reverse=True)
    
    return titles

if __name__ == "__main__":
    titles = scrape_the_verge_titles()
    print("Scraped Titles:")
    for idx, (title, link, date) in enumerate(titles, start=1):
        print(f"{idx}. {title} ({date.strftime('%Y-%m-%d')}) - {link}")
