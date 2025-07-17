--Kto komu ile

WITH 
total_paid AS
(
    SELECT
        payer_id,
        SUM(amount) as paid_amount
    FROM
        expenses
    GROUP BY
        payer_id
),

total_owed AS
(
    SELECT
        participant_id,
        SUM(share) as owed_amount
    FROM
        expense_splits
    GROUP BY
        participant_id
)

SELECT
    p.name,
    COALESCE(tp.paid_amount, 0) as Ile_zaplacil,
    COALESCE(tow.owed_amount, 0) as Ile_powinien_zaplacic,
    (COALESCE(tp.paid_amount, 0) - COALESCE(tow.owed_amount, 0)) as Saldo 
FROM
    participants p 
    LEFT JOIN total_paid tp ON p.participant_id = tp.payer_id
    LEFT JOIN total_owed tow ON p.participant_id = tow.participant_id
ORDER BY
    saldo desc