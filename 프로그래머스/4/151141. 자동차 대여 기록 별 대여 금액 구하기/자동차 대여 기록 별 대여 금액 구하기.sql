WITH T_LIST AS (
    SELECT 
        H.HISTORY_ID AS HISTORY_ID,
        C.DAILY_FEE AS DAILY_FEE,
        DATEDIFF(H.END_DATE, H.START_DATE) + 1 AS RENT_DAYS,
        CASE 
            WHEN DATEDIFF(H.END_DATE, H.START_DATE) + 1 >= 90 THEN '90일 이상'
            WHEN DATEDIFF(H.END_DATE, H.START_DATE) + 1 >= 30 THEN '30일 이상'
            WHEN DATEDIFF(H.END_DATE, H.START_DATE) + 1 >= 7 THEN '7일 이상'
            ELSE 'x' 
        END AS DURATION_TYPE
    FROM CAR_RENTAL_COMPANY_CAR AS C
    JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H 
        ON C.CAR_ID = H.CAR_ID
    WHERE C.CAR_TYPE = '트럭'
)

SELECT 
    T.HISTORY_ID AS HISTORY_ID,
    ROUND(T.DAILY_FEE * T.RENT_DAYS * (1 - IFNULL(P.DISCOUNT_RATE/100, 0))) AS FEE
FROM T_LIST AS T
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS P
    ON T.DURATION_TYPE = P.DURATION_TYPE 
    AND P.CAR_TYPE = '트럭'
ORDER BY FEE DESC, HISTORY_ID DESC