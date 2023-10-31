import argparse
from subs import get_client
from pubs import publish

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # 1 ~ n개
    # parser.add_argument(nargs = '+', help = 'Example) index.html', dest = 'filename')

    # 0 ~ n개
    parser.add_argument('--role', '-r', '-R', nargs = '?', help = 'Choose one { pub | sub }.', default = 'sub', dest = 'role', type = str)

    role = parser.parse_args().role
    print(f"Role: {role}")

    get_client().loop_forever() if role == "sub" else publish()

