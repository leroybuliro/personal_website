from django.contrib import admin
from .models import *

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}
    list_display = ('id','name', 'location')
admin.site.register(Event, EventAdmin)

class ArticleCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}
    list_display = ('id','name')
admin.site.register(ArticleCategory, ArticleCategoryAdmin)

class ArticleTagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}
    list_display = ('id','name')
admin.site.register(ArticleTag, ArticleTagAdmin)

class ArticleStatAdmin(admin.ModelAdmin):
    list_display = ('IPAddres','article','visited')
    readonly_fields = ('IPAddres', 'article', 'device', 'visited')
admin.site.register(ArticleStat, ArticleStatAdmin)

class StatAdmin(admin.ModelAdmin):
    list_display = ('IPAddres','page','visited')
    readonly_fields = ('IPAddres', 'page', 'device', 'visited')
admin.site.register(Stat, StatAdmin)

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',),}
    list_display = ('id', 'title', 'category', 'publishdate', 'status')
admin.site.register(Article, ArticleAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','content_type','object_id','parent','content','timestamp')
    # readonly_fields = ('user', 'content', 'timestamp')
admin.site.register(Comment, CommentAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id','postdate','content','ratings')
    readonly_fields = ('postdate','content','ratings','source')
admin.site.register(Feedback, FeedbackAdmin)

class MailingAdmin(admin.ModelAdmin):
    list_display = ('id','date','email')
    readonly_fields = ('date','email')
admin.site.register(Mailing, MailingAdmin)