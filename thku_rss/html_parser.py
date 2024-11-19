from bs4 import BeautifulSoup
from datetime import date as dt
import requests

class html_parser:
	def __init__(self, url:str, css_selectors:dict):
		self.request = requests.get(url, verify=False)
		self.bs = BeautifulSoup(self.request.content, "html.parser")
		self.css_selectors = css_selectors

	
	def remove_html_tags(self, html_element:str) -> str:
		bs = BeautifulSoup(html_element, "html.parser")
		return bs.get_text()[1:-1]


	def get_href(self, html_element:str) -> str:
		bs = BeautifulSoup(html_element, "html.parser")
		a_element = bs.find('a')
		return a_element.get("href")


	def get_css_selector(self, item_no:int, rss_element_type:str) -> str:
		div_css_selector = self.css_selectors["div"].replace("*", str(item_no))
		return f"{div_css_selector}{self.css_selectors[rss_element_type]}"

		
	def get_total_of_items(self) -> int:
		return len(self.bs.select(self.css_selectors["flex_container"])[0].find_all(recursive=False))
	
	
	def get_title(self, item_no:int) -> str:
		return self.remove_html_tags(str(self.bs.select(self.get_css_selector(item_no, "title"))))


	def get_date(self, item_no:int) -> str:
		return self.remove_html_tags(str(self.bs.select(self.get_css_selector(item_no, "date"))))


	def get_link(self, item_no:int) -> str:
		return self.get_href(str(self.bs.select(self.get_css_selector(item_no, "link"))))

	def get_item_elements(self, item_no:int) -> tuple:
		title = self.get_title(item_no) 
		
		day, month, year = self.get_date(item_no).split(".")
		date = dt(int(year), int(month), int(day)).isoformat()
		
		link = self.get_link(item_no)
		
		return (title, date, link)
