from playwright.async_api import async_playwright
from .base import fetch_rates

async def scrape_kambista():
    url = "https://kambista.com"
    url_logo = "https://d31dn7nfpuwjnm.cloudfront.net/images/valoraciones/0042/0837/kambista-que-es-como-funciona-tipos-cambio_foro.png?1612317683"

    async with async_playwright() as p:
        rates =  fetch_rates(
            url=url,
            buy_selector="#valcompra",
            sell_selector="#valventa",
        )

        if rates:
            buy_rate, sell_rate = await rates
            return {
                "source": "Kambista",
                "buy_rate": buy_rate,
                "sell_rate": sell_rate,
                "url": url,
                "url_logo": url_logo
            }

        return None
