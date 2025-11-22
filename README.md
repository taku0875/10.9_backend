# Me-Tore! Backend (めトレ！ バックエンド)

「めトレ！」のバックエンドAPIサーバーです。FastAPIを使用しています。

## 前提条件 (Prerequisites)
- Python 3.8以上

## セットアップ (Setup)

### 1. 仮想環境の作成と有効化
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 2. 依存関係のインストール
```bash
pip install -r requirements.txt
```

## 起動方法 (How to Run)

以下のコマンドでサーバーを起動します。

```bash
uvicorn main:app --reload --host 0.0.0.0
```

サーバーは `http://localhost:8000` で起動します。
APIドキュメントは `http://localhost:8000/docs` で確認できます。
