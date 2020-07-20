#include "main.hpp"

class Sensor
{
public:

    Sensor() : value(0.0) {}
    Sensor(const float &v) : value(v) {}
    ~Sensor() {}

    float getValue() { return value; }
    void setValue(const float &v) { value = v; }

    float value; 

};

namespace boost
{
    namespace serialization
    {
        
        template<class Archive>
        void serialize(Archive &ar, Sensor &s, const unsigned int version)
        {
            ar & s.value;
        }

    }
}

int main(int argc, char *argv[])
{
    try
    {
        boost::asio::streambuf buffer;
        std::ofstream ofs("filename");

        Sensor s_out(125.0);

        std::cout << "s_out's value:" << s_out.getValue() << std::endl;

        boost::archive::binary_oarchive oa(buffer);
        // boost::archive::text_oarchive oa(ofs);

        oa << s_out;

        ofs.close();

        std::ifstream ifs("filename");

        Sensor s_in;

        boost::archive::binary_iarchive ia(buffer);
        // boost::archive::text_iarchive ia(ifs);

        ia >> s_in;

        ifs.close();

        std::cout << "s_in's value:" << s_in.getValue() << std::endl;

    }
    catch(const std::exception& e)
    {
        std::cerr << e.what() << '\n';
    }
    
}