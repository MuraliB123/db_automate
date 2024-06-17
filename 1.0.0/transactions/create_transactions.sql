CREATE TABLE transactions (
    user_id int NOT NULL ,
    service_id int NOT NULL,
    transaction_id int,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(service_id) REFERENCES services(id)
)