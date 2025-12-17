
from django.db import models

class Employee(models.Model):
	EMPLOYEE_CHOICES = [
		("001", "Ma'am Charisse"),
		("002", "Sir Jude"),
		("003", "Sir Gab"),
		("004", "Ma'am Cheryl"),
		("005", "Sir Julius"),
	]
	emp_id = models.CharField(max_length=3, unique=True, choices=EMPLOYEE_CHOICES)
	name = models.CharField(max_length=50)
	password = models.CharField(max_length=50)

	def __str__(self):
		return f"{self.name} - {self.emp_id}"


from django.utils import timezone

class Quotation(models.Model):
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
	quotation_no = models.CharField(max_length=20, unique=True, editable=False)
	date_created = models.DateField(auto_now_add=True)
	# Add other fields as needed (e.g., client_name, items, total, etc.)

	def save(self, *args, **kwargs):
		if not self.quotation_no:
			year = timezone.now().year
			emp_id = self.employee.emp_id
			# Remove leading zeros for id, then pad to 2 digits
			id_part = str(int(emp_id)).zfill(2)
			# Count existing quotations for this employee and year
			count = Quotation.objects.filter(employee=self.employee, date_created__year=year).count() + 1
			serial = str(count).zfill(4)
			self.quotation_no = f"{id_part}-{year}-{serial}"
		super().save(*args, **kwargs)

	def __str__(self):
		return self.quotation_no
