from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime

# Create your models here.


class Segment(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class CA(models.Model):

    SEGMENT = (
        ('Onglerie', 'Onglerie'),
        ('Epilation', 'Epilation'),
        ('Prestations corps', 'Prestations corps'),
        ('Prestations visage', 'Prestations visage'),
        ('Maquillage', 'Maquillage')
    )
    YEAR = tuple((str(i), str(i)) for i in range(
        2010, int(datetime.date.today().strftime("%Y")) + 1))  # Obtenir la liste des années en format string de 2010 à aujourd'hui.
    MONTH = (("01", "01"), ("02", "02"), ("03", "03"), ("04", "04"), ("05", "05"), ("06", "06"),
             ("07", "07"), ("08", "08"), ("09",
                                          "09"), ("10", "10"), ("11", "11"), ("12", "12")
             )
    month = models.CharField(max_length=200, null=True, choices=MONTH)
    year = models.CharField(max_length=200, null=True, choices=YEAR)
    montant = models.FloatField(null=True)
    company = models.CharField(max_length=200, null=True)
    author = models.ForeignKey(to=User, null=True,
                               on_delete=models.CASCADE)
    segment = models.CharField(max_length=200, null=True, choices=SEGMENT)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date = models.DateTimeField(null=True)

    def __str__(self):
        return 'CA de '+str(self.month) + '/' + str(self.year)

    def save(self, *args, **kwargs):
        date_str = self.month + "-" + self.year[-2:]
        date_ca = datetime.datetime.strptime(date_str, "%m-%y")
        self.date = date_ca

        super(CA, self).save(*args, **kwargs)  # Call the "real" save() method.


class Profile(models.Model):

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    company = models.CharField(max_length=200, null=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    postal_code = models.IntegerField(null=True)
    city = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    segments = models.ManyToManyField(Segment)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.user)


def create_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance, company=instance.username)
        print('Profile created')


post_save.connect(create_profile, sender=User)


def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.profile.save()
        print('Profile created')
        print()
        try:
            instance.profile.save()
            print('profile updated')
        except:
            Profile.objects.create(user=instance)
            print('Profile created for existing user!')


post_save.connect(update_profile, sender=User)



