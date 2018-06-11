# ------------------------------
# 175. Combine Two Tables
# 
# Description:
# Table: Person
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | PersonId    | int     |
# | FirstName   | varchar |
# | LastName    | varchar |
# +-------------+---------+
# PersonId is the primary key column for this table.
# 
# Table: Address
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | AddressId   | int     |
# | PersonId    | int     |
# | City        | varchar |
# | State       | varchar |
# +-------------+---------+
# AddressId is the primary key column for this table.
# 
# Write a SQL query for a report that provides the following information for each person in the Person table, regardless if there is an address for each of those people:
# FirstName, LastName, City, State
# 
# Version: 1.0
# 06/10/18 by Jianfa
# ------------------------------

# Write your MySQL query statement below
select a.FirstName, a.LastName, b.City, b.State
from Person a 
left join Address b
on a.PersonId = b.PersonId;

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# The key point is "regardless if there is an address". Left join rather than inner join is used here.