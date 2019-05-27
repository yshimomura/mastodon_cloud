from mastodon import Mastodon

mastodon = Mastodon(
client_id="app_key.txt",
api_base_url="https://mastdn.jp"
)

mastodon.log_in(
"book.yusuke@gmail.com",
"ys56564989",
to_file="user_key.txt"
)
