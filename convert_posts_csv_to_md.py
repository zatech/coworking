#!/usr/bin/env python3.6
# coding: utf-8
from collections import OrderedDict
from csv import DictReader


posts = DictReader(open('spaces.csv', newline=''), delimiter=',')

for post in posts:
    with open('_posts/2016-07-29-{}.md'.format(post['slug']), 'w') as post_file:
        if not post:
            continue
        lines = ['---', 'layout: post']
        keys = sorted(key for key in post.keys())
        for key in keys:
            key, value = key, post[key]
            value = value.strip()
            if not key or not value or key in ['amenities', 'city', 'city_slug', 'name', 'description']:
                continue
            value = value.replace('\n', '\\n')
            if '"' in value:
                value = value.replace('"', '\\"')
            if ':' in value:
                value = '"{}"'.format(value)
            lines.append('{}: {}'.format(key, value))
            # lines.append('{}: >\n  {}'.format(key, value))
        lines.append('amenities:')
        for amenity in post['amenities'].split(', '):
            lines.append('  - {}'.format(amenity))
        lines.append('category: {}'.format(post['city_slug']))
        lines.append('tags: [{}]'.format(post['city']))
        lines.append('title: {}'.format(post['name']))
        lines.append('date:   2016-07-29 11:13:58 +0200')
        lines.append('---')
        lines.append(post['description'])
        lines = [line + '\n' for line in lines]
        post_file.writelines(lines)
