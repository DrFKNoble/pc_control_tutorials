#include <iostream>

using namespace std;

int main()
{
    enum TEMP {HOT, TEMPERATE, COLD};
    
    TEMP feeling {TEMP::HOT};
    
    if (feeling == TEMP::HOT)
    {
        std::cout << "I'm feeling hot!";
    }

    return 0;
}
