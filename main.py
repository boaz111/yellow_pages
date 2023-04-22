import requests
from bs4 import BeautifulSoup

def scrape_yellow_pages(num_pages_to_scrape):
    base_url = "https://www.yellowpages.com"
    search_url = "/search?search_terms=physiotherapist&geo_location_terms=United+States&page="
    physiotherapists = []

    for page_num in range(1, num_pages_to_scrape + 1):
        url = base_url + search_url + str(page_num)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        for result in soup.find_all('div', class_='result'):
            try:
                name = result.find('a', class_='business-name').text.strip()
                phone = result.find('div', class_='phones phone primary').text.strip()
                location = result.find('div', class_='adr').text.strip()
                business_name = result.find('span', itemprop='name').text.strip() if result.find('span', itemprop='name') else "Not available"
                website_tag = result.find('a', class_='track-visit-website')
                website = website_tag['href'] if website_tag else "Not available"
                physiotherapists.append({'name': name, 'phone': phone, 'location': location, 'business_name': business_name, 'website': website})
            except AttributeError:
                continue

    return physiotherapists

def save_to_text_file(physiotherapists, file_name):
    with open(file_name, 'w') as f:
        for i, physiotherapist in enumerate(physiotherapists, start=1):
            f.write(f"{i}. Name: {physiotherapist['name']}, Phone: {physiotherapist['phone']}, Location: {physiotherapist['location']}, Business Name: {physiotherapist['business_name']}, Website: {physiotherapist['website']}\n")

if __name__ == "__main__":
    num_pages_to_scrape = 100 # Set the number of pages you want to scrape
    physiotherapists = scrape_yellow_pages(num_pages_to_scrape)

    file_name = "list.txt"  # Set the desired output file name
    save_to_text_file(physiotherapists, file_name)
    print(f"Data saved to {file_name}")
