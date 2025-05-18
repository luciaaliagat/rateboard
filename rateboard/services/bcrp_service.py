import requests
from datetime import date, timedelta


def get_bcrp_dollar_history():
    today = date.today()
    start_date = today - timedelta(days=30)
    start_str = start_date.isoformat()
    end_str = today.isoformat()

    url = f"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD04646PD-PD04645PD/json/{start_str}/{end_str}/esp"

    try:
        response = requests.get(url, headers={"Accept": "application/json"})
        response.raise_for_status()
        print("Respuesta HTTP OK")

        data = response.json()
        print("JSON recibido:", data.keys())

        periods = data.get("periods", [])
        print(f"Cantidad de periodos: {len(periods)}")

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

    except Exception as e:
        print("Error al obtener historial de BCRP:", e)
        return {
            "dates": [],
            "buy_rates": [],
            "sell_rates": [],
        }
