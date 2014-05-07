# -*- coding: utf-8 -*-
from WeiboCN import Fetcher

from lxml import etree
import lxml
import lxml.html.soupparser as sper

import re
LogIner = Fetcher()
LogIner.login('fuck@sina.com', 'fuckya', 'cookies.lwp')
content = LogIner.fetch('http://weibo.cn/pku?page=1')

#tree = etree.HTML(content)
#subtree = tree.xpath("//p/text()|//p/a")
