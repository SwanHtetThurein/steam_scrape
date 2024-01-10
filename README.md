# Simple Web Scraping using lxml and requests 

- This python script uses both lxml and requests to parse the HTML content from the "Popular New Releases" on Steam, a popular game website. 
- It uses XPath to extract the container for new releases and then titles, prices, and tags under the new releases container.
- It finally creates a list of dictionaries where each dictionary represents information about a game such as title, price, tag and platform. 
