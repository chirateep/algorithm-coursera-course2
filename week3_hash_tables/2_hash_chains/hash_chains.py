# python3


class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = dict()

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            try:
                self.elems[query.ind].reverse()
                self.write_chain(self.elems[query.ind])
                self.elems[query.ind].reverse()
            except KeyError:
                print('')
        else:
            hash_val = self._hash_func(query.s)
            ind = self.elems.get(hash_val, -1)
            if query.type == 'find':
                found = False
                if ind != -1:
                    for word in self.elems[hash_val]:
                        if word == query.s:
                            found = True
                            break
                self.write_search_result(found)
            elif query.type == 'add':
                if ind == -1:
                    self.elems[hash_val] = [query.s]
                else:
                    try:
                        ind_val = self.elems[hash_val].index(query.s)
                    except ValueError:
                        ind_val = -1
                    if ind_val == -1:
                        self.elems[hash_val].append(query.s)
            else:
                if ind != -1:
                    for i in range(len(self.elems[hash_val])):
                        word = self.elems[hash_val][i]
                        if word == query.s:
                            self.elems[hash_val].pop(i)
                            break

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())


if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
