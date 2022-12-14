from .tasks import convert_480p
from .models import Video
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
import os

@receiver(post_save, sender=Video)
# def video_post_save(sender, instance, created, **kwargs):
#     print('Video wurde gespeichert')
#     if created:
#         print('New Video is created')
#         convert_480p(instance.video_file.path)

# @receiver(post_delete, sender=Video)
# def auto_delete_file_on_delete(sender, instance, **kwargs):
#     """
#     Deletes file from filesystem
#     when corresponding `Video` object is deleted.
#     """
#     if instance.video_file:
#         if os.path.isfile(instance.video_file.path):
#             os.remove(instance.video_file.path)

def video_post_save(sender, instance, created, **kwargs):
    print("Video wurde gespeichert")
    if created:
        print("Video wurde neu erstellt")
       
        print(instance.video_file.path)
        convert_480p(instance.video_file.path)
        # convert_480p(instance.video_file.path)


@receiver(post_delete, sender=Video)
def video_post_delete(sender, instance, *args, **kwargs):
    if instance.video_file:
        if os.path.isfile(instance.video_file.path):
            os.remove(instance.video_file.path)