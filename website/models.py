from django.db import models
#from datetime import date

# Create your models here.
class articles(models.Model):
    titre = models.CharField(max_length=255, primary_key=True,)
    icon = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)
    contenue = models.TextField(default="")
    titre_block_1 = models.CharField(max_length=255)
    image_block_1 = models.ImageField(null=True, blank=True, upload_to="images/")
    block_1 = models.TextField(default="")
    titre_block_2 = models.CharField(max_length=255, null=True, blank=True)
    image_block_2 = models.ImageField(null=True, blank=True, upload_to="images/")
    block_2 = models.TextField(null=True, blank=True, default="")
    titre_block_3 = models.CharField(max_length=255, null=True, blank=True)
    image_block_3 = models.ImageField(null=True, blank=True, upload_to="images/")
    block_3 = models.TextField(null=True, blank=True, default="")
    titre_block_4 = models.CharField(blank=True, max_length=255, null=True)
    image_block_4 = models.ImageField(null=True, blank=True, upload_to="images/")
    block_4 = models.TextField(blank=True, null=True, default="")
    titre_block_5 = models.CharField(blank=True, max_length=255, null=True)
    image_block_5 = models.ImageField(null=True, blank=True, upload_to="images/")
    block_5 = models.TextField(blank=True, null=True, default="")
    titre_block_6 = models.CharField(blank=True, max_length=255, null=True)
    image_block_6 = models.ImageField(null=True, blank=True, upload_to="images/")
    block_6 = models.TextField(blank=True, null=True, default="")

    def __str__(self):
        return self.titre + ' | ' + str(self.date)

class metiers(models.Model):
     titre = models.CharField(max_length=255, primary_key=True,)
     image = models.ImageField(null=True, blank=True, upload_to="images/")
     date = models.DateField(auto_now=True)
     contenue = models.TextField(default="")
     description = models.TextField(default="")

class programmes(models.Model):
     titre = models.CharField(max_length=255, primary_key=True,)
     image = models.ImageField(null=True, blank=True, upload_to="images/")
     date = models.DateField(auto_now=True)
     contenue = models.TextField(default="")
     description = models.TextField(default="")
     licence = models.BooleanField(default=False)
     master = models.BooleanField(default=False)
     licence_sem_1_titre = models.CharField(max_length=255)
     licence_sem_1_mod1_titre = models.CharField(max_length=255)
     licence_sem_1_mod1 = models.TextField(default="")
     licence_sem_1_mod2_titre = models.CharField(max_length=255)
     licence_sem_1_mod2 = models.TextField(default="")
     licence_sem_2_titre = models.CharField(max_length=255)
     licence_sem_2_mod1_titre = models.CharField(max_length=255)
     licence_sem_2_mod1 = models.TextField(default="")
     licence_sem_2_mod2_titre = models.CharField(max_length=255)
     licence_sem_2_mod2 = models.TextField(default="")
     licence_sem_2_fin = models.TextField(default="")
     licence_sem_3_titre = models.CharField(max_length=255)
     licence_sem_3_mod1_titre = models.CharField(max_length=255)
     licence_sem_3_mod1 = models.TextField(default="")
     licence_sem_3_mod2_titre = models.CharField(max_length=255)
     licence_sem_3_mod2 = models.TextField(default="")
     licence_sem_4_titre = models.CharField(max_length=255)
     licence_sem_4_mod1_titre = models.CharField(max_length=255)
     licence_sem_4_mod1 = models.TextField(default="")
     licence_sem_4_mod2_titre = models.CharField(max_length=255)
     licence_sem_4_mod2 = models.TextField(default="")
     licence_sem_4_fin = models.TextField(default="")
     licence_sem_5_titre = models.CharField(max_length=255)
     licence_sem_5_mod1_titre = models.CharField(max_length=255)
     licence_sem_5_mod1 = models.TextField(default="")
     licence_sem_5_mod2_titre = models.CharField(max_length=255)
     licence_sem_5_mod2 = models.TextField(default="")
     licence_sem_6_titre = models.CharField(max_length=255)
     licence_sem_6_mod1_titre = models.CharField(max_length=255)
     licence_sem_6_mod1 = models.TextField(default="")
     licence_sem_6_mod2_titre = models.CharField(max_length=255)
     licence_sem_6_mod2 = models.TextField(default="")
     licence_sem_6_fin = models.TextField(default="")
     master_sem_1_titre = models.CharField(blank=True, null=True, max_length=255)
     master_sem_1_mod1_titre = models.CharField(blank=True, null=True, max_length=255)
     master_sem_1_mod1 = models.TextField(blank=True, null=True, default="")
     master_sem_1_mod2_titre = models.CharField(blank=True, null=True, max_length=255)
     master_sem_1_mod2 = models.TextField(blank=True, null=True, default="")
     master_sem_2_titre = models.CharField(blank=True, null=True, max_length=255)
     master_sem_2_mod1_titre = models.CharField(blank=True, null=True, max_length=255)
     master_sem_2_mod1 = models.TextField(blank=True, null=True, default="")
     master_sem_2_mod2_titre = models.CharField(blank=True, null=True, max_length=255)
     master_sem_2_mod2 = models.TextField(blank=True, null=True, default="")
     master_sem_2_fin = models.TextField(blank=True, null=True, default="")
     master_sem_3_titre = models.CharField(blank=True, null=True, max_length=255)
     master_sem_3_mod1_titre = models.CharField(blank=True, null=True, max_length=255)
     master_sem_3_mod1 = models.TextField(blank=True, null=True, default="")
     master_sem_3_mod2_titre = models.CharField(blank=True, null=True, max_length=255)
     master_sem_3_mod2 = models.TextField(blank=True, null=True, default="")
     master_sem_4_titre = models.CharField(blank=True, null=True, max_length=255)
     master_sem_4_mod1_titre = models.CharField(blank=True, null=True, max_length=255)
     master_sem_4_mod1 = models.TextField(blank=True, null=True, default="")
     master_sem_4_mod2_titre = models.CharField(blank=True, null=True, max_length=255)
     master_sem_4_mod2 = models.TextField(blank=True, null=True, default="")
     master_sem_4_fin = models.TextField(blank=True, null=True, default="")
     

class details(models.Model):
     titre = models.CharField(max_length=255, primary_key=True,)
     contenue = models.TextField(default="")
     description = models.TextField(default="")