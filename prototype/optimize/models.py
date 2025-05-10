from django.db import models

class ChipDesign(models.Model):
    PERFORMANCE_CHOICES = [
        ('Low', 'Low'),
        ('Balanced', 'Balanced'),
        ('High', 'High'),
    ]

    performance = models.CharField(max_length=10, choices=PERFORMANCE_CHOICES)
    max_power = models.IntegerField()
    max_area = models.IntegerField()
    selected_core = models.CharField(max_length=50)
    selected_memory = models.CharField(max_length=50)
    selected_connectivity = models.CharField(max_length=50)
    total_power = models.IntegerField()
    total_area = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.performance} | {self.selected_core} | {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
