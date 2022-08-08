from django.db import models
from django.contrib import auth

class User(auth.models.User):

    class UserRole(models.TextChoices):
        ADMIN = 'admin',
        EMPLOYEE = 'employee'

    role = models.CharField(
        max_length=8,
        choices = UserRole.choices
    )

class Ticket(models.Model):

    class TicketStatus(models.TextChoices):
        OPEN = 'open',
        CLOSE = 'close'

    class TicketPriority(models.TextChoices):
        LOW = 'low',
        MEDIUM = 'medium',
        HIGH = 'high'

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=100, blank=False, default="test")
    status = models.CharField(
        max_length=5,
        choices = TicketStatus.choices,
        default = TicketStatus.OPEN
    )
    priority = models.CharField(
        max_length=6,
        choices = TicketPriority.choices,
        default = TicketPriority.LOW
    )
    assignedTo = models.ForeignKey(User, related_name="userId", on_delete=models.DO_NOTHING)
    createdAt = models.DateTimeField(auto_now_add = True)
