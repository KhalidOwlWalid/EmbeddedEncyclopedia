
#include "ring_buffer.hpp"  // Include the CircularBuffer class

template <class T, std::size_t Size>
algorithms::CircularBuffer<T, Size>::CircularBuffer() :
  _head_idx(0), _tail_idx(0), _is_full(false), _buffer {} {
    std::cout << "Circular Buffer initialized!" << std::endl;
}

template <class T, std::size_t Size>
bool algorithms::CircularBuffer<T, Size>::isBufferEmpty() {
  bool is_empty;
  if (this->_head_idx == this->_tail_idx && not this->_is_full) {
    is_empty = true;
  } else {
    is_empty = false;
  }
  return is_empty;
}

template <class T, std::size_t Size>
bool algorithms::CircularBuffer<T, Size>::isBufferFull() {
  return _is_full;
}

template <class T, std::size_t Size>
void algorithms::CircularBuffer<T, Size>::writeData(const T &new_data) {
  // Need to check if the buffer is full first

  if (this->isBufferFull()) {
    // If buffer is full, then the tail index will increment one step forward, and 
    // data will then be overwritten with new incoming data
    this->_tail_idx += (this->_tail_idx + 1) % Size;
  }

  // Now, we can use the head index to overwrite the data if the buffer was full
  // When writing new data, the data will be placed at wherever the head index is
  // and then it will increment by one step
  this->_buffer[_head_idx] = new_data;
  this->_head_idx += (this->_head_idx + 1) % Size;

  if (this->_head_idx == this->_tail_idx) {
    this->_is_full = true;
  }
}

template <class T, std::size_t Size>
T algorithms::CircularBuffer<T, Size>::readData() {
  // Get the data from where the tail index is currently pointing at
  T data = this->_buffer[_tail_idx];
  this->_tail_idx += (this->_tail_idx + 1) % Size;
  return data;
}

template <class T, std::size_t Size>
std::size_t algorithms::CircularBuffer<T, Size>::getHeadIdx() {
  return _head_idx;
}

int main() {
  algorithms::CircularBuffer<int, 5> circular_buffer_1;
  std::cout << circular_buffer_1.isBufferEmpty() << std::endl;
  int test_data = 3;
  circular_buffer_1.writeData(test_data);
  std::cout << circular_buffer_1.isBufferEmpty() << std::endl;
  return 0;
}