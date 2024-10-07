Job Listing Scraper
This Python-based job scraper allows you to easily find job listings from various company career pages based on specific keywords. It scrapes job titles from career pages, filters them based on relevance, and provides the option to either export the results to an Excel file or display them in the terminal.

Features:
Scrape Job Listings: Automatically scrape job listings from company career pages.
Filter by Keywords: Looks for specific job roles like "Frontend", "Backend", "Full Stack", "Software Engineer", etc.
Export to Excel: Gives an option to export job listings to an Excel file.
Easy Customization: You can modify the list of companies and URLs directly through an Excel sheet.  

How to Use:  
  
1. Clone the repository:
git clone https://github.com/yourusername/job-listing-scraper.git
cd job-listing-scraper
2. Install required libraries:
Make sure you have Python installed. Then, install the required libraries by running:
  
The required libraries include:  

  selenium  
  webdriver-manager  
  beautifulsoup4  
  pandas    
  openpyxl    

3. Prepare the Excel sheet:  
Open the company_urls.xlsx file.  
Add or modify company names and URLs in the sheet under the Company Name and URL columns.  
Save the file.
  
4. Run the Scraper:  
To run the scraper, execute the following command in your terminal:  

**python job_scraper.py**  

5. Export Options:
Once the scraper finishes, it will ask if you want to export the job listings to an Excel file.
If you choose yes, the job listings will be saved to job_listings.xlsx.
If you choose no, the job listings will be displayed in the terminal.  

6. Viewing Results:
If exported to Excel, you can open job_listings.xlsx to view the scraped job listings, including job titles and the corresponding company URLs.
If outputted to the terminal, you will see the list of job titles printed in the console.

Notes:
Make sure you keep the browser window that opens during the scraping process active. The scraper will automatically close the browser once the process is finished.
You can modify the keywords used for filtering job titles by editing the keywords list in the job_scraper.py file.
