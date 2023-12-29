from urllib.parse import urlparse

def parse(url):
    p = urlparse(url)
    path: str = p.path
    path = path.replace('/', ' ').strip()
    items = path.split(' ')
    return dict(make_pairs(items))

def make_pairs(input_list):
    output_list = [(input_list[i], input_list[i+1]) for i in range(0, len(input_list), 2)]
    return output_list