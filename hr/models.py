from django.db import models


class hr_staff(models.Model):
    LastName = models.CharField('Фамилия', max_length=75)
    Name = models.CharField('Имя', max_length=75)
    MiddleName = models.CharField('Отчество', max_length=75)
    BirthDate = models.DateField('Дата рождения')
    Salary = models.FloatField('Оклад сотрудника')
    ViewStaff = models.CharField('Представление сотрудника', max_length=250)

    def __str__(self):
        return self.ViewStaff
        #return f'Сотрудник: {self.ViewStaff}'

    def get_absolute_url(self):
        return f'/{self.id}'


    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
