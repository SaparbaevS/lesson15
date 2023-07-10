from django.db import models

# Create your models here.
# TODO HTTP views


class Task(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=50)
    date_of_creation = models.DateField()
    date_deadline = models.DateTimeField()

    LEVEL = [
        ("small", "малый"),
        ("average", "средний"),
        ("high", "высокий")
    ]

    level = models.CharField(max_length=20, choices=LEVEL)

    # STATUS = [
    #     ("dn", "done"),
    #     ("nd", "not done")
    # ]
    #
    # status = models.CharField(max_length=20, choices=STATUS)