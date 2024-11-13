#include <iostream>

namespace algorithms {
  
  template <class T>
  class CircularBuffer {
    public:
      CircularBuffer(uint size);
      bool isBufferFull();

      bool isBufferEmpty();
      void writeData(T new_data);
      T readData();
      void displayBufferData();

    private:
      bool _is_full = false;
      uint _size; 
      // _buffer

  }; 
} // namespace algorithms

template <class T>
algorithms::CircularBuffer<T>::CircularBuffer(uint size) {
  std::cout << "Circular buffer Initialized!" << std::endl;
}

template <class T>
bool algorithms::CircularBuffer<T>::isBufferEmpty() {
  return true;
}


int main() {
  std::cout << "Test" << std::endl;
  algorithms::CircularBuffer<int> tmp(5);
  return 0;
}