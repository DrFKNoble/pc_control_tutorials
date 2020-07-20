#ifndef __SERIAL_HPP__
#define __SERIAL_HPP__

#include <iostream>
#include <boost/asio.hpp>
#include <boost/bind.hpp>

class SerialPort {
public:

	SerialPort(boost::asio::io_context& io, std::string& device);

	void asyncWrite(std::string& message);

	void asyncRead(std::string* message);

	void close();

private:

	void writeHandle(const boost::system::error_code& e, std::size_t bytes);

	void readHandle(const boost::system::error_code& e, std::size_t byes, std::string* message);

	boost::asio::serial_port m_port;

	boost::asio::streambuf m_readBuffer;
	boost::asio::streambuf m_writeBuffer;

};

#endif //!__SERIAL_HPP__