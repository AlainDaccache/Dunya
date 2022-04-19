#!/bin/bash

echo "Loading environment variables from dotenv / .env file"
if [ -f .env ]
then
  export "$(cat .env | sed 's/#.*//g' | xargs)"
fi

#--------------------------------------------------------------------------
#                                   Django
#--------------------------------------------------------------------------

# Already generated: docker-compose run web django-admin startproject app .


#--------------------------------------------------------------------------
#                                   Sphinx
#--------------------------------------------------------------------------
echo "Quick-starting Sphinx documentation"
sphinx-quickstart docs --sep \
-p "$SPHINX__PROJECT_NAME" \
-a "$SPHINX__AUTHOR_NAME" \
-r "$SPHINX__PROJECT_RELEASE" \
-l "$SPHINX__PROJECT_LANGUAGE"

echo "Adding *Read the Docs* Theme for Sphinx"
if ! grep -q "sphinx_rtd_theme" docs/source/conf.py; then
  find docs/source/conf.py -type f -exec sed -i "s/extensions = \[/extensions = \['sphinx_rtd_theme'/g" {} \;
  find docs/source/conf.py -type f -exec sed -i "s/.*html_theme.*/html_theme = \"sphinx_rtd_theme\"/g" {} \;
fi

echo "Rendering Baseline Documentation"
sphinx-build -b html docs/source/ docs/build/html

if [[ "$OSTYPE" =~ mysys|cygwin|win32 ]]; then # or cygwin or win32
  open docs/build/html/index.html
else
  start docs/build/html/index.html
fi

# exit 0