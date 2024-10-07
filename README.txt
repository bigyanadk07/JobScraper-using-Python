Job Listing Scraper - README

This Python script is designed to scrape job listings from various company career pages. It looks for specific keywords in job titles, filters them based on length, and allows the user to either print the results or export them to an Excel file.

### How to Use This Script:

1. **Set up Python environment:**
    Make sure you have Python 3 installed on your machine. You can download it from: https://www.python.org/downloads/

2. **Install the required libraries:**
    Before running the script, you need to install some dependencies. Run the following command in your terminal or command prompt:

        [pip install selenium beautifulsoup4 webdriver-manager pandas openpyxl]

3. **Prepare the Excel file with URLs:**
    - Create an Excel file named `company_urls.xlsx` with two columns: "Company Name" and "URL".
    - Add the company names in the first column and their respective career page URLs in the second column.

        Example:

        Company Name	URL
        Young Innovations	https://younginnovations.com.np/career
        Soani Tech	https://soanitech.com/career/


4. **Run the script:**
    Open a terminal or command prompt in the project directory and run the script:

        [python scraper_multiple.py]  


5. **Output options:**
After scraping job listings from the provided URLs, the script will ask if you'd like to export the results to an Excel file. You can type `yes` or `no`:
- `yes`: The job listings will be exported to a file called `job_listings.xlsx`.
- `no`: The job listings will be printed in the terminal instead.

### How to Modify for Your Own Job Search:

1. **Modify Keywords:**
You can change the keywords that the script looks for in job titles by editing the `keywords` list in the script. Add or remove job roles that suit your search criteria.

2. **Change Career Pages:**
If you want to scrape job listings from other companies, simply edit the `company_urls.xlsx` file and update it with the desired company names and URLs. There's no need to modify the code for this.

Happy job hunting!
