import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from fastapi import FastAPI, HTTPException  # noqa: E402

from reports.models import Report  # noqa: E402

from .schemas import ReportIn, ReportOut  # noqa: E402

app = FastAPI(title="Reporting Dashboard API")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/reports", response_model=list[ReportOut])
def list_reports(skip: int = 0, limit: int = 50):
    return list(Report.objects.all()[skip : skip + limit])


@app.post("/reports", response_model=ReportOut, status_code=201)
def create_report(payload: ReportIn):
    return Report.objects.create(**payload.model_dump())


def _get_or_404(report_id: int) -> Report:
    try:
        return Report.objects.get(pk=report_id)
    except Report.DoesNotExist:
        raise HTTPException(status_code=404, detail="Report not found")


@app.get("/reports/{report_id}", response_model=ReportOut)
def get_report(report_id: int):
    return _get_or_404(report_id)


@app.put("/reports/{report_id}", response_model=ReportOut)
def update_report(report_id: int, payload: ReportIn):
    report = _get_or_404(report_id)
    for field, value in payload.model_dump().items():
        setattr(report, field, value)
    report.save()
    return report


@app.delete("/reports/{report_id}", status_code=204)
def delete_report(report_id: int):
    _get_or_404(report_id).delete()
