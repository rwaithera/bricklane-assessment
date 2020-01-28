import csv

from bricklane_platform.models.payment import Payment


class PaymentProcessor(object):

    def get_payments(self, csv_path, source):
        payments = []
        with open(csv_path) as f:
            reader = csv.DictReader(f)
            for row in reader:

                ## this is where we make note of bank payments
                ## we change the header name to card_id since Payment only identifies card_id
                ## and we update transfer status
                if 'bank_account_id' in row:
                    row["card_id"] = row["bank_account_id"]
                    card_status = ["processed", "declined"]
                    import random
                    row["card_status"] = random.choice(card_status)
                
                payments.append(Payment(row))

        return payments

    def verify_payments(self, payments):
        successful_payments = []
        for payment in payments:
            if payment.is_successful():
                successful_payments.append(payment)

        return successful_payments
