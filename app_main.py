from fastapi import FastAPI
from app import (
    chat_router,
    policy_router,
    eco_tips_router,
    feedback_router,
    report_router,
    vector_router,
    kpi_upload_router,
    dashboard_router
)

app = FastAPI()

# Include all routers
app.include_router(chat_router.router)
app.include_router(policy_router.router)
app.include_router(eco_tips_router.router)
app.include_router(feedback_router.router)
app.include_router(report_router.router)
app.include_router(vector_router.router)
app.include_router(kpi_upload_router.router)
app.include_router(dashboard_router.router)
