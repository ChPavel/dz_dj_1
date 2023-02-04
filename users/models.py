from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.name


# class UserRole: # вариант с разбора
#     MEMBER = "member"
#     MODERATOR = "moderator"
#     ADMIN = "admin"
#     choices = ((MEMBER, 'Пользователь'), (MODERATOR, 'Модератор'), (ADMIN, 'Администратор'))


class User(models.Model):
    ROLES = [
        ("admin", "Администратор"),
        ("moderator", "Модератор"),
        ("member", "Пользователь"),
    ]
    first_name = models.CharField(verbose_name='Имя', max_length=100, null=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=100, null=True)
    username = models.CharField(verbose_name='Логин', max_length=100, unique=True)
    password = models.CharField(verbose_name='Пароль', max_length=100)
    role = models.CharField(max_length=10, choices=ROLES, default="member")
    # role = models.CharField(choices=UserRole.choices, default=UserRole.MEMBER, max_length=10) # вариант с разбора
    age = models.PositiveSmallIntegerField()
    location = models.ManyToManyField(Location)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
