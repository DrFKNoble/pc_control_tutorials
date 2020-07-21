#include "main.hpp"


void writeHandle(const boost::system::error_code &e, const std::size_t bytes) {

	std::cout << "Bytes Written: " << bytes << std::endl;

}

void readHandle(const boost::system::error_code& e, const std::size_t bytes, const std::istream &stream) {
	
	std::cout << "Bytes Read: " << bytes << ": " << std::endl;

	std::cout << stream.rdbuf() << std::endl;
	
}

int main(int argc, char* argv[]) {

	try {

		boost::asio::io_context io;

		boost::asio::serial_port serial(io, "COM5");

		serial.set_option(boost::asio::serial_port_base::baud_rate(115200));
		serial.set_option(boost::asio::serial_port_base::character_size(8));
		serial.set_option(boost::asio::serial_port_base::parity(boost::asio::serial_port_base::parity::none));
		serial.set_option(boost::asio::serial_port_base::stop_bits(boost::asio::serial_port_base::stop_bits::one));

		std::string data{ "Hello World!\r\n" };

		boost::asio::async_write(serial, boost::asio::buffer(data), boost::bind(writeHandle, boost::asio::placeholders::error, boost::asio::placeholders::bytes_transferred));

		boost::asio::steady_timer t(io, boost::asio::chrono::milliseconds(100));
		t.wait();

		boost::asio::streambuf buf;
		std::istream stream(&buf);

		boost::asio::async_read_until(serial, buf, "\n", boost::bind(readHandle, boost::asio::placeholders::error, boost::asio::placeholders::bytes_transferred, boost::ref(stream)));

		io.run();

		serial.close();

	}
	catch (std::exception & e) {

		std::cout << e.what() << std::endl;

		return 1;

	}
	   
    return 0;
}