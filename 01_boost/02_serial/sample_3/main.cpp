#include "main.hpp"

int main(int argc, char* argv[]) {

	try {

		boost::asio::io_context io;

		SerialPort port(io, std::string( "COM5"));

		std::string writeMessage{ "Hello World!\r\n" };

		port.asyncWrite(writeMessage);

		boost::asio::steady_timer t(io, boost::asio::chrono::milliseconds(100));
		t.wait();

		std::string readMessage{};

		port.asyncRead(&readMessage);

		io.run();

		port.close();
	
	}
	catch (std::exception& e) {

		std::cout << e.what() << std::endl;

		return 1;

	}
	   
    return 0;
}