# scraping code
# a function that takes website url and return all the content from that website
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4  import BeautifulSoup

def scrape_website(website):
    print("Launching chrome...")

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # optional: run in background
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")  # hide automation
    # this above two lines of code help selenium to behave like chrome browsers
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


    try:
        driver.get(website)
        print("page loaded")
        time.sleep(5)
        html = driver.page_source
        return html
    
    finally:
        driver.quit()

#taking the body content 
def extract_body_content(html_content):
    soup = BeautifulSoup(html_content,'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    else:
        return ""
    
#cleaning the body content
def clean_body_content(body_content):
    soup = BeautifulSoup(body_content,'html.parser')
    for script_or_style in soup(['script','style']):
        script_or_style.extract()                                   #basically if it finds any scripts or style in the content it is going to extract it

    cleaned_content = soup.get_text(separator='\n')
    #below code basically says that if there is no content is between the \n so it is just going to remove it that are not separating any texts so splitting will just remove that
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content

#now it is time to separete the data in batches because any llm has the limit of 8000 charecters 
def split_dom_content(dom_content,max_length=6000):
    chunks = []
    for i in range (0,len(dom_content),max_length):
        chunks.append(dom_content[i:i+max_length])                           # in this we are basically slicing dom content into 6000 words chunks
    return chunks









































# import time
# import random
# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from fake_useragent import UserAgent
# import os
# import webbrowser

# # ----- PROXY LIST (Free, rotates randomly) -----
# PROXIES = [
#     "103.173.228.148:8080",
#     "46.4.96.137:8080",
#     "194.233.73.106:443"
# ]

# # ----- USER AGENT SPOOFING -----
# ua = UserAgent()
# user_agent = ua.random

# # ----- SELENIUM CONFIG -----
# options = Options()
# options.add_argument("--headless=new")  # Headless mode
# options.add_argument(f"user-agent={user_agent}")
# options.add_argument("--disable-blink-features=AutomationControlled")

# # Random proxy
# proxy = random.choice(PROXIES)
# options.add_argument(f'--proxy-server=http://{proxy}')

# # ChromeDriver path
# # chrome_driver_path = "./chromedriver.exe"
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # ----- SCRAPE FUNCTION -----
# def scrape_website(url):
#     print(f"[INFO] Loading page: {url}")
#     driver.get(url)
#     time.sleep(5)  # Wait for JS to load fully

#     html = driver.page_source
#     soup = BeautifulSoup(html, "html.parser")

#     # ----- Extract Images -----
#     images = [img.get("src") for img in soup.find_all("img") if img.get("src")]

#     # ----- Extract Text -----
#     texts = [t.get_text(strip=True) for t in soup.find_all() if t.get_text(strip=True)]

#     # ----- Extract Links -----
#     links = [a.get("href") for a in soup.find_all("a", href=True)]

#     return {
#         "images": images,
#         "texts": texts,
#         "links": links
#     }



# # ----- RUN -----
# if __name__ == "__main__":
#     website_url = input("Enter the website URL to scrape: ").strip()
#     data = scrape_website(website_url)

#     print(f"\n[INFO] Found {len(data['images'])} images")
#     for img in data["images"][:10]:  # Show first 10
#         print("IMG:", img)

#     print(f"\n[INFO] Found {len(data['links'])} links")
#     for link in data["links"][:10]:
#         print("LINK:", link)

#     print(f"\n[INFO] Found {len(data['texts'])} text blocks")
#     for text in data["texts"][:10]:
#         print("TEXT:", text)

#     driver.quit()

# # def extract_body_content(html_content):
# #     pass

# # for img in data["images"][:5]:  # Show first 5
# #     webbrowser.open(img)