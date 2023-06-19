import sys
from AutomationFlow.AutomationFlow import Runner

def p2(_, s, end="\n"):
    print(s, end=end)
    print(s, end=end)

if __name__ == "__main__":

    args = sys.argv[1:]
    script = args[0]

#    script = '''
#
#```text
#hi
#```
#
#%% print_twice | 'hi' %%
#    '''

    r = Runner(script,
        _context = {
            "print_twice" : p2,
            "return_s" : lambda _, s: s
    })

    r.run()
