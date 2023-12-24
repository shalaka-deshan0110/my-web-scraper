from selenium import webdriver
from bs4 import BeautifulSoup
import requests


driver = webdriver.Chrome()

def get_dynamic_html(url):
    driver.get(url)
    return driver.page_source

def get_html(url):
    r = requests.get(url)
    return r.text

# https://www.kevinrooke.com/book-recommendations/elon-musk
# soup = BeautifulSoup(get_dynamic_html('https://www.blinkist.com/ap/9-books-elon-musks-reading-list-will-reinvent-life?utm_source=gsn&utm_medium=paid&utm_campaign=20341423861&utm_content=&utm_term=___c__CjwKCAiAp5qsBhAPEiwAP0qeJjt322Q2aXd638wQEu-J0x_EihvbBTToOtoBOIQyASAnDuqkWB6ynRoCwPwQAvD_BwE&gad_source=1&gclid=CjwKCAiAp5qsBhAPEiwAP0qeJjt322Q2aXd638wQEu-J0x_EihvbBTToOtoBOIQyASAnDuqkWB6ynRoCwPwQAvD_BwE'), 'html.parser')
recommender_list = ['richard-branson', 'elon-musk', 'bill-gates', 'sam-altman', 'jeff-bezos', 'keith-rabois', 'paul-graham', 'mark-zuckerberg', 'naval-ravikant', 'peter-thiel', 'mark-cuban', 'barack-obama', 'tim-ferriss', 'benjamin-franklin', 'charlie-munge',
                    'charlie-munger', 'ray-dalio', 'warren-buffett', 'steve-jobs', 'jack-dorsey', 'jeff-bezos', 'bill-gates', 'mark-zuckerberg', 'elon-musk', 'peter-thiel', 'sam-altman', 'naval-ravikant', 'keith-rabois', 'mark-cuban', 'charlie-munger', 'ray-dalio', 'benjamin-franklin', 'richard-branson', 'barack-obama', 'tim-ferriss', 'steve-jobs', 'paul-graham', 'jack-dorsey',
                    'elon-musk', 'bill-gates', 'sam-altman', 'jeff-bezos', 'keith-rabois', 'paul-graham', 'mark-zuckerberg', 'naval-ravikant', 'peter-thiel', 'mark-cuban', 'barack-obama', 'tim-ferriss', 'benjamin-franklin', 'charlie-munge']

recommender_list = list(set(recommender_list))
for man in recommender_list:
    soup = BeautifulSoup(get_dynamic_html(f'https://www.kevinrooke.com/book-recommendations/{man}'), 'html.parser')

    # p_with_em = soup.find_all('p', recursive=False, string=lambda string: string and any(child.name == 'em' for child in string.children))
    # p = soup.find_all('p')
    # for i in p:
    #     print(i.text)
        # with open('output1.txt', 'a', encoding='utf-8') as f:
        #     f.write(i.text + '\n')
    with open('books.txt', 'a', encoding='utf-8') as f:
        f.write('BOOKS RECOMMENDED BY ' + man + '\n')
        
    div_block_10 = soup.find_all('div', class_='div-block-10')
    for i in div_block_10:
        print(i.text)
        with open('books.txt', 'a', encoding='utf-8') as f:
            f.write(i.text + '\n')


driver.quit()

# with open('output2.html', 'w', encoding='utf-8') as f:
#     f.write(soup.prettify())
    
# print(soup.prettify())