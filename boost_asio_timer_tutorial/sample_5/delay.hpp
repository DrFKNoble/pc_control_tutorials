#ifndef __DELAY_HPP__
#define __DELAY_HPP__

#include <iostream>
#include <boost/asio.hpp>
#include <boost/bind.hpp>
#include <boost/thread.hpp>

class Delay {

public:

	Delay(boost::asio::io_context& io);

	void delay(const int& time);


private:

	void timerElapsed(const boost::system::error_code& e);

	boost::asio::steady_timer _t;
	boost::asio::io_context::strand _strand;

};

#endif //!__DELAY_HPP__