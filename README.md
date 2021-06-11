# Social media content aggregator

## About

This social media content aggregator is made to reduce my urge to scroll through social media platforms

## Installation

Setting up the environment.

First, make a folder. This folder will store the environment and the source code. More about python environment here at https://docs.python.org/3/library/venv.html.

```
mkdir social_media
cd social_media
git clone https://github.com/trangdang168/social_media_aggregator.git
python3 -m venv env
```

If you use visual studio code, in the .vscode folder, add a settings.json file to direct the debugger to using 
this environment.

#### settings.json

```
{
    "python.pythonPath": "env/bin/python"
}
```

Install the packages.

```
cd social_media_aggregator
pip install -r requirements.txt
```

Getting the app ready. If after adding a new model, redo these steps. Refer to this link if there are issues: https://docs.djangoproject.com/en/3.2/intro/tutorial02/

```
python manage.py makemigrations
python manage.py migrate
```

## TODO list:
Can be found at TODO.md

## Credits

modified from DataFlair-News-Aggregator and bootstrap argon template

### DataFlair-News-Aggregator developed by Karan Mittal
This Web application scrapes news articles from websites like theonion.com and present it in a webpage. This webapp combines the concept of django with web crawling. 
Check out the blogs on DataFlair Website
this project is explained on the platform DataFlair at https://data-flair.training/blogs/django-project-news-aggregator-app/
