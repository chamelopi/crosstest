#include "mylib.h"


#ifdef __MINGW32__

std::string mylib::get_system_name() {
    return std::string("Windows");
}

#else

std::string mylib::get_system_name() {
    return std::string("Linux");
}

#endif
