#include "main.hpp"

int main(int argc, char* argv[]) {

	try {

		boost::asio::io_context io;

		boost::asio::ip::tcp::resolver resolver(io);

		boost::asio::ip::tcp::resolver::query query("127.0.0.1", "9601");

		boost::asio::ip::tcp::resolver::results_type end_point = resolver.resolve(query);

		boost::asio::ip::tcp::socket socket(io);

		boost::asio::connect(socket, end_point);

		std::string message{ "Hello World!\r\n" };
				   
		std::cout << "Message: " << message << std::endl;

		boost::asio::const_buffer buffer = boost::asio::buffer(message);

		try {

			size_t bytes = boost::asio::write(socket, buffer);

			std::cout << "Bytes Written: " << bytes << std::endl;

		}
		catch (std::exception& e) {

			std::cout << e.what() << std::endl;

			return 2;

		}

		socket.close();
	
	}
	catch (std::exception &e) {

		std::cout << e.what() << std::endl;

		return 1;

	}
	   
    return 0;
}