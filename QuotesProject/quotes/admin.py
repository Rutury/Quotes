from django.contrib import admin
import quotes.models as models
# Register your models here.

@admin.register(models.Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('quote', 'views', 'likes', 'dislikes', 'weight', 'source')
