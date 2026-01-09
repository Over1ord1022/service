from django.db import models
from django.contrib.auth.models import User


# УСЛУГА
class Service(models.Model):
    freelancer = models.ForeignKey(User, on_delete=models.CASCADE)  # Исполнитель
    title = models.CharField(max_length=255)  # Название услуги
    description = models.TextField()  # Описание
    category = models.CharField(max_length=100)  # Категория
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания

    def __str__(self):
        return self.title


# ЗАКАЗ
class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)  # Клиент
    service = models.ForeignKey(Service, on_delete=models.CASCADE)  # Какая услуга
    status = models.CharField(max_length=50)  # Статус: "в работе", "завершен" и т.д.
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # Сумма заказа
    deadline = models.DateField()  # Срок выполнения
    created_at = models.DateTimeField(auto_now_add=True)  # Дата заказа

    def __str__(self):
        return f"Заказ #{self.id}"

# ОТЗЫВ
class Review(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  # К какому заказу
    rating = models.IntegerField()  # Оценка от 1 до 5
    comment = models.TextField()  # Текст отзыва
    created_at = models.DateTimeField(auto_now_add=True)  # Дата отзыва

    def __str__(self):
        return f"Отзыв на заказ #{self.order.id}"