import argparse
import os


def change_directory(node):
    for dir_name, dirs, files in os.walk('.'):
        for file_name in files:
            file_path = os.path.join(dir_name, file_name)
            if 'change_host' in file_path or '.py' not in file_path or '.md' not in file_path:
                continue
            file_regex = ''
            with open(file_path) as f:
               for s in f.readlines():
                    if 'self.host = ' in s and 'skyapi' in dir_name:
                        file_regex += s[s.find('self.host = ')]
                        file_regex += 'self.host = ' + node + '\n'
                    else:
                        file_regex += s

            with open(file_path, "w") as f:
                f.write(file_regex)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--node", help="Specific Node Address")
    args = parser.parse_args()
    print(args)

    if args.node:
        print("Updating server address")
        change_directory(args.node)
    else:
        print('set a specific node address')


main()


if __name__ == '__main__':
    main()
