# plugin_template

# Structure
* ### /api
directory for api endpoints

* ### /models/db
directory for db sqlalchemy models
* ### /models/pd
directory for `pydatinc` serializers* 

* ### /static
  directory for static files
  * /css/ - subdirecory for .css files
  * /js/ - subdirectory for .js files

* ### /templates
directory for .html files / jinja templates

* ### config.yml
file for module settings, accessible via `self.descriptor.config` in module

* ### metadata.json
metadata file

* ### rpc.py [optional]
file for rpc functions

