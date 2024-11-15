cmake_minimum_required(VERSION 3.15...3.31)

# This is your project statement. You should always list languages;
# Listing the version is nice here since it sets lots of useful variables
project(
  EmbeddedAlgorithms
  VERSION 1.0
  LANGUAGES CXX)

enable_testing()

# add_subdirectory(${PROJECT_SOURCE_DIR}/cpp/tests)

set(RING_BUFFER_HEADER 
  ${PROJECT_SOURCE_DIR}/cpp/include)

add_executable(ring_buffer cpp/src/ring_buffer.cpp)
target_include_directories(ring_buffer PUBLIC cpp/include)