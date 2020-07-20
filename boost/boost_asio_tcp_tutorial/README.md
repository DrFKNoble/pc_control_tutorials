# Network Communication with Boost

Welcome to my tutorial on how to communicate over a network using Boost's Asio library.

## Section 1: Introduction

Consider the following situation: you're an engineer working at a large factory. Your office is on one side of the factory; a machine you need to monitor is on the other side. Your employer requires regular measurements of the machine's state. What do you do?

Here are some potential solutions:

1. You walk over to the machine and manually make a measurement.
1. You develop a system to automatically make a measurement and save the machine's state to a computer. You walk over to the computer at the end of the day and download the day's log file.
1. You develop a system to automatically make a measurement and transmit the machine's state to your office's computer. You develop an application that displays the machine's state and save it locally.

Given a desired number and frequency of measurements, and the physical distance between your office and the machine, there's a number of issues with the first two options: you may spend too much time walking between your office and the machine, you may mis-count the number of measurements you've made, the machine may experience a fault before the end of the day and you wouldn't know, etc. A more satisfactory solution is the last option: an embedded system consisting of a sensor, amplifier, microcontroller, power supply, and network interface that will allow for consistent, continuous, and remote measurements. You don't need to constantly walk between your office and the machine, you get accurate measurements, and you'll know there's been a fault immediately. The last solution could be extended further to include remote control.

The problem is, how do you communicate with a remote system? Fortunately, there are a number of tools, e.g. [PuTTY](https://www.putty.org/), and software frameworks and libraries, e.g. [Qt](https://www.qt.io/) and [Boost](https://www.boost.org/), which have been developed to facilitate this. PuTTY allows users to connect to a desired end-point and send raw data, e.g. a string. Qt provides its networking module and Boost provides the Asio library, which both allow for network communication.

In this tutorial, I show you how to use Boost's Asio library to communicate over a network using the Transmission Control Protocal (TCP) and Internet Prototcol (IP), i.e. TCP/IP. Sample 1 and Sample 2 shows how to synchronously write and read data over a network; Sample 3 shows how to asynchronously read data over a network using a class structure. The remainder of this tutorial is structured as follows: Section 2 describes the tutorial's requirements; Section 3 describes how to build the tutorial's samples; Section 4 presents and describes Sample 1's source code; Section 5 presents and describes Sample 2's source code; Section 5 presents an activity for you to complete; Section 7 present and describe sample 3's Sample code; Section 8 presents an activity for you complete; and Section 9 concludes the tutorial.

## Section 2: Requirements

### Windows

You need the following programs and libraries installed on your computer to build the tutorial's samples and activities:

1. [CMake](https://cmake.org/).
1. [Boost](https://www.boost.org/).
1. [Visual Studio IDE](https://visualstudio.microsoft.com/).

This tutorial has been validated using the following software versions:

1. CMake 3.17.2
1. Boost 1.73.0
1. Visual Studio IDE 2019, Community Edition

If you haven't got these installed, click on each link to go to the program's respective website. To install CMake and Visual Studio IDE, run the respective installer. Most Boost libraries are header-only, i.e. they consist entirely of header files containing templates and inline functions, and require no separately-compiled library binaries or special treatment when linking. However, some libraries, e.g. Boost.Chrono, must be built separately. More information about getting started with Boost can be found [here](https://www.boost.org/doc/libs/1_70_0/more/getting_started/windows.html).

If you'd like to use an alternative to Microsoft's Visual Studio Integrated Development Environment (IDE), consider Microsoft's [Visual Studio Code](https://code.visualstudio.com/). It's a light-weight, flexible alternative to Visual Studio IDE.

Once you've CMake, Boost, and an IDE installed, you're ready to get started.

## Section 3: Build Instructions

This tutorial contains the following files:

1. [./README.md](./README.md)
1. [./activity_1/client/CMakeLists.txt](./activity_1/client/CMakeLists.txt)
1. [./activity_1/client/main.cpp](./activity_1/client/main.cpp)
1. [./activity_1/client/main.hpp](./activity_1/client/main.hpp)
1. [./activity_1/server/CMakeLists.txt](./activity_1/server/CMakeLists.txt)
1. [./activity_1/server/main.cpp](./activity_1/server/main.cpp)
1. [./activity_1/server/main.hpp](./activity_1/server/main.hpp)
1. [./activity_2/client/CMakeLists.txt](./activity_2/client/CMakeLists.txt)
1. [./activity_2/client/main.cpp](./activity_2/client/main.cpp)
1. [./activity_2/client/main.hpp](./activity_2/client/main.hpp)
1. [./activity_2/server/CMakeLists.txt](./activity_2/server/CMakeLists.txt)
1. [./activity_2/server/main.cpp](./activity_2/server/main.cpp)
1. [./activity_2/server/main.hpp](./activity_2/server/main.hpp)
1. [./sample_1/CMakeLists.txt](./sample_1/CMakeLists.txt)
1. [./sample_1/main.cpp](./sample_1/main.cpp)
1. [./sample_1/main.hpp](./sample_1/main.hpp)
1. [./sample_2/CMakeLists.txt](./sample_2/CMakeLists.txt)
1. [./sample_2/main.cpp](./sample_2/main.cpp)
1. [./sample_2/main.hpp](./sample_2/main.hpp)
1. [./sample_3/CMakeLists.txt](./sample_3/CMakeLists.txt)
1. [./sample_3/main.cpp](./sample_3/main.cpp)
1. [./sample_3/main.hpp](./sample_3/main.hpp)
1. [./sample_3/tcp.cpp](./sample_3/tcp.cpp)
1. [./sample_3/tcp.hpp](./sample_3/tcp.hpp)

The sample_1 sub-directory contains source code that shows you how to connect to an endpoint and synchronously write a message via a socket using TCP/IP. The sample_2 sub-directory contains source code that shows you how to accept connections and synchronously read a message via a socket using TCP/IP. The sample_3 sub-directory contains source code that shows you how to accept connections and asynchronously read a message via a socket using TCP/IP. The activity_1 and activity_2 sub-directories contain projects set-up for you to complete the tutorial's actvitities.

### Windows

The following describe how to build the tutorial's sample and activity using either: 1) console commands, or 2) Visual Studio IDE.

### Console Commands

To build a Debug version of a sample or activity, browse to its directory via the command line and use the following commands:

    mkdir build
    cd build
    cmake -G "Visual Studio 16 2019" ..
    cmake --build . --config Debug --target install

To run the built binary, browse to the bin sub-directory and use the following commands:

    cd ..
    cd bin
    .\project.exe

To build a Release version of a sample or activity, browse to its directory via the command line and use the following commands:

    mkdir build
    cd build
    cmake -G "Visual Studio 16 2019" ..
    cmake --build . --config Release --target install

To run the built binary, browse to the bin sub-directory and use the following commands:

    cd ..
    cd bin
    .\project.exe

### Visual Studio IDE

To build a Debug version of a sample or activity:

1. Open Visual Studio IDE
1. Click on 'File > Open > CMake'
1. Browse to the sample or activity's directory
1. Select 'CMakeLists.txt' and click on 'Open'
1. Click 'Build > Build All'

To run the built binary:

1. Click 'Debug > Start'

To change the build configuration:

1. Click 'Project > Change CMake Settings for project'
1. Select the build configuration

To build a 64-bit, debug application, select 'x64-Debug'; to build a 64-bit, release application, select 'x64-Release'. CMake's default is a 64-bit, debug configuration.

## Section 4: Sample 1

This sample is an example of a client application. It shows how to syncrhonously write data to a server.

Browse to the sample_1 sub-directory. Let's have a look the sample's source code.

main.hpp

```cpp
#ifndef __MAIN_HPP__
#define __MAIN_HPP__

#include <iostream>
#include <boost/asio.hpp>

#endif //!__MAIN_HPP__
```

main.cpp

```cpp
#include "main.hpp"

int main(int argc, char* argv[]) {

	try {

		boost::asio::io_context io;

		boost::asio::ip::tcp::resolver resolver(io);

		boost::asio::ip::tcp::resolver::query query("127.0.0.1", "9601");

		boost::asio::ip::tcp::resolver::results_type end_point = resolver.resolve(query);

		boost::asio::ip::tcp::socket socket(io);

		boost::asio::connect(socket, end_point);

		std::string message{ "Hello World!\r\n" };
				   
		std::cout << "Message: " << message << std::endl;

		boost::asio::const_buffer buffer = boost::asio::buffer(message);

		try {

			size_t bytes = boost::asio::write(socket, buffer);

			std::cout << "Bytes Written: " << bytes << std::endl;

		}
		catch (std::exception& e) {

			std::cout << e.what() << std::endl;

		}

		socket.close();
	
	}
	catch (std::exception &e) {

		std::cout << e.what() << std::endl;

		return 1;

	}
	   
    return 0;
}
```

Let's go through main.hpp, block by block.

The block

```cpp
#ifndef __MAIN_HPP__
#define __MAIN_HPP__
    ...
#endif //!__MAIN_HPP__
```

defines a header guard, which prevents including a header file more than once. When main.hpp is included, the first thing it does is check if `__MAIN_HPP__` has been defined. If it hasn't, it defines `__MAIN_HPP__` and declares and defines any objects specified. If is has been defined, the entire header is ignored. More informaiton about header guards can be found [here](https://www.learncpp.com/cpp-tutorial/header-guards/).

The block

```cpp
#include <iostream>
#include <boost/asio.hpp>
```

instructs the preprocessor to copy the contents of iostream and asio.hpp to main.cpp. The iostream header defines the standard Input and Output (I/O) stream objects. The asio header defines network and low-level I/O objects. In this sample, we use iostream's and asio.hpp's contents to display text to the user and communicate over a network via the Transmission Control Protocol (TCP).
More information about Boost's Asio library can be found [here](https://www.boost.org/doc/libs/1_70_0/doc/html/boost_asio.html).

Now, let's consider main.cpp, block by block.

The block

```cpp
 int main(int argc, char* argv[]) {
     ...
     return 0;
 }
```

defines the program's entry point. ```main()``` has two parameters, ```int argc```, and ```char* argv[]```, and returns an ```int``` value. ```argc``` is the number of command-line parameters; ```argv``` is an array of the command-line parameters. In this sample, we don't use either parameter. If the program completes successfully, the program returns 0.

The block

```cpp
try {
    ...
} catch(std::exception& e) {

    std::cout << e.what() << std::endl;

    return 1;

}
```

defines a try block and a catch block. In the try block, we try to write a message to a server. If an exception is raised, the program's execution proceeds to the catch block, which processes a `std::exception` type exception. The handler displays what exception was raised and the program returns 1. More information about exception handling can be found [here](https://www.learncpp.com/cpp-tutorial/142-basic-exception-handling/).

The line

```cpp
boost::asio::io_context io;
```

defines an instance of the Asio library's `io_context` class. It provides core synchronous and asynchronous I/O functionality. More information about `io_context` can be found [here](https://www.boost.org/doc/libs/1_70_0/doc/html/boost_asio/reference/io_context.html).

The line

```cpp
boost::asio::ip::tcp::resolver resolver(io);
```

defines an instance of the Asio library's `ip::tcp::resolver` class. It provides the ability to resolve a query to a list of endpoints. Here, the class is instantiated using the variable `io`. More information about `ip::tcp::resolver` can be found [here](https://www.boost.org/doc/libs/1_70_0/doc/html/boost_asio/reference/ip__tcp/resolver.html).

The line

```cpp
boost::asio::ip::tcp::resolver::query query("127.0.0.1", "9601");
```

defines an instance of the Asio library's `ip::tcp::resolver::resolver` class's `query` type. It describes a query that can be passed to a resolver. Here, we want to connect to the IP address `127.0.0.1` and port `9601`. More information about `ip::tcp::resolver::query` can be found [here](https://www.boost.org/doc/libs/1_70_0/doc/html/boost_asio/reference/ip__basic_resolver/query.html).

The line

```cpp
boost::asio::ip::tcp::resolver::results_type end_point = resolver.resolve(query);
```

defines an instance of the Asio library's `ip::tcp::resolver` class's `results_type` type. It defines a range over the results returned by a resolver. More information about `ip::tcp::resolver::results_type` can be found [here](https://www.boost.org/doc/libs/1_70_0/doc/html/boost_asio/reference/ip__basic_resolver/results_type.html).

The line

```cpp
boost::asio::ip::tcp::socket socket(io);
```

defines an instance of the Asio library's ```ip::tcp::socket``` class. It provides synchronous and asynchronous stream-orientated socket functionality. Here, the class is instantiated using the variable `io`. More information about ```ip::tcp::socket``` can be found [here](https://www.boost.org/doc/libs/1_70_0/doc/html/boost_asio/reference/ip__tcp/socket.html).

The line

```cpp
boost::asio::connect(socket, end_point);
```

establishes a socket connection with the endpoint. ```connect()``` is a function template and has 12 overloads. Here, it is used with two parameters, ```basic_socket<Protocol, Executor>& s``` and ```const EndpointSequence& endpoints```, and returns the successfully connected endpoint. ```s``` is the socket to be connected. ```endpoints``` is a sequence of endpoints. More information about ```connect()``` can be found [here](https://www.boost.org/doc/libs/1_70_0/doc/html/boost_asio/reference/connect.html).

The line

```cpp
std::string message{ "Hello World!\r\n" };
```

defines an instance of a string. In this sample, "Hello World!\r\n" is the message that is sent to the endpoint.

The line

```cpp
boost::asio::const_buffer buffer = boost::asio::buffer(message);
```

defines an instance of the Asio library's ```const_buffer``` class. It holds a buffer that cannot be modified. Here, the Asio library's ```buffer()``` is used to create a non-modifiable buffer from an existing string. ```buffer``` is a template function and has 32 overloads. Here, it is used with one parameter, ```const std::basic_string<Elem, Traits, Allocator>& data```, and returns a ```const_buffer``` buffer. `data` is a std::string. More information about ```buffer()``` can be found [here](https://www.boost.org/doc/libs/1_70_0/doc/html/boost_asio/reference/buffer.html).

The block

```cpp
try {

    boost::asio::write(socket, buffer);

}
catch (std::exception& e) {

    std::cout << e.what() << std::endl;

}
```

defines a try block and a catch block. In the try block, we try to synchronously write the buffer to the connected socket. If an exception is raised, the program's execution proceeds to the catch block, which processes a `std::exception` type exception. The handler displays what exception was raised.

Here, the Asio library's ```write()``` is used to synchronously write all the supplied data to a stream before returning. ```write()``` is a function template and has 16 overloads. Here, it is used with two parameters, ```SyncWriteStream& s``` and ```const ConstBufferSequence& buffers```, and returns a ```size_t``` value of bytes written. `s` is the stream to which the data is to be written; and `buffers` is one or more buffers containing the data to be written. More information about ```write()``` can be found [here](https://www.boost.org/doc/libs/1_70_0/doc/html/boost_asio/reference/write.html). 

Note, it's worth wrapping ```write()``` in a try block and a catch block. Consider the case where the endpoint doesn't accept a connection, e.g. the server running on the endpoint may not have started: ```write()``` will throw an exception; which, if not caught, will cause your program to abort. Catching the exception will allow you to do something more useful, e.g. trying to connect with the server again in 10 minutes.

The line

```cpp
socket.close();
```

uses `socket`'s `close` member function to close the connected socket.

Now that we've looked at the sample's source code, build its binary.

Because Sample 1's binary tries to connect to a server, we'll leave running it until we've built and run Sample 2's binary.

## Section 5: Sample 2

This sample is an example of a server application. It reads a message from a client.

Browse to the sample_2 sub-directory. Let's have a look the sample's source code.

main.hpp

```cpp
#ifndef __MAIN_HPP__
#define __MAIN_HPP__

#include <iostream>
#include <boost/asio.hpp>

#endif //!__MAIN_HPP__
```

main.cpp

```cpp
#include "main.hpp"

int main(int argc, char* argv[]) {

	try {

		boost::asio::io_context io;

		boost::asio::ip::tcp::endpoint end_points(boost::asio::ip::tcp::v4(), 9601);

		boost::asio::ip::tcp::acceptor acceptor(io, end_points);
		
		bool loop{ true };

		while (loop) {

			boost::asio::ip::tcp::socket socket(io);

			acceptor.accept(socket);

			try {

				boost::asio::streambuf readBuffer;

				boost::asio::read_until (socket, readBuffer, '\n');

				boost::asio::const_buffer input = readBuffer.data();

				std::string message(boost::asio::buffers_begin(input),
					boost::asio::buffers_begin(input) + input.size());

				std::cout << message << std::endl;

			}
			catch (std::exception& e) {

				std::cout << e.what() << std::endl;

				loop = false;

			}
						
		}

		acceptor.close();

	}
	catch (std::exception& e) {

		std::cout << e.what() << std::endl;

		return 1;

	}
	   
    return 0;

}
```

Let's go through main.hpp, block by block.

The block

```cpp
#ifndef __MAIN_HPP__
#define __MAIN_HPP__
    ...
#endif //!__MAIN_HPP__
```

defines a header guard, which prevents including a header file more than once. When main.hpp is included, the first thing it does is check if `__MAIN_HPP__` has been defined. If it hasn't, it defines `__MAIN_HPP__` and declares and defines any objects specified. If is has been defined, the entire header is ignored. More informaiton about header guards can be found [here](https://www.learncpp.com/cpp-tutorial/header-guards/).

The block

```cpp
#include <iostream>
#include <boost/asio.hpp>
```

instructs the preprocessor to copy the contents of iostream and asio.hpp to main.cpp. The iostream header defines the standard Input and Output (I/O) stream objects. The asio header defines network and low-level I/O objects. In this sample, we use iostream's and asio.hpp's contents to display text to the user and communicate over a network via the Transmission Control Protocol (TCP).

Now, let's consider main.cpp, block by block.

The block

```cpp
 int main(int argc, char* argv[]) {
     ...
     return 0;
 }
```

defines the program's entry point. ```main()``` has two parameters, ```int argc```, and ```char* argv[]```, and returns an ```int``` value. ```argc``` is the number of command-line parameters; ```argv``` is an array of the command-line parameters. In this sample, we don't use either parameter. If the program completes successfully, the program returns 0.

The block

```cpp
try {
    ...
} catch(std::exception& e) {

    std::cout << e.what() << std::endl;

    return 1;

}
```

defines a try block and a catch block. In the try block, we try to read a message from a client. If an exception is raised, the program's execution proceeds to the catch handler, which processes a std::exception data type. If the catch handler handles a ```std::exception``` type exception, the program returns 1.

The line

```cpp
boost::asio::io_context io;
```

defines an instance of the Asio library's ```io_context``` class. It provides core synchronous and asynchronous I/O functionality. More information about ```io_context``` can be found [here](https://www.boost.org/doc/libs/1_70_0/doc/html/boost_asio/reference/io_context.html).

The line

```cpp
boost::asio::ip::tcp::endpoint end_points(boost::asio::ip::tcp::v4(), 9601);

```

defines an instance of the Asio library's `ip::tcp::endpoint` class. `ip::tcp::endpoint` describes an endpoint that may be associated with a particular socket. Here, the class is instantiated with an IP v4 address type and the port number 9601. More information about `ip::tcp::endpoint` can be found [here](https://www.boost.org/doc/libs/1_70_0/doc/html/boost_asio/reference/ip__tcp/endpoint.html).

The line

```cpp
boost::asio::ip::tcp::acceptor acceptor(io, end_points);
```

defines an instance of the Asio library's `ip::tcp::acceptor` class. `ip::tcp::acceptor` is used for accepting new socket connections. Here, the class is instantiated using the variables `io` and `end_points`. More information about `ip::tcp::acceptor` can be found [here](https://www.boost.org/doc/libs/1_70_0/doc/html/boost_asio/reference/ip__tcp/acceptor.html).

The block

```cpp
bool loop {true};

while(loop) {
    ...
}
```

defines the boolean variable `loop` and a while loop, which loops continuously while `loop` is true.

The line

```cpp
boost::asio::ip::tcp::socket socket(io);
```

defines an instance of the Asio library's ```ip::tcp::socket``` class. Here, the class is instantiated using the variable `io`.

The line

```cpp
acceptor.accept(socket);
```

uses `acceptors`'s `accept` member function to accept a new connection. Here, the class is instantiated using the variable `socket`

The block

```cpp
try {
    ...
} catch(std::exception& e) {

    std::cout << e.what() << std::endl;

    loop = false;

}
```

defines a try block and a catch block. In the try block, we try to synchronously read a message from a connected socket. If an exception is raised, the program's execution proceeds to the catch block, which processes a `std::exception` type exception. The handler displays what exception was raised and then stops the while loop.

The line

```cpp
boost::asio::streambuf readBuffer;
```

defines an instance of Asio library's `streambuf` class. It holds a buffer that can be modified.

The line

```cpp
boost::asio::read_until (socket, readBuffer, '\n');
```

synchronously reads data into a dynamic buffer sequence, or streambuf, until it contains a delimiter, matches a regular expression, or a function object indicates a match. `read_until()` is a function template and has 24 overloads. Here it is used with three parameters, `SyncReadStream & s` `DynamicBuffer_v1 && buffers`, and `char delim`, and returns a `std::size_t` value of bytes in the buffer. `s` is the stream from which the data is to be read; `buffers` is the dynamic buffer sequence into which the data will be read, and `delim` is the delimiter character. More information about `read_until()` can be found [here](https://www.boost.org/doc/libs/1_70_0/doc/html/boost_asio/reference/read_until.html).

The line

```cpp
boost::asio::const_buffer input = readBuffer.data();
```

defines an instance of the Asio library's `const_buffer` class. It holds a buffer that cannot be modified. Here, `readBuffer`'s member function is used to create a non-modifiable buffer from an existing string.

The line

```cpp
std::string message(boost::asio::buffers_begin(input),
    boost::asio::buffers_begin(input) + input.size());
```

defines an instance of a string. Here, it is instantiated using the Asio library's `buffers_begin()`. `buffers_begin()` constructs an iterator represneting the beginning of the buffer's data. More information about `buffers_begin()` can be found [here](https://www.boost.org/doc/libs/1_70_0/doc/html/boost_asio/reference/buffers_begin.html).

The line

```cpp
std::cout << message << std::endl;
```

prints the contents of `message` on the console.

The line

```cpp
acceptor.close();
```

uses `acceptor`'s `close()` member function to close the acceptor.

Now that we've looked at the sample's source code, build and run its binary.

To test Sample 1 and Sample 2's binaries, first run Sample 2's binary and then next run Sample 1's binary. 

You should see the following images displayed:

<div>
<div align="center">
<p>Figure: Sample 1's Output. Sample 1 writes a single string, "Hello World!\r\n" to 127.0.0.1:9601.</P>
<img src=./sample_1/Capture.PNG alt="Capture.PNG" width=640>
</div>

<div align="center">
<p>Figure: Sample 2's Output. Sample 2 reads a string from 127.0.0.1:9601. Running Sample 1's binary multiple times will append multiple "Hello World!\r\n" strings to Sample 2's output.</P>
<img src=./sample_2/Capture.PNG alt="Capture.PNG" width=640>
</div>
</div>

## Section 6: Activity 1

Now that you know how to use Boost's Asio library to communicate over a network, complete the following:

1. Write a client application that uses Boost's Asio library to synchronously write a `std::vector<double>` data type to 127.0.0.1:1000 .
1. Write a server application that uses Boost's Asio library to synchronously read a `std::vector<double>` data type from 127.0.0.1:1000.

The activity_1 sub-directory is set up for you to get started. Also, have a look at Boost's Serialization library, you will find it helpful.

## Section 7: Sample 3

This sample is an improved example of a server application. It accepts connections from multiple clients.

Browse to the sample_2 sub-directory. Let's have a look the sample's source code.

main.hpp

```cpp
#ifndef __MAIN_HPP__
#define __MAIN_HPP__

#include <iostream>
#include <boost/asio.hpp>

#include "tcp.hpp"

#endif // !__MAIN_HPP__
```

main.cpp

```cpp
#include "main.hpp"

int main(int argc, char* argv[]) {

	try {

		boost::asio::io_context io;

		Server server(io, 9601);

		io.run();

	}
	catch (std::exception& e) {

		std::cout << e.what() << std::endl;

		return 1;

	}

    return 0;
}
```

tcp.hpp

```cpp
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

	boost::asio::ip::tcp::socket& socket();

	void start();

private:
	Connection(boost::asio::io_context& io_context);

	void readHandle(const boost::system::error_code& e,
		size_t bytes);

	boost::asio::ip::tcp::socket m_socket;

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

	boost::asio::io_context& m_io_context;
	boost::asio::ip::tcp::acceptor m_acceptor;
	
};

#endif //!__TCP_HPP
```

tcp.cpp

```cpp
#include "tcp.hpp"

boost::shared_ptr<Connection> Connection::create(boost::asio::io_context& io_context) {
	return boost::shared_ptr<Connection>(new Connection(io_context));
}

boost::asio::ip::tcp::socket& Connection::socket()
{
	return m_socket;
}

void Connection::start()
{

	boost::asio::async_read_until(m_socket, m_buffer, '\n',
		boost::bind(&Connection::readHandle, shared_from_this(), boost::asio::placeholders::error, boost::asio::placeholders::bytes_transferred));

}

Connection::Connection(boost::asio::io_context& io_context) :
	m_socket(io_context) {
}

void Connection::readHandle(const boost::system::error_code& e,
	size_t bytes)
{

	boost::asio::const_buffer input = m_buffer.data();

	std::string message(boost::asio::buffers_begin(input),
		boost::asio::buffers_begin(input) + input.size());

	std::cout << message << std::endl;

}


Server::Server(boost::asio::io_context & io_context, int port)
	: m_io_context(io_context),
	m_acceptor(io_context, boost::asio::ip::tcp::endpoint(boost::asio::ip::tcp::v4(), port))
{
	start_accept();
}

void Server::start_accept()
{
	boost::shared_ptr<Connection> new_connection = Connection::create(m_io_context);

	m_acceptor.async_accept(new_connection->socket(), boost::bind(&Server::acceptHandle, this, new_connection, boost::asio::placeholders::error));
}

void Server::acceptHandle(boost::shared_ptr<Connection> new_connection,
	const boost::system::error_code & error)
{
	if (!error)
	{
		new_connection->start();
	}

	start_accept();
}
```

Let's go through main.hpp, block by block.

The block

```cpp
#ifndef __MAIN_HPP__
#define __MAIN_HPP__
    ...
#endif //!__MAIN_HPP__
```

defines a header guard, which prevents including a header file more than once.

The block

```cpp
#include <iostream>
#include <boost/asio.hpp>

#include "tcp.hpp"
```

instructs the preprocessor to copy the contents of iostream, asio.hpp, and tcp.hpp to main.cpp. The tcp header defines the sample's Server and Connection classes, which accept and handle connections from client applications.

Now, let's consider main.cpp, block by block.

The block

```cpp
 int main(int argc, char* argv[]) {
     ...
     return 0;
 }
```

defines the program's entry point. ```main()``` has two parameters, ```int argc```, and ```char* argv[]```, and returns an ```int``` value. ```argc``` is the number of command-line parameters; ```argv``` is an array of the command-line parameters. In this sample, we don't use either parameter. If the program completes successfully, the program returns 0.

The block

```cpp
try {
    ...
} catch(std::exception& e) {

    std::cout << e.what() << std::endl;

    return 1;

}
```

defines a try block and a catch block. In the try block, we try to read a message from a client. If an exception is raised, the program's execution proceeds to the catch handler, which processes a std::exception data type. If the catch handler handles a ```std::exception``` type exception, the program returns 1.

The line

```cpp
boost::asio::io_context io;
```

defines an instance of the Asio library's ```io_context``` class. It provides core synchronous and asynchronous I/O functionality.

The line

```cpp
Server server(io, 9601);
```

defines an instance of the sample's `Server` class. `Server` accepts a connection from a client application and reads data from the corresponding socket. Here, it is instantiated with the variable `io` and the port number 9601. The `Server` class will be described shortly.

The line

```cpp
io.run();
```

uses `io`'s `run()` member function to run the io_context object's event processing loop.

Now, let's look at tcp.hpp, block by block.

The block

```cpp
#ifndef __TCP_HPP__
#define __TCP_HPP__
    ...
#endif //!__TCP_HPP__
```

defines a header guard, which prevents including a header file more than once.

The block

```cpp
#include <iostream>
#include <boost/asio.hpp>
#include <boost/bind.hpp>
#include <boost/enable_shared_from_this.hpp>
#include <boost/shared_ptr.hpp>
```

instructs the preprocessor to copy the contents of iostream, asio.hpp, bind.hpp, enable_shared_from_this.hpp, and shared_ptr.hpp to main.hpp. The bind header allows for the generalisation of the standard functions `std::bind1st` and `std::bind2nd`; it supports arbitrary function objects, functions, function pointers, and member function pointers, and is able to bind any argument to a specific value or route input arguments into arbitrary positions. More information about boost's Bind library can be found [here](https://www.boost.org/doc/libs/1_70_0/libs/bind/doc/html/bind.html). The enable_shared_from _this and shared_ptr headers allow for the use of the `shared_ptr` class, a versatile tool for managing shared ownership of an object; and the `enable_shared_from_this` class, a helper class that enables acquisition of a `shared_ptr` pointing to `this`. More information about Boost's Smart Ptr library can be found [here](https://www.boost.org/doc/libs/1_70_0/libs/smart_ptr/doc/html/smart_ptr.html). For more information about smart points, see [here](https://www.learncpp.com/cpp-tutorial/15-1-intro-to-smart-pointers-move-semantics/).

The block

```cpp
class Connection : public boost::enable_shared_from_this<Connection>
{
public:

    static boost::shared_ptr<Connection> create(boost::asio::io_context& io_context);

    boost::asio::ip::tcp::socket& socket();

    void start();

private:

    Connection(boost::asio::io_context& io_context);

    void readHandle(const boost::system::error_code& e,
        size_t bytes);

    boost::asio::ip::tcp::socket m_socket;

    boost::asio::streambuf m_buffer{};
};
```

declares the sample's `Connection` class. `Connection` is responsible for creating the `Server` class's socket and reading data from the client application. `create()` returns a smart_pointer to the class; `socket()` returns the class's socket; `start()` asynchronously reads data from the class's socket into a buffer; `Connection()` defines the class's socket; `readHandle()` handles the asysnchronous read operation; `m_socket` is the class's socket; and `m_buffer` is the class's buffer. Here, `shared_ptr` and `enable_shared_from_this` are used because we want to keep the `Connection` object alive as long as there is an operation that refers to it.

The block

```cpp

class Server
{
public:

    Server(boost::asio::io_context& io_context, int port);

private:

    void startAccept();

    void acceptHandle(boost::shared_ptr<Connection> new_connection,
        const boost::system::error_code& error);

    boost::asio::io_context& m_io_context;
    boost::asio::ip::tcp::acceptor m_acceptor;

};
```

declares the sample's `Server` class. `Server` is responsible for accepting connections from the client application. `Server()` defines the class's `io_context` and acceptor; `startAccept()` creates an instance of the `Connection` class and asyncrhonous accepts connections; `acceptHandle()` handles the asyncrhonous accept operation; `m_io_context` is the class's `io_context`; and `m_acceptor` is the class's acceptor.

Now, let's go through tcp.cpp, block by block.

The block

```cpp
boost::shared_ptr<Connection> Connection::create(boost::asio::io_context& io_context) {

    return boost::shared_ptr<Connection>(new Connection(io_context));

}
```

defines the `Connection` class's `create()` member function. `create()` has one parameter, `boost::asio::io_context& io_context`, and returns a shared pointer to a new instance of the `Connection` class.

The block

```cpp
boost::asio::ip::tcp::socket& Connection::socket()
{

    return m_socket;

}
```

defines the `Connection` class's `socket()` member function. `socket()` has no parameters, and returns a reference to the class's `m_socket` data member.

The block

```cpp
void Connection::start()
{

    boost::asio::async_read_until(m_socket, m_buffer, '\n',
        boost::bind(&Connection::readHandle, shared_from_this(), boost::asio::placeholders::error, boost::asio::placeholders::bytes_transferred));

}
```

defines the `Connection` class's `start()` member function. `start()` has no parameters, and does not return any values. It uses the Asio library's `async_read_until()` to asynchronously read data into the class's buffer until it contains the '\n' delimiter. `async_read_until()` is a function template and has 12 overloads. Here it is used with four parameters, `AsyncReadStream& s`, `DynamicBuffer_v1 && buffers`, `char delim`, `ReadHandler && handler`, and does not return any value. `s` is the stream from which the data is to be read; `buffers` is the dynamic buffer sequence into which the data will be read; `delim` is the delimiter character; and `handler` is the handler to be called when the read operation completes. When the read operation completes, it calls the class's `readHandle()`. For more information about `async_read_until()`, see [here](https://www.boost.org/doc/libs/1_70_0/doc/html/boost_asio/reference/async_read_until.html).

The block

```cpp
Connection::Connection(boost::asio::io_context& io_context) :
    m_socket(io_context) {

}
```

defines the `Connection` class's constructor. It defines the class's `m_socket` data member using an initilisation list. For more information about initialisation lists, see [here](https://www.learncpp.com/cpp-tutorial/8-5a-constructor-member-initializer-lists/).

The block

```cpp
void Connection::readHandle(const boost::system::error_code& e,
    size_t bytes)
{

    boost::asio::const_buffer input = m_buffer.data();

    std::string message(boost::asio::buffers_begin(input),
        boost::asio::buffers_begin(input) + input.size());

    std::cout << message << std::endl;

}
```

defines the `Connection` class's `readHandle()` member function. `readHandle()` has two parameters, `const boost::system::error_code& e` and `size_t bytes` and does not return any values. It defines a non-modifiable buffer of the data saved in the class's `m_buffer` data member, which is then converted into an instance of a string whose contents are printed on the console.

The block

```cpp
Server::Server(boost::asio::io_context & io_context, int port)
    : m_io_context(io_context),
    m_acceptor(io_context, boost::asio::ip::tcp::endpoint(boost::asio::ip::tcp::v4(), port))
{

    startAccept();

}
```

defines the `Server` class's constructor. It defines the class's `m_io_context` and `m_acceptor` data members using an initialisation list, and calls the class's `startAccept()` member function.

The block

```cpp
void Server::startAccept()
{

    boost::shared_ptr<Connection> new_connection = Connection::create(m_io_context);

    m_acceptor.async_accept(new_connection->socket(), boost::bind(&Server::acceptHandle, this, new_connection, boost::asio::placeholders::error));

}
```

defines the `Server` class's `startAccept()` member function. It defines a new instance of the `Connection` class and asyncrhonously accepts connections from a client application. It uses the class's `m_acceptor`'s `async_accept()` member function to start an asynchronous accept operation. `async_accept()` is a template function and has 8 overloads. Here it is used with two parameters, `basic_socket< Protocol1, Executor1 >& peer` and `AcceptHandler && handler`, and does not return any values. `peer` is the socket into which the new connection will be accepted; and `handler` is the handler to be called when the accept operation completes. When the accept operation completes, it calls the class's `acceptHandle()`. For more information about `async_accept()`, see [here](https://www.boost.org/doc/libs/1_70_0/doc/html/boost_asio/reference/basic_socket_acceptor/async_accept.html).

The block

```cpp
void Server::acceptHandle(boost::shared_ptr<Connection> new_connection,
    const boost::system::error_code & error)
{

    if (!error)
    {

        new_connection->start();

    }

    startAccept();

}
```

defines the `Server` class's `acceptHandle()` member function. If the class's asycnhronous accept completed successfully, it calls the connection's `start()` member;  then it calls `startAccept()` to accept a new connection.

Now that we've looked at the sample's source code, build and run its binary.

To test Sample 3's binary, first run it and then next run Sample 1's binary.

You should see the following images displayed:

<div>
<div align="center">
<p>Figure: Sample 1's Output. Sample 1 writes a single string, "Hello World!\r\n" to 127.0.0.1:9601.</P>
<img src=./sample_1/Capture.PNG alt="Capture.PNG" width=640>
</div>

<div align="center">
<p>Figure: Sample 3's Output. Sample 2 reads a string from 127.0.0.1:9601. Running Sample 1's binary multiple times will append multiple "Hello World!\r\n" strings to Sample 3's output.</P>
<img src=./sample_3/Capture.PNG alt="Capture.PNG" width=640>
</div>
</div>

## Section 8: Activity 2

Now that you know how to use Boost's Asio library to communicate over a network asynchronously, complete the following:

1. Write a client application that uses Boost's Asio library and a class structure to asynchronously write a `std::vector<double>` data type to 127.0.0.1:1000 .
1. Write a server application that uses Boost's Asio library and a class structre to asynchronously read a `std::vector<double>` data type from 127.0.0.1:1000.
The activity_1 sub-directory is set up for you to get started.

Also, have a look at Boost's Serialization library, you will find it helpful.

## Section 9: Conclusion

In this tutorial, I have shown you how to communicate with a remote system using Boost's Asio library.

You have used the Asio library to syncrhonously and asyncrhonously read and write data from and to client and server applications.

I hope this tutorial has been useful.

## Credit

Dr Frazer K. Noble  
Department of Mechanical and Electrical Engineering  
School of Food and Advanced Technology  
Massey University  
New Zealand