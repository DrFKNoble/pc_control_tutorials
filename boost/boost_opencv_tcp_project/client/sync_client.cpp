#include "sync_client.h"

sync_client::sync_client(const std::string ip_address, const size_t port) :
	endpoint_(boost::asio::ip::address_v4::from_string(ip_address), port),
	socket_(io_context_)
{

	socket_.open(boost::asio::ip::tcp::v4());

}


sync_client::~sync_client()
{
}


void sync_client::connect() {

	try {
		socket_.connect(endpoint_);
	}
	catch (boost::system::system_error &e) {
		std::cerr << e.what() << std::endl;
	}
}

void sync_client::close() {

	try {
		socket_.shutdown(boost::asio::ip::tcp::socket::shutdown_both);
		socket_.close();
	}
	catch (boost::system::system_error &e) {
		std::cerr << e.what() << std::endl;
	}

}

void sync_client::getFrame(cv::Mat *frame) {

	/*boost::asio::streambuf read_buffer;

	size_t bytes_read{ 0 };

	try {

		bytes_read = boost::asio::read(socket_, read_buffer);

	}
	catch (boost::system::system_error &e) {
		if (e.code() == boost::asio::error::eof) {

			boost::archive::binary_iarchive input_archive(read_buffer);

			input_archive >> *frame;

		}
		else {

			std::cerr << e.what() << std::endl;

		}
	}

*/

	boost::asio::streambuf read_buffer;

	boost::system::error_code error;

	size_t bytes_read{ 0 };

	bytes_read = boost::asio::read(socket_, read_buffer, error);

	if (error = boost::asio::error::eof) {
	
		boost::archive::binary_iarchive input_archive(read_buffer);

		input_archive >> *frame;

	}
	else {

		std::cerr << error.message() << std::endl;

	}

	std::cout << bytes_read << std::endl;

}