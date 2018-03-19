code = r'''#include <iostream>

void somebody_once_told_me() {
    std::cout << "Somebody once told me\n"
              << "The world is gonna roll me.\n"
              << "I ain't the sharpest tool the shed.\n";
}
'''

with open("index.h", 'w') as file:
    print(code, file=file)