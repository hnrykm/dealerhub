from django.db import models


class AutomobileVO(models.Model):
    import_href = models.CharField(max_length=100, unique=True)
    vin = models.CharField(max_length=17, unique=True)
    sold = models.BooleanField(default=False)

class Technician(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    employee_id = models.PositiveSmallIntegerField()


class Appointment(models.Model):
    date_time = models.DateTimeField()
    reason = models.TextField()
    status = models.CharField(max_length=100)
    vin = models.CharField(max_length=17)
    customer = models.CharField(max_length=100)
    technician = models.ForeignKey(
        Technician, related_name="appointment", on_delete=models.CASCADE
    )
