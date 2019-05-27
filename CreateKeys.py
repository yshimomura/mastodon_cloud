from mastodon import Mastodon

url = "https://mstdn.jp"
name = input('クライアント名: ')

Mastodon.create_app(name,
api_base_url=url,
to_file="app_key.txt"
)
print('api_key作成完了')

mail = input('メールアドレス: ')
passwd = input('パスワード: ')

mastodon = Mastodon(
client_id="app_key.txt",
api_base_url=url
)

mastodon.log_in(
mail,
passwd,
to_file = "user_key.txt"
)
print('user_key作成完了')
