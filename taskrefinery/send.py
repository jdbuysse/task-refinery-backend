import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTkzNDYxMjE1LCJqdGkiOiJkNDQwYjRlOWEwZmI0OTUwYTQyOTg4NDIwYzAxN2JiZiIsInVzZXJfaWQiOjF9.HJydH4aya7OvmyUFOt5gtr7nTFElxWzTL8BvCfBfMu4'

r = requests.get('http://127.0.0.1:8000/tasks', headers=headers)

print(r.text)