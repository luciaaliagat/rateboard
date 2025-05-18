import asyncio

from django.utils.timezone import make_aware
from rates.scrapers.scraper import get_rates as scrape_rates
from rateboard.models.rate import Rate
from datetime import datetime, time


def get_rates(use_db=True):
    now = datetime.now()
    today = now.date()
    two_pm = time(14, 0)

    cutoff_datetime = make_aware(datetime.combine(today, two_pm))

    if use_db:
        rates_today = Rate.objects.filter(timestamp__gte=cutoff_datetime)
        if rates_today.exists():
            return list(rates_today)
        else:
            results = scrape_rates()

            if results:
                Rate.objects.all().delete()

                for r in results:
                    Rate.objects.create(
                        source=r['source'],
                        buy_rate=r['buy_rate'],
                        sell_rate=r['sell_rate'],
                        url=r['url'],
                        url_logo=r.get('url_logo', '')
                    )
                # Devolver lo que se guardó
                return list(Rate.objects.all())
            else:
                # Si scrap falla, devolver lo que hay (aunque sea viejo)
                return list(Rate.objects.all())

    else:
        # Si use_db es False, solo scrapear sin guardar
        results = asyncio.run(scrape_rates())
        return results

def clean_bcrp_data(raw_data):
    periods = raw_data.get("periods", [])
    dates = []
    buys = []
    sells = []

    for period in periods:
        buy_str, sell_str = period["values"]
        if buy_str != "n.d." and sell_str != "n.d.":
            dates.append(period["name"])
            buys.append(float(buy_str))
            sells.append(float(sell_str))
    return {
        "dates": dates,
        "buy_rates": buys,
        "sell_rates": sells,
    }
