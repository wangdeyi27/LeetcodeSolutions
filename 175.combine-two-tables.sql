--
-- @lc app=leetcode id=175 lang=mysql
--
-- [175] Combine Two Tables
--
-- https://leetcode.com/problems/combine-two-tables/description/
--
-- database
-- Easy (48.68%)
-- Total Accepted:    140.2K
-- Total Submissions: 283.6K
-- Testcase Example:  '{"headers": {"Person": ["PersonId", "LastName", "FirstName"], "Address": ["AddressId", "PersonId", "City", "State"]}, "rows": {"Person": [[1, "Wang", "Allen"]], "Address": [[1, 2, "New York City", "New York"]]}}'
--
-- Table: Person
-- 
-- 
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | PersonId    | int     |
-- | FirstName   | varchar |
-- | LastName    | varchar |
-- +-------------+---------+
-- PersonId is the primary key column for this table.
-- 
-- 
-- Table: Address
-- 
-- 
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | AddressId   | int     |
-- | PersonId    | int     |
-- | City        | varchar |
-- | State       | varchar |
-- +-------------+---------+
-- AddressId is the primary key column for this table.
-- 
-- 
-- 
-- 
-- Write a SQL query for a report that provides the following information for
-- each person in the Person table, regardless if there is an address for each
-- of those people:
-- 
-- 
-- FirstName, LastName, City, State
-- 
-- 
--
# Write your MySQL query statement below
select FirstName, LastName, City, State
from
(
    select PersonId,FirstName,LastName from Person
) t1
left outer join
(
    select PersonId,City,State from Address
) t2
on t1.PersonId=t2.PersonId
