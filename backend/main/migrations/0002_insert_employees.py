from django.db import migrations

def create_employees(apps, schema_editor):
    Employee = apps.get_model('main', 'Employee')
    employees = [
        {"emp_id": "001", "name": "Ma'am Charisse", "password": "charisse123"},
        {"emp_id": "002", "name": "Sir Jude", "password": "jude123"},
        {"emp_id": "003", "name": "Sir Gab", "password": "gab123"},
        {"emp_id": "004", "name": "Ma'am Cheryl", "password": "cheryl123"},
        {"emp_id": "005", "name": "Sir Julius", "password": "julius123"},
    ]
    for emp in employees:
        Employee.objects.update_or_create(emp_id=emp["emp_id"], defaults=emp)

class Migration(migrations.Migration):
    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_employees),
    ]
