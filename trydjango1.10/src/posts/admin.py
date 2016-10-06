from django.contrib import admin

# Register your models here.
# .models because models and admin are in the same Location/Directry
from .models import Post   

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "updated", "timestamp"]
	list_display_links = ["updated"]
	list_filter = ["title", "updated", "timestamp"]
	list_editable = ["title"]
	search_fields = ["title", "content"]
	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)
