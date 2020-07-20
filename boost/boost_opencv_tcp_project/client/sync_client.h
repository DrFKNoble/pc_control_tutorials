#pragma once

#include <boost/archive/binary_iarchive.hpp>
#include <boost/archive/binary_oarchive.hpp>
#include <boost/asio.hpp>
#include <iostream>
#include <opencv2/opencv.hpp>

namespace boost {
	namespace serialization {

		template<class Archive>
		void serialize(Archive &ar, cv::Mat& mat, const unsigned int)
		{
			int cols, rows, type;
			bool continuous;

			if (Archive::is_saving::value) {
				cols = mat.cols; rows = mat.rows; type = mat.type();
				continuous = mat.isContinuous();
			}

			ar & cols & rows & type & continuous;

			if (Archive::is_loading::value)
				mat.create(rows, cols, type);

			if (continuous) {
				const size_t data_size = rows * cols * mat.elemSize();
				ar & boost::serialization::make_array(mat.ptr(), data_size);
			}
			else {
				const size_t row_size = cols * mat.elemSize();
				for (int i = 0; i < rows; i++) {
					ar & boost::serialization::make_array(mat.ptr(i), row_size);
				}
			}

		}

	} // namespace serialization
} // namespace boost

class sync_client
{
public:
	sync_client(const std::string ip_address, const size_t port);
	~sync_client();

	void connect();
	void close();

	void getFrame(cv::Mat *frame);

private:

	boost::asio::io_context io_context_;
	boost::asio::ip::tcp::endpoint endpoint_;
	boost::asio::ip::tcp::socket socket_;

};

