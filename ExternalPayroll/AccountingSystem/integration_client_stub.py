"""
integration_client_stub.py

Stub client for External Payroll/AccountingSystem integration.
Demonstrates how the Employee Management System Monolith backend could interact
with an external payroll/accounting API. Intended as a reference/stub only.

No real payroll logic implemented.
"""

import requests

# PUBLIC_INTERFACE
class ExternalPayrollAPIClient:
    """
    Stub client for interacting with an external payroll/accounting API.
    Replace the base_url and adapt methods as needed for real integration.
    """

    def __init__(self, base_url):
        """
        :param base_url: The root URL of the external payroll/accounting system (e.g., http://external-payroll/api)
        """
        self.base_url = base_url

    # PUBLIC_INTERFACE
    def submit_payroll_batch(self, batch_payload):
        """
        Submit a payroll batch for processing.

        Args:
            batch_payload (dict): Payroll batch data (employee payments, period, etc.)

        Returns:
            dict: Stubbed response from external API.
        """
        # For stub/demo: just log and simulate a success response.
        url = f"{self.base_url}/payroll/batch"
        print(f"[STUB] Submitting payroll batch to {url} with payload:")
        print(batch_payload)
        # Simulate HTTP call (in real usage, uncomment the next lines)
        # response = requests.post(url, json=batch_payload)
        # return response.json()
        return {"status": "submitted", "batch_id": "stub-123", "message": "Stubbed: payroll batch accepted."}

    # PUBLIC_INTERFACE
    def get_accounting_ledger(self, period):
        """
        Fetch ledger data for reconciliation.

        Args:
            period (str): Period identifier (e.g., '2024-05')

        Returns:
            dict: Stubbed ledger data.
        """
        url = f"{self.base_url}/accounting/ledger/{period}"
        print(f"[STUB] Fetching ledger for period '{period}' from {url}")
        # In a real implementation:
        # response = requests.get(url)
        # return response.json()
        return {
            "period": period,
            "entries": [],
            "message": "Stubbed: ledger data."
        }

    # PUBLIC_INTERFACE
    def webhook_payroll_status(self, payload):
        """
        Example webhook handler stub.

        Args:
            payload (dict): Webhook event payload (e.g., payroll status update).

        Returns:
            dict: Stubbed handling response.
        """
        print("[STUB] Payroll webhook event received:")
        print(payload)
        return {"status": "received", "message": "Stubbed: webhook data processed."}

# Example usage (for demo/testing only)
if __name__ == "__main__":
    client = ExternalPayrollAPIClient(base_url="http://localhost:8083")
    dummy_batch = {"employees": [{"id": 1, "amount": 3000}], "period": "2024-05"}
    client.submit_payroll_batch(dummy_batch)
    client.get_accounting_ledger("2024-05")
    client.webhook_payroll_status({"event": "PAYROLL_PROCESSED", "batch_id": "stub-123"})

