from playwright.async_api import async_playwright
from .base import fetch_rates

async def scrape_tucambista():
    url = "https://tucambista.pe/"
    url_logo = "https://tucambista.pe/_next/static/media/Logo.08353e5e.svg"

    async with async_playwright() as p:
        rates = await fetch_rates(
            url=url,
            buy_selector='tbody.font-bold tr.style_first-tr__gB8W4 td:nth-child(2)',
            sell_selector = 'tbody.font-bold tr.style_first-tr__gB8W4 td:nth-child(3)'

        )
        if rates:
            buy_rate, sell_rate = rates
            return {
                "source": "Tucambista",
                "buy_rate": buy_rate,
                "sell_rate": sell_rate,
                "url": url,
                "url_logo": url_logo
            }

        return None
