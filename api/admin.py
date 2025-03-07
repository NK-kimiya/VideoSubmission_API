from django.contrib import admin
from .models import Video,User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

'''
カスタムユーザーモデルを適切に表示・管理するための設定
'''
class UserAdmin(BaseUserAdmin):#BaseUserAdmin を継承し、カスタムユーザーモデル (User モデル) を Django の管理画面で適切に表示・管理できるようにする。
    #管理画面で ユーザーを id の昇順（古い順）で表示
    ordering = ['id']
    #管理画面のユーザー一覧ページ で表示する項目を指定
    list_display = ['email', 'username']
    #編集ページのフィールド設定
    fieldsets = (
        (None, {'fields': ('email', 'password')}),#見出しを表示せず、メールアドレスとパスワードを入力するフォームを表示
        (_('Personal Info'), {'fields': ('username',)}),#"Personal Info" という見出しをつけ、ユーザー名を入力できるフォームを表示
        (
            _('Permissions'),#"Permissions" という見出しをつけ、 ユーザーのアクティブ状態や管理者権限を設定するチェックボックス を表示
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),#最後にログインした日時を表示
    )
    #新規ユーザー作成時の入力項目：管理画面で新しいユーザーを追加するときの入力フィールドを設定
    add_fieldsets = (
        (None, {
            'classes': ('wide',),#入力フォームを広くする
            'fields': ('email', 'password1', 'password2')#	メールとパスワードを入力
        }),
    )
admin.site.register(User,UserAdmin)
admin.site.register(Video)

#管理ユーザー
'''
superuser@gmail.com
super
'''