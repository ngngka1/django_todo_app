from django.db import models
import datetime

# Create your models here.

# To extract data from database, we have to use Django's query API
class ToDoItem(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateField(default=datetime.date.today)
    completed = models.BooleanField(default=False)
    # is_urgent = models.BooleanField(default=False)
    # modifying = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title
