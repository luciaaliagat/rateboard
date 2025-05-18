import aiohttp

async def scrape_sunat_sbs():
    url = "https://www.sunat.gob.pe/a/txt/tipoCambio.txt"
    url_logo="https://www.sbs.gob.pe/portals/0/img/sbs_logotipo.svg"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                print(f"Error al obtener datos de SUNAT: status {resp.status}")
                return None
            text = await resp.text()

    parts = text.strip().split("|")
    if len(parts) < 3:
        print("Formato inesperado en archivo SUNAT")
        return None

    try:
        buy_rate = float(parts[1])
        sell_rate = float(parts[2])
        date = (parts[0])
    except Exception as e:
        print(f"Error parsing SUNAT rates: {e}")
        return None

    return {
        "source": "SBS",
        "buy_rate": buy_rate,
        "sell_rate": sell_rate,
        "url": url,
        "url_logo": url_logo,
        "date": date
    }
