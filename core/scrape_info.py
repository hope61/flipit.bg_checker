def scrape_info(soup):
    # Find the <div> element with the specified class name
    div_element = soup.find('div', class_='slider-image-container')

    # Find the <img> element within the <div> element
    image_element = div_element.find('img')

    # Extract the image URL from the src attribute
    image_url = image_element['src']

    phone_title_unformatted = soup.find('h1', class_='phone-title')
    phone_title = phone_title_unformatted.text.strip()

    return image_url, phone_title
