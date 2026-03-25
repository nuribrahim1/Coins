WITH prices AS (
    SELECT * FROM {{ ref('stg_prices') }}
),

market_caps AS (
    SELECT * FROM {{ ref('stg_market_caps') }}
),

volumes AS (
 SELECT * FROM {{ ref('stg_volumes') }}
)

SELECT p.coin_id, p.event_time, p.price_gbp, mc.market_cap_gbp, v.volume_gbp
FROM prices p
LEFT JOIN market_caps mc
ON p.coin_id = mc.coin_id
AND p.event_time = mc.event_time
LEFT JOIN volumes v
ON p.coin_id = v.coin_id
AND p.event_time = v.event_time