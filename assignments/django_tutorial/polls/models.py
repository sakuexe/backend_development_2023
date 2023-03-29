from django.db import models
import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    """ Creates a questions table for the database.
        Django automatically creates IDs
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # Python's ToString() method

    def __str__(self):
        return self.question_text
    # class method for checking if the question was published within the last
    # 24 hours

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# create another table for choices
class Choice(models.Model):
    # refers to another table (that being the question)
    # also on deletion will get removed because of the last argument
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
