# !/usr/bin/env python
#! -*- coding:utf-8 -*-
# Author:   wolfanature
# filename: 1108.DefangingAnIpAddress.py

# srcurl: https://leetcode.com/problems/defanging-an-ip-address/

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace(".", "[.]")
        

def testCase():
    S = Solution()
    address = "1.1.1.1"
    result = S.defangIPaddr(address)
    targetAddress = "1[.]1[.]1[.]1"
    assert(result==targetAddress)
    print("result = {S}".format(S=result))
    print("test done")

if __name__ == '__main__':
    testCase()















