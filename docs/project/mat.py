# -*- coding: utf-8 -*-
# Copyright (c) 2019,
# Silvio Peroni <silvio.peroni@unibo.it>
#
# Permission to use, copy, modify, and/or distribute this software for any purpose
# with or without fee is hereby granted, provided that the above copyright notice
# and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT,
# OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
# DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
# ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
# SOFTWARE.

# The following importing line is used to include in the definition of this class
# the particular functions implemented by a group. The 'my_test_group' module specified
# here is just a placeholder, since it defines only the signature of the various
# functions but it returns always None.
from my_test_group import *


class MetaAnalyserTool(object):
    def __init__(self, metadata_file_path):
        self.data = process_metadata(metadata_file_path)

    def get_ids(self, str_value, field_set):
        return do_get_ids(self.data, str_value, field_set)

    def get_by_id(self, id, field_set):
        return do_get_by_id(self.data, id, field_set)

    def filter(self, field_value_list):
        return do_filter(self.data, field_value_list)

    def coauthor_graph(self, author_id, level):
        return do_coauthor_graph(self.data, author_id, level)

    def author_network(self):
        return do_author_network(self.data)

    def retrieve_tree_of_venues(self, no_ids):
        return do_retrieve_tree_of_venues(self.data, no_ids)
