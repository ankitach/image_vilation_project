from django.db import models
# Create your models here.

# Create your models here.
class vid_stream_cameras(models.Model):
    id=models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')   #integer NOT NULL,
    camera=models.CharField()   #character varying(100) NOT NULL,
    password=models.CharField()   #character varying(100) NOT NULL,
    ip=models.CharField()   #character varying(100) NOT NULL,
    cam_location= models.CharField()   #character varying(100) NOT NULL,
    Model_no= models.CharField()   #character varying(100) NOT NULL,
    Serial_no= models.CharField()   #character varying(100) NOT NULL,
    Port= models.CharField()   #character varying(100) NOT NULL,
    analytics= models.BooleanField()   #boolean NOT NULL,
    video =models.BooleanField()   #boolean NOT NULL,
    localhost= models.CharField()   #character varying(100),
    
    def __str__(self):
        return self.camera
    

class vid_stream_violations(models.Model):
    id=models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    viol_date=models.DateField()
    viol_time=models.TimeField()
    violations=models.CharField(max_length=100)
    viol_suit=models.IntegerField()
    viol_without_suit=models.IntegerField()
    viol_Camera_id = models.ForeignKey(vid_stream_cameras, on_delete=models.CASCADE)
    def __str__(self):
        return "%s " %(self.viol_Camera_id)

