import os.path

from django.db import models
import uuid


class DishType(models.Model):
    dish_type_name = models.CharField(max_length=50, unique=True, verbose_name="Назва категорії")
    dish_type_order = models.PositiveIntegerField(unique=True, verbose_name="Порядок")
    dish_type_access = models.BooleanField(default=True, verbose_name="Доступ")

    def __str__(self):
        return f"{self.dish_type_name}"

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"
        ordering = ("dish_type_order", )


class Menu(models.Model):
    def get_file_name(self, filename):
        tmp = filename.strip().split('.')[-1]
        filename = f"{uuid.uuid4()}.{tmp}"
        return os.path.join('images/dishes/', filename)

    dish_name = models.CharField(max_length=50, unique=True, verbose_name="Назва стави")
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, verbose_name="Тип страви")
    dish_cost = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Вартість")
    dish_ingredients = models.CharField(max_length=300)
    dish_access = models.BooleanField(default=True, verbose_name="Доступ")
    dish_order = models.SmallIntegerField(verbose_name="Порядок")
    dish_is_special = models.BooleanField(default=False, verbose_name="Спеціальна")
    dish_image = models.ImageField(upload_to=get_file_name)
    dish_about = models.TextField(blank=True)

    def __str__(self):
        return f"{self.dish_type.dish_type_name}: {self.dish_order}: {self.dish_name}"

    class Meta:
        verbose_name = "Страва"
        verbose_name_plural = "Страви"
        ordering = ("dish_type", "dish_order")


class Events(models.Model):
    def get_file_name(self, filename):
        tmp = filename.strip().split('.')[-1]
        filename = f"{uuid.uuid4()}.{tmp}"
        return os.path.join('images/gallery/', filename)
    event_order = models.SmallIntegerField(unique=True, default=0, verbose_name="Порядок")
    event_title = models.TextField(verbose_name="Заголовок")
    event_cost = models.PositiveIntegerField(verbose_name="Вартість")
    event_about_start = models.TextField(verbose_name="Пролог")
    event_about1 = models.TextField(blank=True, verbose_name="Про п.1")
    event_about2 = models.TextField(blank=True, verbose_name="Про п.2")
    event_about3 = models.TextField(blank=True, verbose_name="Про п.3")
    event_about_finish = models.TextField(blank=True, verbose_name="Епілог")
    event_image = models.ImageField(upload_to=get_file_name, null=True, default="", verbose_name="Фото")

    def __str__(self):
        return f"{self.event_order}: {self.event_title}"

    class Meta:
        verbose_name = "Евент"
        verbose_name_plural = "Евенти"
        ordering = ("event_order", )



class About(models.Model):
    about_title = models.TextField(verbose_name="Заголовок")
    about_start_text = models.TextField(verbose_name="Епілог")
    about_p1 = models.TextField(verbose_name="Про п.1")
    about_p2 = models.TextField(blank=True, verbose_name="Про п.1")
    about_p3 = models.TextField(blank=True, verbose_name="Про п.2")
    about_end = models.TextField(blank=True, verbose_name="Про п.3")

    def __str__(self):
        return self.about_title

    class Meta:
        verbose_name = "Про нас"
        verbose_name_plural = "Про нас"


class Gallery(models.Model):
    def get_file_name(self, filename):
        tmp = filename.strip().split('.')[-1]
        filename = f"{uuid.uuid4()}.{tmp}"
        return os.path.join('images/gallery/', filename)

    photo = models.ImageField(upload_to=get_file_name, verbose_name="Фото")
    visible = models.BooleanField(default=True, verbose_name="Доступ")

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галерея"
        ordering = ("photo", )

    def __str__(self):
        return self.photo.__str__()


class Carousel(models.Model):
    def get_file_name(self, filename):
        tmp = filename.strip().split('.')[-1]
        filename = f"{uuid.uuid4()}.{tmp}"
        return os.path.join('images/gallery/', filename)

    carousel_name = models.CharField(max_length=30, verbose_name="Заголовок")
    carousel_about = models.TextField(verbose_name="Опис")
    carousel_image = models.ImageField(upload_to=get_file_name, verbose_name="Фото")
    carousel_access = models.BooleanField(default=True, verbose_name="Доступ")

    def __str__(self):
        return self.carousel_name

    class Meta:
        verbose_name = "Карусель"
        verbose_name_plural = "Карусель"


class Whuus(models.Model):
    whuus_order = models.SmallIntegerField(unique=True, verbose_name="Порядок")
    whuus_title = models.CharField(max_length=20, verbose_name="Заголовок")
    whuus_about = models.CharField(max_length=100, verbose_name="Опис")

    def __str__(self):
        return self.whuus_title

    class Meta:
        verbose_name = "Чому ми"
        verbose_name_plural = "Чому ми"
        ordering = ("whuus_order",)


class Chefs(models.Model):
    def get_file_name(self, filename):
        tmp = filename.strip().split('.')[-1]
        filename = f"{uuid.uuid4()}.{tmp}"
        return os.path.join('images/gallery/', filename)
    chefs_order = models.SmallIntegerField(unique=True)
    chefs_name = models.CharField(max_length=20, verbose_name="Ім'я")
    chefs_role = models.CharField(max_length=20, verbose_name="Роль")
    chefs_twitter = models.CharField(max_length=50, verbose_name="Твітер", blank=True)
    chefs_facebook = models.CharField(max_length=50, verbose_name="Фейсбук", blank=True)
    chefs_instagram = models.CharField(max_length=50, verbose_name="Інстаграм", blank=True)
    chefs_linkedin = models.CharField(max_length=50, verbose_name="Лінкедін", blank=True)
    chefs_image = models.ImageField(upload_to=get_file_name, verbose_name="Фото")

    def __str__(self):
        return self.chefs_name

    class Meta:
        verbose_name = "Шеф-кухар"
        verbose_name_plural = "Шеф-кухарі"
        ordering = ("chefs_order", )


class Testimonials(models.Model):
    def get_file_name(self, filename):
        tmp = filename.strip().split('.')[-1]
        filename = f"{uuid.uuid4()}.{tmp}"
        return os.path.join('images/gallery/', filename)
    test_order = models.SmallIntegerField(unique=True, verbose_name="Порядок")
    test_name = models.CharField(max_length=20, verbose_name="Ім'я")
    test_role = models.CharField(max_length=20, verbose_name="Роль")
    test_about = models.CharField(max_length=200, verbose_name="Опис")
    test_image = models.ImageField(upload_to=get_file_name, verbose_name="Фото")

    def __str__(self):
        return  self.test_name

    class Meta:
        verbose_name = "Програмісти сайту?"
        verbose_name_plural = "Програмісти сайту?"
        ordering = ("test_order", )


class Contacts(models.Model):
    location1 = models.CharField(max_length=50, verbose_name="Локація 1")
    location2 = models.CharField(max_length=50, blank=True, verbose_name="Локація 2")
    open_hours1 = models.CharField(max_length=50, verbose_name="Відчинено 1")
    open_hours2 = models.CharField(max_length=50, blank=True, verbose_name="Відчинено 2")
    email1 = models.CharField(max_length=50, verbose_name="Мейл 1")
    email2 = models.CharField(max_length=50, blank=True, verbose_name="Мейл 2")
    call1 = models.CharField(max_length=50, verbose_name="Телефон 1")
    call2 = models.CharField(max_length=50, blank=True, verbose_name="Телефон 2")

    def __str__(self):
        return "Основна інформація"

    class Meta:
        verbose_name = "Контакти"
        verbose_name_plural = "Контакти"


