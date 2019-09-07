# -*- coding: UTF-8 -*-

# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

# Full getext (please don't change)
_ = lambda x : x

# Add-on information variables
addon_info = {
	# for previously unpublished addons, please follow the community guidelines at:
	# https://bitbucket.org/nvdaaddonteam/todo/raw/master/guideLines.txt
	# add-on Name, internal for nvda
	"addon_name" : "linkLibrary",
	# Add-on summary, usually the user visible name of the addon.
	# Translators: Summary for this add-on to be shown on installation and add-on information.
	"addon_summary" : _("Link Library"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on add-on information from add-ons manager
	"addon_description" : _("""This addon helps the user to arrange his links or bookmarks in library like way.
From the main dialog of libraries, you can choose the library or category you like and press enter on it.
On the opened dialog, you will have all links in that category in a list and have access to source url an the about info of each llink if present.
This addon does not come with a default or assigned gesture or shortcut to it
You can as always add a gesture or change the existed one going to :
NVDA menu>preferences>inputGestures>Link Library."""),
	# version
	"addon_version" : "0.4-dev",
	# Author(s)
	"addon_author" : u"ibrahim hamadeh<ibra.hamadeh@hotmail.com>",
	# URL for the add-on documentation support
	"addon_url" : "https://github.com/ibrahim-s/linkLibrary.git",
	# Documentation file name
	"addon_docFileName" : "readme.html",
	# Minimum NVDA version supported (e.g. "2018.3.0")
	"addon_minimumNVDAVersion" : "2018.3.0",
	# Last NVDA version supported/tested (e.g. "2018.4.0", ideally more recent than minimum version)
	"addon_lastTestedNVDAVersion" : "2019.4.0",
	# Add-on update channel (default is stable or None)
	"addon_updateChannel" : None,
}


import os.path

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = [os.path.join("addon", "globalPlugins", "linkLibrary", "*.py"), ]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []
