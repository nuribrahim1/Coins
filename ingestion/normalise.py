from datetime import datetime, UTC

def normalise(coin_id:str, levels:list[list], metric:str) -> list[dict]:
    rows = []
    for ts, value in levels:
        rows.append ({
            "coin_id" : coin_id,
            "event_time" : datetime.fromtimestamp((ts/1000),UTC),
            metric : value
        })

    return rows
