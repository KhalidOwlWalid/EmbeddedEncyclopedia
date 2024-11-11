# This file implements ring buffer which is usually used in embedded systems for handling UART data etc.
# See wiki to learn more about the concept of ring buffer

# TODO:
# Implement head and tail for the ring buffer
# Check if the buffer is full before updating the tail
# if full, then we would need to overwrite the data at the tail

class CircularBuffer:
  
  def __init__(self, size):
    self._buffer = [None]
    self._size = size
    
    if isinstance(size, int) and size > 0:
      self._buffer *= self._size
    else:
      self._buffer *= 10
      print("Please ensure value is non-negative and unsigned integer. Defaulting to buffer size of 10!")

    self._head = 0
    self._tail = 0
    self._buff_curr_size = 0
    self._is_full = False
  
  def isBufferFull(self):
    # Buffer is full when the head's position equals the tail's position
    if self._head == self._tail:
      self._is_full = True
    else:
      self._is_full = False

  def isBufferEmpty():
    pass

  def writeData(self, new_data):
    # Update the new data at the head's position if not full
    # Otherwise, if 
    self._buffer[self._head] = new_data
    self._head = (self._head + 1) % self._size
    print(self._buffer)

  def readData(self):
    data = self._buffer[self._tail]
    return data

if __name__ == "__main__":
  buffer = CircularBuffer(5)

  buffer.writeData(100)
  buffer.writeData(101)
  buffer.writeData(102)
  buffer.writeData(103)
  buffer.writeData(104)
  # Data should wraparound here since the buffer is already full
  buffer.writeData(105)