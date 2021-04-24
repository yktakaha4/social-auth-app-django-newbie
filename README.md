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
