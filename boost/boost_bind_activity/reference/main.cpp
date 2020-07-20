#include "main.hpp"

void add(const boost::function<void(const int&)> &f, const int &a, const int &b) 
{
    
    const int sum = a + b;
    f(sum);

    return;
}

void defaultAddHandle(const int &a)
{

    std::cout << a << std::endl;

    return;
}

void newAddHandle(const int &a, const std::string &message)
{
    std::cout << message << std::endl;

    std::cout << a << std::endl;

    return;
}


int main(int argc, char* argv[])
{

    try
    {

    int a = 1, b = 2, c = 0;

    add(defaultAddHandle, a, b);

    const std::string message{"The sum is: "};

    auto f = boost::bind(newAddHandle, _1, message);

    add(f, a, b);

    return 0;

    }
    catch(std::exception &e)
    {
        std::cout << e.what() << std::endl;

        return 1;

    }

}