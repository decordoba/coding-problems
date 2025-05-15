"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/572/
Title: Best Time to Buy and Sell Stock
Official difficulty: Easy
Real difficulty: 5/10

Description:
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a
    different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any
    profit, return 0.

Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.

Example 2:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
    1 <= prices.length <= 10^5
    0 <= prices[i] <= 10^4
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        max_profit = 0
        min_price = prices[0]
        for p in prices:
            if p < min_price:
                min_price = p
            elif p - min_price > max_profit:
                max_profit = p - min_price
        return max_profit
