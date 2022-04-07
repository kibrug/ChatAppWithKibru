from django.contrib import admin

from .models import Post,AdvantagesofVerticalFarming,LeadersofVerticalFarming,WhatisVerticalFarming

admin.site.register(Post)
admin.site.register(WhatisVerticalFarming)
admin.site.register(AdvantagesofVerticalFarming)
admin.site.register(LeadersofVerticalFarming)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title',  'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    #prepopulated_fields = {'slug': ('title')}

#admin.site.register( PostAdmin)
