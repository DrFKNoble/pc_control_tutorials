#include "sync_server.h"


sync_server::sync_server(const size_t port) :
	acceptor_(io_context_, boost::asio::ip::tcp::endpoint(boost::asio::ip::address_v4(), port)),
	socket_(io_context_)
{
}


sync_server::~sync_server()
{
}

void sync_server::connect() {

	try {
		socket_ = boost::asio::ip::tcp::socket(io_context_);
		acceptor_.accept(socket_);
	}
	catch (boost::system::system_error &e) {
		std::cerr << e.what() << std::endl;
	}

}

void sync_server::close() {

	try {

	}
	catch (boost::system::system_error &e) {
		std::cerr << e.what() << std::endl;
	}

}

void sync_server::sendFrames(const cv::Mat &frame) {

	boost::asio::streambuf write_buffer;
	boost::archive::binary_oarchive output_archive(write_buffer);

	output_archive << frame;

	size_t bytes_sent{ 0 };

	try {

		bytes_sent = boost::asio::write(socket_, write_buffer);

	}
	catch (boost::system::system_error &e) {
		std::cerr << e.what() << std::endl;
	}

	socket_.shutdown(boost::asio::ip::tcp::socket::shutdown_both);

	std::cout << bytes_sent << std::endl;

}