from django.db import models

# Create your models here.


class User(models.Model):

    USER_ROLE = (
        ('A', 'Administrator'),
        ('E', 'Employee')
    )

    USER_STATE = (
        ('A', 'Activate'),
        ('D', 'Deactivate')
    )

    name = models.CharField(max_length=100)
    user_role = models.CharField(max_length=1, choices=USER_ROLE)
    user_state = models.CharField(max_length=1, choices=USER_STATE)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
