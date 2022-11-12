import re


class CNF:
    def __init__(self):
        self.rules: dict[str, list[list[str]]] = {}
        self.start = 'START'

    @staticmethod
    def get_var_name(i: int) -> str:
        alphabet = chr(i % 26 + ord('A'))
        num = i // 26
        if num > 0:
            alphabet += str(num)
        return alphabet

    def dump(self, filename: str):
        with open(filename, 'w') as f:
            strs = []
            start = self.rules.pop(self.start)
            strs.append(
                f"{self.start} -> " + " | ".join([" ".join(right) for right in start]))
            for key, value in self.rules.items():
                strs.append(
                    f"{key} -> " + " | ".join([" ".join(right) for right in value]))

            f.write("\n".join(strs))

    def load(self, filename: str):
        self.rules = {}
        with open(filename, 'r') as f:
            buffer = f.readlines()
        self.start = None
        for rule in buffer:
            left, right = re.split(r' *-> *', rule)
            if self.start is None:
                self.start = left
            rightList = []
            for r in re.split(r' *\| *', right):
                rightList.append(
                    [" " if x == "space" else x for x in r.split()])
            self.rules[left] = rightList

    def subtitute_all_postfix(self, postfix, replacement: str):
        keys = list(self.rules.keys())
        for key in keys:
            value = self.rules[key]
            for right in value:
                if right[-len(postfix):] == postfix:
                    right[-len(postfix):] = [replacement]

    def subtitute_all(self, old: str, new: str):
        for key, value in self.rules.items():
            value = self.rules[key]
            for right in value:
                for i in range(len(right)):
                    if right[i] == old:
                        right[i] = new
