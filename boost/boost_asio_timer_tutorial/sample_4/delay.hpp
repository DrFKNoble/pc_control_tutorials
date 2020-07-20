#ifndef __DELAY_HPP__
#define __DELAY_HPP__

#include <iostream>
#include <boost/asio.hpp>
#include <boost/bind.hpp>

class Delay {

public:

	Delay(boost::asio::io_context& io);

	void delay(const int& time);


private:

	void timerElapsed(const boost::system::error_code& e);

	boost::asio::steady_timer m_t;

};

#endif //!__DELAY_HPP__