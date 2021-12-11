import json

with open('image_info_test-dev2017.json') as f:
    data = json.load(f)
    images = len(data.get('images'))
    categories = len(data.get('categories'))

    for j in data.get('images'):
        if j['file_name'] == '000000000001.jpg':
            url, height, width, id = j['coco_url'], j['height'], j['width'], j['id']

    id_s = [j.get('id') for j in data.get('images')]
    id_s.sort()

    print(images)
    print(categories)
    print(url, height, width, id)
    print(id_s[-1])

