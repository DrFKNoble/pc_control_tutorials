#include "main.hpp"

void add(const boost::function<void(const int &)> &f, const int &a, const int &b)
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

    std::cout << message << a << std::endl;

    return;
}

int main(int argc, char *argv[])
{

    try
    {
        int a = 1;
        int b = 2;

        add(defaultAddHandle, a, b);

        std::string message{"The sum is equal to: "};

        auto f = boost::bind(newAddHandle, _1, message);

        f(1);

        add(f, a, b);

        return 0;
    }
    catch (const std::exception &e)
    {
        std::cerr << e.what() << '\n';

        return 1;
    }
}