# Copyright (c) 2020 Huawei Technologies Co.,Ltd.
#
# openGauss is licensed under Mulan PSL v2.
# You can use this software according to the terms and conditions of the Mulan PSL v2.
# You may obtain a copy of Mulan PSL v2 at:
#
#          http://license.coscl.org.cn/MulanPSL2
#
# THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
# EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
# MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
# See the Mulan PSL v2 for more details.
import getpass
import unittest

from dbmind.common.platform import LINUX
from dbmind.common.cmd_executor import ExecutorFactory


class TestExecutor(unittest.TestCase):
    def test_remote(self):
        if not LINUX:
            return
        ssh = ExecutorFactory().set_host('127.0.0.1').set_user(getpass.getuser()).set_pwd('').get_executor()
        # Padding your information.
        self.assertIsNotNone(ssh.exec_command_sync("cat /proc/cpuinfo | grep \"processor\" | wc -l"))
        self.assertIsNotNone(ssh.exec_command_sync("cat /proc/self/cmdline | xargs -0"))
        self.assertIsNotNone(ssh.exec_command_sync("echo -e 'hello \\n world'")[0].count('\n'))
        self.assertIsNotNone(ssh.exec_command_sync("echo -e 'hello \\n world'")[0])
        self.assertIsNotNone(ssh.exec_command_sync('echo $SHELL'))


if __name__ == "__main__":
    unittest.main()
