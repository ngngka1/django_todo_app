from django.db import models
import datetime

# Create your models here.
    
class Subject(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return str(self.name)

class ToDoItem(models.Model):
    title = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    due_date = models.DateField(default=datetime.date.today)
    completed = models.BooleanField(default=False)
    # is_urgent = models.BooleanField(default=False)
    # modifying = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title

