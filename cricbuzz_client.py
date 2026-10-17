import requests
from config import RAPIDAPI_KEY, RAPIDAPI_HOST, BASE_API_URL

class CricbuzzClient:
    def __init__(self):
        self.headers = {
            "x-rapidapi-key": RAPIDAPI_KEY,
            "x-rapidapi-host": RAPIDAPI_HOST
        }

    def test_connection(self):
        if not RAPIDAPI_KEY or RAPIDAPI_KEY == "your_rapidapi_key_here":
            return False, "API Key is missing or default placeholder."
        try:
            resp = requests.get(f"{BASE_API_URL}/matches/v1/live", headers=self.headers, timeout=10)
            return resp.status_code == 200, f"Status: {resp.status_code}"
        except Exception as e:
            return False, str(e)

    def get_live_matches(self):
        if not RAPIDAPI_KEY:
            return self._mock_live_data()
        try:
            resp = requests.get(f"{BASE_API_URL}/matches/v1/live", headers=self.headers, timeout=10)
            if resp.status_code == 200:
                return resp.json()
        except Exception:
            pass
        return self._mock_live_data()

    def _mock_live_data(self):
        return {
            "typeMatches": [
                {
                    "matchType": "International",
                    "seriesMatches": [
                        {
                            "seriesAdWrapper": {
                                "seriesName": "T20 International Championship",
                                "matches": [
                                    {
                                        "matchInfo": {
                                            "matchDesc": "Final",
                                            "team1": {"teamName": "India", "teamSName": "IND"},
                                            "team2": {"teamName": "Australia", "teamSName": "AUS"},
                                            "venueInfo": {"ground": "Narendra Modi Stadium", "city": "Ahmedabad"},
                                            "status": "India won by 24 runs"
                                        },
                                        "matchScore": {
                                            "team1Score": {"inngs1": {"runs": 205, "wickets": 5, "overs": 20.0}},
                                            "team2Score": {"inngs1": {"runs": 181, "wickets": 7, "overs": 20.0}}
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }
