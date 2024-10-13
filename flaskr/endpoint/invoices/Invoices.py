from flask_restful import Resource
from flask import jsonify, request
import logging
import requests
from ...application.invoice_service import InvoiceService
from http import HTTPStatus
from ...infrastructure.databases import InvoicePostgresqlRepository,InvoiceDetailPostgresqlRepository

from ...utils import Logger

from config import Config

log = Logger()

class Invoices(Resource):

    def __init__(self):
        config = Config()
        self.repository = InvoicePostgresqlRepository(config.DATABASE_URI)
        self.invoice_detail_repository=InvoiceDetailPostgresqlRepository(config.DATABASE_URI)
        self.service = InvoiceService(self.repository,None,self.invoice_detail_repository)
        

    def get(self, customer_id):
        try:
            log.info(f'Receive request to get the data from customer_id {customer_id}')
            invoices = self.service.list_invoices_by_customer(customer_id)
            return invoices
        except Exception as ex:
            log.error(f'Some error occurred trying to get the data from {customer_id}: {ex}')
            return {'message': 'Something was wrong trying to get the data'}, HTTPStatus.INTERNAL_SERVER_ERROR




    def post(self, action=None):
        if action == 'generateInvoices':
            return self.generate_invoices()
        else:
            return {"message": "Action not found"}, 404


    def generate_invoices(self):
        self.service.generate_invoices()
        return '',200