import yaml
import xml.etree.ElementTree as xml_tree

with open('feed.ymal','r') as file:
    yaml_data = yaml.safe_load(file)

rss_element = xml_tree.Element('rss')
