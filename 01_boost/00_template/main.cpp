#include "main.hpp"


int main(int argc, char* argv[]) {

	try {

		boost::asio::io_context io;

		boost::thread t(boost::bind(&boost::asio::io_context::run, &io));

		std::cout << "Hello World!\r\n";

		io.run();

		t.join();

	} 
	catch (std::exception& e) {

		std::cout << e.what() << std::endl;

		return 1;

	}
	
    return 0;
}