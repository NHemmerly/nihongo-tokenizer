import MeCab

def main():
    tokenizer = MeCab.Tagger("-Owakati -r /dev/null -d ./lib/python3.9/site-packages/unidic_lite/dicdir")
    tokens = tokenizer.parse("こんにちは、僕の名前はニールです。日本語を話せます。").split()
    print(tokens)

if __name__ == "__main__":
    main()