from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Define the keywords to look for in job listings
keywords = [
    "Front End", "Front-End", "Back End", "Back-End", "Full Stack", "Full-Stack",
    "React", "ReactJS", "Node", "NodeJS", "MongoDB", "Web Developer", 
    "Web Designer", "UI/UX", "UI/UX Designer", "QA Engineer", "QA"
]

# Ask for the website link to scrape
website_link = input("Enter the website link you want to scrape job listings from (e.g., https://example.com/careers): ")

# Initialize the WebDriver for Google Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Open the careers page of the target website
    driver.get(website_link)
    
    # Wait for the page to load
    time.sleep(5)

    # Get page source after it has fully loaded
    page_source = driver.page_source

    # Use BeautifulSoup to parse the page source
    soup = BeautifulSoup(page_source, 'html.parser')

    # Create a list to hold job postings
    job_listings = []

    # Search for keywords in the text
    for keyword in keywords:
        # Find all elements that contain the keyword
        for element in soup(text=lambda text: text and keyword.lower() in text.lower()):
            # Get the parent element that contains this text
            parent = element.find_parent()
            job_title = element.strip()  # The text of the job title
            
            # If a parent tag is found, attempt to extract additional information
            if parent:
                job_info = parent.get_text(separator="\n").strip()
                job_listings.append((job_title, job_info))

    # Check if any job listings were found
    if not job_listings:
        print("No job listings found with the specified keywords.")
    else:
        print(f"Found {len(job_listings)} job listings:")
        for title, info in job_listings:
            print(f"Job Title: {title}\nInfo: {info}\n")

finally:
    # Close the WebDriver
    driver.quit()
