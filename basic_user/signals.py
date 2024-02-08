from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import BasicUser

@receiver(pre_save, sender=BasicUser)
def custom_user_pre_save(sender, instance, **kwargs):

    if instance.pk:

        changes = get_patch_changes(instance)


        if changes:
            print(f"Changes in BasicUser instance with id {instance.id} during PATCH request:")
            for field_name, change_data in changes.items():
                print(f"  {field_name}: {change_data['from']} -> {change_data['to']}")


@receiver(post_save, sender=BasicUser)
def custom_user_post_save(sender, instance, created, **kwargs):

    if created:
        print(f"New Basic User instance created.")

def get_patch_changes(instance):

    changes = {}

    try:
        db_instance = BasicUser.objects.get(pk=instance.pk)
    except BasicUser.DoesNotExist:

        return changes


    for field in BasicUser._meta.fields:
        current_value = getattr(instance, field.name)
        previous_value = getattr(db_instance, field.name)
        if current_value != previous_value:
            changes[field.name] = {'from': previous_value, 'to': current_value}

    return changes