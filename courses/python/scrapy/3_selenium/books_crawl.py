from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def crawl_books():
	"""
	Crawl all links in https://books.toscrape.com/index.html
	"""
	START_URL = "https://books.toscrape.com/index.html"

	# List of urls to parse
	parse_urls = []

	# WebDriver options
	options = webdriver.ChromeOptions()
	options.add_argument('headless')
	desired_capabilities = options.to_capabilities();

	driver = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=desired_capabilities)
	driver.get(START_URL)

	try:
		links = driver.find_elements_by_xpath("//div[@class='image_container']/a")

		# Get attributes for each tag
		for link in links:
			hyperlink = link.get_attribute("href")
			parse_urls.append(hyperlink)

	except NoSuchElementException:
		print("Error: Elements selected are not found")
		pass

	# Print all hyperlinks
	print(parse_urls)

	driver.quit()


if __name__ == "__main__":
	# Start Crawler
	crawl_books()


