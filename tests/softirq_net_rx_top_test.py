#!/usr/bin/env python

import unittest
from netutils_linux.softirqs import Softirqs


class SoftirqsTest(unittest.TestCase):

    def test_file2data(self):
        for cpu in ('dualcore', 'i7'):
            for i in xrange(1, 6):
                self.assertIn('NET_RX', Softirqs('tests/softirqs/{0}/softirqs{1}'.format(cpu, i)).file2data())

if __name__ == '__main__':
    unittest.main()