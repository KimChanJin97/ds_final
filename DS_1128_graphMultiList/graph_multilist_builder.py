class GraphMultilistBuilder:
    @staticmethod
    def build(mat):
        if not mat:
            raise Exception("the mat should not be none.")

        size = len(mat)
        ret = [None] * size # head 없음!
        …
        return ret