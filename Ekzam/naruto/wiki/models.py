from django.db import models


class Village(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(blank=True,null=True,upload_to='Villages_picture/')
    description = models.FileField(blank=True,null=True,upload_to='Villages_description/')

    def __str__(self):
        return self.name


class Battle(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(blank=True, null=True, upload_to='Battle_picture/')
    description = models.FileField(blank=True, null=True, upload_to='Battle_description/')

    def __str__(self):
        return self.name


class Technics(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(blank=True, null=True, upload_to='Technics_picture/')
    description = models.FileField(blank=True, null=True, upload_to='Technics_description/')
    Chakra_Status = (
        ('Фууто́н', 'Ветер'),
        ('Райто́н', 'Молнии'),
        ('Като́н', 'Огонь'),
        ('Суйто́н', 'Вода'),
        ('Дото́н', 'Земля'),
    )
    chakra = models.CharField(max_length= 15, choices=Chakra_Status, blank=True, default='Ве')

    def __str__(self):
        return self.name


class Shinobi(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(blank=True, null=True, upload_to='Shinobi_picture/')
    description = models.FileField(blank=True, null=True, upload_to='Shinobi_description/')
    village = models.ForeignKey(Village,on_delete=models.SET_NULL , blank = True , null = True)
    battle = models.ManyToManyField(Battle)
    technics = models.ManyToManyField(Technics)

    def __str__(self):
        return self.name
