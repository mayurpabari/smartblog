from django.contrib import admin

# Register your models here.
#from posts.model import Post. As model and admin both are into same module we can write as below.

from .models import Post, Blog, Author, Entry, Tags

class PostModelAdmin(admin.ModelAdmin):
	list_display = ['title', 'content', 'timestamp', 'updated']
	list_display_links = ['title', 'timestamp']
	list_filter = ['timestamp', 'updated']
	search_fields = ['^title', '^content']
	#list_editable = ['title']
	class Meta: #i am not 100% sure why we write this
		model = Post
		


admin.site.register(Post, PostModelAdmin)

class BlogModelAdmin(admin.ModelAdmin):
	class Meta:
		model = Blog

admin.site.register(Blog, BlogModelAdmin)

class AuthorModelAdmin(admin.ModelAdmin):
	list_display = ['name', 'email'] #i am getting error of author not callable while adding column of author
	class Meta:
		model = Author

admin.site.register(Author, AuthorModelAdmin)

class EntryModelAdmin(admin.ModelAdmin):
	list_display = ['blog', 'headline', 'pub_date','mod_date','n_comments', 'n_pingbacks', 'rating']
	list_filter = ['pub_date', 'n_comments', 'n_pingbacks', 'rating']
	search_fields = ['headline'] #i was getting error of "type error" while taking blog in the search field.
	class Meta:
		model = Entry

admin.site.register(Entry, EntryModelAdmin)


admin.site.register(Tags)