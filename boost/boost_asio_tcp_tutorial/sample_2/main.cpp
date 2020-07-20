#include "main.hpp"

int main(int argc, char* argv[]) {

	try {

		boost::asio::io_context io;

		boost::asio::ip::tcp::endpoint end_points(boost::asio::ip::tcp::v4(), 9601);

		boost::asio::ip::tcp::acceptor acceptor(io, end_points);
		
		bool loop{ true };

		while (loop) {

			boost::asio::ip::tcp::socket socket(io);

			acceptor.accept(socket);

			try {

				boost::asio::streambuf readBuffer;

				boost::asio::read_until (socket, readBuffer, '\n');

				boost::asio::const_buffer input = readBuffer.data();

				std::string message(boost::asio::buffers_begin(input), boost::asio::buffers_begin(input) + input.size());

				std::cout << message << std::endl;

			}
			catch (std::exception& e) {

				std::cout << e.what() << std::endl;

				loop = false;

				return 2;

			}
						
		}

		acceptor.close();

	}
	catch (std::exception& e) {

		std::cout << e.what() << std::endl;

		return 1;

	}
	   
    return 0;

}