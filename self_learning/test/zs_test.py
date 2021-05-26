import argparse

import argparse



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('num', type=int, help='a number')
    parser.add_argument('str', type=str, help='a str')
    parser.add_argument('--ext', type=str, default="ext string",
                        help='default value')
    args = parser.parse_args()

    print(args.num)
    print(args.str)
    print(args.ext)

if __name__ == '__main__':
    main()



