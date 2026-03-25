SELECT
    coin_id,
    event_time,
    volume_gbp
FROM {{ source ('raw', 'raw_volumes') }}