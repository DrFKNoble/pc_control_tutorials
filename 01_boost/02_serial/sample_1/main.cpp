#include "main.hpp"

int main(int argc, char* argv[]) {

	try {

		boost::asio::io_context io;

		boost::asio::serial_port serial(io, "COM5");

		serial.set_option(boost::asio::serial_port_base::baud_rate(115200));
		serial.set_option(boost::asio::serial_port_base::character_size(8));
		serial.set_option(boost::asio::serial_port_base::parity(boost::asio::serial_port_base::parity::none));
		serial.set_option(boost::asio::serial_port_base::stop_bits(boost::asio::serial_port_base::stop_bits::one));

		std::string data{ "Hello World!\r\n" };

		boost::asio::write(serial, boost::asio::buffer(data, data.size()));
		
		bool read{ true };

		while (read) {

			char c{ NULL };

			boost::asio::read(serial, boost::asio::buffer(&c, 1));

			switch (c) {
			case '\r':
				break;
			case '\n':
				read = false;
				break;
			default:
				std::cout << c;
			}

		}

		serial.close();

	}
	catch (std::exception& e) {

		std::cout << e.what() << std::endl;

		return 1;

	}

	return 0;
}