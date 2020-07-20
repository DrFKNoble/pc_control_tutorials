#ifndef __MAIN_HPP__
#define __MAIN_HPP__

#include <iostream>
#include <boost/asio.hpp>
#include <boost/bind.hpp>

void writeHandle(const boost::system::error_code& e, const std::size_t bytes);

void readHandle(const boost::system::error_code& e, const std::size_t bytes, const std::istream &stream);

#endif //!__MAIN_HPP__