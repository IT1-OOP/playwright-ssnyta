import os
from playwright.sync_api import sync_playwright,expect
import urllib.parse

def test_page_title():
    file_path = os.path.abspath("../index.html")
    file_path = urllib.parse.unquote(file_path)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(f"file:///{file_path}")
        nadpis_1 = page.locator('h1').first
        expect(nadpis_1).to_be_visible()
        #title = page.title()print(title)
        browser.close()