from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from django.db.models.signals import m2m_changed
from taggit.models import Tag
from .models import Phones



@receiver(post_save, sender=Phones)
def clear_phones_cache_after_save(sender, instance, **kwargs):
    cache.delete("home:latest_phones")


@receiver(post_delete, sender=Phones)
def clear_phones_cache_after_delete(sender, instance, **kwargs):
    cache.delete("home:latest_phones")



@receiver(post_save, sender=Tag)
def clear_cache_after_tag_save(sender, instance, **kwargs):
    print("🔥 TAG MODEL SAVED")

    cache.delete("home:tags")
    cache.delete("home:latest_phones")

    print("🗑️ TAG CACHES DELETED")


@receiver(post_delete, sender=Tag)
def clear_cache_after_tag_delete(sender, instance, **kwargs):
    print("🔥 TAG MODEL DELETED")

    cache.delete("home:tags")
    cache.delete("home:latest_phones")

    print("🗑️ TAG CACHES DELETED")