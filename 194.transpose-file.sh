#
# @lc app=leetcode id=194 lang=bash
#
# [194] Transpose File
#
# https://leetcode.com/problems/transpose-file/description/
#
# shell
# Medium (22.20%)
# Total Accepted:    9.7K
# Total Submissions: 42.4K
# Testcase Example:  'a'
#
# Given a text file file.txt, transpose its content.
# 
# You may assume that each row has the same number of columns and each field is
# separated by the ' ' character.
# 
# Example:
# 
# If file.txt has the following content:
# 
# 
# name age
# alice 21
# ryan 30
# 
# 
# Output the following:
# 
# 
# name alice ryan
# age 21 30
# 
# 
# 
# 
#
# Read from the file file.txt and print its transposed content to stdout.
awk '
{
    for (i = 1; i <= NF; i++) {
        if(NR == 1) {
            s[i] = $i;
        } else {
            s[i] = s[i] " " $i;
        }
    }
}
END {
    for (i = 1; s[i] != ""; i++) {
        print s[i];
    }
}' file.txt
