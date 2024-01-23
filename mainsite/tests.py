import requests

headers = {
	"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
	"Content-Type": "application/x-www-form-urlencoded",
	"Accept": "application/json"
}
access_token_url = "https://api.bilibili.com/x/account-oauth2/v1/token"
access_token_json = {
	"client_id": "302763bae0404eee",
	"client_secret": "aef73864a09a42bcbe1bbec8130ee5ed",
	"grant_type": "authorization_code",
	"code": "293ddafacc484f659e0d37b63561e5bd",
}

access_token_response = requests.post(
	url=access_token_url, data=access_token_json, headers=headers
)
print(access_token_response.json())