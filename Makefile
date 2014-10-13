
web:
	python africanspending/manage.py runserver


countries:
	wget -O contrib/obs.json http://obstracker.internationalbudget.org/countries.json
	python contrib/convert_countries.py

contrib/maps/admin0.zip:
	mkdir -p contrib/maps
	wget -O contrib/maps/admin0.zip http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/ne_10m_admin_0_map_subunits.zip
	unzip -n -d contrib/maps contrib/maps/admin0.zip

contrib/maps/places.zip:
	mkdir -p contrib/maps
	wget -O contrib/maps/places.zip http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/ne_10m_populated_places.zip
	unzip -n -d contrib/maps contrib/maps/places.zip

maps: contrib/maps/admin0.zip contrib/maps/places.zip
	@rm -f contrib/maps/subunits.json
	@ogr2ogr \
		-f GeoJSON \
		-where "ADM0_A3 IN ('SOL', 'AGO', 'BDI', 'BEN', 'BFA', 'BWA', 'CAF', 'CIV', 'CMR', 'COD', 'COG', 'CPV', 'DJI', 'DZA', 'EGY', 'ERI', 'ETH', 'GAB', 'GHA', 'GIN', 'GMB', 'GNB', 'GNQ', 'KEN', 'LBR', 'LBY', 'LSO', 'MAR', 'MDG', 'MLI', 'MOZ', 'MRT', 'MUS', 'MWI', 'NAM', 'NER', 'NGA', 'RWA', 'SAH', 'SDN', 'SDS', 'SEN', 'SLE', 'SOM', 'STP', 'SWZ', 'SYC', 'TCD', 'TGO', 'TUN', 'TZA', 'UGA', 'ZAF', 'ZMB', 'ZWE')" \
		contrib/maps/subunits.json \
		contrib/maps/ne_10m_admin_0_map_subunits.shp
	
	@rm -f contrib/maps/places.json
	@ogr2ogr \
		-f GeoJSON \
		-where "SCALERANK < 2 AND ADM0_A3 IN ('SOL', 'AGO', 'BDI', 'BEN', 'BFA', 'BWA', 'CAF', 'CIV', 'CMR', 'COD', 'COG', 'CPV', 'DJI', 'DZA', 'EGY', 'ERI', 'ETH', 'GAB', 'GHA', 'GIN', 'GMB', 'GNB', 'GNQ', 'KEN', 'LBR', 'LBY', 'LSO', 'MAR', 'MDG', 'MLI', 'MOZ', 'MRT', 'MUS', 'MWI', 'NAM', 'NER', 'NGA', 'RWA', 'SAH', 'SDN', 'SDS', 'SEN', 'SLE', 'SOM', 'STP', 'SWZ', 'SYC', 'TCD', 'TGO', 'TUN', 'TZA', 'UGA', 'ZAF', 'ZMB', 'ZWE')" \
		contrib/maps/places.json \
		contrib/maps/ne_10m_populated_places.shp

	@topojson -o africanspending/static/maps/africa.json \
		--id-property ADM0_A3 \
		--properties name=NAME \
		-- \
		contrib/maps/subunits.json \
		contrib/maps/places.json

#maps: africanspending/static/maps/africa.json

clean:
	rm -rf contrib/maps
	rm -f africanspending/static/maps/africa.json

