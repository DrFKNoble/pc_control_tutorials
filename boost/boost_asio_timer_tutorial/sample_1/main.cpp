#include "main.hpp"

int main(int argc, char* argv[]) {

	try {

		boost::asio::io_context io;

		boost::asio::steady_timer t(io, boost::asio::chrono::seconds(5));

		std::cout << "Timer Started" << std::endl;

		t.wait();

		std::cout << "Timer Elapsed" << std::endl;

	}
	catch (std::exception & e) {

		std::cout << e.what() << std::endl;

		return 1;
	}

    return 0;
}