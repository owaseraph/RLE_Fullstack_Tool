from django.db import models
from django.contrib.auth.models import User

class RLEHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    input_text = models.TextField()
    output_text = models.TextField()

    action_type = models.CharField(max_length=10)  # 'encode' or 'decode'

    ratio = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.action_type} at {self.created_at}"