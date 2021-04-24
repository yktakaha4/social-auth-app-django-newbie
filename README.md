# social-auth-app-django-newbie

## prerequirements

- python
  - 3.9.x
- poetry
- direnv

## development

```
$ cp -p .envrc.sample .envrc
$ direnv allow

$ make install
$ make dev
```

## oauth settings

### github

https://github.com/settings/developers

callback: `http://localhost:8000/social/complete/github/`

### twitter

https://developer.twitter.com/en/portal/projects-and-apps

callback: `http://localhost:8000/social/complete/twitter/`

### qiita

https://qiita.com/settings/applications

callback: `http://localhost:8000/social/complete/qiita/`

## memo

### バックエンド実装がどこにあるか

https://github.com/python-social-auth/social-core/tree/master/social_core/backends

### ストラテジ実装がどこにあるか

https://github.com/python-social-auth/social-app-django/blob/master/social_django/strategy.py

### クエリパラメータの違い

GitHub: `?code=aaaaa&state=bbbbb`

Twitter: `?redirect_state=aaaaa&oauth_token=bbbbb&oauth_verifier=ccccc`

Qiita: `?code=aaaaa&state=bbbbb`
