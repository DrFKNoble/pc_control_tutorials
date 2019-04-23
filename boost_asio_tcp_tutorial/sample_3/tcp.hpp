#ifndef __TCP_HPP__
#define __TCP_HPP__

#include <iostream>
#include <boost/asio.hpp>
#include <boost/bind.hpp>
#include <boost/enable_shared_from_this.hpp>
#include <boost/shared_ptr.hpp>

class Connection : public boost::enable_shared_from_this<Connection>
{
public:

	static boost::shared_ptr<Connection> create(boost::asio::io_context& io_context);

	boost::asio::basic_stream_socket<boost::asio::ip::tcp>& socket();

	void start();

private:
	Connection(boost::asio::io_context& io_context);

	void readHandle(const boost::system::error_code& e,
		size_t bytes);

	boost::asio::basic_stream_socket<boost::asio::ip::tcp> m_socket;

	boost::asio::streambuf m_buffer{};
};

class Server
{
public:
	Server(boost::asio::io_context& io_context, int port);

private:
	void start_accept();

	void acceptHandle(boost::shared_ptr<Connection> new_connection,
		const boost::system::error_code& error);

	boost::asio::io_context& io_context_;
	boost::asio::basic_socket_acceptor<boost::asio::ip::tcp> m_acceptor;
	
};

#endif //!__TCP_HPP