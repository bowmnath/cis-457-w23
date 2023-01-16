#!/usr/bin/env python3
from collections import defaultdict
import re



def create_column(first, second):
    if len(first) > 0 and len(second) > 0:
        return first + '<br><br>' + second
    elif len(first) > 0:
        return first
    else:
        return second


def create_link(link):
    '''
    Entry format is:
    text, link (optional), additional text (optional)
    '''
    if len(link) > 1 and len(link[1]) > 0:
        out = '[%s](%s)' % link[:2]
    else:
        out = str(link[0])

    if len(link) > 2:
        out += ' -- %s' % ', '.join(link[2:])

    return out


def create_comma_list(parts):
    return ','.join(parts)


def gen_week_number(week):
    start = '|  '
    end = '  | '
    if week < 10:
        end = ' ' + end

    return start + str(week) + end


def gen_headings(data):
    headings = list(data['Headings'].keys())
    first_line = '| ' + ' | '.join(headings) + ' |\n'
    second_line = re.sub('[a-zA-Z0-9]', '-', first_line)
    return first_line + second_line


def gen_links_from_data(data, week, category, sep='<br>'):
    return gen_from_data(data, week, category, sep, processor=create_link)


def gen_strings_from_data(data, week, category, sep='<br>'):
    return gen_from_data(data, week, category, sep, processor=create_comma_list)


def gen_from_data(data, week, category, sep, processor):
    week = str(week)
    all_links = data[category][week]
    out = []
    for link in all_links:
        out.append(processor(link))
    return sep.join(out)


heading_symbol = '>'
comment_symbol = '#'
data_file_name = '.readme-data.txt'
delimiter = ','
first_week = 1
last_week = 16
base_fname = '.base-readme.md'
output_fname = 'README.md'

current_heading = None
data = defaultdict(lambda : defaultdict(list))
with open(data_file_name, 'r') as f:
    for line in f:
        line = line.strip()
        if line.startswith(heading_symbol):
            current_heading = line[1:].strip()
        elif line.startswith(comment_symbol):
            pass
        elif len(line) != 0:
            split_line = [s.strip() for s in line.split(delimiter)]
            week = split_line[0]
            data[current_heading][week].append(tuple(split_line[1:]))

schedule = gen_headings(data)
for week in range(first_week, last_week + 1):
    slides = gen_links_from_data(data, week, 'Slides')
    videos = gen_links_from_data(data, week, 'Videos')
    topics = create_column(slides, videos)

    activities = gen_links_from_data(data, week, 'Activities')
    readings = gen_strings_from_data(data, week, 'Readings')
    readings = create_column(activities, readings)

    deliverables = gen_links_from_data(data, week, 'Deliverables', sep='<br><br>')

    schedule += gen_week_number(week) + ' | '.join([topics, readings, deliverables]) + ' |\n'

with open(base_fname, 'r') as f:
    base = f.read()

with open(output_fname, 'w') as f:
    f.write(base + schedule)
