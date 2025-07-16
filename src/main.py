import MeCab

def main():
    tokenizer = MeCab.Tagger("-r /dev/null -d ./lib/python3.9/site-packages/unidic_lite/dicdir")
    tokens = tokenizer.parse("こんにちは、僕の名前はニールです。日本語を話せます。").split("\n")
    token_dict = []
    for line in tokens:
        out = line.split("\t")
        if len(out) > 1:
            token = {
                "surface": out[0],
                "reading": out[1],
                "lem": out[3],
                "pos": out[4]
            }
        token_dict.append(token)
    print(token_dict)

if __name__ == "__main__":
    main()