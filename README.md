✅インストールライブラリ

djangorestframework, django-cors-headers, djoser, djangorestframework-simplejwt,pillow


✅youtube_api ディレクトリ（Djangoプロジェクト）

| ファイル | 役割 |
| --- | --- |
| settings.py | Djangoの設定ファイル |
| urls.py | プロジェクト全体のルーティング設定 |
| asgi.py/wsgi.py | ASGI / WSGI アプリケーションのエントリーポイント |
| __init__.py | 	パッケージとして認識させるためのファイル |


✅api ディレクトリ（Djangoアプリ）

| ファイル | 役割 |
| --- | --- |
| models.py | データベースのテーブル |
| serializers.py | モデルをJSONに変換（シリアライザー） |
| views.py | APIの処理を記述（APIView などを実装） |
| urls.py | api アプリのルーティング設定 |
| admin.py | Django管理画面へのモデル登録 |
| apps.py | api アプリの設定 \
