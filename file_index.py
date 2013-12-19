#!/usr/bin/env python
# coding=utf-8
import os
import sys

#
# Copyright 2013 nava
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
EXTRA_PATHS = [
    DIR_PATH,
    os.path.join(DIR_PATH, 'lib', 'django-haystack-2.1.0'),
    os.path.join(DIR_PATH, 'lib', 'whoosh-2.5.1', 'src'),
    os.path.join(DIR_PATH, 'lib', 'pytz-master'),
]
sys.path = EXTRA_PATHS + sys.path
from whoosh.fields import Schema, TEXT,ID,STORED
from whoosh import index

from whoosh.query import *
from whoosh.qparser import QueryParser
import locale


def string_to_utf8(value):
    """   """
    try:
        encoding = locale.getdefaultlocale()[1]
        if encoding is None:
            encoding = u"utf-8"
        if isinstance(value, str):
            value = unicode(value, encoding, errors="ignore")
    except Exception, ex:
        pass

    return value


def add_doc(writer, path):
    with open(path, "rb") as fileobj:
        content = fileobj.read()
        content = string_to_utf8(content)
        writer.add_document(path=path, content=content)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_search.settings")
    if len(sys.argv) < 2:
        sys.argv.append("runserver")

    #
    # 创建schema
    #
    schema = Schema(path=ID(unique=True, stored=True), content=TEXT)
    if not os.path.exists("file_index"):
        os.mkdir("file_index")

    ix = index.create_in("file_index", schema)
    #ix = index.open_dir("file_index")

    #
    # Indexing documents
    #
    writer = ix.writer()
    add_doc(writer, u"file_src\\a.txt")
    add_doc(writer, u"file_src\\b.txt")
    writer.commit()

    ##Searching
    searcher = ix.searcher()

    #Single Word Search:
    #myquery = u'Michael'
    #Multiword Search:
    #myquery = And([Term("content", u'Roger'), Term("content", u'Michael')])

    #query = QueryParser("content", schema=ix.schema).parse(myquery)

    parser = QueryParser("content", ix.schema)
    #query = parser.parse(myquery)
    query = parser.parse(u"dd")

    #with ix.searcher() as searcher:

    results = searcher.search(query, limit=None)

    print "Length of Results :", len(results)
    print "\nResults : "
    for i in range (0,len(results)):
        print results[i]