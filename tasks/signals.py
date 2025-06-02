# filepath: c:\Users\Lenovo\Desktop\MGA\tasks\signals.py
from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver
from .models import Task, TaskHistory
import json

@receiver(post_save, sender=Task)
def log_task_change(sender, instance, created, **kwargs):
    if created:
        action = 'Utworzenie'
        changes = {
            'name': [None, instance.name],
            'description': [None, instance.description],
            'status': [None, instance.status],
            'assigned_user': [None, instance.assigned_user.id if instance.assigned_user else None]
        }
    else:
        action = 'Aktualizacja'
        old = Task.objects.get(pk=instance.pk)
        changes = {}
        fields = ['name', 'description', 'status', 'assigned_user']
        for field in fields:
            old_val = getattr(old, field)
            new_val = getattr(instance, field)
            if old_val != new_val:
                if field == 'assigned_user':
                    changes[field] = [
                        old_val.id if old_val else None,
                        new_val.id if new_val else None
                    ]
                else:
                    changes[field] = [old_val, new_val]
    
    if changes:
        TaskHistory.objects.create(
            task=instance,
            changed_by=instance.assigned_user,
            changes=json.dumps(changes)
        )

@receiver(pre_delete, sender=Task)
def log_task_deletion(sender, instance, **kwargs):
    changes = {
        'name': [instance.name, None],
        'description': [instance.description, None],
        'status': [instance.status, None],
        'assigned_user': [
            instance.assigned_user.id if instance.assigned_user else None,
            None
        ]
    }
    TaskHistory.objects.create(
        task=instance,
        changed_by=None,
        changes=json.dumps(changes))
    
@receiver(pre_save, sender=Task)
def save_task_history(sender, instance, **kwargs):
    if not instance.pk:
        return
    try:
        old = Task.objects.get(pk=instance.pk)
    except Task.DoesNotExist:
        return
    changes = {}
    for field in ['name', 'description', 'status', 'assigned_user']:
        old_value = getattr(old, field)
        new_value = getattr(instance, field)
        if old_value != new_value:
            changes[field] = {'old': str(old_value), 'new': str(new_value)}
    if changes:
        TaskHistory.objects.create(
            task=instance,
            changed_by=None,
            changes=changes
        )