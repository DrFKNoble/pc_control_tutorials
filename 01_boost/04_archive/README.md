# Boost Serialisation Activity

## Introduction

To learn how to serialise data using Boost, let's write a program that uses Boost's archive library.

## Aims

The aims of this activity are to:

1. Practise writing programs in C++.
1. Pratise building software using CMake.
1. Familiarise ourselves with Boost's archive library and its functions.

## Objectives

The objectives of this activity are to:

1. Write a program that uses Boost's archive library to serialise an object.
1. Write a CMakeLists.txt file.
1. Build an executable using CMake.

## Requirements

To complete this activity, you need the following tools:

1. [CMake 3.17.2](https://cmake.org/).
1. [Visual Studio Code](https://code.visualstudio.com/) and either: 
    1) GCC via [Mingw-w64](http://mingw-w64.org/doku.php).
    
    or
    
    2) [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/).

    or

1. [Visual Studio Community 2019](https://visualstudio.microsoft.com/vs/).
1. [Boost 1.73.0](https://boost.org/).

I recommend installing Visual Studio Community 2019 and the Desktop development with C++ workload. If you've installed Visual Studio IDE, you can use its C++ in Visual Studio Code.

## List of Files

This project is organised as follows:

1. [CMakeLists.txt](CMakeLists.txt).
1. [main.cpp](main.cpp).
1. [main.hpp](main.hpp).
1. [README.md](README.md).

The file CMakeLists.txt is a text file. We will use it to type commands that CMake will use to build our project. The files main.cpp and main.hpp are C++ source and header files. We will use them to write code that the compiler will use to build our executable. 

## Steps

Here, we will work throught the steps needed to bind a function. 

## Step 1

Open [CMakeLists.txt](CMakeLists.txt). Complete the following:

1. Use CMake's `cmake_minimum_required()` function to define a minimum required CMake version.
1. Use CMake's `project()` to name the project "main".
1. Use CMake's `set()` function to set the C++ standard to be C++17.
1. Use CMake's `find_package()` function find the Boost package. If Boost is not installed in the default location, set the BOOST_ROOT variable to the path where you have installed Boost.
1. Use CMake's `include_directories()` function to include Boost's include directories to the project. The Boost_INCLUDE_DIRS variable contains a list of Boost's include directories.
1. Use CMake's `link_directories()` function to include Boost's libraries directories to the project. The Boost_LIBRARY_DIRS variable contains a list of Boost's library directories.
1. Use CMake's `add_executable()` function to add source files to the project.
1. Use CMake's `target_link_libraries()` function to link the project and Boost's libaries. The Boost_LIBRARIES variable contains a list of Boost's libaries.
1. Use CMake's `install()` function to copy the built project into a sub-directory named "bin".

## Step 2

Open [main.hpp](main.hpp). Complete the following:

1. Create a header guard.
1. Include Boost's `binary_iarchive.hpp`.
1. Include Boost's `binary_oarchive.hpp`.
1. Include Boost's `text_iarchive.hpp`.
1. Include Boost's `text_oarchive.hpp`.
1. Include Boost's `asio.hpp` header.
1. Inlcude the standard library's `fstream` header.
1. Include the standard library's `iostream` header.

## Step 3

Open [main.cpp](main.cpp). Complete the following:

1. Include main.hpp.
1. Define a class named "Sensor".
1. In `Sensor`:
    1. Use the `public` keyword to specify following members are public members of `Sensor`.
    1. Define a public default constructor. The constructor should not accept any arguments and and should initialise `value` as 0.0.
    1. Define a public constructor that accepts the following argument: `float v`. The constructor should initialise `value` as `v`.
    1. Define a public default destructor.
    1. Define a public member function named "getValue()". The function should not any arguments. The function should return an `float` data type.
    1. Define a public member function named "setValue()". The function should accept the following arguments: `const float &v`. The function should not return a value. In the function, assign the parameter `v` to the member variable `value`.
    1. Use the `private` keyword to speficy following members are private members of `Sensor`.
    1. Use the `friend` keyword to make `Sensor` a friend of the `boost::serialization::access` class.
    1. Define a `class Archive` template function named "serialize()". The function should accept the following arguments; `Archive &ar`, and `const unsigned int version`. The function should not return a value. In the function, assign the member variable `value` to the `archive`.
    1. Declare a private floating point member variable named "value".
1. Define a function named "main". The function should accept the following arguments: `int argc` and `char* argv[]`. The function should return an `int` data type.
1. In `main()`:
    1. Write a try-catch statement.
    1. In the try statement:
        1. Create an instance of the `std::ofstream` class named "ofs". Instantiate it with the string "filename".
        1. Create an instance of the `Sensor` class named "s_out". Instantiatie it with the value 125.0.
        1. Create an instance of the `boost::archive::text_oarchive` class named "oa". Instantiate it with the output file stream `ofs`.
        1. Use the insertion operator (`<<`) to write `s_out` to `oa`.
        1. Use `ofs`'s `close()` member function to close the output file stream.
        1. Create an instance of the `std::ifstream` class named "ifs". Instantiate it with the string "filename".
        1. Create an instance of the `Sensor` class named "s_in".
        1. Create an instance of the `boost::archive::text_iarchive` class named "ia". Instantiate it with the input file stream `ifs`.
        1. Use the extraction operator (`>>`) to write `ia` to `s_in`.
        1. Use `ifs`'s `close()` member function to close the input file stream.
        1. Use the insertion operator to write the string "s_in: " and the value returned by `s_in`'s `getValue()` member function to the `std::cout` stream.
    1. In the catch statement:
        1. Display information about an exception.
    1. Return 0.
<!-- Use the standard library's `cout` output stream to display the contents of parameter `a`.  -->

## Step 4

To build the project, either build the project: 1) Visual Studio Code; or 2) Visual Studio IDE.

### 1. Build in Visual Studio Code

To configure the project, open the Command Palette via either the shortcut <kbd>CTRL</kbd> + <kbd>SHIFT</kbd> + <kbd>P</kbd> or <kbd>F1</kbd>, or open the "View" menu and left click on Command Palette. Afterwards, enter the following command:

    CMake:Configure

Wait for the command to complete.

To build the project, open the Command Palette and enter the following command:

    CMake:Build

Wait for the command to complete.

To run the built executable, open the Command Palette and enter the following command:

    CMake:Run Without Debugging

Wait for the command to complete.

To install the build executable, open the Command Palette and enter the following command:

    CMake:Install

Wait for the command to complete.

### 2. Build in Visual Studio IDE

To build the project, use the shortcut <kbd>CTRL</kbd> + <kbd>SHIFT</kbd> + <kbd>B</kbd> or open the "Build" menu and left click on "Build All".

Wait for the command to complete.

Left click on the drop down menu next to "Select Startup Item" and select "main.exe". 

To run the built executable, left click on the selected startup item.

To install the built executable, open the "Build" menu and left click on install "main.exe".

To run the installed executable, left click on the drop down menu next to "Select Startup Item" and select "main.exe (install)". Afterwards, left click on the selected startup item. 

## Output

Upon successful completion of Steps 1 - 4, the following will be displayed in a terminal:

    s_in: 125

## Conclusion

In this activity, we've written a program that uses the code and functions introduced in the Boost tutorials.

I hope you've found it helpful.