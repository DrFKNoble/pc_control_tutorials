
#include "serial.hpp"

SerialPort::SerialPort(boost::asio::io_context& io, std::string& device) :
	m_port(io, device)
{

	m_port.set_option(boost::asio::serial_port_base::baud_rate(115200));
	m_port.set_option(boost::asio::serial_port_base::character_size(8));
	m_port.set_option(boost::asio::serial_port_base::parity(boost::asio::serial_port_base::parity::none));
	m_port.set_option(boost::asio::serial_port_base::stop_bits(boost::asio::serial_port_base::stop_bits::one));

}

void SerialPort::asyncWrite(std::string& message) {

	std::ostream output(&m_writeBuffer);

	output << message;

	boost::asio::async_write(m_port, m_writeBuffer.data(), boost::bind(&SerialPort::writeHandle, this, boost::asio::placeholders::error, boost::asio::placeholders::bytes_transferred));

}

void SerialPort::asyncRead(std::string* message) {

	boost::asio::async_read_until(m_port, m_readBuffer, "\n", boost::bind(&SerialPort::readHandle, this, boost::asio::placeholders::error, boost::asio::placeholders::bytes_transferred, message));

}

void SerialPort::close() {

	m_port.close();

}

void SerialPort::writeHandle(const boost::system::error_code& e, std::size_t bytes) {

	boost::asio::const_buffer output = m_writeBuffer.data();

	std::string message(boost::asio::buffers_begin(output),
		boost::asio::buffers_begin(output) + output.size());

	std::cout << "Message Written: " << message << std::endl;

}

void SerialPort::readHandle(const boost::system::error_code& e, std::size_t byes, std::string* message) {

	boost::asio::const_buffer input = m_readBuffer.data();

	*message = std::string(boost::asio::buffers_begin(input),
		boost::asio::buffers_begin(input) + input.size());

	std::cout << "Message Read: " << *message << std::endl;

}
