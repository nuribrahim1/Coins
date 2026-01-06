import requests
from typing import Dict, Any, List

class CoinGeckoClient:
    BASE_URL = "https://api.coingecko.com/api/v3"

    def __init__(self, timeout: int=10):
        self.session = requests.Session()
        self.timeout = timeout

    def _get(self, endpoint: str, params: Dict[str, Any] | None=None ) -> Any:
        url = f"{self.BASE_URL}{endpoint}"
        response = self.session.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()
        return response.json()

    def get_markets(
        self,
        vs_currency: str = "gbp",
        per_page: int = 100,
        page: int = 1
    ) -> List[Dict[str, Any]]:
        return self._get(
            "/coins/markets",
            params={
                "vs_currency": vs_currency,
                "per_page": per_page,
                "page": page,
            },
        )

    def get_market_chart(
            self,
            coin_id: str,
            vs_currency: str = "gbp",
            days: int = 30
            ) -> Dict[str, Any]:
        return self._get(
            f"/coins/{coin_id}/market_chart",
            params={
                "vs_currency": vs_currency,
                "days": days,
            },
        )