from django.urls import path
from djangoProject102.departments.views import show_departments, show_department_details, redirect_to_first_department, \
    show_not_found

urlpatterns = (
    # http://127.0.0.1:8000/departments/
    path('', show_departments, name='show departments'),

    # http://127.0.0.1:8000/departments/not-found
    path('not-found/', show_not_found, name='not found'),

    # http://127.0.0.1:8000/departments/redirect
    path('redirect/', redirect_to_first_department, name='redirect demo'),

    # /departments/{department_id}/
    path('<department_id>/', show_department_details, name='with string'),

    # /departments/int/{department_id}/
    path('int/<int:department_id>/', show_department_details, name='details'),
)



