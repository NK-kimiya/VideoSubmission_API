from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User,Video

#、JSON 形式と Django の Model オブジェクトの間の変換を行う

'''
serializers.ModelSerializer を継承
    ・ModelSerializer を使うことで、Djangoのモデル (User) を簡単にJSONに変換できる
    ・ユーザーのデータをシリアル化（JSON化）したり、JSONデータをモデルに変換できる
    
    ※serializers.ModelSerializer を継承すれば、デフォルトで create・update などのメソッドが定義されているが、
    　ユーザー作成時のように独自の処理をしたい場合は、オーバーライドを行う 
'''

class UserSerializer(serializers.ModelSerializer):


    class Meta:
        #get_user_model() を使って Django のカスタムユーザーモデルを取得。
        model = get_user_model()
        #fields にリストを指定すると、シリアライズの対象フィールドを制限できる
        fields = ('email', 'password','username','id')
        #password フィールドに 特別な設定 を適用
        #write_only=True → password は 書き込み専用
        #min_length=5 → 最小5文字の制約を設定
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        #create_user を使って、新しいユーザーを作成
        user = get_user_model().objects.create_user(**validated_data)

        return user

'''
serializers.ModelSerializer を継承
    ・ModelSerializer を使うことで、Djangoのモデル (Video) を簡単にJSONに変換できる
    ・データをシリアル化（JSON化）したり、JSONデータをモデルに変換できる
'''
class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        #Video モデルのフィールドを JSON で出力できるようにする
        model = Video
        #シリアライズの対象フィールドを制限
        fields = ['id','title','video','thum','like','dislike']