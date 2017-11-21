#!/usr/bin/env python

'''
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
import json
from stacks.utils.RMFTestCase import *
from mock.mock import patch

from only_for_platform import not_for_platform, PLATFORM_WINDOWS

@not_for_platform(PLATFORM_WINDOWS)
class TestKafkaBroker(RMFTestCase):
    COMMON_SERVICES_PACKAGE_DIR = "KAFKA/0.8.1/package"
    STACK_VERSION = "2.6"

    CONFIG_OVERRIDES = {"serviceName":"KAFKA", "role":"KAFKA_BROKER"}

    def test_configure_default(self):
        self.executeScript(self.COMMON_SERVICES_PACKAGE_DIR + "/scripts/kafka_broker.py",
                           classname = "KafkaBroker",
                           command = "configure",
                           config_file="default_kafak_sasl.json",
                           stack_version = self.STACK_VERSION,
                           target = RMFTestCase.TARGET_COMMON_SERVICES
                           )
        self.assertResourceCalled('Directory', '/var/log/kafka',
                                  owner = 'kafka',
                                  group = 'hadoop',
                                  create_parents = True,
                                  mode = 0755,
                                  cd_access = 'a',
                                  recursive_ownership = True,
                                  )

        self.assertResourceCalled('Directory', '/var/run/kafka',
                                  owner = 'kafka',
                                  group = 'hadoop',
                                  create_parents = True,
                                  mode = 0755,
                                  cd_access = 'a',
                                  recursive_ownership = True,
                                  )

        self.assertResourceCalled('Directory', '/usr/hdp/current/kafka-broker/config',
                                  owner = 'kafka',
                                  group = 'hadoop',
                                  create_parents = True,
                                  mode = 0755,
                                  cd_access = 'a',
                                  recursive_ownership = True,
                                  )
        self.assertResourceCalled('Directory', '/tmp/log/dir',
                                  owner = 'kafka',
                                  create_parents = True,
                                  group = 'hadoop',
                                  mode = 0755,
                                  cd_access = 'a',
                                  recursive_ownership = True,
                                  )
