from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, EmployeeViewSet, PayrollViewSet, TimeAttendanceViewSet, BenefitViewSet, PerformanceReviewViewSet

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'payrolls', PayrollViewSet)
router.register(r'time-attendance', TimeAttendanceViewSet)
router.register(r'benefits', BenefitViewSet)
router.register(r'performance-reviews', PerformanceReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('employees/', views.employees_view, name='employees'),  # Example URL pattern
    # path('benefits/', views.benefits_view, name='benefits'),  # Example URL pattern
    # Define more paths as needed
]


