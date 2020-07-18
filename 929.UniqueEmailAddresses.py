# !/usr/bin/env python
#! -*- coding:utf-8 -*-
# Author:   wolfanature
# filename: 929.UniqueEmailAddresses.py


# https://leetcode.com/problems/unique-email-addresses/


# Every email consists of a local name and a domain name, 
# separated by the @ sign.

# For example, in alice@leetcode.com, alice is the local name,
# and leetcode.com is the domain name.

# Besides lowercase letters, these emails may contain '.'s or '+'s.

# If you add periods ('.') between some characters in 
# the local name part of an email address, 
# mail sent there will be forwarded to the same address without dots in the local name.  For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.  (Note that this rule does not apply for domain names.)

# If you add a plus ('+') in the local name, 
# everything after the first plus sign will be ignored.
#  This allows certain emails to be filtered, 
#  for example m.y+name@email.com will be forwarded to my@email.com. 
#   (Again, this rule does not apply for domain names.)
# It is possible to use both of these rules at the same time.

# Given a list of emails, we send one email to
#  each address in the list. 
#   How many different addresses actually receive mails? 

 

# Example 1:

# Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails


class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        alist = [self.emailHandle(email) for email in emails]
        return len(set(alist))

    def emailHandle(self, email):
    	pre, postfix = email.split("@")
    	cn = pre.split("+")
    	cn[0] = "".join(cn[0].split("."))
    	target =  "@".join([cn[0], postfix])
    	return target


# others' versison
class Solution2(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """ 
        aset = set()
        for e in emails:
        	index = index2 = e.index("@")
        	if "+" in e[:index]:
        		index2 = e[:index].index("+")
        	aset.add(e[:min(index, index2)].replace(".", "") + e[index:])
        return len(aset)

def testCase1():
	alist = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
	s = Solution()
	print(s.numUniqueEmails(alist))


def testCase2():
	alist = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
	# alist = ["test.email+alex@leetcode.com"]
	s = Solution2()
	print(s.numUniqueEmails(alist))

def test():
	# testCase1()
	testCase2()
	pass

if __name__ == '__main__':
	test()



