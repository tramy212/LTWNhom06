from django.http import JsonResponse
from django.db.models import Q
from .models import Employee


def employee_search(request):
    query = request.GET.get('q', '')
    if len(query) < 2:
        return JsonResponse([], safe=False)

    employees = Employee.objects.filter(
        Q(code__icontains=query) |
        Q(first_name__icontains=query) |
        Q(last_name__icontains=query) |
        Q(full_name__icontains=query) |
        Q(email__icontains=query)
    ).filter(is_active=True)[:10]

    results = []
    for employee in employees:
        department_name = ""
        if employee.position and employee.position.department:
            department_name = employee.position.department.name

        results.append({
            'id': employee.id,
            'code': employee.code,
            'full_name': employee.full_name,
            'position': employee.position.name if employee.position else '',
            'department': department_name
        })

    return JsonResponse(results, safe=False)