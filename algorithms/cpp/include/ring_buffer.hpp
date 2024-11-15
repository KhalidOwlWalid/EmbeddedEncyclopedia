#ifndef RING_BUFFER_HPP
#define RING_BUFFER_HPP

#include <iostream>
#include <array>

namespace algorithms {
  
  template <class T, std::size_t Size>
  class CircularBuffer {
    public:
      CircularBuffer();
      bool isBufferFull();
      bool isBufferEmpty();
      void writeData(const T &new_data);
      T readData();
      void displayBufferData();
      
      // Setters
      void setHeadIdx();
      void setTailIdx();

      // Getters
      std::size_t getHeadIdx();
      void getTailIdx();

    private:
      bool _is_full;
      std::size_t _head_idx;
      std::size_t _tail_idx;
      std::array<T, Size> _buffer;

  };
} // namespace algorithms

#endif // RING_BUFFER_HPP