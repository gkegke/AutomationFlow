"""
Uses AutomationFlow to create a very simple console
'dictionary' application.

Contents
 
# helper funcs

 - initialize
 - get_valid_input
 - prefix_search

"""

from Trie import DTrie
from AutomationFlow.AutomationFlow import Runner

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
END = "\033[00m"

def red(s): return RED + s + END

def green(s): return GREEN + s + END

def yellow(s): return YELLOW + s + END


def initialize():
    """

    Args

    Return

    @DTrie - a fully initialized DTrie

    Initializes a DTrie and inserts words from a word list
    text file.

    ** Also adds some gimmicky stuff to make the initialization
    look pretty.

    """

    T = DTrie(use_set=True)

    words = [word.strip("\n") for word in open("words.txt", "r")]

    wlen = len(words)

    for i, w in enumerate(words, start=1):

        T.insert(w)
        n = int((i/wlen)*20)

        s = "{}/{} words [{}]".format(
            i, # numerator
            wlen, # denominator
            ("#" * n) + (" " * (19 - n)), # increasing # as progress bar moves ahead
        )

        if i < wlen / 4:
            s = red(s)
        elif i < (wlen / 3)*2:
            s = yellow(s)
        else:
            s = green(s)

        if i % 100 == 0:
            print(s, end="\r")

    print("", end="\n")

    return T

def get_valid_input(_type, required):
    """

    Args

        _type string
          - a string used to reference to a type function in
          the valid_types dictionary

          e.g.
           - "string" -> str
           - "float" -> float

        required [](string, list, dict)
          - a list of tuples that contain variables that allow
          the testing/validation of a users input

          string
           - references a test_name in a dict of tests that contain
             predifend test functions

           e.g. "length_lt" => length_lt function

          list
           - values that the test function will be run with

          kwargs
           - kwargs that the test function will be run with

    Return

        Input - an input

    Gets and validates input from the user

    """


    valid_types = {
        "string" : str,
        "float" : float,
        "int" : int,
    }

    valid_required = {
        "length_lt": {
            "test": lambda item, length: len(item) < float(length),
            "err_msg" : lambda item, length: "Input must be less than {} characters in length\n".format(length)
        },
    }

    while True:

        trial_inp = input("> ")

        try:

            inp = valid_types[_type](trial_inp)

            for test_name, args, kwargs in required:

                rtest = valid_required[test_name]
                
                if rtest["test"](inp, *args, **kwargs) != True:
                    print(red(rtest["err_msg"](inp, *args, **kwargs)))
                    raise

        except Exception as e:
            err_msg = "Input \"{}\" wasn't valid please enter a prefix/word again..\"".format(
                trial_inp,
            )
            print(red(err_msg))
            continue


        return inp

def prefix_search(DT):

    """

    Args

        DT - the Dtrie to be used for the prefix search

    Return

        string
         - A "human readable" string form of results of the
         prefix search. Only shallow prefix searches are done.


    A prefix search is where the Trie is searched for all
    "words" contained in it that match a given prefix.

    Given prefix "he" => ["hey", "hello", ...]
    Given prefix "hi" => ["hi", "hit", ...]

    However, instead of returning the list as is, the function
    tries to return it as a string in a human readable format.

    """



    menu_msg = (
        "Please enter a word or a prefix to search for,\n"
        "or enter {} for more options\n"
        "or enter {} close this application\n"
    ).format(green("HELP"), green("EXIT"))

    while True:

        print(menu_msg)

        prefix = get_valid_input("string", [("length_lt", [30], dict())])

        if prefix == "EXIT":
            break

        result = DT.shallow_prefix_search(prefix)

        rlen = len(result)

        if rlen < 20:

            res = [
                green("\nResults: {} words in total that start with {}\n".format(rlen, red(prefix))),
                *result,
                "\n"
            ]

        else:

            res = [
                green("\nResults: Displaying 20 of many words that start with {}\n".format(red(prefix))),
                *result[:10],
                "\n......\n",
                *result[10:],
                "\n"
            ]

        print("\n".join(res))

if __name__ == "__main__":

    r = Runner(script_fpath="script.md",
           _context = {
        "initialize" : initialize,
        "len" : len,
        "print" : print,
        "float" : lambda state, n: float(n),
        "sleep" : lambda state, n: time.sleep(n),
        "get_valid_input" : get_valid_input,
        "prefixsearch" : prefix_search,
    })

    r.run()
