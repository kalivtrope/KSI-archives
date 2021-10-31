from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://ksi.fi.muni.cz")


def save_problem(num):
    driver.get(f"https://ksi.fi.muni.cz/ulohy/{num}")
    time.sleep(1)
    with open(f'../data/problems/problem_{num}.html', 'w') as f:
        f.write(driver.page_source)


def save_solution(num):
    driver.get(f"https://ksi.fi.muni.cz/ulohy/{num}/reseni")
    time.sleep(2)
    with open(f'../data/solutions/solution_{num}.html', 'w') as f:
        f.write(driver.page_source)


def exec(first, last):
    for i in range(first, last + 1):
        save_problem(i)
        save_solution(i)
