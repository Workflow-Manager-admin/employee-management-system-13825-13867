"""
mock_external_api.py

A simple mock API to simulate an external payroll/accounting system.
Use for development/demo/testing of integration stubs.

Run:
    python mock_external_api.py

Requires: fastapi, uvicorn

All responses are stubbed/dummy for contract testing only.
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Mock External Payroll/Accounting System API",
    description="Stubbed endpoints for ExternalPayroll/AccountingSystem integration. For demo/testing only.",
    version="0.1.0"
)

# PUBLIC_INTERFACE
@app.post("/payroll/batch")
async def payroll_batch(request: Request):
    """Receives a payroll batch submission (stub implementation)."""
    payload = await request.json()
    print(f"[MOCK API] Received batch payload: {payload}")
    return JSONResponse({
        "status": "submitted",
        "batch_id": "mock-batch-001",
        "message": "Payroll batch received (mock response)."
    })

# PUBLIC_INTERFACE
@app.get("/accounting/ledger/{period}")
async def accounting_ledger(period: str):
    """Returns mock accounting ledger data for the period."""
    print(f"[MOCK API] Query for ledger: {period}")
    return {
        "period": period,
        "entries": [],
        "message": "Mock ledger data for demonstration."
    }

# PUBLIC_INTERFACE
@app.post("/webhook/payroll-status")
async def webhook_payroll_status(request: Request):
    """Receives webhook notifications from the payroll service (stub)."""
    payload = await request.json()
    print(f"[MOCK API] Webhook received: {payload}")
    return {"status": "received", "message": "Webhook processed (mock)."}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("mock_external_api:app", host="0.0.0.0", port=8083, reload=True)
