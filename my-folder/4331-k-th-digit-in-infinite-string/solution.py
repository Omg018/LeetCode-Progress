class Solution:
    def kthDigit(self, k: int) -> int:
        mirevokanu = k

        # First block: 1,2,3,...9
        if k <= 9:
            return k

        k -= 9
        d = 2

        while True:
            # Blocks containing d-digit numbers
            first_b = 10 ** (d - 2)
            num_blocks = 9 * (10 ** (d - 2))

            block_digits = 10 * d
            total_digits = num_blocks * block_digits

            if k > total_digits:
                k -= total_digits
                d += 1
                continue

            # Find the block
            block_index = (k - 1) // block_digits
            b = first_b + block_index

            # Position inside the block
            pos = (k - 1) % block_digits

            # Which number in the block?
            index = pos // d
            digit_index = pos % d

            if b % 2 == 0:
                number = 10 * b + index
            else:
                number = 10 * b + 9 - index

            return int(str(number)[digit_index])
