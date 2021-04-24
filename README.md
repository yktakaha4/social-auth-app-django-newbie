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

コールバック URL は `http://localhost:8000/social/complete/xxxxx` の形式で設定する

### github

https://github.com/settings/applications/new
