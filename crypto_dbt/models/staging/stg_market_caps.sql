SELECT
    coin_id,
    event_time,
    market_cap_gbp
FROM {{ source ('raw', 'raw_market_caps') }}