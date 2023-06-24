# Web Scraping Readme

This repository contains code for web scraping laptop information from Flipkart and Amazon websites, specifically targeting laptops priced under 200,000 INR.

## Prerequisites

To run the web scraping scripts, you need to have the following software and libraries installed:

- Python 3.x
- BeautifulSoup: a Python library for web scraping
- Requests: a Python library for making HTTP requests

You can install the required libraries by running the following command:

```
pip install beautifulsoup4 requests
```

## Usage

1. Clone the repository to your local machine or download the source code as a ZIP file.

2. Open a terminal or command prompt and navigate to the project directory.

3. Modify the `Flipkart_WebScraping.py` and `Amazon_web_scraping.ipynb` files according to your requirements. Specifically, you may want to adjust the target URL, search parameters, and budget constraints. Make sure to specify the correct laptop price range (200,000 INR).

4. Run the following command to execute the Flipkart scraper:

```
python Flipkart_WebScraping.py
```

The script will scrape laptop information from Flipkart and store it in a CSV file named `Flipkart_Laptop_Under_200000.csv`.

5. Run the following command to execute the Amazon scraper:

```
python Amazon_web_scraping.ipynb
```

The script will scrape laptop information from Amazon and store it in a CSV file named `Amazon_Laptop_Under_200000.csv`.

## Output

After running the web scraping scripts, you will find two CSV files in the project directory:

- `flipkart_laptops.csv`: Contains the scraped laptop information from Flipkart, including the laptop name, price, and product URL.

- `amazon_laptops.csv`: Contains the scraped laptop information from Amazon, including the laptop name, price, and product URL.

## Important Note

Web scraping may be subject to the terms of service and legal policies of the websites being scraped. Before using this code, make sure to review and comply with the terms and conditions of Flipkart and Amazon. Ensure that your web scraping activities are in compliance with ethical guidelines and the laws of your jurisdiction.

## License

The code in this repository is licensed under the [MIT License](LICENSE). Feel free to modify and distribute the code for personal or commercial purposes. However, please note that the web scraping activities you perform using this code may be subject to the terms and conditions of third-party websites.
