from thku_rss.html_parser import html_parser
from thku_rss.database import database
from datetime import datetime
from loguru import logger
from rfeed import Item, Feed
import json
import pkg_resources

config_file = pkg_resources.resource_filename("thku_rss", "config.json") 
with open(config_file, "r") as config_file:
	configs = json.loads(config_file.read())

MAX_FEED_ITEMS = configs["max_feed_items"]
CSS_SELECTORS = configs["css_selectors"]
FEEDS = configs["feeds"]
LOG_FOLDER = configs["log_folder_path"]

now = datetime.now()
log_file = now.strftime(f"{LOG_FOLDER}%d-%m-%Y_%H:%M:%S.log")
logger.add(log_file)

@logger.catch
def main():
	database_file = pkg_resources.resource_filename("thku_rss", "fetched_items.db")
	db = database(database_file)

	for feed in FEEDS:
		try:
			parser = html_parser(url=feed["link"], css_selectors=CSS_SELECTORS)
		except:
			logger.error(f"Fetching HTML failed: {feed['link']}")
		else:
			logger.info(f"HTML page is fetched: {feed['link']}")
		
		total_of_items = parser.get_total_of_items()
		total_fetch = min(MAX_FEED_ITEMS, total_of_items)

		table = feed["db_table"]

		last_titles = [[item_no, parser.get_title(item_no)] for item_no in range(1, total_fetch+1)]


		feed_items = []
		for item_no, title in last_titles:
			if not db.title_exists(title, table):
				try:
					item_elements = parser.get_item_elements(item_no)
				except:
					logger.error(f"Fetching HTML failed: {title}")
				else:
					logger.info(f"HTML page is fetched: {title}")

				try:
					db.insert_item(item_elements, table)
				except:
					logger.warning(f"Inserting item to database failed: {title}")

			
			else:
				item_elements = db.get_item(title, table)
				logger.info(f"Item fetched from database: {title}")
		
			feed_items.append(Item(title=item_elements[0], pubDate=datetime.fromisoformat(item_elements[1]), link=item_elements[2], description=f"<![CDATA[{item_elements[3]}]]>"))

		feed_obj = Feed(title=feed["title"],
				link=feed["link"],
				description=feed["description"],
				lastBuildDate=datetime.now(),
				items = feed_items)

		with open(feed["xml_file_path"], "w+") as xml_file:
			xml_file.write(feed_obj.rss())
			logger.info(f"XML file created: {feed['xml_file_path']}")
