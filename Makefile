
web:
	python africanspending/manage.py runserver


countries:
	wget -O contrib/obs.json http://obstracker.internationalbudget.org/countries.json
	python contrib/convert_countries.py
