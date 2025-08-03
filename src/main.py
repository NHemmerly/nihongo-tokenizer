import argparse
import pickle
import json
import MeCab

def load_pickles(pickle_name):
    with open(pickle_name, "rb") as file:
        jlpt_dict = pickle.load(file)
        return jlpt_dict
        
def tokenize(phrase):
    tokenizer = MeCab.Tagger("-r /dev/null")
    tokens = tokenizer.parse(phrase).split("\n")
    token_dict = []
    for line in tokens:
        out = line.split("\t")
        if 'EOS' in out:
            break
        if len(out) > 1:
            token = {
                "surface": out[0],
                "reading": out[1],
                "lem": out[3],
                "pos": out[4]
            }
        token_dict.append(token)
    return token_dict

def tag(token_dict, jlpt_dict):
    for token in token_dict:
        if token["lem"] in jlpt_dict:
            token["difficulty"] = jlpt_dict[token["lem"]]["Difficulty"]
        else:
            token["difficulty"] = "0"

def main():
    parser = argparse.ArgumentParser(
        prog="nihongo_tokenizer",
        description="Tokenize and return tagged japanese input"
    )
    parser.add_argument("-i", "--inputText", help="input text to be analyzed")
    parser.add_argument("-p", "--pickle_name", help="Pathname to pickle file that contains jlpt information")
    args = parser.parse_args()
    jlpt_dict = load_pickles(args.pickle_name)
    tokens = tokenize(args.inputText)
    tag(tokens, jlpt_dict)
    
    print(json.dumps(tokens, ensure_ascii=False))



if __name__ == "__main__":
    main()