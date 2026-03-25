SELECT
    coin_id,
    event_time,
    price_gbp
FROM {{ source ('raw', 'raw_prices') }}