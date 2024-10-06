from typing import List
import json
from ...domain.models import Invoice

class InvoiceMapper:
    def list_response(self, invoices: List[Invoice]):
        invoices_dict = [self._to_dict(invoice) for invoice in invoices]
        return json.loads(json.dumps(invoices_dict))

    def _to_dict(self, invoice:Invoice):
        return {
            'id': str(invoice.id),
            'invoiceId': invoice.invoice_id,
            'customerId': str(invoice.customer_id),
            'paymentId': str(invoice.payment_id) if invoice.payment_id else None,
            'amount': float(invoice.amount),
            'tax': float(invoice.tax),
            'totalAmount': float(invoice.total_amount),
            'subscription': invoice.subscription,
            'subscriptionId': str(invoice.subscription_id),
            'status': invoice.status,
            'createdAt': invoice.created_at.isoformat(),
            'updatedAt': invoice.updated_at.isoformat(),
            'generationDate': invoice.generation_date.isoformat(),
            'period': invoice.period.isoformat()
        }