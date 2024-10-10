DO
$do$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_database WHERE datname = 'payment-db'
   ) THEN
      PERFORM dblink_exec('dbname=postgres', 'CREATE DATABASE "payment-db"');
   END IF;
END
$do$;

CREATE TABLE IF NOT EXIST invoice_status(
   id SERIAL PRIMARY KEY,
   name VARCHAR(20)
);


CREATE TABLE IF NOT EXIST payment_method(
   id SERIAL PRIMARY KEY,
   name VARCHAR(20)
);

CREATE TABLE IF NOT EXIST payment_status(
   id SERIAL PRIMARY KEY,
   name VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS invoice (
    id UUID PRIMARY KEY,
    customer_id UUID,
    invoice_id VARCHAR(50) NULL,
    amount NUMERIC(10, 2),
    tax NUMERIC(10, 2),
    total_amount NUMERIC(10, 2),
    plan_id UUID,
    status Integer,
    created_at TIMESTAMP WITH TIME ZONE,
    updated_at TIMESTAMP WITH TIME ZONE,
    generation_date TIMESTAMP WITH TIME ZONE,
    start_at TIMESTAMP WITH TIME ZONE,
    end_at TIMESTAMP WITH TIME ZONE,

    CONSTRAINT fk_status
        FOREIGN KEY (status) 
        REFERENCES invoice_status (id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS invoice_detail (
      id SERIAL PRIMARY KEY,
      detail VARCHAR(255),
      amount NUMERIC(10, 2),
      tax NUMERIC(10, 2),
      total_amount NUMERIC(10, 2),
      issue_id UUID NULL,
      chanel_plan_id Integer NULL,
      invoice_id UUID,
      CONSTRAINT fk_invoice
         FOREIGN KEY (invoice_id)
         REFERENCES invoice(id)
         ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS payment (
    id UUID PRIMARY KEY,
    amount NUMERIC(10, 2),
    created_at TIMESTAMP WITH TIME ZONE,
    invoice_id UUID,
    status Integer,
    method Integer,
      CONSTRAINT fk_invoice
         FOREIGN KEY (invoice_id)
         REFERENCES invoice(id)
         ON DELETE CASCADE,
      CONSTRAINT fk_method
         FOREIGN KEY (method)
         REFERENCES payment_method(id)
         ON DELETE CASCADE,
      CONSTRAINT fk_status
         FOREIGN KEY (status)
         REFERENCES payment_status(id)
         ON DELETE CASCADE,
);