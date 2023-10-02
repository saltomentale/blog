import re
import requests
from bs4 import BeautifulSoup
from bs4.element import SoupStrainer


def get_all_posts_in_page(page):
	url = "https://saltomentale.it/page/{}".format(page)
	posts = []
	data = requests.get(url).text
	soup = BeautifulSoup(data, "html.parser", parse_only=SoupStrainer('a', attrs={"class": "more-link"}))
	return [x.attrs["href"] for x in soup.findAll()]


def get_post_image_name(url):
	data = requests.get(url).text
	soup = BeautifulSoup(data, "html.parser", parse_only=SoupStrainer('article'))
	cover_img = soup.findChild("img")
	img_url = cover_img.attrs["data-src"]
	img_url = re.sub("https://saltomentale.it/wp-content/uploads/[\d]+/[\d]+/", "", img_url)
	local_url = re.sub("-[\d]+x[\d]+.", ".", img_url)
	return local_url


def main():
	all_posts = []
	for i in range(1, 10):
		all_posts += get_all_posts_in_page(i)

	for url in all_posts:
		local_url = get_post_image_name(url)
		print("{} \t {}".format(url, local_url))


if __name__ == '__main__':
	main()

