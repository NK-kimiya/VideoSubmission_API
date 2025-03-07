from rest_framework import viewsets
from rest_framework import generics
from .serializers import VideoSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from .models import Video

# Create your views here.
#リクエストがデータを作成するものか、取得するものかを判断

'''
ユーザー作成API
'''
#CreateAPIView を継承し、新規ユーザーを作成するAPI を提供
class CreateUserView(generics.CreateAPIView):
    #serializer_class = UserSerializer → UserSerializer を使用 してユーザー情報を処理
    serializer_class = UserSerializer
    #permission_classes = (AllowAny,) → 認証なしでアクセス可能
    permission_classes = (AllowAny,)

'''
動画データのCRUD（作成・取得・更新・削除）を提供
'''
#ModelViewSet を継承 → 自動的に list, retrieve, create, update, destroy のメソッドを持つ
class VideoViewSet(viewsets.ModelViewSet):
    #queryset = Video.objects.all() → すべての動画を取得できるようにする
    queryset = Video.objects.all()
    #serializer_class = VideoSerializer → VideoSerializer を使用
    serializer_class = VideoSerializer





