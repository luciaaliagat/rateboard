import json

from django.shortcuts import render
from .services.service import get_rates
from .services.bcrp_service import get_bcrp_dollar_history

def home(request):
    rates = get_rates(use_db=True)
    history_data = get_bcrp_dollar_history()

    sunat_sbs_rate = next((r for r in rates if r.source == "SBS"), None)

    context = {
        "sources": [r for r in rates if r.source != "SBS"],
        "reference_buy_rate": sunat_sbs_rate.buy_rate if sunat_sbs_rate else "N/A",
        "reference_sell_rate": sunat_sbs_rate.sell_rate if sunat_sbs_rate else "N/A",
        "reference_source": sunat_sbs_rate.source if sunat_sbs_rate else "N/A",
        "reference_logo": sunat_sbs_rate.url_logo if sunat_sbs_rate else "N/A",
        "history_data": json.dumps(history_data),
    }

    return render(request, "home.html", context)