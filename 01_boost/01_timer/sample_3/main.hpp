#ifndef __MAIN_HPP__
#define __MAIN_HPP__

#include <iostream>
#include <boost/asio.hpp>
#include <boost/bind.hpp>

void waitHandle(const boost::system::error_code& e, boost::asio::steady_timer* t, int* count);

#endif // !__MAIN_HPP__
