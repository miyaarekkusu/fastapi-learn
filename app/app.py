from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse

# FastAPI起動
app = FastAPI()
text_posts = {
    1: {"title": "新規投稿", "content": "面白いテスト用投稿"},
    2: {"title": "今日のお昼ご飯", "content": "近くにできた新しいラーメン屋に行きました。とても美味しかったです！"},
    3: {"title": "テスト投稿（長文）", "content": "この投稿はシステムが長い文章を正しく処理できるかを確認するためのテストです。改行や記号なども含めて、表示崩れが起きないかをチェックしてください。"},
    4: {"title": "Hello World", "content": "Welcome to my new application!"},
    5: {"title": "【重要】メンテナンスのお知らせ", "content": "来週の月曜日午前2:00〜4:00の間、システムメンテナンスを行います。"},
    6: {"title": "バグ確認用", "content": "<script>alert('test')</script> 特殊文字のプレーンテキスト処理テスト。"},
    7: {"title": "短文", "content": "あ"},
    8: {"title": "画像なし投稿テスト", "content": "テキストのみの投稿がタイムラインでどのように表示されるかの確認用データ。"},
    9: {"title": "Draft", "content": "これは下書き状態のテストデータです。"},
    10: {"title": "おわり", "content": "10個目のテスト投稿です。これでデータ作成完了！"}
}

@app.get("/posts")
def get_all_posts(limit: int):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int) -> PostResponse:
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="投稿見つかりませんでした")
    return text_posts.get(id)

# クエリパラメータ
# ?の後にくるもの(フィルタリング用)

# FastAPIではデータ制限は自動的に行われる
# 関数にデータを送信した際、データタイプが適切かどうかを事前に判断
# スキーマを作成することを推奨
# データタイプマッチングしないとき、自動的にFastAPIがエラーを返す

@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post

# # 最初のAPIエンドポイントを作成
# @app.get("/hello-world")
# def hello_world():
#     return {"message": "Hello World"}