from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid

'''
動画ファイル (.mp4) とサムネイル画像の保存パスを設定する
'''
def load_path_video(instance, filename):#instance：Videoモデルのインスタンス　filename：アップロードされたファイルの元の名前
    #videoフォルダ内にVideoモデルのタイトル.mp4という名前で保存
    return '/'.join(['video', str(instance.title)+str(".mp4")])

def load_path_thum(instance, filename):#instance：Videoモデルのインスタンス　filename：アップロードされたファイルの元の名前
    #拡張子を取得
    ext = filename.split('.')[-1]
    #もとの拡張子を維持したままthumフォルダ内にVideoモデルのタイトル.拡張子という名前で保存
    return '/'.join(['thum', str(instance.title)+str(".")+str(ext)])

'''
ユーザーを作成・管理するためのマネージャー
'''
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        #メールアドレスが空かどうかチェック
        if not email:
            raise ValueError('Email address is must')

        #ユーザーオブジェクトを作成
        #メールの正規化・追加のフィールド(usernameなど)を受取れるようにする。
        user = self.model(email=self.normalize_email(email), **extra_fields)
        #パスワードをハッシュ化して保存
        user.set_password(password)
        #ユーザーをデータベースに保存
        user.save(using=self._db)

        #作成したユーザーを返す
        return user

    def create_superuser(self, email, password):
        #create_user を呼び出して、基本的なユーザーを作成
        user = self.create_user(email, password)
        #Djangoの管理画面にアクセスできる権限を付与
        user.is_staff = True
        #すべての権限を持つスーパーユーザーにする
        user.is_superuser = True
        #スーパーユーザーを返す
        user.save(using=self._db)

        return user


'''
カスタムユーザーモデルの定義
'''
class User(AbstractBaseUser, PermissionsMixin):

    #ユーザーのidをランダムにする
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, editable=False)

    #メールアドレスを重複禁止で定義
    email = models.EmailField(max_length=255, unique=True)
    #ユーザー名を定義・必須ではない
    username = models.CharField(max_length=255, blank=True)
    #ユーザーのアクティブ状態を管理・Falseにすると、ユーザーのアカウントが無効化
    is_active = models.BooleanField(default=True)
    #管理画面（Django Admin）にアクセスできるかどうかを示すフラグ・Trueにすると管理者としてログインできる。
    is_staff = models.BooleanField(default=False)

    #UserManager を objects にセットし、ユーザーの作成ロジックを統一 する
    objects = UserManager()

    #Djangoのデフォルトでは username をユーザー名として使用するが、メールアドレスでログインできるようにするため、USERNAME_FIELD を email に設定
    USERNAME_FIELD = 'email'

    #print(user) などをしたときに、デフォルトで ユーザーのメールアドレスを表示 する
    def __str__(self):
        return self.email

class Video(models.Model):
    #idを定義
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, editable=False)
    #タイトルとして文字列を定義
    title = models.CharField(max_length=30, blank=False)
    #ビデオファイルを定義：ファイルはload_path_videoの処理内容の通りに格納
    video = models.FileField(blank=False, upload_to=load_path_video)
    #画像ファイルを格納：load_path_thumの処理内容の通りに格納
    thum = models.ImageField(blank=False,  upload_to=load_path_thum)
    #いいねを推すと数値を1つ増やす
    like = models.IntegerField(default=0)
    # 低評価を推すと数値を1つ増やす
    dislike = models.IntegerField(default=0)

    def __str__(self):
        return self.title
