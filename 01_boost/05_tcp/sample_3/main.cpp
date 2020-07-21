#include "main.hpp"

int main(int argc, char* argv[]) {

	try {

		boost::asio::io_context io;

		Server server(io, 9601);

		io.run();

	}
	catch (std::exception& e) {

		std::cout << e.what() << std::endl;

		return 1;

	}
	   
    return 0;
}