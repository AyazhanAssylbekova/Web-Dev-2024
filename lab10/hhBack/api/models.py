from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    city = models.CharField(max_length=500)
    address = models.TextField()

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"
    


class Vacancy(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"

    def __str__(self):
        return f"Company name: {self.company}, Vacancy name: {self.name}"
    