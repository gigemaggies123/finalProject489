# Scrapy settings for finalproject project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'finalproject'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['finalproject.spiders']
NEWSPIDER_MODULE = 'finalproject.spiders'
DEFAULT_ITEM_CLASS = 'finalproject.items.FinalprojectItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

