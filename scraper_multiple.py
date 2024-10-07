from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import re
import time
import pandas as pd

# Define the keywords to look for in job listings
keywords = [
    "Front End", "Back End", "Full Stack",
    "React", "Node", "MongoDB", "Web Developer", 
    "UI/UX", "Developer", 
    "Java", ".NET", "PHP", "Laravel", 
    "MERN", "Software Engineer", "Internship"
]

# Define a blacklist of non-job title phrases
blacklist_phrases = [
    "Delicious daily meals", "Grow your professional network", 
    "Life at", "Join our team", "Come work with us", "Learn more about"
]

# Load the URLs and company names from an Excel file
excel_file = 'company_info.xlsx'  # Replace with the path to your Excel file
data = pd.read_excel(excel_file)

# Extract the URLs and company names from the DataFrame
urls = data['URL'].tolist()
company_names = data['Company Name'].tolist()

# Initialize the WebDriver for Google Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    all_job_listings = set()  # Use a set to avoid duplicates

    # Compile a regex pattern to match valid job titles
    keyword_pattern = re.compile(r'\b(?:' + '|'.join(keywords) + r')\b', re.IGNORECASE)

    # Iterate over each URL
    for i, url in enumerate(urls):
        company = company_names[i]  # Get the company name corresponding to the URL
        print(f"Scraping: {company} ({url})")
        driver.get(url)

        # Wait for the page to load
        time.sleep(5)

        # Get page source after it has fully loaded
        page_source = driver.page_source

        # Use BeautifulSoup to parse the page source
        soup = BeautifulSoup(page_source, 'html.parser')

        # Find relevant tags for job titles
        relevant_tags = ['h1', 'h2', 'h3', 'li']  # Add more tags as needed
        for tag in relevant_tags:
            for element in soup.find_all(tag):
                job_title = element.get_text(separator=" ", strip=True)

                # Check if the job title contains any of the keywords and is not in the blacklist
                if (keyword_pattern.search(job_title) and
                    not any(phrase in job_title for phrase in blacklist_phrases) and
                    len(job_title) > 10 and len(job_title) <= 30):  # Set min/max length for job titles
                    all_job_listings.add((job_title.strip(), company))  # Add to set to avoid duplicates

finally:
    # Close the WebDriver before prompting the user
    driver.quit()

# After scraping, display the number of job listings found
print(f"\n\nFound {len(all_job_listings)} job listings.")

# Ask the user if they want to export to an Excel file
export = input("\nDo you want to export the job listings to an Excel file? (yes/no): ").strip().lower()

if export in ['yes', 'y']:
    # Prepare the data for export
    df = pd.DataFrame(list(all_job_listings), columns=["Job Title", "Company Name"])
    # Export to Excel
    df.to_excel("job_listings.xlsx", index=False)
    print("\nJob listings exported to 'job_listings.xlsx'.")
else:
    # If the user chooses not to export, print the job listings in the console
    print("\nJob listings:")
    for title, company in all_job_listings:
        print(f"\nJob Title: {title}\nCompany: {company}")
