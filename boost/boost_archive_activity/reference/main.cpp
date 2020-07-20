#include "main.hpp"

class Sensor
{
public:

    Sensor() : value(0.0) {}
    Sensor(float v) : value(v) {}
    ~Sensor() {}

    float getValue() { return value; }
    void setValue(const float &v) { value = v;}

private:
    
    friend class boost::serialization::access;

    template<class Archive>
    void serialize(Archive &ar, const unsigned int version) { ar & value; }

    float value;

};


int main(int argc, char* argv[])
{

    try
    {
        
        // boost::asio::streambuf buffer;
        std::ofstream ofs("filename");
        
        Sensor s_out(125.00);

        // boost::archive::binary_oarchive oa(buffer);
        boost::archive::binary_oarchive oa(ofs);
        // boost::archive::text_oarchive oa(ofs);

        oa << s_out;

        ofs.close();
                
        boost::asio::io_context io;
        boost::asio::steady_timer t(io);
        t.expires_after(boost::asio::chrono::seconds(1));
        t.wait();

        std::ifstream ifs("filename");
    
        Sensor s_in;

        // boost::archive::binary_iarchive ia(buffer);
        boost::archive::binary_iarchive ia(ifs);
        // boost::archive::text_iarchive ia(ifs);

        ia >> s_in;

        ifs.close();

        std::cout << "s_in: " << s_in.getValue() << std::endl;        

    }
    catch(const std::exception& e)
    {
        std::cerr << e.what() << '\n';
    }

    return 0;    

}