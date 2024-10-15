from django.db import models
from django.contrib.auth.models import User

# โมเดลลโปรไฟลล์
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username}'


# โมเดลร้านอาหาร
class Restaurant(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    opening_hours = models.TextField()
    social_media = models.TextField(null=True, blank=True)
    images = models.ImageField(upload_to='restaurant_images/', null=True, blank=True)  # รูปโปรไฟล์ร้าน

    def __str__(self):
        return self.name

class RestaurantImage(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='additional_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='restaurant_additional_images/',null=True, blank=True)

    def __str__(self):
        return f'{self.restaurant.name} - Image'

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name



# โมเดลหมวดหมู่และหมวดหมู่ย่อยของอาหาร
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.category.name} - {self.name}'

# โมเดลอาหาร ที่เชื่อมกับร้านอาหาร
class Food(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='foods')  # เชื่อมกับร้านอาหาร
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='foods')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='foods')
    image = models.ImageField(upload_to='food_images/', null=True, blank=True)  # รูปภาพอาหาร

    def __str__(self):
        return f'{self.name} - {self.restaurant.name}'


# โมเดลความคิดเห็นร้านอาหาร
class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)  # เชื่อมกับร้านอาหาร
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # เชื่อมกับผู้ใช้
    rating = models.IntegerField()  # คะแนนที่ผู้ใช้ให้ (1-5 ดาว)
    comment = models.TextField()  # ข้อความแสดงความคิดเห็น
    created_at = models.DateTimeField(auto_now_add=True)  # วันที่และเวลาที่แสดงความคิดเห็น

    def __str__(self):
        return f'Review by {self.user.username} on {self.restaurant.name}'



# โมเดลกระทู้
class Thread(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# โมเดลความคิดเห็นในกระทู้
class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user} on {self.thread}'




