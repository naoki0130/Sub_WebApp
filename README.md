# django command

```
django-admin startproject ex
python manage.py runserver
python manage.py startapp polls
python manage.py makemigrations 
python manage.py migrate

```

# pyenv command

### 仮想環境

```
pyenv install x
pyenv virtualenv x ~~
Pyenv local ~~
```

# git command

### デプロイまで

```
git add .
git commit
git push origin master

git push heroku master 
(heroku config:set DISABLE_COLLECTSTATIC=1)
heroku run python manage.py migrate
heroku open
```

### git 消去

```
rm -rf .git/
```

### git remote

```
git remote add origin ~~
```

# heroku command

### heroku アプリ作成

```
heroku create 
heroku open --app アプリ名
heroku run python manage.py createsuperuser
heroku apps:destroy --app (app名) --confirm (app名）

heroku ps:scale web=1
```

# iframeのレスポンシブ対応方法
YouTubeの共有から埋め込みを選択してコピペ

### html
```
<div class="iframe-wrap">
　<iframe src="埋め込むページのURL" frameboader="0"></iframe>
</div>
```

### css
```
.iframe-wrap {
  position: relative;
  width: 100%;
  padding-top: 56.25%;
  overflow:auto; 
  -webkit-overflow-scrolling:touch;
  border:2px solid #ccc; 
}
.iframe-wrap iframe {
    position:absolute;
    top:0;
    left:0;
    width:100%;
    height:100%;
    border:none;
    display:block;
}
```

# django ページング

### bootstrapで綺麗に！！

```
{% for post in post_list %}
    <p>{{ post.title }}</p>
{% endfor %}

<ul class="pagination">
    <!-- 前へ の部分 -->
    {% if page_obj.has_previous %}
        <li class="page-item">
            <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                <span aria-hidden="true">&laquo;</span>
            </a>
        </li>
    {% endif %}

    <!-- 数字の部分 -->
    {% for num in page_obj.paginator.page_range %}
        {% if page_obj.number == num %}
            <li class="page-item active"><a class="page-link" href="#!">{{ num }}</a></li>
        {% else %}
            <li class="page-item"><a class="page-link" href="?page={{ num }}">{{ num }}</a></li>
        {% endif %}
    {% endfor %}

    <!-- 次へ の部分 -->
    {% if page_obj.has_next %}
        <li class="page-item">
            <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                <span aria-hidden="true">&raquo;</span>
            </a>
        </li>
    {% endif %}
</ul>
```

# Python: Getting Started

A barebones Django app, which can easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Running Locally

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org). To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone https://github.com/heroku/python-getting-started.git
$ cd python-getting-started

$ python3 -m venv getting-started
$ pip install -r requirements.txt

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
