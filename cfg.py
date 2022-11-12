import re
from cnf import CNF


class CFG:
    def __init__(self) -> None:
        self.rules: dict[str, list[list[str]]] = {}

    def load(self, filename: str) -> None:
        self.rules = {}
        with open(filename, 'r') as f:
            buffer = f.readlines()
        for rule in buffer:
            left, right = re.split(r' *-> *', rule)
            rightList = []
            for r in re.split(r' *\| *', right):
                rightList.append(r.split())
            self.rules[left] = rightList

    def to_cnf(self) -> CNF:
        cnf = CNF()
        var_count = 0
        rules_map = {}

        for key in self.rules:
            if key != "START":
                alphabet = CNF.get_var_name(var_count)
                var_count += 1
                rules_map[key] = alphabet

        for key, value in self.rules.items():
            new_right = []
            for right in value:
                rules = []
                for rule in right:
                    mapped = rules_map.get(rule, rule)
                    rules.append(mapped)
                new_right.append(rules)

            mapped = rules_map.get(key, key)
            cnf.rules[mapped] = new_right

        # check if there is start in right
        make_new_start = False
        for value in cnf.rules.values():
            for right in value:
                if "START" in right:
                    make_new_start = True
                    break
        if make_new_start:
            cnf.rules["START'"] = [["START"]]
            cnf.start = "START'"

        # removes all epsilons
        for key, value in cnf.rules.items():

            # remove epsilon if exist
            is_epsilon = False
            for right in value:
                if ("e" in right):
                    value.remove(right)
                    is_epsilon = True
                    break

            if not is_epsilon:
                continue

            # list variabel yang diketahui bisa bernilai epsilon
            to_remove = [key]
            while len(to_remove) > 0:

                # key yang akan dihapus
                remove_key = to_remove.pop()
                keys = cnf.rules.keys()
                # cari key yang valuenya terdapat remove_key, lalu kombinasikan penghapusan remove_key
                for key2 in keys:
                    value2 = cnf.rules[key2]
                    for right2 in value2:
                        for i, el in enumerate(right2):
                            if el == remove_key:
                                new = [right2[k]
                                       for k in range(len(right2)) if k != i]

                                # jika yang baru ternyata epsilon juga, maka key2 mengandung epsilon
                                if len(new) == 0:
                                    if key2 not in to_remove:
                                        to_remove.append(key2)
                                elif new not in value2 and new != [key2]:
                                    value2.append(new)

        keys = list(cnf.rules.keys())

        # ubah semua bagian kanan prod rule yang panjangnya lebih dari 2
        substitutes = {}
        for key in keys:
            value = cnf.rules[key]
            for right in value:
                to_change = None
                if len(right) > 2:
                    to_change = right[1:]
                while to_change is not None:
                    if to_change in substitutes.values():
                        continue
                    new_var = CNF.get_var_name(var_count)
                    var_count += 1
                    cnf.subtitute_all_postfix(to_change, new_var)
                    substitutes[new_var] = to_change
                    cnf.rules[new_var] = [to_change]
                    if len(to_change) > 2:
                        to_change = to_change[1:]
                    else:
                        to_change = None

        # ubah semua terminal yang panjang rulenya = 2 menjadi variabel
        keys = list(cnf.rules.keys())
        for key in keys:
            value = cnf.rules[key]
            for right in value:
                if len(right) == 2:
                    for i, el in enumerate(right):
                        if not el.isupper():
                            new_var = CNF.get_var_name(var_count)
                            var_count += 1
                            cnf.subtitute_all(el, new_var)
                            cnf.rules[new_var] = [[el]]

        # substitusi semua rule yang berisi variabel dengan panjang 1
        keys = list(cnf.rules.keys())
        for key in keys:
            value = cnf.rules[key][::]
            for right in value:
                if len(right) == 1 and right[0].isupper():
                    to_sub = right[0]
                    sub = cnf.rules[to_sub]
                    ks = list(cnf.rules.keys())
                    for k in ks:
                        v = cnf.rules[k]
                        if [to_sub] in v:
                            for s in sub:
                                if s not in v:
                                    v.append(s)
                            v.remove([to_sub])

        return cnf
