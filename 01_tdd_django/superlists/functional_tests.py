from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


browser = webdriver.Chrome()
browser.get('http://127.0.0.1:8000/')


assert 'The' in browser.title
print('completed successfully')