# DircleFeed
A sites url / RSS feeds / articles polymer favorites tool.

Test site: dfeed.geek.moe

## Design

Apps: 

* DFFavs
* DFRSS
* DFReader

## URLS

* dfeed.geek.moe // Home
	* /favs
		* newest favs ...
	* /rss
	* /reader
	* /u/dimpurr
		* overview
		* /u/dimpurr/favs
		* /u/dimpurr/rss
			* rss lists ...
			* /u/dimpurr/rss/anime // alias
		* /u/dimpurr/reader

## Commonly used script

```bash
python manage.py migrate
python manage.py makemigrations
python manage.py shell
```

```python
from DFRSS.models import RSSList, RSSListSource
from django.utils import timezone

RSSList.objects.all()

r.rsslistsource_set.create(source_name="dim", url="http://blog.dimpurr.com/feed/", create_date=timezone.now())

python manage.py createsuperuser
```