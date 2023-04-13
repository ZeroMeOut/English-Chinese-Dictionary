import regex
class Combined:

    def main_dict(self):
        main_dict = {}
        index = 1

        with open('words.txt') as f:
            for line in f:
                temp_store = line.strip()
                en = ""
                en_type = []

                for char in temp_store:
                    if not char.isspace():
                        en += char.lower()
                        f_char = char
                        new_temp = temp_store.replace(f_char, "", 1)
                        temp_store = new_temp
                    else:
                        break

                for pair in temp_store.split():
                    temp_pair = pair
                    pair_type = " "

                    for i, v in enumerate(temp_pair):
                        if v != ".":
                            pair_type += v
                            f_v = v
                            new_pair = temp_pair.replace(f_v, "", 1)
                            temp_pair = new_pair
                        else:
                            en_type.append(pair_type)
                            pair_type = " "
                            break
                        temp_store = temp_pair[1:]
                main_dict.update({index: {"en": en, "type": ",".join(en_type), "cn": temp_store}})
                index += 1
        return main_dict

    def combined_words(self):
        word = " "
        main_dict = self.main_dict()

        for i in main_dict:
            for v in main_dict[i]["en"]:
                if not v.isspace() and not regex.search(r'\p{Han}', v) and v.isalpha():
                    word += v
        return word
