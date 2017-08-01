#include <iostream>
#include <cstdlib>

#include "mylib.h"

int main(void)
{
    std::cout << "Hello " << mylib::get_system_name() << "!" << std::endl;
    return EXIT_SUCCESS;
}
