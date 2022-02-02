from django.urls import path
from .views import (
    create_report_view,
    ReportListView,
    ReportDetailView,
    render_pdf_view,
    UploadTemplateView,
    csv_upload_view
)

app_name = 'reports'

urlpatterns = [
    path('', ReportListView.as_view(), name='list'),
    path('<pk>', ReportDetailView.as_view(), name='report_detail'),
    path('save/', create_report_view, name='create_report'),
    path('upload_file/', UploadTemplateView.as_view(), name='upload_from'),
    path('upload/', csv_upload_view, name='upload'),
    path('<pk>/pdf/', render_pdf_view, name='pdf'),
    
    
]
