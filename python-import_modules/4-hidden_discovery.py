#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    a = dir(hidden_4)
    for names in a:
        if names[:2] != "__":
            print(names)
