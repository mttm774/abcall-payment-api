INSERT INTO invoices (
    id,
    customer_id,
    invoice_id,
    payment_id,
    amount,
    tax,
    total_amount,
    subscription,
    subscription_id,
    status,
    created_at,
    updated_at,
    generation_date,
    period
) VALUES
-- First random record
(
    'b06e6adc-f35d-42b7-a9b6-633c8c5bd1b1', -- id
    '63d85da4-e3d9-4e76-9821-e6a3ca626962', -- customerId (same for all)
    '1234', -- invoiceId
    'f960f955-02d6-4342-91c0-72772d0f2d6b', -- paymentId
    1000, -- amount
    120, -- tax
    1120, -- totalAmount
    'Entrepreneur', -- subscription
    '60b41fbc-5043-4974-8503-111c55e05cc7', -- subscriptionId
    'IN_PROGRESS', -- status
    '2024-09-22 00:20:00.454+00', -- createdAt
    '2024-09-22 00:20:00.454+00', -- updatedAt
    '2024-09-22 00:20:00.454+00', -- generationDate
    '2024-09-15 00:00:00.000+00' -- period
),
-- Second random record
(
    'c07f7adc-d35f-53b8-b9b7-734c9c6ce2c2', -- id
    '63d85da4-e3d9-4e76-9821-e6a3ca626962', -- customerId
    '1235', -- invoiceId
    'c070c967-03d7-5353-a2d1-83883e1e3e7d', -- paymentId
    1500, -- amount
    180, -- tax
    1680, -- totalAmount
    'Pro Plan', -- subscription
    '61d52fbd-5144-5074-9604-212c77f06dd8', -- subscriptionId
    'COMPLETED', -- status
    '2024-09-22 10:30:00.454+00', -- createdAt
    '2024-09-22 11:00:00.454+00', -- updatedAt
    '2024-09-22 10:30:00.454+00', -- generationDate
    '2024-09-16 00:00:00.000+00' -- period
),
-- Third random record
(
    'd08a8bdd-e46f-64c9-cac9-845d9d7de2d3', -- id
    '63d85da4-e3d9-4e76-9821-e6a3ca626962', -- customerId
    '1236', -- invoiceId
    'd180d078-04d8-6464-b3d2-94994f2f4f8e', -- paymentId
    2000, -- amount
    240, -- tax
    2240, -- totalAmount
    'Business Plan', -- subscription
    '62e63fce-5245-6175-0705-323d88c18ee9', -- subscriptionId
    'IN_PROGRESS', -- status
    '2024-09-23 12:40:00.454+00', -- createdAt
    '2024-09-23 13:00:00.454+00', -- updatedAt
    '2024-09-23 12:40:00.454+00', -- generationDate
    '2024-09-17 00:00:00.000+00' -- period
),
-- Fourth random record
(
    'e09b9cee-f57a-75d0-dbda-956eaf8ef3f4', -- id
    '63d85da4-e3d9-4e76-9821-e6a3ca626962', -- customerId
    '1237', -- invoiceId
    'a290b189-05e9-7575-c4e3-05005d3c3e9f', -- paymentId
    2500, -- amount
    300, -- tax
    2800, -- totalAmount
    'Premium Plan', -- subscription
    '63f74adf-6356-7286-1816-434e99e29ff0', -- subscriptionId
    'COMPLETED', -- status
    '2024-09-24 14:50:00.454+00', -- createdAt
    '2024-09-24 15:00:00.454+00', -- updatedAt
    '2024-09-24 14:50:00.454+00', -- generationDate
    '2024-09-18 00:00:00.000+00' -- period
),
-- Fifth random record
(
    'f10e0ddf-c68d-86e1-ecec-0670bf9a404b', -- id
    '63d85da4-e3d9-4e76-9821-e6a3ca626962', -- customerId
    '1238', -- invoiceId
    'a390b290-06fa-8686-d5f4-16116c4d5e0f', -- paymentId
    3000, -- amount
    360, -- tax
    3360, -- totalAmount
    'Ultimate Plan', -- subscription
    '64a85bfc-7467-8397-2927-545d00e3aff1', -- subscriptionId
    'IN_PROGRESS', -- status
    '2024-09-25 16:00:00.454+00', -- createdAt
    '2024-09-25 16:30:00.454+00', -- updatedAt
    '2024-09-25 16:00:00.454+00', -- generationDate
    '2024-09-19 00:00:00.000+00' -- period
);