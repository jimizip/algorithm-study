-- 코드를 입력하세요
SELECT I.INGREDIENT_TYPE AS INGREDIENT_TYPE, SUM(TOTAL_ORDER) AS TOTAL_ORDER
FROM FIRST_HALF H
JOIN ICECREAM_INFO I ON H.FLAVOR = I.FLAVOR
GROUP BY INGREDIENT_TYPE
ORDER BY TOTAL_ORDER