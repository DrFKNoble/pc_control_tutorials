#include "main.hpp"

void waitHandle(const boost::system::error_code& e) {

	std::cout << "Timer Elapsed" << std::endl;

}

int main(int argc, char* argv[]) {

	try {

		boost::asio::io_context io;

		boost::asio::steady_timer t(io, boost::asio::chrono::seconds(5));

		t.async_wait(&waitHandle);

		std::cout << "Timer Started" << std::endl;

		io.run();

	}
	catch (std::exception & e) {

		std::cout << e.what() << std::endl;

		return 1;

	}
	
    return 0;
}