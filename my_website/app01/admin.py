from django.contrib import admin
from app01 import models
# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ('username','email','signature')
    search_fields = ('username','email')
    list_per_page = 5
    list_editable = ['signature',]


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','account','get_tags')
    list_filter = ('account','pub_date')
    #fields = ('title','content','pub_date')
    date_hierarchy = ('pub_date')

    fieldsets = (
        ('Article About',{
            'fields':['title','content'],
            'classes':('wide','extrapretty'),
        }),(
            'Advanced',{
                # 'classes':('collapse',),  collapse the advanced part
                'fields':('account','tags','pub_date',)
            }
        )
    )
    autocomplete_fields = ['account',]  # Only for FK
    # radio_fields = {'account': admin.VERTICAL}  Only for FK
    filter_horizontal = ('tags',)  # Only for many2many

admin.site.register(models.Account, AccountAdmin)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Tag)