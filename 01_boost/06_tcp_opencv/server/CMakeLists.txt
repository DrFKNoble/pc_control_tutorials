project(server)

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

add_library(sync_server sync_server.h sync_server.cpp)

add_executable(server camera_server.cpp)

target_link_libraries(server ${Boost_LIBRARIES})
target_link_libraries(server ${OpenCV_LIBS})
target_link_libraries(server sync_server)

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

add_custom_command(TARGET server POST_BUILD COMMAND ${CMAKE_COMMAND} ARGS -E copy ${PROJECT_SOURCE_DIR}/video.mp4 $<TARGET_FILE_DIR:server>)

foreach(file ${OPENCV_DLLS})
	add_custom_command(TARGET server POST_BUILD COMMAND ${CMAKE_COMMAND} ARGS -E copy ${file} $<TARGET_FILE_DIR:server>)
endforeach(file)

# install

install(TARGETS server DESTINATION ${PROJECT_SOURCE_DIR}/bin)
install(FILES "video.mp4" DESTINATION ${PROJECT_SOURCE_DIR}/bin)

foreach(file ${OPENCV_DLLS})
	install(FILES ${file} DESTINATION ${PROJECT_SOURCE_DIR}/bin)
endforeach(file)
