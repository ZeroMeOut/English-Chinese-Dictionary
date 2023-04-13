class Dict:

    def __init__(self, userinput):
        self.userinput = userinput

    def main_dict(self):
        main_dict = {}
        index = 1

        with open('words.txt') as f:
            for line in f:
                temp_store = line.strip()
                en = " "
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

    def user_dict(self):
        main_dict = self.main_dict()
        user_dict = {}
        index = 1

        for i in main_dict:
            word = main_dict[i]["en"]
            word_type = main_dict[i]["type"]
            cn = main_dict[i]["cn"]

            len_dict_en = len(word)
            len_dict_cn = len(cn)
            len_input = len(self.userinput)

            if len_dict_en >= len_input:
                if self.userinput in word[0:len_input + 1]:
                    user_dict.update({index: {"en": word, "type": word_type, "cn": cn}})
                    index += 1

            if len_dict_cn >= len_input:
                if self.userinput in cn:
                    user_dict.update({index: {"en": word, "type": word_type, "cn": cn}})
                    index += 1
        return user_dict




