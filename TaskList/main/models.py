from django.db import models
from django.utils.text import slugify

PRIORITY_CHOICES = (('High', 'High'), ('Middle', 'Middle'), ('Low', 'Low'))
STATUS_CHOICES = (('In progress', 'In progress'), ('Completed', 'Completed'))


class Task(models.Model):
    title = models.CharField('Title', max_length=255)
    description = models.TextField('Description')
    priority = models.CharField('Priority', choices=PRIORITY_CHOICES, max_length=7, default='High')
    create_at = models.DateTimeField('Create Time', auto_now_add=True)
    deadline = models.DateTimeField('Deadline')
    status = models.CharField('Status', choices=STATUS_CHOICES, max_length=12, default='In progress')
    completed_at = models.DateTimeField('Completed', null=True, blank=True)
    image = models.ImageField('Image', upload_to='image/%Y/%m/%d')
    slug = models.SlugField('Slug', unique=True, max_length=255, null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify('{}-{}'.format(self.title, self.image))
        super(Task, self).save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.title


class ActionType(models.Model):
    name = models.CharField('Action', max_length=255)

    def __str__(self):
        return self.name


class Action(models.Model):
    action = models.ForeignKey('ActionType', on_delete=models.DO_NOTHING, verbose_name='Action')
    date = models.DateTimeField('Date')

    def __str__(self):
        return self.action.name
