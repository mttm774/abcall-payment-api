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

CREATE TABLE IF NOT EXISTS invoices (
    id UUID PRIMARY KEY,
    customer_id UUID,
    invoice_id VARCHAR(50) NULL,
    payment_id UUID,
    amount NUMERIC(10, 2),
    tax NUMERIC(10, 2),
    total_amount NUMERIC(10, 2),
    subscription VARCHAR(100),
    subscription_id UUID,
    status VARCHAR(20),
    created_at TIMESTAMP WITH TIME ZONE,
    updated_at TIMESTAMP WITH TIME ZONE,
    generation_date TIMESTAMP WITH TIME ZONE,
    period TIMESTAMP WITH TIME ZONE
);