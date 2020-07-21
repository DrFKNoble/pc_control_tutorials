# Activity 1

## Introduction

To develop our understanding of the Boost's bind library, let's write a program that uses the code and functions introduced in the Boost tutorials.

## Aims

The aims of this activity are to:

1. Practise writing programs in C++.
1. Pratise building software using CMake.
1. Familiarise ourselves with Boost's `bind()` fuction.

## Objectives

The objectives of this activity are to:

1. Write a program that uses the C++ standard and Boost libraries to bind a function.
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
1. Use CMake's `find_package()` function find the Boost package.
1. Use CMake's `include_directories()` function to include Boost's include directories to the project.
1. Use CMake's `link_directories()` function to include Boost's libraries directories to the project.
1. Use CMake's `add_executable()` function to add source files to the project.
1. Use CMake's `install()` function to copy the built project into a sub-directory named "bin".

## Step 2

Open [main.hpp](main.hpp). Complete the following:

1. Create a header guard.
1. Include the standard library's iostream header.
1. Include Boost's function and bind header files.

## Step 3

Open [main.cpp](main.cpp). Complete the following:

1. Include main.hpp.
1. Define a function named "add". The function should accept the following arguments: `const boost::function<void(const int&)> &f`, `const int &a`, `const int &b`. The function should not return a value.
1. In `add()`:
    1. Assign the sum of parameters `a` and `b` to an integer variable named `sum`.
    1. Call `f()` with the following argument: `sum`.
1. Define a function named "defaultAddHandle". The function should accept the following argument: ``const int &a`. The function should not return a value.
1. In `defaultAddHandle()`:
    1. Use the standard library's `cout` output stream to display the contents of parameter `a`. 
1. Define a function named "newAddHandle". The function should accept the following argument: ``const int &a`, and `const std::string &message`. The function should not return a value.
1. In `newAddHandle()`:
    1.  Use the standard library's `cout` output stream to display the contents of parameter `message`. 
    1.  Use the standard library's `cout` output stream to display the contents of parameter `a`. 
1. Define a function named "main". The function should accept the following arguments: `int argc` and `char* argv[]`. The function should return an `int` data type.
1. In `main()`:
    1. Write a try-catch statement.
    1. In the try statement:
        1. Assign the value 1 to an integer variable named "a".
        1. Assign the value 2 to an integer variable named "b".
        1. Call `add()` with the following arguments: `defaultHandle`, `a`, and `b`.
        1. Assign the string "The sum is: " to a string variable named "message".
        1. Use Boost's `bind()` function with following arguments: `newAddHandle`, `_1`, and `message`. Assign the results to a variable named "f".
        1. call `add()` with the following arguments `f`, `a`, and `b`.
        1. Return 0.
    1. In the catch statement:
        1. Display information about an exception.

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

    3
    The sum is:
    3

## Conclusion

In this activity, we've written a program that uses the code and functions introduced in the Boost tutorials.

I hope you've found it helpful.