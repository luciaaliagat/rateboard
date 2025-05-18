import asyncio
from .kambista import scrape_kambista
from .tkambio import scrape_tkambio
from .dollarhouse import scrape_dollarhouse
from .tucambista import scrape_tucambista
from .chaskidolar import scrape_chaskidolar
from .sunat_sbs import scrape_sunat_sbs

async def run_scrapers():
    scrapers = [scrape_chaskidolar, scrape_kambista, scrape_tkambio, scrape_dollarhouse, scrape_tucambista, scrape_sunat_sbs]
    tasks = [asyncio.create_task(scraper()) for scraper in scrapers]

    results = []
    for task in asyncio.as_completed(tasks):
        result = await task
        if result:
            print(f"Scraper returned: {result}")
            results.append(result)
        else:
            print("Scraper failed.")
    return results

def get_rates():
    return asyncio.run(run_scrapers())


if __name__ == "__main__":
    rates = get_rates()
    print("Final rates:", rates)