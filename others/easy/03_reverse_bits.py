"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/648/
Title: Reverse Bits
Official difficulty: Easy
Real difficulty: 5/10

Description:
    Reverse bits of a given 32 bits unsigned integer.

Note:
    In some languages, such as Java, there is no unsigned integer type. In this case,
    both input and output will be given as a signed integer type. This should not affect
    your implementation, as the integer's internal binary representation is the same.

    In Java, the compiler represents the signed integers using 2's complement notation.
    Therefore, in Example 2 below, the input represents the signed integer -3 and the
    output represents the signed integer -1073741825.

Example 1:
    Input: n = 00000010100101000001111010011100
    Output: 964176192 (00111001011110000010100101000000)
    Explanation: The input represents the unsigned integer 43261596. Its reversed binary
        form is 00111001011110000010100101000000, which is 964176192.

Example 2:
    Input: n = 11111111111111111111111111111101
    Output: 3221225471 (10111111111111111111111111111111)
    Explanation: The input represents the unsigned integer 4294967293. Its reversed binary
        form is 10111111111111111111111111111111, which is 3221225471.

Constraints:
    The input must be a binary string of length 32

Follow-up:
    If this function is called many times, how would you optimize it?
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        bin_in = bin(n)[2:]
        # add leading 0s
        bin_in = ("0" * (32 - len(bin_in))) + bin_in
        n_out = 0
        base2 = 1
        for c in bin_in:
            if c == "1":
                n_out += base2
            base2 *= 2
        return n_out

    def reverseBits_binary(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result <<= 1          # shift result to the left
            result |= n & 1       # copy the least significant bit of n
            n >>= 1               # shift n to the right
        return result

    def reverseBits_binary2(self, n: int) -> int:
        r = 0
        for _ in range(32):
            r = r << 1
            r += n & 1
            n = n >> 1
        return r
