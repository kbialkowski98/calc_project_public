--TABELE

CREATE TABLE participants
(

    participant_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL

);

CREATE TABLE expenses
(

    expense_id SERIAL PRIMARY KEY,
    description VARCHAR(255),
    amount DECIMAL(10,2) NOT NULL,
    date DATE,
    payer_id INT,

    FOREIGN KEY (payer_id ) REFERENCES participants(participant_id)

);

CREATE TABLE expense_splits
(

    split_id SERIAL PRIMARY KEY,
    expense_id INT,
    participant_id INT,
    share DECIMAL(10,2) NOT NULL,

    FOREIGN KEY (expense_id) REFERENCES expenses(expense_id),
    FOREIGN KEY (participant_id) REFERENCES participants(participant_id)

)
