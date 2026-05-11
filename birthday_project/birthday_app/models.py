from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/')
    caption = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    is_favorite = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title

class LoveMessage(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message from {self.created_at}"

class BirthdayWish(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}: {self.message[:50]}"

# NEW MODEL FOR PICKUP LINES
class PickupLine(models.Model):
    question = models.CharField(max_length=500, help_text="The pickup line question to ask")
    expected_keywords = models.CharField(max_length=500, help_text="Comma-separated keywords that will trigger the sweet response (e.g., 'time,clock,what time')")
    sweet_response = models.TextField(help_text="The romantic response to show after she answers")
    hint = models.CharField(max_length=200, blank=True, help_text="A small hint to help her answer")
    order = models.IntegerField(default=0, help_text="Order in which questions appear")
    is_active = models.BooleanField(default=True, help_text="Show this pickup line in the game")
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.order}. {self.question[:50]}"
    
    def get_keywords_list(self):
        """Convert comma-separated keywords to a list"""
        return [keyword.strip().lower() for keyword in self.expected_keywords.split(',')]