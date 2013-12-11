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
    os.path.join(DIR_PATH, 'lib', 'tornado-3.1'),
    os.path.join(DIR_PATH, 'lib', 'blinker-1.3'),
    os.path.join(DIR_PATH, 'lib', 'tornado-redis-2.4.7'),
    os.path.join(DIR_PATH, 'lib', 'rarfile-2.6'),
]
sys.path = EXTRA_PATHS + sys.path


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_search.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
