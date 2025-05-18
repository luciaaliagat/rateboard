from playwright.async_api import async_playwright
from .base import fetch_rates

async def scrape_tkambio():
    url = "https://tkambio.com/"
    url_logo = "https://s3-ced-uploads-01.s3.amazonaws.com/1700582713774-tkambio.svg"

    async with async_playwright() as p:
        rates =  fetch_rates(
            url= url,
            buy_selector=".purcharse-content .price",
            sell_selector=".sale-content .price"
        )
        if rates:
            buy_rate, sell_rate =  await rates
            return {
                "source": "TKambio",
                "buy_rate": buy_rate,
                "sell_rate": sell_rate,
                "url": url,
                "url_logo": url_logo
            }

            return None
