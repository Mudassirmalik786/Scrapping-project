import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
import os

def scrape_page_data(url, soup):
    all_data = []
    car_divs = soup.select(".col-md-9.grid-style .col-md-12.grid-date")
    for div in car_divs:
        vehicle_name = div.find_previous("h3").get_text(strip=True)
        vehicle_city = div.select_one(".search-vehicle-info").get_text(strip=True)
        info = div.select_one(".search-vehicle-info-2")
        if info:
            info = [item.get_text(strip=True) for item in info.find_all("li")]
            # Handle missing "Grade" by inserting a default value because some cars don't contain grade on the website
            if len(info) < 6:
                info.insert(5, "N/A")
            all_data.append([vehicle_name, vehicle_city, *info])

    updated_times = soup.select(".col-md-9.grid-style .search-bottom .dated")
    for i, data in enumerate(all_data):
        if i < len(updated_times):
            data.append(updated_times[i].get_text(strip=True))
        else:
            data.append("N/A")
    # Column names use to show information and save in csv file
    columns = ["Car Name", "Vehicle City", "Year", "KM", "Type", "CC", "Type 2", "Grade", "Updated Time"]
    df = pd.DataFrame(all_data, columns=columns)
    return df

base_url = "https://www.pakwheels.com/used-cars/search/-/featured_1/"
first_page_soup = BeautifulSoup(requests.get(base_url).content, "html.parser")
df = scrape_page_data(base_url, first_page_soup)
pagination = first_page_soup.select(".pagination li")
total_pages = int(re.search(r'\d+', pagination[1].text).group()) if pagination else 1
for page_num in range(3, 269):
    print(page_num)
    url = f"https://www.pakwheels.com/used-cars/search/-/featured_1/?page={page_num}"
    page_soup = BeautifulSoup(requests.get(url).content, "html.parser")
    df_page = scrape_page_data(url, page_soup)
    df = pd.concat([df, df_page], ignore_index=True)
    # I have printed df so that I should know on which page there is a error because I have connection problems many times
    print(df)
    file_path = "E:\\DSA_LABS\\DSA_Mid_Project\\all_data.csv"
    # This line of code checks wheteher the file exists or not for avoiding any issues
    file_exists = os.path.isfile(file_path)
    df.to_csv(file_path, mode='a', header=not file_exists, index=False)
# This is a whole code which scraps data from pak wheels website