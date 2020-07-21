project(client)

cmake_minimum_required(VERSION 3.5)

set(CMAKE_CXX_STANDARD 17)

set(BOOST_ROOT "C:/boost_1_73_0")
find_package(Boost)

set(OpenCV_DIR "C:/opencv/build")
find_package(OpenCV)

include_directories(${Boost_INCLUDE_DIRS})
link_directories(${Boost_LIBRARY_DIRS})

include_directories(${OpenCV_INCLUDE_DIRS})
link_directories(${OpenCV_LIBS_DIRS})

add_library(sync_client sync_client.h sync_client.cpp)

add_executable(client camera_client.cpp)

target_link_libraries(client ${Boost_LIBRARIES})
target_link_libraries(client ${OpenCV_LIBS})
target_link_libraries(client sync_client)

# utilities

if(CMAKE_BUILD_TYPE STREQUAL "Debug")
	set(OPENCV_DLLS
		${OpenCV_DIR}/x64/vc15/bin/opencv_world430d.dll
	)
elseif(CMAKE_BUILD_TYPE STREQUAL "Release")
	set(OPENCV_DLLS
		${OpenCV_DIR}/x64/vc15/bin/opencv_world430.dll
	)
endif()

# build

foreach(file ${OPENCV_DLLS})
	add_custom_command(TARGET client POST_BUILD COMMAND ${CMAKE_COMMAND} ARGS -E copy ${file} $<TARGET_FILE_DIR:client>)
endforeach(file)

# install

install(TARGETS client DESTINATION ${PROJECT_SOURCE_DIR}/bin)

foreach(file ${OPENCV_DLLS})
	install(FILES ${file} DESTINATION ${PROJECT_SOURCE_DIR}/bin)
endforeach(file)
