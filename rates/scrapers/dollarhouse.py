from playwright.async_api import async_playwright

from .base import fetch_rates

async def scrape_dollarhouse():
    url = "https://dollarhouse.pe/"
    url_logo="https://s3-ced-uploads-01.s3.amazonaws.com/1702304946735-dollar-house-v2.svg"

    async with async_playwright() as p:
        rates =  fetch_rates(
            url= "https://app.dollarhouse.pe/calculadorav2",
            buy_selector=".exchange-rate.purchase span",
            sell_selector=".exchange-rate.sale span",
            buy_strip=["S/"],
            sell_strip=["S/"]
        )
        if rates:
            buy_rate, sell_rate = await rates
            return {
                "source": "DollarHouse",
                "buy_rate": buy_rate,
                "sell_rate": sell_rate,
                "url": url,
                "url_logo": url_logo
            }

            return None

