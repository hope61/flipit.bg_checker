def get_price(soup):
    # Find the <div> element with class name "final-price"
    price_div = soup.find('div', class_='final-price')

    # Extract the price value
    price = price_div.text.strip()

    # Remove the newline character and currency symbol
    price = price.replace('\n', '').replace('лв', '')

    # Remove any extra spaces
    price = price.strip()

    # Insert a comma before the last two digits
    price_formatted = price[:-2] + "." + price[-2:]
    return float(price_formatted)