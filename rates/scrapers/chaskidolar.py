from playwright.async_api import async_playwright
from .base import fetch_rates

async def scrape_chaskidolar():
    url = "https://chaskidolar.com/"
    url_logo = "https://s3-ced-uploads-01.s3.amazonaws.com/1724079421732-chaski%20dolar-3.svg"

    async with async_playwright() as p:
        rates = fetch_rates(
            url=url,
            buy_selector='.converter__prices p:has-text("TÚ COMPRAS DÓLARES") span.text-black',
            sell_selector='.converter__prices p:has-text("TÚ VENDES DÓLARES") span.text-black',
            buy_strip=["S/"],
            sell_strip=["S/"]
        )
        if rates:
            buy_rate, sell_rate = await rates
            return {
                "source": "Chaskidolar",
                "buy_rate": buy_rate,
                "sell_rate": sell_rate,
                "url": url,
                "url_logo": url_logo
            }

        return None
