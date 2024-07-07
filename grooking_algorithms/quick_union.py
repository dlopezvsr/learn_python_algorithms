class QuickUnionUF:
    def __init__(self, n):
        """
        Initializes an empty union-find data structure with
        n elements 0 through n-1. Initially, each element is in its own set.

        :param n: The number of elements
        :raises ValueError: if n < 0
        """
        if n < 0:
            raise ValueError("Number of elements must be non-negative")
        self.parent = list(range(n))
        self.count = n

    def count(self):
        """
        Returns the number of sets.

        :return: the number of sets (between 1 and n)
        """
        return self.count

    def find(self, p):
        """
        Returns the canonical element of the set containing element p.

        :param p: an element
        :return: the canonical element of the set containing p
        :raises ValueError: unless 0 <= p < n
        """
        self._validate(p)
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def _validate(self, p):
        """
        Validate that p is a valid index

        :param p: an element
        :raises ValueError: if p is not a valid index
        """
        n = len(self.parent)
        if p < 0 or p >= n:
            raise ValueError(f"index {p} is not between 0 and {n - 1}")

    def connected(self, p, q):
        """
        Returns true if the two elements are in the same set.

        :param p: one element
        :param q: the other element
        :return: True if p and q are in the same set; False otherwise
        :raises ValueError: unless both 0 <= p < n and 0 <= q < n
        """
        return self.find(p) == self.find(q)

    def union(self, p, q):
        """
        Merges the set containing element p with the set containing element q.

        :param p: one element
        :param q: the other element
        :raises ValueError: unless both 0 <= p < n and 0 <= q < n
        """
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return
        self.parent[rootP] = rootQ
        self.count -= 1

    @staticmethod
    def main(n):
        import sys
        input = sys.stdin.read
        data = input().split()

        n = int(data[0])
        uf = QuickUnionUF(n)

        i = 1
        while i < len(data):
            p = int(data[i])
            q = int(data[i + 1])
            i += 2
            if uf.find(p) == uf.find(q):
                continue
            uf.union(p, q)
            print(f"{p} {q}")

        print(f"{uf.count()} components")


# Example of usage (would be removed in a proper module):
if __name__ == "__main__":
    QuickUnionUF.main()