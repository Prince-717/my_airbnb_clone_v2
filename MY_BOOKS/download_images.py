#!/usr/bin/python3

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Replace with the URL of the book's website
base_url = "https://www.google.com.gh/books/edition/Designing_with_Creo_Parametric_8_0/-VE2EAAAQBAJ?hl=en&gbpv=1&dq=ptc+creo+user+guide&printsec=frontcover"

response = requests.get(base_url)
soup = BeautifulSoup(response.content, "html.parser")

image_tags = soup.find_all("img")

# Create a directory to save images
if not os.path.exists("images"):
    os.makedirs("images")

for img_tag in image_tags:
    img_url = urljoin(base_url, img_tag["src"])
    img_data = requests.get(img_url).content

    # Extract the image filename from the URL
    img_filename = os.path.basename(img_url)

    # Save the image to the images directory
    with open(os.path.join("images", img_filename), "wb") as img_file:
        img_file.write(img_data)

print("Images downloaded successfully.")

