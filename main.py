import requests
from bs4 import BeautifulSoup
import socket
import spacy
from prettytable import PrettyTable


def get_location(website):
    ip = socket.gethostbyname(website)
    if ip:
        try:
            response = requests.get(f'https://ipapi.co/{ip}/json/').json()
            location_data = {
                "ip": ip,
                "city": response.get("city"),
                "region": response.get("region"),
                "country": response.get("country_name"),
                "zip code": response.get("postal")
            }
            return location_data
        except requests.RequestException as e:
            print("Error while retrieving location data:", e)
    return None


def extract_text_from_html(html_content):
    # parse html content with beautifulsoup
    soup = BeautifulSoup(html_content, "html.parser")

    # extract text from html
    text = soup.get_text()

    return text


websites = ["dollyandoatmeal.com", "andrewhuang.com", "doctorneha.com", "drmikesevilla.com", "drdavidgeier.com",
            "mynameisyeh.com", "amandafrederickson.com", "saricastudio.com", "golivehq.co",
            "ashergardner.com", "galadarling.com", "cookieandkate.com", "thefashionguitar.com",
            "colormecourtney.com", "girlwithcurves.com", "tim.blog", "amberfillerup.com",
            "teachjunkie.com"]

table = PrettyTable()
table.field_names = ["Website", "Location",
                     "Names", "Email", "Instagram",
                     "YouTube", "LinkedIn",
                     "Twitter", "Facebook"]


nlp = spacy.load("en_core_web_sm")
# looping through websites
for website in websites:
    url = f"https://www.{website}/about"
    response = requests.get(url)
    html_content = response.text

    # parse html content
    soup = BeautifulSoup(html_content, "html.parser")

    # find the links using beautifulsoup
    twitter_link = soup.find("a", href=lambda href: href and "twitter.com" in href)
    facebook_link = soup.find("a", href=lambda href: href and "facebook.com" in href)
    linkedin_link = soup.find("a", href=lambda href: href and "linkedin.com" in href)
    youtube_link = soup.find("a", href=lambda href: href and "youtube.com" in href)
    instagram_link = soup.find("a", href=lambda href: href and "instagram.com" in href)
    email_link = soup.find("a", href=lambda href: href and href.startswith("mailto:"))

    # calling get_location function
    location_data = get_location(website)

    # find names using scrapy
    text = extract_text_from_html(html_content)
    text = text.replace('\n', '')
    doc = nlp(text)
    names = []
    for ent in doc.ents:
        if ent.label_ == "PERSON" and (len(ent.text.split()) >= 1 and len(ent.text.split()) < 3):
            names.append(ent.text.strip())

    location = location_data or "N/A"
    names = names if names else "N/A"
    email = email_link["href"] if email_link else "N/A"
    instagram = instagram_link["href"] if instagram_link else "N/A"
    youtube = youtube_link["href"] if youtube_link else "N/A"
    linkedin = linkedin_link["href"] if linkedin_link else "N/A"
    twitter = twitter_link["href"] if twitter_link else "N/A"
    facebook = facebook_link["href"] if facebook_link else "N/A"

    # add data into table
    table.add_row([website, location, names, email, instagram, youtube, linkedin, twitter, facebook])

print(table)
