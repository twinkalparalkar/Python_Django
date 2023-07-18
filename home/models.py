from django.db import models
import uuid
import os

class Folder(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created_at=models.DateField(auto_now_add=True)

def get_upload_to_path(instance,filename):
    return os.path.join(str(instance.folder.uid),filename)

class File(models.Model):
    folder=models.ForeignKey(Folder,on_delete=models.CASCADE, related_name='folder')
    file=models.FileField( upload_to=get_upload_to_path)
    created_at=models.DateField(auto_now_add=True)