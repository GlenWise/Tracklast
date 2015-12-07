from django import template

register = template.Library()

@register.filter(name='prepareurl')
def prepareURL(url):
	if url.startswith('http://'):
		url = url[7:]
	if url.startswith('https://'):
		url = url[8:]
	if url.startswith('https://www.'):
		url = url[12:]
	if url.startswith('http://www.'):
		url = url[11:]
	return url