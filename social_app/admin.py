from django.contrib import admin
from .models import FacebookAccount, FacebookPost


@admin.register(FacebookAccount)
class FacebookAccountAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'facebook_id', 'email', 'fecha_vinculacion')
    search_fields = ('nombre', 'facebook_id', 'email')
    readonly_fields = ('fecha_vinculacion',)


@admin.register(FacebookPost)
class FacebookPostAdmin(admin.ModelAdmin):
    list_display = (
        'account',
        'estado',
        'fecha_publicacion',
        'likes',
        'comentarios',
        'compartidos',
        'alcance',
        'engagement_total',
    )
    list_filter = ('estado',)
    search_fields = ('mensaje', 'post_id')
    readonly_fields = ('fecha_publicacion', 'fecha_actualizacion')
