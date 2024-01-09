from playwright.sync_api import sync_playwright
from time import sleep

def main(playwright):
	browser = playwright.chromium.launch(headless=True)
	context = browser.new_context()
	page = context.new_page()
	page.goto("https://www.baidu.com")
	sleep(120)
	page.close()
	context.close()
	browser.close()


with sync_playwright() as playwright:
	main(playwright)