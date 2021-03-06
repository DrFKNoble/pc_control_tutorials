// camera_client.cpp : Defines the entry point for the console application.
//

#include "sync_client.h"

int main()
{

	cv::namedWindow("frame", cv::WINDOW_AUTOSIZE);

	sync_client client("127.0.0.1", 9601);

	while(true)
	{

		cv::Mat frame;

		client.connect();

		client.getFrame(&frame);

		client.close();

		if (frame.empty()) 
		{
			continue;
		}

		cv::imshow("frame", frame);

		if (cv::waitKey(1) == 27) 
		{
			break;
		}

	}

	cv::destroyAllWindows();
	
	return 0;
}

