"""
If the soup = BeautifulSoup(page_source, "html.parser") line is giving you an empty list,
it suggests that the desired content is likely loaded dynamically through JavaScript.
In this case, you would need to use a tool like Selenium,
which can execute the JavaScript code and retrieve the fully rendered HTML. So, we are not using requests module,

"""

from selenium import webdriver
from bs4 import BeautifulSoup

# Configure Selenium to use a web driver
driver = webdriver.Chrome()  # You'll need to have Chrome and Chromedriver installed

# Load the webpage using Selenium
url = "https://www.empireonline.com/movies/features/best-movies-2/"
driver.get(url)

# Get the page source after dynamic content is loaded
page_source = driver.page_source

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(page_source, "html.parser")

# Find all <h3> elements
h3_elements = soup.find_all("h3")
movies = []
# Print the text content of each <h3> element
for element in h3_elements:
    movies.append(element.text)
print(*movies[::-1], sep="\n")
# Close the browser
driver.quit()

